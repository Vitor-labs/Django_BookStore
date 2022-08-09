from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from inventory.serializer import BookSerializer
from inventory.models import Book


# TESTED - OK
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_by_genre(self, request, pk=None):
        book = Book.objects.filter(genre=pk)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)