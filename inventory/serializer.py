from rest_framework import serializers

from inventory.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'summary', 'pages', 'rating',
                  'price', 'isbn', 'publisher', 'pub_date', 'cover', 'genre']
