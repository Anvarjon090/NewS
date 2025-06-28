# accounts/serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
        username=validated_data['email'],  # Yechim shu!
        email=validated_data['email'],
        password=validated_data['password'],
        is_active=False
        )
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        link = f"http://localhost:8000/api/activate/{uid}/{token}/"
        send_mail("Tasdiqlash", f"Tasdiqlash uchun link: {link}",
                  settings.DEFAULT_FROM_EMAIL, [user.email])
        return user
    