import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import talib
import pynance as pn

def calculate_movig_avg(data, window):


    return data.rolling(window=window).mean()
    

def analyze_text_lengths(data, column):
    """
    Analyze the lengths of text in a specified column.
    :param data: DataFrame containing the text data.
    :param column: Name of the column to analyze.
    :return: Series of descriptive statistics for text lengths.
    """
    data['text_length'] = data[column].apply(len)
    return data['text_length'].describe()

def count_articles_by_publisher(data, column):
    """
    Count the number of articles per publisher.
    :param data: DataFrame containing the data.
    :param column: Name of the column containing publisher information.
    :return: Series of article counts by publisher.
    """
    return data[column].value_counts()

def extract_top_keywords(data, column, top_n=10):
    """
    Extract the top keywords from a text column using TF-IDF.
    :param data: DataFrame containing the text data.
    :param column: Name of the column to analyze.
    :param top_n: Number of top keywords to extract.
    :return: DataFrame with top keywords and their TF-IDF scores.
    """
    vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
    tfidf_matrix = vectorizer.fit_transform(data[column])
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.sum(axis=0).A1
    return pd.DataFrame({
        "keyword": feature_names,
        "score": tfidf_scores
    }).sort_values(by="score", ascending=False)

def calculate_rsi(data, period):
    """
    Calculate the Relative Strength Index (RSI) for a given DataFrame.
    :param data: DataFrame with a 'Close' price column.
    :param period: Time period for RSI calculation (default 14).
    :return: DataFrame with an additional 'RSI' column.
    """
    data['RSI'] = talib.RSI(data['Close'], timeperiod=period)
    return data

def calculate_MACD(data):
    """
    Calculate the MACD for a given DataFrame.
    :param data: DataFrame with a 'Close' price column.
    :return: DataFrame with an additional 'MACD', 'MACD_Signal', and 'MACD_Hist' column.
    """  
    macd, macd_signal, macd_hist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    data['MACD'] = macd
    data['MACD_Signal'] = macd_signal
    data['MACD_Hist'] = macd_hist
    
    return data


def compute_indicators(data, sma_window=50, ema_window=20):
    """
    Compute SMA and EMA using TA-Lib and add them to the DataFrame.
    
    Parameters:
    - data: DataFrame containing the column 'Close'
    - sma_window: int, period for Simple Moving Average
    - ema_window: int, period for Exponential Moving Average
    
    Returns:
    - DataFrame with added SMA and EMA columns
    """
    data = data.copy()
    #data = {'Close': [100, 102, 105, 110, 108, 107, 105, 106, 109, 111, 115, 116, 118]}
    # Check required columns
    if 'Close' not in data.columns:
        raise ValueError("Missing required column: 'Close'")
    
    # Calculate Simple Moving Average (SMA)
    data['SMA'] = talib.SMA(data['Close'], timeperiod=sma_window)
    
    # Calculate Exponential Moving Average (EMA)
    data['EMA'] = talib.EMA(data['Close'], timeperiod=ema_window)
    
    return data

