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