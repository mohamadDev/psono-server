try:
    from django.utils.http import urlsafe_base64_decode as uid_decoder
except:
    # make compatible with django 1.5
    from django.utils.http import base36_to_int as uid_decoder

from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from ..models import User_Group_Membership

class MembershipDeclineSerializer(serializers.Serializer):

    membership_id = serializers.UUIDField(required=True)

    def validate(self, attrs):

        membership_id = attrs.get('membership_id')

        try:
            membership_obj = User_Group_Membership.objects.get(pk=membership_id, user=self.context['request'].user, accepted=None)
        except User_Group_Membership.DoesNotExist:
            msg = _("You don't have permission to access it or it does not exist or you already accepted or declined this membership.")
            raise exceptions.ValidationError(msg)

        attrs['membership_obj'] = membership_obj

        return attrs