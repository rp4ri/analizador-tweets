# coding: cp1252

import pandas as pd

def get_sentimientos():
    """read the raw file and return a dataframe with the data
    Returns:
        df(pd.DataFrame): a dataframe with the raw data
    """
    df = pd.read_json('data/1_intermediate/0_intermediate-sentimientos.json', orient='records', lines=True)
    df = df.drop_duplicates(subset=['texto-original'])
    df = df.drop(columns=['texto-traducido'])

    df.to_excel('data/2_processed/1_sentimientos.xlsx', index=False)
    return df
def get_puntos3d():
    """read the raw file and return a dataframe with the data
    Returns:
        df(pd.DataFrame): a dataframe with the raw data
    """
    df = pd.read_excel('data/2_processed/0_texto(sinrep)_puntos3d.xlsx')
    df = df.drop(df.columns[0], axis=1)

    return df
def main():
    sentimientos = get_sentimientos()
    puntos3d = get_puntos3d()
    
    html = f'''
    <!DOCTYPE html>
    <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">

            <title>Resumen de los resultados obtenidos</title>

            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="estilos/styles.css">
        </head>
        <body>
        <div class="section padding-bottom-big over-hide">
        <div class="container">
        <div class="row">
        <div class="col-12 text-center mt-3 mb-2">
        <div class="blog-post-text">
            <h2>Tablas obtenidas</h2>
            <p class="mb-3 mt-3">A continuación se describirá las tablas generadas.</p>

            <h3>Tabla de tweets en espacio 3D</h3>
            <p class="mb-3 mt-3">Obtenida al aplicar el modelo BERT preentrenado para español a los tweets, y reducirlos a 3 dimensiones.</p>
            ''' + puntos3d.head(3).to_html().replace('<tr style="text-align: right;">', '<tr style="text-align: center;">') + '''

            <p class="mb-3 mt-3">Al hacer clustering se generó la grafica 3_elbow-method.png con el propósito de aplicar el método elbow</p>
            <img src='figures/3_elbow-method.png' width="700">

            <p class="mb-3 mt-3">La gráfica 3_count_elements_in_clusters.png muestra la cantidad de elementos en cada cluster al aplicar el algoritmo de clustering a nuestra tabla.</p>
            <img src='figures/3_count_elements_in_clusters.png' width="700">

            <p class="mb-3 mt-3">El archivo 3d-scatter-plot.html es una visualización interactiva de los puntos en el espacio tridimensional.</p>
            ''' + '''<img src='figures/3d-scatter-plot.png' width="700">''' + '''

            <h3>Tabla de análisis de sentimientos</h3>
            <p class="mb-3 mt-3">Obtenida al aplicar un análisis de sentimientos a los tweets.</p>
            ''' + sentimientos.head(3).to_html().replace('<tr style="text-align: right;">', '<tr style="text-align: center;">') + '''
            <p class="mb-3 mt-3">La siguiente tabla es una descripción de la tabla obtenida.</p>
            <div style="margin: auto; display: block; width: 50%;">''' + sentimientos.describe().loc[['count', 'mean', 'min', 'max']].to_html().replace('<tr style="text-align: right;">', '<tr style="text-align: center;">').replace('<table border="1" class="dataframe">', '<table border="1" class="dataframe" style="margin : auto;">') + '''</div>

            <p class="mb-3 mt-3">Al analizar el texto, se generó una nube de palabras wordcloud.png.</p>
            <img src='figures/wordcloud.png' width="700">
        </div>
        </div>
        </div>
        </div>
        </div>
        </body>
    </html>
    '''

    with open('reports/html_report.html', 'w', encoding="utf-8") as f:
        f.write(html)
if __name__ == '__main__':
    main()
