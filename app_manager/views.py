from rest_framework.response import Response
from rest_framework import status
from random import random
from rest_framework import viewsets
from commons.utils import get_logger

from .utils import string_reverser

from .serializers import (
    ApiBaseSerializer
)

logger = get_logger()


class MessageApiView(viewsets.ModelViewSet):
    serializer_class = ApiBaseSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        serializer = ApiBaseSerializer(
            data=request.data, context={"request": request})
        if serializer.is_valid():
            response['message'] = string_reverser(request.data)
            response['rand'] = random()
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
