from django.test import TestCase
from faker import Faker

import logging

from authentication.models import User

fake = Faker()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    filename='tests.log', 
                    filemode='w', 
                    format='%(name)s - %(levelname)s - %(message)s')

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='craudim',
            email='craudimEbochecha@turumdum.test'
            )

    def tes_user_creation(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.__str__(), self.user.username)

    def test_user_list(self):
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
    
    def test_user_update(self): 
        username = fake.name()
        self.user.username = username
        self.user.save()
        self.assertEqual(username, self.user.__str__())

    def test_user_delete(self): 
        self.user.delete()
        self.assertFalse(User.objects.filter(id=self.user.id).exists())