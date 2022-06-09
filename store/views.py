from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
from store.models import Cart, Client, Payment
from store.serializer import CartSerializer, ClientSerializer, PaymentSerializer


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows carts to be viewed or edited.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
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