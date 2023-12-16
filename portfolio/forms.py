from django import forms


class StockTickerForm(forms.Form):
    ticker = forms.CharField(label='Please enter a valid stock, commodity or ETF ticker')
