from django.shortcuts import render

def home(request):
    return render(request, 'main\home.html')
def cart(request):
    return render(request, 'main\cart.html')
