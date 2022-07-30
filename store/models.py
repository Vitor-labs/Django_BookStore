from django.db import models


# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        db_table = 'Client'

    def __str__(self):
        return self.client_id


class Cart(models.Model):
    id = models.AutoField(primary_key=True)

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'Cart'

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

    date_added = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'
        ordering = ['cart', '-date_added']

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.book.title


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    date_added = models.DateField(auto_now_add=True)
    client = models.ForeignKey(
        'store.Client',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    choices = (
        ('Ca', 'Cash'),
        ('Cr', 'Credit Card'),
        ('De', 'Debit Card'),
        ('Pp', 'Paypal'),
    )
    method = models.CharField(
        max_length=2,
        choices=choices,
        default='Ca',
    )

    class Meta:
        db_table = 'Payment'

    def __str__(self):
        return str(self.payment_id, self.date_added)
