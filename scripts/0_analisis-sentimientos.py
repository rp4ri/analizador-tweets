# Un script para analizar sentimientos en ../data/0_raw/0_raw.xlsx y
# guardar los resultados en ../data/1_intermediate/0_intermediate-sentimientos.xlsx

import pandas as pd

import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud

from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('stopwords')
stop_words = stopwords.words('spanish')

# leer los datos
def get_raw():
    """read the raw file and return a dataframe with the data
    Returns:
        df(pd.DataFrame): a dataframe with the raw data
    """
    df = pd.read_excel('data/0_raw/0_raw.xlsx')
    return df
# funciones para crear nuevas columnas
def compound_nltk(text):
    try:
        return SentimentIntensityAnalyzer().polarity_scores(text)['compound']
    except:
        return None

def polarity_tb(text):
    try:
        return TextBlob(text).sentiment.polarity
    except:
        return None

def subjectivity_tb(text):
    try:
        return TextBlob(text).sentiment.subjectivity
    except:
        return None
# main, generate the intermediate file
def main():
    df = get_raw()
    
    # apply the functions to the dataframe
    df['compound_nltk'] = df['texto-traducido'].apply(compound_nltk)
    df['polarity_tb'] = df['texto-traducido'].apply(polarity_tb)
    df['subjectivity_tb'] = df['texto-traducido'].apply(subjectivity_tb)

    df.to_json('data/1_intermediate/0_intermediate-sentimientos.json', orient='records', lines=True)
    #df.to_excel('data/1_intermediate/0_intermediate-sentimientos.xlsx', index=False)
# run the script
if __name__ == '__main__':
    main()