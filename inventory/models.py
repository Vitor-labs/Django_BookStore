from django.db import models

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
    cover = models.ImageField(upload_to='covers/', blank=True)
    genre = models.CharField(max_length=200)

    class Meta:
        db_table = 'Book'

    def __str__(self):
        return self.title

