from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class User(AbstractUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True)

    is_staff = models.BooleanField(default=False) # can log into admin site
    is_superuser = models.BooleanField(default=False) # superuser has all permissions
    is_active = models.BooleanField(default=True) # default=True / False to most 3 months inactive
    is_valid = models.BooleanField(default=False) # Checks if the user is verified | email is verified, username is verified, etc.

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    class Meta:
        db_table = 'User'

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def __str__(self):
        return str(self.username)
