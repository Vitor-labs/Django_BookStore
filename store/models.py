import datetime
from django.db import models


# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True, default=1)

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'Client'
        ordering = ['id']

    def __str__(self):
        return self.client_id


class Cart(models.Model):
    id = models.AutoField(primary_key=True, default=0)

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'Cart'
        ordering = ['id']

    def __str__(self):
        return str(self.cart_id)


class CartItem(models.Model):
    cart = models.ForeignKey(
        'store.Cart',
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        'inventory.Book',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField()

    date_added = models.DateField(default=datetime.date.today)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'
        ordering = ['cart', '-date_added']

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.book.title


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    date_added = models.DateField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=255,
    )
    client = models.ForeignKey(
        'store.Client',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    status = models.CharField(
        max_length=255,
        default='Pending',
    )

    class Meta:
        db_table = 'Payment'
        ordering = ['date_added']

    def __str__(self):
        return str(self.payment_id, self.date_added)
