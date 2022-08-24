from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from django.contrib import auth
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=32, min_length=8, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already exists')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists')
        if not username.isalnum():
            raise serializers.ValidationError('Username must be alphanumeric')

        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['token']

    def validate(self, data):
        token = data.get('token')
        if not token:
            raise serializers.ValidationError('Token is required')

        return data

    def update(self, instance, validated_data):
        instance.is_verified = True
        instance.save()

        return instance

from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    tokens = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['username','email', 'password', 'tokens']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials')
        if not user.is_active:
            raise AuthenticationFailed('User is not active')
        if not user.is_verified:
            raise AuthenticationFailed('User is not verified')
        if not email:
            raise serializers.ValidationError('Email is required')
        if not password:
            raise serializers.ValidationError('Password is required')

        return {
            'email': email,
            'password': password,
            'token': user.tokens
        }

class RequestPasswordResetSerializer(serializers.Serializer):
    email= serializers.EmailField(min_length=10)

    class Meta:
        fields = ['email',]

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.PasswordField(min_length=8, max_length=20, write_only=True)
    token = serializers.CharField(write_only=True)
    uidb64 = serializers.CharField(write_only=True)

    class Meta:
        fields=['password', 'token', 'uidb64']

    def validate(self, data):
        try:
            password = data.get('password')
            token = data.get('token')
            uidb64 = data.get('uidb64')

            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('Invalid Link', 401)

            user.set_password(password)
            user.save()
            
            return user
        except Exception as exc:
            message= {'Invalid Link': str(exc)}
            raise AuthenticationFailed(message, 401)