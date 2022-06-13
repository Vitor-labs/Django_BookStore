from rest_framework import serializers

from store.models import Cart, Client, Payment

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['cart_id', 'date_added', 'client']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'user', 'first_name', 'last_name', 'phone_number', 'address', 'city', 'state', 'zip_code', 'country']
    
    
class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'date_added', 'payment_method', 'client', 'cart','amount']
