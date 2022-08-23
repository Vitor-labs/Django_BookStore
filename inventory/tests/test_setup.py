from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetUp(APITestCase):
    def setUp(self):
        self.books_url : str = reverse('books')
        self.fake = Faker()

        self.book : dict = {
            'title': self.fake.name(),
            'author': self.fake.name(),
            'summary': self.fake.text(),
            'pages': self.fake.random_int(min=1, max=1500),
            'rating': self.fake.random_int(min=1, max=5),
            'price': self.fake.random_number(digits=4),
            'isbn': self.fake.isbn10(),
            'publisher': self.fake.company(),
            'pub_date': self.fake.date_between(start_date="-10y", end_date="today"),
            'cover': self.fake.image_url(width=None, height=None),
            'genre': self.fake.name()
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
        