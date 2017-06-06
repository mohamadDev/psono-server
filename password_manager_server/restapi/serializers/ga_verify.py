from django.conf import settings
from ..authentication import TokenAuthentication
import hashlib

try:
    from django.utils.http import urlsafe_base64_decode as uid_decoder
except:
    # make compatible with django 1.5
    from django.utils.http import base36_to_int as uid_decoder

from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions
from ..models import Token, Google_Authenticator
import nacl.utils
import nacl.secret
import nacl.encoding
import pyotp

class GAVerifySerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    ga_token = serializers.CharField(max_length=6, min_length=6, required=True)

    def validate(self, attrs):

        ga_token = attrs.get('ga_token').lower().strip()

        if not ga_token.isdigit():
            msg = _('GA Tokens only contain digits.')
            raise exceptions.ValidationError(msg)

        token_hash = TokenAuthentication.user_token_to_token_hash(attrs.get('token'))

        try:
            token = Token.objects.filter(key=token_hash, active=False).get()
        except Token.DoesNotExist:
            msg = _('Token incorrect.')
            raise exceptions.ValidationError(msg)

        # prepare decryption
        secret_key = hashlib.sha256(settings.DB_SECRET).hexdigest()
        crypto_box = nacl.secret.SecretBox(secret_key, encoder=nacl.encoding.HexEncoder)

        ga_token_correct = False
        for ga in Google_Authenticator.objects.filter(user=token.user):
            encrypted_ga_secret = nacl.encoding.HexEncoder.decode(ga.secret)
            decrypted_ga_secret = crypto_box.decrypt(encrypted_ga_secret)
            totp = pyotp.TOTP(decrypted_ga_secret)
            if totp.verify(ga_token):
                ga_token_correct = True
                break

        if not ga_token_correct:
            msg = _('GA Token incorrect.')
            raise exceptions.ValidationError(msg)

        attrs['token'] = token
        return attrs
