from re import M
from django.test import TestCase
from faker import Faker

from inventory.models import Book
from store.models import Client, Cart, CartItem, Payment

fake = Faker()

class BookTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title=fake.name(),
            author=fake.name(),
            summary=fake.text(),
            pages=fake.random_int(min=1, max=1000),
            rating=fake.random_int(min=1, max=5),
            price=fake.random_int(0, 100),
            isbn=fake.isbn13(),
            publisher=fake.name(),
            pub_date=fake.date(),
            cover_image=fake.image_url(),
            genre=fake.name(),
        )
        self.cart = Cart.objects.create(
            client=Client.objects.create(
                first_name=fake.name(),
                last_name=fake.name(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                city=fake.city(),
                state=fake.state(),
                zip_code=fake.zipcode(),
                country=fake.country(),
            )
        )
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            book=self.book,
            quantity=fake.random_int(min=1, max=10),
        )
        self.cart_item2 = CartItem.objects.create(
            cart=self.cart,
            book=self.book,
            quantity=fake.random_int(min=1, max=10),
        )
        self.payment = Payment.objects.create(
            cart=self.cart,
            amount=self.cart.total(),
            method='Pp',
        )

    def test_book_creation(self):
        self.assertTrue(isinstance(self.book, Book))
        self.assertEqual(self.book.__str__(), self.book.title)

    def test_book_list(self):
        books = Book.objects.all()
        self.assertTrue(len(books) > 0)

    def test_book_update(self):
        title = fake.name()
        self.book.title = title
        self.book.save()
        self.assertEqual(title, self.book.__str__())

    def test_cart_creation(self):
        self.assertTrue(isinstance(self.cart, Cart))
        self.assertEqual(self.cart.__str__(), self.cart.client.__str__())

    def test_cart_list(self):
        carts = Cart.objects.all()
        self.assertTrue(len(carts) > 0)

    def test_cart_update(self):
        first_name = fake.name()
        self.cart.client.first_name = first_name
        self.cart.client.save()
        self.assertEqual(first_name, self.cart.client.__str__())

    def test_cart_item_creation(self):
        self.assertTrue(isinstance(self.cart_item, CartItem))
        self.assertEqual(self.cart_item.__str__(), self.cart_item.book.__str__())

    def test_cart_item_list(self):
        cart_items = CartItem.objects.all()
        self.assertTrue(len(cart_items) > 0)

    def test_cart_item_update(self):
        quantity = fake.random_int(min=1, max=10)
        self.cart_item.quantity = quantity
        self.cart_item.save()
        self.assertEqual(quantity, self.cart_item.quantity)

    def test_payment_creation(self):
        self.assertTrue(isinstance(self.payment, Payment))
        self.assertEqual(self.payment.__str__(), self.payment.cart.__str__())

    def test_payment_list(self):
        payments = Payment.objects.all()
        self.assertTrue(len(payments) > 0)

    def test_payment_update(self):
        amount = fake.random_int(0, 100)
        self.payment.amount = amount
        self.payment.save()
        self.assertEqual(amount, self.payment.amount)

    def test_payment_delete(self):
        self.payment.delete()
        self.assertFalse(Payment.objects.filter(id=self.payment.id).exists())

    def test_cart_item_delete_cart(self):
        self.cart.delete()
        self.assertFalse(CartItem.objects.filter(cart=self.cart).exists())

    def test_cart_item_delete_book(self):
        self.book.delete()
        self.assertFalse(CartItem.objects.filter(book=self.book).exists())

    def test_cart_item_delete(self):
        self.cart_item.delete()
        self.assertFalse(CartItem.objects.filter(id=self.cart_item.id).exists())

    def test_cart_delete(self):
        self.cart.delete()
        self.assertFalse(Cart.objects.filter(id=self.cart.id).exists())
    
    def test_book_delete(self):
        self.book.delete()
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
