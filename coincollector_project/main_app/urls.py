from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coins/', views.coins_index, name='index'),
    path('coins/<int:coin_id>/', views.coins_detail, name='detail'),
    path('coins/create/', views.CoinCreate.as_view(), name='coins_create'),
    path('coins/<int:pk>/update/', views.CoinUpdate.as_view(), name='coins_update'),
    path('coins/<int:pk>/delete/', views.CoinDelete.as_view(), name='coins_delete'),
    path('coins/<int:pk>/add_purchase/', views.add_purchase, name='add_purchase'),
    
    path('coins/<int:pk>/assoc_investor/<int:investor_pk>/', views.assoc_investor, name='assoc_investor'),
    path('coins/<int:pk>/assoc_delete/<int:investor_pk>', views.assoc_delete, name='assoc_delete'),

    path('investors/', views.InvestorList.as_view(), name='investors_index'),
    path('investors/<int:pk>/', views.InvestorDetail.as_view(), name='investors_detail'),
    path('investors/create/', views.InvestorCreate.as_view(), name='investors_create'),
    path('investors/<int:pk>/update/', views.InvestorUpdate.as_view(), name='investors_update'),
    path('investors/<int:pk>/delete/', views.InvestorDelete.as_view(), name='investors_delete'),

]