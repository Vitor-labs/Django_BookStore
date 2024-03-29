from django.test import TestCase
from faker import Faker

import logging

from inventory.models import Book

fake = Faker()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    filename='tests.log', 
                    filemode='w', 
                    format='%(name)s - %(levelname)s - %(message)s')

class BookTestCase(TestCase):
    def setUp(self): # Tested OK
        self.book = Book.objects.create(
            title=fake.name(),
            author=fake.name(),
            summary=fake.text(),
            pages=fake.random_int(min=1, max=1500),
            rating=fake.random_int(min=1, max=5),
            price=fake.random_number(digits=4),
            isbn=fake.isbn10(),
            publisher=fake.company(),
            pub_date=fake.date_between(start_date="-10y", end_date="today"),
            cover=fake.image_url(width=None, height=None),
            genre=fake.name()
        )

    def test_book_creation(self): # Tested OK
        self.assertTrue(isinstance(self.book, Book))
        self.assertEqual(self.book.__str__(), self.book.title)

    def test_book_list(self): # Tested OK
        books = Book.objects.all()
        self.assertTrue(len(books) > 0)

    def test_book_update(self): # Tested OK
        title = fake.name()
        self.book.title = title
        self.book.save()
        self.assertEqual(title, self.book.__str__())

    def test_book_delete(self): # Tested OK
        self.book.delete()
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())