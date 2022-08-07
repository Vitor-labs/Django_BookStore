from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
from store.models import Cart, CartItem, Client, Payment
from store.serializer import CartSerializer, CartItemSerializer, ClientSerializer, PaymentSerializer


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows carts to be viewed or edited.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        cart = self.get_object()
        items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def client(self, request, pk=None):
        cart = self.get_object()
        client = Client.objects.get(cart=cart)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def pay(self, request, pk=None):
        cart = self.get_object()
        items = CartItem.objects.filter(cart=cart)
        total = 0
        for item in items:
            total += item.book.price * item.quantity

        client = Client.objects.get(cart=cart)
        serializer = PaymentSerializer(
            data={'client': client.id, 'amount': total, 'method': 'Cr'})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
        

class CartItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cart items to be viewed or edited.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows payments to be viewed or edited.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
