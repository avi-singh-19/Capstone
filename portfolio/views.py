from django.shortcuts import render
from .forms import StockTickerForm
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go


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
            historical_data = stock_data.history(period='1d', interval='2m')

            if not historical_data.empty and 'Close' in historical_data:
                last_price = historical_data['Close'].iloc[-1]
                message = None

                figure = go.Figure(data=go.Scatter(
                    x=historical_data.index,
                    y=historical_data['Close'],
                    mode='lines+markers',
                    line=dict(color='blue', width=2, dash='solid')
                ))
                figure.update_layout(
                    title=ticker + ' 24 Hour Stock Price',
                    yaxis_title='Stock Price (USD per Shares)'
                )

                graph_div = figure.to_html(full_html=False)

            else:
                message = f"No historical data available for {ticker}, please try a valid ticker. Company names do " \
                          f"not work here, sorry about that."
                last_price = None
                graph_div = None

            return render(request, 'portfolio/stock_price.html', {
                'ticker': ticker,
                'last_price': last_price,
                'message': message,
                'graph_div': graph_div
            })

    return render(request, 'portfolio/stock_form.html', {'form': form})
