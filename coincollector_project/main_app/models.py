from django.db import models
from django.urls import reverse

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'coin_id': self.id})
