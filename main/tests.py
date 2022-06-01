from django.test import TestCase

from inventory.models import Book

class BookTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title="Test Book", 
                                        author="Test Author", 
                                        summary="Test Summary", 
                                        pages=1, rating=0.0, price=1.0, 
                                        isbn="123456789", 
                                        publisher="Test Publisher", 
                                        pub_date="2017-01-01", 
                                        cover="Test Cover",
                                        genre="Test Genre")

    def test_book_title(self):
        self.assertEqual(self.book.title, "Test Book")

    def test_book_author(self):
        self.assertEqual(self.book.author, "Test Author")

    def test_book_summary(self):
        self.assertEqual(self.book.summary, "Test Summary")

    def test_book_pages(self):
        self.assertEqual(self.book.pages, 1)

    def test_book_rating(self):
        self.assertEqual(self.book.rating, 0.0)

    def test_book_price(self):
        self.assertEqual(self.book.price, 1.0)

    def test_book_isbn(self):
        self.assertEqual(self.book.isbn, "123456789")

    def test_book_publisher(self):
        self.assertEqual(self.book.publisher, "Test Publisher")

    def test_book_pub_date(self):
        self.assertEqual(self.book.pub_date, "2017-01-01")

    def test_book_cover(self):
        self.assertEqual(self.book.cover, "Test Cover")

    def test_book_genre(self):
        self.assertEqual(self.book.genre, "Test Genre")

