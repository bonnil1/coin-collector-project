from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Coin, Investor
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
    investors = Investor
    id_list = coin.investors.all().values_list('id')
    investors_not = Investor.objects.exclude(id__in=id_list)
    purchase_form = PurchaseForm()
    return render(request, 'coins/detail.html', {
        'coin': coin,
        'purchase_form': purchase_form,
        'investors': investors_not,
    })

def add_purchase(request, pk):
    form = PurchaseForm(request.POST)

    if form.is_valid():
        new_purchase = form.save(commit=False)
        new_purchase.coin_id = pk
        new_purchase.save()
    return redirect('detail', coin_id=pk)

def assoc_investor(request, pk, investor_pk):
  Coin.objects.get(id=pk).investors.add(investor_pk)
  return redirect('detail', coin_id=pk)

def assoc_delete(request, pk, investor_pk):
    Coin.objects.get(id=pk).investors.remove(investor_pk)
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

class InvestorList(ListView):
  model = Investor

class InvestorDetail(DetailView):
  model = Investor

class InvestorCreate(CreateView):
  model = Investor
  fields = ['name']

class InvestorUpdate(UpdateView):
  model = Investor
  fields = ['name']

class InvestorDelete(DeleteView):
  model = Investor
  success_url = '/investors'

