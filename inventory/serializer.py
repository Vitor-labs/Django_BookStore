from django.contrib.auth.models import User, Group
from rest_framework import serializers

from inventory.models import Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'summary', 'pages', 'rating', 'price', 'isbn', 'publisher', 'pub_date', 'cover', 'genre']
