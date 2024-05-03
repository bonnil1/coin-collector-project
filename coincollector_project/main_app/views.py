from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coin

"""
coins = [
    {'name': 'Bitcoin', 'symbol': 'BTC', 'price': '63,332.98'},
    {'name': 'Ethereum', 'symbol': 'ETH', 'price': '3,247,03'},
    {'name': 'Dogecoin', 'symbol': 'DOGE', 'price': '0.1475'},
]
"""

# Create your views here.
def home(request):
    return render(request, 'coins/home.html')

def about(request):
    return render(request, 'coins/about.html')

def coins_index(request):
    coins = Coin.objects.all()
    return render(request, 'coins/index.html', {
        'coins': coins
    })

def coins_detail(request, coin_id):
    coin = Coin.objects.get(id=coin_id)
    return render(request, 'coins/detail.html', {'coin': coin})

class CoinCreate(CreateView):
  model = Coin
  fields = ['name', 'symbol', 'price', 'description']

class CoinUpdate(UpdateView):
  model = Coin
  fields = ['price', 'description']

class CoinDelete(DeleteView):
  model = Coin
  success_url = '/coins'
