from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


fake = Faker()

class TestSetUp(APITestCase):
    def setUp(self):
        self.book : dict = {
            'title': fake.name(),
            'author': fake.name(),
            'summary': fake.text(),
            'pages': fake.random_int(min=1, max=1500),
            'rating': fake.random_int(min=1, max=5),
            'price': fake.random_number(digits=4),
            'isbn': fake.isbn10(),
            'publisher': fake.company(),
            'pub_date': fake.date_between(start_date="-10y", end_date="today"),
            'cover': fake.image_url(width=None, height=None),
            'genre': fake.name()
        }

        self.books_url : str = reverse('books')

        return super().setUp()

    def tearDown(self):
        self.book.delete()
        self.book = None
        self.assertEqual(self.book, None)
