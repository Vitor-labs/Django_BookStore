from rest_framework import serializers

from inventory.models import Book, User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

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
