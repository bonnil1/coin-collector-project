from django.contrib import admin
from .models import Coin, Purchase, Investor

# Register your models here.
admin.site.register(Coin)
admin.site.register(Purchase)
admin.site.register(Investor)