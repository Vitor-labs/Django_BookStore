from rest_framework import serializers

from inventory.models import Book
from store.models import Cart, CartItem, Client, Payment


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'client']


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    def add_to_cart(self, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return False

        cart_item, created = CartItem.objects.get_or_create(
            cart=self,
            book=book,
        )

        if created:
            cart_item.quantity = 1
            cart_item.save()
            return cart_item
        else:
            cart_item.quantity += 1
            cart_item.save()
            return cart_item

    def remove_from_cart(self, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return False

        cart_item = CartItem.objects.get(
            cart=self,
            book=book,
        )

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            return cart_item
        else:
            cart_item.delete()
            return None

    def remove_all_from_cart(self, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return False

        cart_item = CartItem.objects.get(
            cart=self,
            book=book,
        )

        cart_item.delete()
        return None

    class Meta:
        model = CartItem
        fields = ['__all__']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'phone_number',
                  'address', 'city', 'state', 'zip_code', 'country']


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'date_added',
                  'payment_method', 'client', 'cart', 'amount']
