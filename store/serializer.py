from rest_framework import serializers

from store.models import Cart, Client, Payment


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Cart
        fields = ['__all__']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Client
        fields = ['__all__']

    def create(self, validated_data):
        ...
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        ...
        instance.save()
        return instance


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Payment
        fields = ['__all__']
