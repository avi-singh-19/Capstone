from django.shortcuts import render
from .forms import StockTickerForm
import yfinance as yf


def index(request):
    return render(request, "portfolio/index.html")


def professional_details(request):
    return render(request, "portfolio/professional_details.html")


def personal_interests(request):
    return render(request, "portfolio/personal_interests.html")


def take_in_stock_price(request):
    form = StockTickerForm()  # Initialize form outside the conditional block
    if request.method == 'POST':
        form = StockTickerForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            stock_data = yf.Ticker(ticker)
            historical_data = stock_data.history(period='1d')

            if not historical_data.empty and 'Close' in historical_data:
                last_price = historical_data['Close'].iloc[-1]
                message = None
            else:
                message = f"No historical data available for {ticker}, please try a valid ticker. Company names do " \
                          f"not work here, sorry about that."
                last_price = None

            return render(request, 'portfolio/stock_price.html', {
                'ticker': ticker,
                'last_price': last_price,
                'message': message
            })

    return render(request, 'portfolio/stock_form.html', {'form': form})
