from django.db import models

# Create your models here.


class Cart(models.Model):
    date_added = models.DateField(auto_now_add=True)

    client = models.OneToOneField(
        'store.Client',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    items = models.ManyToManyField(
        'inventory.Book',
        related_name='carts',
    )

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
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

    credit_card_number = models.CharField(
        max_length=255, blank=True, null=True)
    credit_card_expiration_date = models.CharField(
        max_length=255, blank=True, null=True)
    credit_card_cvv = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'Client'

    def __str__(self):
        return self.client_id


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    date_added = models.DateField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=255, blank=True, null=True)

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
        return self.payment_id
