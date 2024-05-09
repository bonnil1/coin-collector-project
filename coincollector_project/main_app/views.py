from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coin
from .forms import PurchaseForm

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
    purchase_form = PurchaseForm()
    return render(request, 'coins/detail.html', {
        'coin': coin,
        'purchase_form': purchase_form,
    })

def add_purchase(request, pk):
    form = PurchaseForm(request.POST)

    if form.is_valid():
        new_purchase = form.save(commit=False)
        new_purchase.coin_id = pk
        new_purchase.save()
    return redirect('detail', coin_id=pk)

class CoinCreate(CreateView):
  model = Coin
  fields = ['name', 'symbol', 'price', 'description']

class CoinUpdate(UpdateView):
  model = Coin
  fields = ['price', 'description']

class CoinDelete(DeleteView):
  model = Coin
  success_url = '/coins'
