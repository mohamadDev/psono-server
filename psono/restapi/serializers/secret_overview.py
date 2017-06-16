import uuid

try:
    from django.utils.http import urlsafe_base64_decode as uid_decoder
except:
    # make compatible with django 1.5
    from django.utils.http import base36_to_int as uid_decoder

from rest_framework import serializers


class SecretOverviewSerializer(serializers.Serializer):

    id = serializers.UUIDField(default=uuid.uuid4)