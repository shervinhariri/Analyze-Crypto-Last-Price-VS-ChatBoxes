from django.db import models

# Create your models here.
class Exchanges(models.Model):
    exchange_name = models.CharField(max_length = 20)

    def __str__(self):
        return "NAME_IS : {}".format(self.exchange_name)