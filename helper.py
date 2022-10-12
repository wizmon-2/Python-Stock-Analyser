## Module to use rich , mplfinance and yfinance modules
## with stock picked from Main module
##

# Import modules
import yfinance as yf
import rich
from rich.layout import Layout
import totable
import pandas as pd
import mplfinance as mpf
from multiprocessing import Process

ticker = ""

# Method to load stock
def load(stock):
    global ticker
    ticker = yf.Ticker(stock)

# Method to make rich layout
def makelayout2(table1,table2):
    layout = Layout()

    layout.split_row(
    Layout(name="left"),
    Layout(name="right"),
    )

    layout["left"].size = 100
    layout["right"].size = 100

    layout['left'].update(table1)
    layout['right'].update(table2)

    return layout

# Method to check if stock exists
def checkStock():
    if (ticker.info['regularMarketPrice'] == None):
        return False
    else:
        return True

# Method to put picks throut picker method
def helper(picks):
    if type(picks) != list:
        picks = [picks]

    for pick in picks:
        picker(pick)

# Method to run appropriate methods selected by user
def picker(pick):
    if pick == 0:
        info()

    elif pick == 1:
        financials()

    elif pick == 2:
        balance_sheet()

    elif pick == 3:
        cashflow()

    elif pick == 4:
        earnings()

    elif pick == 5:
        analysis()

    elif pick == 6:
        Process(target=gmax, args=(ticker,)).start()

    elif pick == 7:
        Process(target=g5y, args=(ticker,)).start()

    elif pick == 8:
        Process(target=gytd, args=(ticker,)).start()

    elif pick == 9:
        Process(target=g1mo, args=(ticker,)).start()

    elif pick == 10:
        Process(target=g1d, args=(ticker,)).start()

    else:
        print("Invalid Choice")

# Method to print stock info
def info():
    inf = ticker.info
    df = pd.DataFrame.from_dict(inf, orient='index')

    table = totable.dft(df, title_name="Info")

    rich.print(table)

# Method to print stock financials
def financials():
    df1 = ticker.financials
    df2 = ticker.quarterly_financials

    table1 = totable.dft(df1, title_name="Financials")
    table2 = totable.dft(df2, title_name="Financials Quaterly")

    layout = makelayout2(table1, table2)

    rich.print(layout)

# Method to print stock balance sheet
def balance_sheet():
    df1 = ticker.balance_sheet
    df2 = ticker.quarterly_balance_sheet

    table1 = totable.dft(df1, title_name="Balance Sheet")
    table2 = totable.dft(df2, title_name="Balance Sheet Quaterly")

    layout = makelayout2(table1, table2)

    rich.print(layout)

# Method to print stock cash flow
def cashflow():
    df1 = ticker.cashflow
    df2 = ticker.quarterly_cashflow

    table1 = totable.dft(df1, title_name="Cash Flow")
    table2 = totable.dft(df2, title_name="Cash Flow Quaterly")

    layout = makelayout2(table1, table2)

    rich.print(layout)

# Method to print stock earnings
def earnings():
    df1 = ticker.earnings
    df2 = ticker.quarterly_earnings

    table1 = totable.dft(df1, title_name="Earnings")
    table2 = totable.dft(df2, title_name="Earnings Quaterly")

    rich.print(table1)
    rich.print(table2)

# Method to print stock analysis
def analysis():
    df = ticker.recommendations

    table = totable.dft(df, title_name="Analysis", convert=False)

    rich.print(table)

# Method to show graph of MAX period OHLS
def gmax(ticker):
    df = ticker.history(period="max")

    mpf.plot(df, type='line', volume=True, title='MAX')

# Method to show graph of 5 year period OHLS
def g5y(ticker):
    df = ticker.history(period="5y")

    mpf.plot(df, type='candle', volume=True, title='5Y')

# Method to show graph of current year OHLS
def gytd(ticker):
    df = ticker.history(period="ytd")

    mpf.plot(df, type='candle', volume=True, title='YTD')

# Method to show graph of 1 month period OHLS
def g1mo(ticker):
    df = ticker.history(period="1mo")

    mpf.plot(df, type='candle', volume=True, title='1MO')

# Method to show graph of 1 day period OHLS
def g1d(ticker):
    df = ticker.history(period="1d", interval="1m")

    mpf.plot(df, type='candle', volume=True, title='1D')