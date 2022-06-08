from rest_framework import serializers

from store.models import Cart, Client, Payment


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Cart
        fields = ['__all__']

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.client = validated_data.get('client', instance.client)
        instance.save()
        return instance

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Client
        fields = ('dlient_id',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'address',
                  'city',
                  'state',
                  'zip_code',
                  'country')

    
class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Payment
        fields = ['__all__']
