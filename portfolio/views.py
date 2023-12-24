from django.shortcuts import render
from .forms import StockTickerForm
from .models import Stock
from django.conf import settings
import os
import yfinance as yf
import plotly.graph_objects as go


def index(request):
    welcome = os.path.join(settings.BASE_DIR, 'portfolio/static/portfolio/text/welcome.txt')
    with open(welcome, 'r') as file:
        welcome_content = file.read()

    return render(request, "portfolio/index.html",{
        'welcome_text': welcome_content
    })


def professional_details(request):
    solirius = os.path.join(settings.BASE_DIR, 'portfolio/static/portfolio/text/solirius.txt')
    with open(solirius, 'r') as file:
        solirius_content = file.read()

    birmingham = os.path.join(settings.BASE_DIR, 'portfolio/static/portfolio/text/birmingham.txt')
    with open(birmingham, 'r') as file:
        birmingham_content = file.read()

    return render(request, "portfolio/professional_details.html", {
        'solirius_description': solirius_content,
        'birmingham_description': birmingham_content
    })


def personal_interests(request):
    return render(request, "portfolio/personal_interests.html")


def take_in_stock_price(request):
    form = StockTickerForm()
    all_searches = Stock.objects.all().order_by("-date_searched")
    previous_searches = all_searches[:10]

    if request.method == 'POST':
        form = StockTickerForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            stock_data = yf.Ticker(ticker)
            historical_data = stock_data.history(period='1d', interval='2m')

            stock_obj, created = Stock.objects.get_or_create(ticker=ticker)
            if created:
                stock_obj.company_name = ticker
            stock_obj.save()
            previous_searches = Stock.objects.all().order_by("date_searched").reverse()

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
                'graph_div': graph_div,
                'previous_searches': previous_searches
            })

    return render(request, 'portfolio/stock_form.html', {
        'form': form,
        'previous_searches': previous_searches
    })


def wordle_game(request):
    return render(request, 'portfolio/wordle.html')
