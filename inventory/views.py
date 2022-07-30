from rest_framework import viewsets, permissions

from inventory.serializer import BookSerializer
from inventory.models import Book


# NOT TESTED
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
