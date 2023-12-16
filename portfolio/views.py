from django.shortcuts import render
from .forms import StockTickerForm
import yfinance as yf


def index(request):
    return render(request, "portfolio/index.html")


def take_in_stock_price(request):
    form = StockTickerForm()  # Initialize form outside the conditional block
    if request.method == 'POST':
        form = StockTickerForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            stock_data = yf.Ticker(ticker)
            last_price = stock_data.history(period='1d')['Close'].iloc[-1]
            return render(request, 'portfolio/stock_price.html', {
                'ticker': ticker,
                'last_price': last_price
            })

    return render(request, 'portfolio/stock_form.html', {'form': form})
