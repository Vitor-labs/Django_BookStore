from django.db import models

# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(primary_key=True, max_length=50)
    date_added = models.DateField(auto_now_add=True)

    client = models.OneToOneField(
        'store.Client',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
        book = models.ForeignKey(
            'inventory.Book',
            on_delete=models.CASCADE,
        )
        cart = models.ForeignKey(
            'store.Cart',
            on_delete=models.CASCADE,
        )
        quantity = models.IntegerField()
        active = models.BooleanField(default=True)
    
        class Meta:
            db_table = 'CartItem'
            ordering = ['cart', 'book']
    
        def sub_total(self):
            return self.product.price * self.quantity
    
        def __str__(self):
            return self.book

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
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

    def __str__(self):
        return self.client_id


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    date_added = models.DateField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=255, 
        blank=True, 
        null=True)
    client = models.ForeignKey(
        'store.Client',
        on_delete=models.CASCADE,
    )
    cart = models.ForeignKey(
        'store.Cart',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    class Meta:
        db_table = 'Payment'
        ordering = ['date_added']

    def __str__(self):
        return str(self.payment_id, self.date_added)
