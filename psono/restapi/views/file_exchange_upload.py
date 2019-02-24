from django.db import transaction
from django.db.models import F
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

import json
import urllib

from ..permissions import IsAuthenticated

from ..app_settings import (
    FileExchangeUploadSerializer
)

from ..models import File_Chunk

from ..utils import decrypt_with_db_secret, gcs_construct_signed_upload_url
from ..authentication import TokenAuthentication


class FileExchangeUploadView(GenericAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('PUT', 'OPTIONS', 'HEAD')

    def get(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request, *args, **kwargs):
        """
        Prepares a chunk upload to a file exchange

        :param request:
        :type request:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return: 200 / 400
        :rtype:
        """

        serializer = FileExchangeUploadSerializer(data=request.data, context=self.get_serializer_context())

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        file_transfer = serializer.validated_data.get('file_transfer')
        user_id = serializer.validated_data.get('user_id')
        chunk_position = serializer.validated_data.get('chunk_position')
        chunk_size = serializer.validated_data.get('chunk_size')
        hash_checksum = serializer.validated_data.get('hash_checksum')


        with transaction.atomic():
            File_Chunk.objects.create(
                user_id=user_id,
                file_id=file_transfer.file_id,
                hash_checksum=hash_checksum,
                position=chunk_position,
                size=chunk_size,
            )

            file_transfer.size_transferred = F('size_transferred') + chunk_size
            file_transfer.chunk_count_transferred = F('chunk_count_transferred') + 1
            file_transfer.save(update_fields=["size_transferred", "chunk_count_transferred", "write_date"])


        data = json.loads(decrypt_with_db_secret(file_transfer.file_exchange.data))

        base_url, query_params = gcs_construct_signed_upload_url(data['gcp_cloud_storage_bucket'], data['gcp_cloud_storage_json_key'], hash_checksum)

        # create an url that contains all the url encoded params
        url = base_url + "?" + urllib.parse.urlencode(query_params)

        return Response({
            'url': url
        }, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
