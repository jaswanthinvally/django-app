from django.contrib import admin
from django.urls import path
from main.views import home
from main.views import cart
from main.views import payment
from main.views import login

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('cart/', cart, name='cart'),
    path('payment/', payment, name = 'payment'),
    path('login/', login, name='login')
]
