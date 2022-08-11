from faker import Faker

import logging

from inventory.models import Book
from inventory.tests.test_setup import TestSetUp

fake = Faker()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    filename='tests.log', 
                    filemode='w', 
                    format='%(name)s - %(levelname)s - %(message)s')

class BookViewSetTestCase(TestSetUp):
    def test_book_create(self):
        logger.info('Test BookViewSetTestCase - test_book_create')
        
        try:
            response = self.client.post(self.books_url, self.book, format='json')
            
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.data['title'], self.book['title'])

            logger.info('Test BookViewSetTestCase - test_book_create - OK')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - test_book_create - {}'.format(e))
            raise e

    def test_book_list(self):
        logger.info('Test BookViewSetTestCase - test_book_list')
        try:
            response = self.client.get(self.books_url)

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
            response = self.client.get('/books/{self.book.id}/')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['id'], self.book.id)
            self.assertEqual(response.data['title'], self.book.title)

            logger.info('Test BookViewSetTestCase - test_book_detail - OK')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - test_book_detail - {}'.format(e))
            raise e

    def test_book_update(self):
        logger.info('Test BookViewSetTestCase - test_book_update')
        
        try:
            response = self.client.put('/books/{self.book.id}/', self.book, format='json')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['title'], self.book['title'])

            logger.info('Test BookViewSetTestCase - test_book_update - OK')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - test_book_update - {}'.format(e))
            raise e

    def test_book_delete(self):
        logger.info('Test BookViewSetTestCase - test_book_delete')
        try:
            response = self.client.delete('/books/{self.book.id}/')

            self.assertEqual(response.status_code, 204)
            self.assertFalse(Book.objects.filter(id=self.book.id).exists())

            logger.info('Test BookViewSetTestCase - test_book_delete - OK')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - test_book_delete - {}'.format(e))
            raise e

    def test_book_get_by_genre(self):
        logger.info('Test BookViewSetTestCase - test_book_get_by_genre')
        try:
            response = self.client.get('/books/genre/{self.book.genre}/')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['count'], 1)
            self.assertEqual(response.data['results'][0]['title'], self.book.title)

            logger.info('Test BookViewSetTestCase - test_book_get_by_genre - OK')

        except Exception as e:
            logger.error('Test BookViewSetTestCase - test_book_get_by_genre - {}'.format(e))
            raise e