import pandas as pd

import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud

nltk.download('stopwords')
stop_words = stopwords.words('spanish')

def get_raw():
    """read the raw file and return a dataframe with the data
    Returns:
        df(pd.DataFrame): a dataframe with the raw data
    """
    df = pd.read_excel('data/0_raw/0_raw.xlsx')
    return df
def preproc_data_nube(df):
    df = df["texto-original"]
    df = df.drop_duplicates()
    df = df.str.lower().str.replace('[^\w\s]','')

    for i in range(df.shape[0]):
        try:
            while '\n' in df.iloc[i]:
                df.iloc[i].text = df.iloc[i].text.replace('\n', ' ')
            while '\t' in df.iloc[i]:
                df.iloc[i].text = df.iloc[i].text.replace('\t', ' ')
        except:
            pass
    return df
def get_nube(df):
    """Generate a wordcloud from the text of the dataframe
    Args:
        df(pd.DataFrame): a dataframe
    Returns:
        wordcloud(WordCloud): a wordcloud object
    """
    stop_words = stop_words + ['rt', 'si', 'ser', 'q', 'tan', ',', '.', 'http', 'https', 't', 'co']
    wordcloud = WordCloud(width=800,
                    height=500,
                    background_color ='white',
                    stopwords=stop_words,
                    random_state=21,
                    max_font_size=150).generate(' '.join(df))
    #plt.figure(figsize=(20, 15))
    #plt.imshow(wordcloud, interpolation="bilinear")
    #plt.axis('off')
    #plt.show()
    return wordcloud
def main():
    df = get_raw()
    df = preproc_data_nube(df)
    wordcloud = get_nube(df)
    wordcloud.to_file('reports/figures/wordcloud.png')
if __name__ == '__main__':
    main()