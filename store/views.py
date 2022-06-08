from rest_framework import viewsets, permissions
from rest_framework.response import Response

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

    def list(self, request, *args, **kwargs):
        queryset = Cart.objects.all()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrive(self, request, *args, **kwargs):
        queryset = Cart.objects.get(id=kwargs['pk'])
        serializer = CartSerializer(queryset)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, *args, **kwargs):
        cart = Cart.objects.get(id=kwargs['pk'])
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self, request, *args, **kwargs):
        cart = Cart.objects.get(id=kwargs['pk'])
        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        cart = Cart.objects.get(id=kwargs['pk'])
        cart.delete()
        return Response(status=204)


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrive(self, request, *args, **kwargs):
        queryset = Client.objects.get(id=kwargs['pk'])
        serializer = ClientSerializer(queryset)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, *args, **kwargs):
        client = Client.objects.get(id=kwargs['pk'])
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self, request, *args, **kwargs):
        client = Client.objects.get(id=kwargs['pk'])
        serializer = ClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        client = Client.objects.get(id=kwargs['pk'])
        client.delete()
        return Response(status=204)


class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows payments to be viewed or edited.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        start, end = request.GET.get('start'), request.GET.get('end')
        queryset = Payment.objects.filter(
            date__gte=start, date__lte=end)
        
        serializer = PaymentSerializer(queryset, many=True)

        return Response(serializer.data)
        
    def retrive(self, request, *args, **kwargs):
        queryset = Payment.objects.get(id=kwargs['pk'])
        serializer = PaymentSerializer(queryset)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, *args, **kwargs):
        payment = Payment.objects.get(id=kwargs['pk'])
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self, request, *args, **kwargs):
        payment = Payment.objects.get(id=kwargs['pk'])
        serializer = PaymentSerializer(
            payment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        payment = Payment.objects.get(id=kwargs['pk'])
        payment.delete()
        return Response(status=204)
