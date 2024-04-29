from django.shortcuts import render

coins = [
    {'name': 'Bitcoin', 'symbol': 'BTC', 'price': '63,332.98'},
    {'name': 'Ethereum', 'symbol': 'ETH', 'price': '3,247,03'},
    {'name': 'Dogecoin', 'symbol': 'DOGE', 'price': '0.1475'},
]

# Create your views here.
def home(request):
    return render(request, 'coins/home.html')

def about(request):
    return render(request, 'coins/about.html')

def coins_index(request):
    return render(request, 'coins/index.html', {
        'coins': coins
    })