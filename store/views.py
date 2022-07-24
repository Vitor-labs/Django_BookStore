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

    @action(detail=True, methods=['get'], url_path='items', url_name='items')
    def retrive(self, pk=None):
        if pk is not None:
            cart = Cart.objects.get(pk=pk)
            cart_items = CartItem.objects.filter(cart=cart)
            serializer = CartItemSerializer(cart_items, many=True)

            return Response(serializer.data)

        return Response(status=400)


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
