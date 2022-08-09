from django.test import TestCase
from faker import Faker

import logging, requests

from inventory.models import Book

fake = Faker()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    filename='tests.log', 
                    filemode='w', 
                    format='%(name)s - %(levelname)s - %(message)s')

# ==========================[INTERNAL TESTS - Book]===========================
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
# =============================================================================

# =============================[API TESTS - Book]==============================
class BookViewSetTestCase(TestCase):
    def setUp(self): # Tested OK
        try:
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
            self.auth = requests.auth.HTTPBasicAuth('computador', 'pass1234')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - setUp - {}'.format(e))
            raise e

    def test_book_create(self):
        logger.info('Test BookViewSetTestCase - test_book_create')
        data = {
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
        try:
            response = requests.post('http://127.0.0.1:8000/books/', data=data, auth=self.auth)
            
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.data['title'], data['title'])

            logger.info('Test BookViewSetTestCase - test_book_create - OK')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - test_book_create - {}'.format(e))
            raise e

    def test_book_list(self):
        logger.info('Test BookViewSetTestCase - test_book_list')
        try:
            response = requests.get('http://127.0.0.1:8080/books)', auth=self.auth)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['count'], 1)
            self.assertEqual(response.data['results'][0]['title'], self.book.title)

            logger.info('Test BookViewSetTestCase - test_book_list - OK')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - test_book_list - {}'.format(e))
            raise e

    def test_book_detail(self):
        logger.info('Test BookViewSetTestCase - test_book_detail')
        try:
            response = requests.get('http://127.0.0.1:8080/books/{self.book.id}', auth=self.auth)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['id'], self.book.id)
            self.assertEqual(response.data['title'], self.book.title)

            logger.info('Test BookViewSetTestCase - test_book_detail - OK')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - test_book_detail - {}'.format(e))
            raise e

    def test_book_update(self):
        logger.info('Test BookViewSetTestCase - test_book_update')
        data = {
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
        try:
            response = requests.put('http://127.0.0.1:8080/books/{self.book.id}', data=data, auth=self.auth)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['title'], data['title'])

            logger.info('Test BookViewSetTestCase - test_book_update - OK')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - test_book_update - {}'.format(e))
            raise e

    def test_book_delete(self):
        logger.info('Test BookViewSetTestCase - test_book_delete')
        try:
            response = requests.delete('http://127.0.0.1:8080/books/{self.book.id}', auth=self.auth)
            self.assertEqual(response.status_code, 204)
            self.assertFalse(Book.objects.filter(id=self.book.id).exists())

            logger.info('Test BookViewSetTestCase - test_book_delete - OK')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - test_book_delete - {}'.format(e))
            raise e

    def test_book_get_by_genre(self):
        logger.info('Test BookViewSetTestCase - test_book_get_by_genre')
        try:
            response = requests.get('http://127.0.0.1:8080/books/genre/{self.book.genre}', auth=self.auth)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['count'], 1)
            self.assertEqual(response.data['results'][0]['title'], self.book.title)

            logger.info('Test BookViewSetTestCase - test_book_get_by_genre - OK')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - test_book_get_by_genre - {}'.format(e))
            raise e
# ================================================================================