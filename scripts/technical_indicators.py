import pandas as pd
import talib

def calculate_technical_indicators(data):
    """
    Calculate Moving Averages, RSI, and MACD using TA-Lib.
    :param data: DataFrame containing stock price data.
    :return: DataFrame with new columns for technical indicators.
    """
    data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)  # 20-day Simple Moving Average
    data['EMA_20'] = talib.EMA(data['Close'], timeperiod=20)  # 20-day Exponential Moving Average
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)  # Relative Strength Index (14 days)

    # MACD Calculation
    data['MACD'], data['MACD_signal'], data['MACD_hist'] = talib.MACD(data['Close'], 
                                                                      fastperiod=12, 
                                                                      slowperiod=26, 
                                                                      signalperiod=9)
    return data
