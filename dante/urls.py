from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('products/', products, name='products'),
    path('product/<int:pk>', product, name='product'),
    path('search/', search, name='search')
]
