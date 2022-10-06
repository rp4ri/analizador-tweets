import pandas as pd
import numpy as np

from sklearn.decomposition import PCA

import torch
from pytorch_transformers import *

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertModel.from_pretrained('bert-base-multilingual-cased')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def get_raw():
    """read the raw file and return a dataframe with the data
    Returns:
        df(pd.DataFrame): a dataframe with the raw data
    """
    df = pd.read_excel('data/0_raw/0_raw.xlsx')
    return df
def preproc_data_bert(df):
    tokenized = df.apply((lambda x: torch.tensor([tokenizer.encode(x, add_special_tokens=True)])))
    last_hidden_states = tokenized.apply(lambda x: model(x)[0])
    average = last_hidden_states.apply(lambda x: torch.mean(x, dim=1))

    # convert to numpy
    average = average.apply(lambda x: x.detach().numpy())
    # dimension (1, 768) to (768,)
    average = average.apply(lambda x: x[0])

    average.to_json('../data/1_intermediate/1_intermediate-vectores.json', orient='records', lines=True)
def get_vectores():
    """read the intermediate file and return a dataframe with the data
    Returns:
        df(pd.DataFrame): a dataframe with the intermediate data
    """
    df = pd.read_json('data/1_intermediate/1_intermediate-vectores.json', orient='records', lines=True)
    return df
def preproc_vectores(df):
    # convert to numpy
    df['vectores'] = df.apply(lambda x: x.iloc[0:].values, axis=1)
    df['vectores'] = df['vectores'].apply(lambda x: np.array(x))

    return df
def get_pca(df):
    pca = PCA(n_components=3)
    pca.fit(df['vectores'].values.tolist())
    df['vectores'] = df['vectores'].apply(lambda x: pca.transform([x])[0])

    df_transformed = pd.DataFrame(df['vectores'].values.tolist(), columns=['x', 'y', 'z'])
    return df_transformed
def main():
    df = get_raw()
    preproc_data_bert(df)
    df = get_vectores()
    df = preproc_vectores(df)
    df = get_pca(df)
    df.to_json('data/1_intermediate/1_intermediate-vectores-reducidos-pca.json', orient='records', lines=True)
if __name__ == '__main__':
    main()
