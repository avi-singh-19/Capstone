from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=100)
    date_searched = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.company_name} with ticker {self.ticker} last searched on {self.date_searched.strftime("%B %d %Y at %I:%M %p")}'
