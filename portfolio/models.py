from django.contrib.auth.models import AbstractUser
from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.ticker} - {self.company_name}'
