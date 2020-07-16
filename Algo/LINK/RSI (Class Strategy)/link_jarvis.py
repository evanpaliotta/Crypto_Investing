import os
import numpy as np
import pandas as pd
import ccxt
import asyncio

import hvplot.pandas
import panel as pn

pn.extension()


def initialize(cash=None):
    """Initialize the dashboard, data storage, and account balances."""
    print("Intializing Account and DataFrame")

    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # Initialize dataframe
    # @TODO: We will update this later!
    df = fetch_data()

    # Intialize the dashboard
    dashboard = build_dashboard()

    # @TODO: We will complete the rest of this later!
    return account, df, dashboard


def build_dashboard():
    """Build the dashboard."""
    loading_text = pn.widgets.StaticText(name="Trading Dashboard", value="Loading...")
    dashboard = pn.Column(loading_text)
    print("init dashboard")
    return dashboard


def update_dashboard(df, dashboard):
    """Update the dashboard."""
    dashboard[0] = df.hvplot()
    return


def fetch_data():
    """Fetches the latest prices."""
    kraken_public_key = os.getenv("KRAKEN_PUBLIC_KEY")
    kraken_secret_key = os.getenv("KRAKEN_SECRET_KEY")
    kraken = ccxt.kraken({"apiKey": kraken_public_key, "secret": kraken_secret_key})

    close = kraken.fetch_ticker("LINK/USD")["close"]
    datetime = kraken.fetch_ticker("LINK/USD")["datetime"]
    df = pd.DataFrame({"close": [close]})
    df.index = pd.to_datetime([datetime])
    return df


def generate_signals(df):
    """Generates trading signals for a given dataset."""
    print("Generating Signals")
    # Set window
    window_length = 14

    signals = df.copy()
    
    signals['Delta'] = signals['close'].diff()
    signals = signals.dropna()
    
    up, down = signals['Delta'].copy(),signals['Delta'].copy()
    up[up < 0] = 0
    down[down > 0] = 0
    
    # Calculate the EWMA
    roll_up1 = up.ewm(span=window_length).mean()
    roll_down1 = down.abs().ewm(span=window_length).mean()

    # Calculate the RSI based on EWMA
    RS1 = roll_up1 / roll_down1
    signals['RSI1'] = 100.0 - (100.0 / (1.0 + RS1))
    
    signals["signal"] = 0.0


    # Generate the trading signal 0 or 1,
    signals['short'] = np.where(signals['RSI1'] > 70, -1.0, 0.0)
    signals['long'] = np.where(signals['RSI1'] < 30, 1.0, 0.0)


    # Calculate the points in time at which a position should be taken, 1 or -1
    signals["entry/exit"]  = signals['short'] + signals['long']

    return signals


def execute_trade_strategy(signals, account):
    """Makes a buy/sell/hold decision."""

    print("Executing Trading Strategy!")

    if signals["entry/exit"].iloc[-1] == 1.0:
        print("buy")
        number_to_buy = round(account["balance"] / signals["close"].iloc[-1], 0) * 0.001
        account["balance"] -= number_to_buy * signals["close"].iloc[-1]
        account["shares"] += number_to_buy
    elif signals["entry/exit"].iloc[-1] == -1.0:
        print("sell")
        account["balance"] += signals["close"].iloc[-1] * account["shares"]
        account["shares"] = 0
    else:
        print("hold")

    return account


account, df, dashboard = initialize(10000)
dashboard.servable()


async def main():
    loop = asyncio.get_event_loop()

    while True:
        global account
        global df
        global dashboard

        new_df = await loop.run_in_executor(None, fetch_data)
        df = df.append(new_df, ignore_index=True)

        min_window = 22
        if df.shape[0] >= min_window:
            signals = generate_signals(df)
            account = execute_trade_strategy(signals, account)

        update_dashboard(df, dashboard)

        await asyncio.sleep(1)


# Python 3.7+
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# panel serve --log-level debug --show blocked_dashboard.py 