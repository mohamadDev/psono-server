from ..authentication import TokenAuthentication

try:
    from django.utils.http import urlsafe_base64_decode as uid_decoder
except:
    # make compatible with django 1.5
    from django.utils.http import base36_to_int as uid_decoder

from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions
from ..models import Token
import nacl.utils
from nacl.exceptions import CryptoError
import nacl.secret
import nacl.encoding

class ActivateTokenSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    verification = serializers.CharField(required=True)
    verification_nonce = serializers.CharField(max_length=64, required=True)

    def validate(self, attrs):
        verification_hex = attrs.get('verification')
        verification = nacl.encoding.HexEncoder.decode(verification_hex)
        verification_nonce_hex = attrs.get('verification_nonce')
        verification_nonce = nacl.encoding.HexEncoder.decode(verification_nonce_hex)

        token_hash = TokenAuthentication.user_token_to_token_hash(attrs.get('token'))

        try:
            token = Token.objects.filter(key=token_hash, active=False).get()
        except Token.DoesNotExist:
            msg = _('Token incorrect.')
            raise exceptions.ValidationError(msg)

        if token.google_authenticator_2fa:
            msg = _('GA challenge unsolved.')
            raise exceptions.ValidationError(msg)

        if token.google_authenticator_2fa:
            msg = _('YubiKey challenge unsolved.')
            raise exceptions.ValidationError(msg)

        crypto_box = nacl.secret.SecretBox(token.secret_key, encoder=nacl.encoding.HexEncoder)

        try:
            decrypted = crypto_box.decrypt(verification, verification_nonce)
        except CryptoError:
            msg = _('Verification code incorrect.')
            raise exceptions.ValidationError(msg)


        if token.user_validator != decrypted:
            msg = _('Verification code incorrect.')
            raise exceptions.ValidationError(msg)

        attrs['token'] = token
        return attrs