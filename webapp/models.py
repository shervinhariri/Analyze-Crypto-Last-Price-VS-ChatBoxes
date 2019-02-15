from django.db import models

# Create your models here.
class exchnges(models.Model):
    exchnge_name = models.Charfield(max_length = 20)