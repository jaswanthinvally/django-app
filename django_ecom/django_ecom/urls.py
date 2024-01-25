from django.contrib import admin
from django.urls import path
from main.views import home
from main.views import cart

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('cart/', cart, name='cart'),
]
