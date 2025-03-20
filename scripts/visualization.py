import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_publication_trends(data, date_column):
    """
    Plot the number of articles published over time.
    :param data: DataFrame containing the data.
    :param date_column: Name of the date column.
    :return: None (displays plot).
    """
    # Ensure the 'date_column' is in datetime format
    data[date_column] = pd.to_datetime(data[date_column], errors='coerce')
    data.groupby(data[date_column].dt.date).size().plot(kind='line', figsize=(10, 5))
    plt.title("Publication Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.show() 

def plot_sentiment_distribution(data, sentiment_column):
    """
    Plot the sentiment score distribution.
    :param data: DataFrame containing sentiment data.
    :param sentiment_column: The column containing sentiment scores.
    :return: None (displays plot).
    """
    sns.histplot(data[sentiment_column], bins=30, kde=True, color='blue')
    plt.title("Sentiment Distribution of Financial News Headlines")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.show()



def plot_moving_averages(data, stock_name):
    """
    Plot stock price along with SMA and EMA.
    :param data: DataFrame containing stock prices and moving averages.
    :param stock_name: Name of the stock for title.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Close'], label='Closing Price', color='blue')
    plt.plot(data['Date'], data['Moving Average'], label='Moving Avaerage', linestyle='dashed', color='red')

    plt.title(f"{stock_name} - Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.show()

def plot_rsi(data, title="RSI Indicator"):
    """
    Plot RSI indicator for stock data.
    :param data: DataFrame with 'Date' and 'RSI' columns.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('RSI Value')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_macd(data,stock_name):
    plt.figure(figsize=(14,7))

    # Plot Close Price
    plt.subplot(2,1,1)
    plt.plot(data['Close'], label='Close Price')
    plt.title(f'{stock_name} stock price and MACD')
    plt.legend()

    # Plot MACD
    plt.subplot(2,1,2)
    plt.plot(data['MACD'], label='MACD Line', color='blue')
    plt.plot(data['MACD_Signal'], label='Signal Line', color='red')
    plt.bar(data.index, data['MACD_Hist'], label='Histogram', color='grey', alpha=0.5)
    plt.legend()
    plt.show()


def plot_macd_with_signals(data, stock_name):
    
    # Make a safe copy to avoid SettingWithCopyWarning
    data = data.copy()
    
    # Identify bullish and bearish run start points
    data['Bullish_Run_Start'] = (data['MACD'] > data['MACD_Signal']) & (data['MACD'].shift(1) <= data['MACD_Signal'].shift(1))
    data['Bearish_Run_Start'] = (data['MACD'] < data['MACD_Signal']) & (data['MACD'].shift(1) >= data['MACD_Signal'].shift(1))

    # Identify bullish and bearish crossover points
    data['Bullish_Crossover'] = (data['MACD'] > data['MACD_Signal']) & (data['MACD'].shift(1) <= data['MACD_Signal'].shift(1))
    data['Bearish_Crossover'] = (data['MACD'] < data['MACD_Signal']) & (data['MACD'].shift(1) >= data['MACD_Signal'].shift(1))

    # Plot combined figure
    plt.figure(figsize=(16, 10))

    # Close Price with bullish/bearish run start markers
    plt.subplot(2, 1, 1)
    plt.plot(data['Close'], label='Close Price', color='black')
    plt.scatter(data.index[data['Bullish_Run_Start']], data['Close'][data['Bullish_Run_Start']], 
                marker='^', color='green', edgecolors='black', s=80, label='Start Bullish Run')
    plt.scatter(data.index[data['Bearish_Run_Start']], data['Close'][data['Bearish_Run_Start']], 
                marker='v', color='red', edgecolors='black', s=80, label='Start Bearish Run')
    plt.title(f'{stock_name} Close Price with Bullish & Bearish Run Starts')
    plt.grid(True, alpha=0.3)
    plt.legend()

    # MACD with crossovers
    plt.subplot(2, 1, 2)
    plt.plot(data['MACD'], label='MACD Line', color='blue', linewidth=1.5)
    plt.plot(data['MACD_Signal'], label='Signal Line', color='red', linewidth=1.5)
    plt.bar(data.index, data['MACD_Hist'], label='Histogram', color='grey', alpha=0.4)

    plt.scatter(data.index[data['Bullish_Crossover']], data['MACD'][data['Bullish_Crossover']], 
                marker='^', color='green', edgecolors='black', s=80, label='Bullish Crossover')
    plt.scatter(data.index[data['Bearish_Crossover']], data['MACD'][data['Bearish_Crossover']], 
                marker='v', color='red', edgecolors='black', s=80, label='Bearish Crossover')

    plt.title(f'{stock_name} MACD with Bullish & Bearish Crossovers')
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_indicators(data,stock_name, sma_window=50, ema_window=20):
    """
    Plot the Close price, SMA, and EMA.
    
    Parameters:
    - data: DataFrame containing the 'Close', 'SMA', and 'EMA' columns
    """
    plt.figure(figsize=(12, 6))
    
    # Plot Close price
    plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.7)
    
    # Plot SMA and EMA
    plt.plot(data['SMA'], label=f'{sma_window}-period SMA', color='red', linestyle='--')
    plt.plot(data['EMA'], label=f'{ema_window}-period EMA', color='green', linestyle='--')
    
    plt.title(f'{stock_name} Close Price, SMA, and EMA')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()



def plot_correlation(merged_df):
    """
    Plot scatter plot and regression line between daily stock returns and sentiment scores.
    
    Args:
        merged_df (pd.DataFrame): DataFrame containing 'Daily_Return' and 'Sentiment_Score' columns.
    """
    plt.figure(figsize=(10, 6))
    sns.regplot(
        x='Avg_Sentiment_Score', 
        y='Daily_Return', 
        data=merged_df, 
        scatter_kws={'alpha':0.6}, 
        line_kws={'color':'red'},
        ci=None
    )
    plt.title('Correlation Between Daily Sentiment Scores and Stock Returns', fontsize=14)
    plt.xlabel('Average Daily Sentiment Score', fontsize=12)
    plt.ylabel('Daily Stock Return (%)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
