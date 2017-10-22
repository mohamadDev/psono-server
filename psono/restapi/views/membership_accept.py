from .share_tree import create_share_link
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from ..utils import readbuffer
from ..authentication import TokenAuthentication

from ..app_settings import (
    MembershipAcceptSerializer,
)

# import the logging
from ..utils import log_info
import logging
logger = logging.getLogger(__name__)

class MembershipAcceptView(GenericAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, *args, **kwargs):
        """
        Marks a Membership as accepted. In addition update the membership with the new encryption key.

        :param request:
        :param args:
        :param kwargs:
        :return: 200 / 400
        """

        serializer = MembershipAcceptSerializer(data=request.data, context=self.get_serializer_context())

        if not serializer.is_valid():

            log_info(logger=logger, request=request, status='HTTP_400_BAD_REQUEST', event='ACCEPT_MEMBERSHIP_ERROR', errors=serializer.errors)

            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        membership_obj = serializer.validated_data.get('membership_obj')

        membership_obj.accepted = True

        membership_obj.save()

        log_info(logger=logger, request=request, status='HTTP_200_OK', event='ACCEPT_MEMBERSHIP_SUCCESS', request_resource=request.data['membership_id'])

        shares = []

        for share_right in membership_obj.group.group_share_rights.all():
            if share_right.read:
                shares.append({
                    "share_id": share_right.share.id,
                    "share_title": share_right.title,
                    "share_title_nonce": share_right.title_nonce,
                    "share_type": share_right.type,
                    "share_type_nonce": share_right.type_nonce,
                    "share_data": readbuffer(share_right.share.data),
                    "share_data_nonce": share_right.share.data_nonce,
                    "share_key": share_right.key,
                    "share_key_nonce": share_right.key_nonce,
                })

            else:
                shares.append({
                    "share_id": share_right.share.id,
                    "share_title": share_right.title,
                    "share_title_nonce": share_right.title_nonce,
                    "share_type": share_right.type,
                    "share_type_nonce": share_right.type_nonce,
                    "share_key": share_right.key,
                    "share_key_nonce": share_right.key_nonce,
                })

        return Response({
            "shares": shares,
            "secret_key": membership_obj.secret_key,
            "secret_key_nonce": membership_obj.secret_key_nonce,
            "secret_key_type": membership_obj.secret_key_type,
            "private_key": membership_obj.private_key,
            "private_key_nonce": membership_obj.private_key_nonce,
            "private_key_type": membership_obj.private_key_type,
        }, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


