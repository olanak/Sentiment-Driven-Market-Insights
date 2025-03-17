from textblob import TextBlob

def calculate_sentiment(data, column):
    """
    Calculate sentiment polarity for a text column.
    :param data: DataFrame containing the text data.
    :param column: Name of the column to analyze.
    :return: DataFrame with an added sentiment column.
    """
    data['sentiment'] = data[column].apply(lambda x: TextBlob(x).sentiment.polarity)
    return data