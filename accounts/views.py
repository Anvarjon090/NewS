from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .serializers import RegisterSerializer
from django.utils.encoding import force_str
from rest_framework import status




User = get_user_model()

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

class ActivateUserView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except Exception:
            return Response({"error": "Xatolik yuz berdi"}, status=400)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"message": "Email tasdiqlandi"})
        return Response({"error": "Token yaroqsiz"}, status=400)
    





User = get_user_model()

class ConfirmEmailAPIView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error': 'Invalid user'}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'Email tasdiqlandi'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Token noto‘g‘ri yoki eskirgan'}, status=status.HTTP_400_BAD_REQUEST)