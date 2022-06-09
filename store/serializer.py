from rest_framework import serializers

from store.models import Cart, Client, Payment

class CartSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return Cart.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.client = validated_data.get('client', instance.client)
        instance.save()
        return instance

    class Meta:
        model = Cart
        fields = ['cart_id', 'client', 'date_added']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'user', 'first_name', 'last_name', 'phone_number', 'address', 'city', 'state', 'zip_code', 'country']
    
    
class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'date_added', 'payment_method', 'client', 'cart','amount']
