"""Book_Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from inventory import views as inventory_views
from store import views as store_views

router = routers.DefaultRouter()

# Books, Users [inventory app] routes - Tested OK
router.register(r'books', inventory_views.BookViewSet)
router.register(r'users', inventory_views.UserViewSet)

# Client, Cart, Payment [store app] routes - Tested OK
router.register(r'clients', store_views.ClientViewSet)
router.register(r'carts', store_views.CartViewSet)
router.register(r'items', store_views.CartItemViewSet)
router.register(r'payments', store_views.PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('inventory.urls'), name='auth'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
