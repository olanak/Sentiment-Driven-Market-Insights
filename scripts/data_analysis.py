import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

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