from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, default="Here some Text")
    pages = models.IntegerField(default=1)
    rating = models.FloatField(default=0.0)
    price = models.FloatField()
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=200)
    pub_date = models.DateField()
    cover = models.ImageField(upload_to='covers/')
    genre = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.book.title


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
