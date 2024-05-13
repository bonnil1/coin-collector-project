from django.db import models
from django.urls import reverse

# Create your models here.

class Investor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coins_detail', kwargs={'pk': self.id})
        
class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField(max_length=250)
    investors = models.ManyToManyField(Investor)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'coin_id': self.id})

class Purchase(models.Model):
    date = models.DateField()
    dollar_amount = models.FloatField()
    coin_amount = models.FloatField()

    # coin_id FK
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.coin_amount} on {self.date}'
    
    class Meta:
        ordering = ['-date']
