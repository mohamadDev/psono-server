from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import (
    Token
)

from ..app_settings import (
    GAVerifySerializer
)
from ..authentication import TokenAuthenticationAllowInactive

# import the logging
from ..utils import log_info
import logging
logger = logging.getLogger(__name__)

class GAVerifyView(GenericAPIView):

    authentication_classes = (TokenAuthenticationAllowInactive, )
    permission_classes = (IsAuthenticated,)
    serializer_class = GAVerifySerializer
    token_model = Token
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')
    throttle_scope = 'ga_verify'

    def get(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, *args, **kwargs):
        """
        Validates a Google Authenticator based OATH-TOTP

        :param request:
        :type request:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return: 200 / 400
        :rtype:
        """

        serializer = self.get_serializer(data=self.request.data)

        if not serializer.is_valid():

            log_info(logger=logger, request=request, status='HTTP_400_BAD_REQUEST', event='LOGIN_GA_VERIFY_ERROR', errors=serializer.errors)

            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        # Google Authenticator challenge has been solved, so lets update the token
        token = serializer.validated_data['token']
        token.google_authenticator_2fa = False
        token.save()

        log_info(logger=logger, request=request, status='HTTP_200_OK',
                 event='LOGIN_GA_VERIFY_SUCCESS', request_resource=serializer.validated_data['ga_token'].id)

        return Response(status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)