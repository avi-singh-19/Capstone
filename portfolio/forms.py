from django import forms


class StockTickerForm(forms.Form):
    ticker = forms.CharField(label='Enter stock ticker')
