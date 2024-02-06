from django.shortcuts import render

def home(request):
    data = {
        'name': 'jaswanth',
        'role': 'admin'
    }
    return render(request, 'main\home.html')
def cart(request):
    return render(request, 'main\cart.html')
def payment(request):
    return render(request, 'main\payment.html')
def login(request):
    return render(request,'main\login.html')
