from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AuthSerializer


class AuthView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({'Welcome': user.email}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
