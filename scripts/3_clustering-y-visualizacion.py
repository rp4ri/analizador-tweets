import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import plotly.graph_objs as go
import seaborn as sns

from sklearn.cluster import KMeans

def get_raw():
    """read the raw file and return a dataframe with the data
    Returns:
        df(pd.DataFrame): a dataframe with the raw data
    """
    df = pd.read_excel('data/0_raw/0_raw.xlsx')
    return df
def get_vectores_reducidos():
    """read the intermediate file and return a dataframe with the data
    Returns:
        df(pd.DataFrame): a dataframe with the intermediate data
    """
    df = pd.read_json('data/1_intermediate/1_intermediate-vectores-reducidos-pca.json', orient='records', lines=True)
    return df
def preproc_clusters(df1, df2):
    """using the dataframe with the reduced vectors, and the raw, we create a new dataframe
    Returns:
        df(pd.DataFrame): a dataframe with the raw data and the reduced vectors
    """
    df1 = df1.drop_duplicates(subset=['texto-original'])
    df1 = df1['texto-original']

    df = pd.concat([df1, df2], axis=1)
    return df
def get_elbow_and_clustering(df, n_clusters=5):
    X = df.iloc[:, 1:4].values
    # delete nan's
    X = X[~np.isnan(X).any(axis=1)]

    WCSS = []
    for i in range(1,11):
        model = KMeans(n_clusters = i,init = 'k-means++')
        model.fit(X)
        WCSS.append(model.inertia_)
    fig = plt.figure(figsize = (7,7))

    # export fig to html file in reports/figures
    plt.plot(range(1,11),WCSS)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.savefig('reports/figures/3_elbow-method.png')

    model = KMeans(n_clusters = n_clusters, init = "k-means++", max_iter = 300, n_init = 10, random_state = 0)
    model.fit(X)

    #sns.set_style("darkgrid", {"axes.facecolor": ".9"})
    #plt.style.use('dark_background')
    sns.countplot(y_clusters)

    plt.savefig('reports/figures/3_count_elements_in_clusters.png')

    Scene = dict(xaxis = dict(title  = '<-- x -->'),yaxis = dict(title  = '<-- y -->'),zaxis = dict(title  = '<-- z -->'))

    # model.labels_ is nothing but the predicted clusters i.e y_clusters
    # , hover_name="text"
    labels = model.labels_
    #trace = go.Scatter3d(x=X[:, 0], y=X[:, 1], z=X[:, 2], mode='markers',marker=dict(color = labels, size= 10, line=dict(color= 'black',width = 10),opacity=0.8))
    trace = go.Scatter3d(x=X[:, 0],
                        y=X[:, 1],
                        z=X[:, 2],
                        mode='markers',
                        # in text put first 50 characters of the tweet
                        text=df['texto-original'].str[:150],
                        marker=dict(color = labels, size= 10, line=dict(color= 'black',width = 10),opacity=0.8))
    layout = go.Layout(margin=dict(l=0,r=0),scene = Scene,height = 1200,width = 1200, template="plotly_dark")
    data = [trace]
    fig = go.Figure(data = data, layout = layout)

    fig.write_html("reports/figures/3d-scatter-plot.html")

    # export df to excel
    df.to_excel("data/2_processed/0_texto(sinrep)_puntos3d.xlsx")
def main():
    df_raw = get_raw()
    df_vectores_reducidos = get_vectores_reducidos()
    df = preproc_clusters(df_raw, df_vectores_reducidos)
    get_elbow_and_clustering(df, n_clusters=5)

if __name__ == '__main__':
    main()