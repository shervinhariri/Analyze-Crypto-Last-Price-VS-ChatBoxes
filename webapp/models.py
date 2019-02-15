from django.db import models

# Create your models here.
class Exchanges(models.Model):
    exchange_name = models.CharField(max_length = 20)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.DecimalField(max_digits=7, decimal_places=3)
    #date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "NAME_IS : {}".format(self.exchange_name)