import pandas as pd
from textblob import TextBlob
from scipy.stats import pearsonr


def align_datasets_by_date(news_df, stock_df, news_date_col='date', stock_date_col='Date'):
    """
    Align and normalize dates in news and stock datasets.
    
    Args:
        news_df (pd.DataFrame): DataFrame containing news data.
        stock_df (pd.DataFrame): DataFrame containing stock price data.
        news_date_col (str): Column name for dates in news_df.
        stock_date_col (str): Column name for dates in stock_df.
    
    Returns:
        tuple: (normalized_news_df, normalized_stock_df)
    """
    # Convert to datetime and normalize both to date only (no time part)
    news_df = news_df.copy()
    stock_df = stock_df.copy()
    
    news_df[news_date_col] = pd.to_datetime(news_df[news_date_col], errors='coerce').dt.date
    stock_df[stock_date_col] = pd.to_datetime(stock_df[stock_date_col], errors='coerce').dt.date
    
    # Optionally: filter to keep only dates that exist in both datasets
    common_dates = set(news_df[news_date_col]).intersection(set(stock_df[stock_date_col]))
    news_df = news_df[news_df[news_date_col].isin(common_dates)]
    stock_df = stock_df[stock_df[stock_date_col].isin(common_dates)]
    
    # Sort by date (optional but clean)
    news_df = news_df.sort_values(by=news_date_col).reset_index(drop=True)
    stock_df = stock_df.sort_values(by=stock_date_col).reset_index(drop=True)
    
    return news_df, stock_df



def perform_sentiment_analysis(news_df, headline_col='headline'):
    """
    Perform sentiment analysis on news headlines.
    
    Args:
        news_df (pd.DataFrame): DataFrame containing news headlines.
        headline_col (str): Column name of the headline text.
    
    Returns:
        pd.DataFrame: The input DataFrame with an added 'Sentiment_Score' column.
    """
    news_df = news_df.copy()
    
    def get_sentiment(text):
        analysis = TextBlob(str(text))
        return analysis.sentiment.polarity  # Range: -1 (negative) to 1 (positive)
    
    news_df['Sentiment_Score'] = news_df[headline_col].apply(get_sentiment)
    
    return news_df



def analyze_correlation_between_sentiment_and_returns(stock_data, news_data):
    news_data = news_data.copy()
    news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce')
    
    # Group by just the date (not datetime)
    daily_sentiment = news_data.groupby(news_data['date'].dt.date)['Sentiment_Score'].mean().reset_index()
    daily_sentiment.rename(columns={'date': 'Date', 'Sentiment_Score': 'Avg_Sentiment_Score'}, inplace=True)
    daily_sentiment.columns = ['Date', 'Avg_Sentiment_Score']  # make sure columns are correct
    
    # If your stock_data['Date'] is also datetime, convert to .dt.date for proper matching
    stock_data = stock_data.copy()
    stock_data['Date'] = pd.to_datetime(stock_data['Date'], errors='coerce')
    stock_data['Date'] = stock_data['Date'].dt.date
    
    merged_df = pd.merge(stock_data, daily_sentiment, on='Date', how='inner')
    return merged_df

