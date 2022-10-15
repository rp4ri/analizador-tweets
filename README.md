# analizador-tweets

- **By:** Rodrigo Pari

- **Contact:** rodrigo.parisusao25201@gmail.com

Proyecto con script básicos para analizar tweets en general.

## Licence


This project has not a license file


## Outputs

Se generará un archivo con un resumen del análisis de los tweets html_report.html, para visualizar el reporte de ejemplo se puede usar este enlace:

[https://rodrigopari.github.io/analizador-tweets/html_report.html]

Se generán dos tablas en excel:

- 0_texto(sinrep)_puntos3d.xlsx : Tabla con los tweets y sus respectivos puntos 3D obtenidos al aplicar BERT preentrenado.
- 1_sentimientos.xlsx : Tabla con los tweets sin repetir y los valores obtenidos al aplicar análisis sentimiento.

También se generarán los siguientes archivos

- 3_count_elements_in_clusters.png
- 3_elbow-method.png
- 3d-scatter-plot.html
- 3d-scatter-plot.png
- wordcloud.png

Entre los cuales se incluye una nube de palabras

![alt text](https://github.com/rp4ri/analizador_tweets/blob/main/reports/figures/wordcloud.png?raw=true)

Y un gráfico 3D interactivo generado usando plotly

![alt text](https://github.com/rp4ri/analizador_tweets/blob/main/reports/figures/3d-scatter-plot.png?raw=true)

## Directories Distribution
```
├── LICENCE
├── README.md
├── main.py
├── data
│   ├── 0_external
│   ├── 0_raw
│   │   └── 0_raw.xlsx
│   ├── 1_intermediate
│   │   ├── 0_intermediate-sentimientos.json
│   │   ├── 1_intermediate-vectores-reducidos-pca.json
│   │   └── 1_intermediate-vectores.json
│   └── 2_processed
│   │   ├── 0_texto(sinrep)_puntos3d.xlsx
│   │   └── 1_sentimientos.xlsx
├── docs
├── environment.yaml
├── notebooks
│   ├── 0.0-intro-analisis-sentimientos.ipynb
│   ├── 0.1-generar-nube-palabras.ipynb
│   ├── 0.2-bert-preentrenado.ipynb
│   ├── 0.3-reductor-de-dimension.ipynb
│   ├── 1.0-clustering.ipynb
│   └── 1.1-exportaciones-finales-html.ipynb
├── reports
│   ├── estilos
│   │   └── styles.css
│   ├── figures
│   │   ├── 3_count_elements_in_clusters.png
│   │   ├── 3_elbow-method.png
│   │   ├── 3d-scatter-plot.html
│   │   ├── 3d-scatter-plot.png
│   │   └── wordcloud.png
│   └── html_report.html
├── requirements.txt
├── scripts
│   ├── 0_analisis-sentimientos.py
│   ├── 1_generar-nube-palabras.py
│   ├── 2_generar-puntos-espacio3d.py
│   ├── 3_clustering-y-visualizacion.py
│   └── 4_exportaciones-creacion-html.py
├── setup.py
└── analizador_tweets_packages
    ├── __init__.py
    └── utils
        └── __init__.py 

```

## Datos

En este caso, 0_raw.xlsx en la carpeta data/0_raw funciona como el input, los datos en dicho archivo tienen que tener la forma:

| texto-traducido | texto-original |
|-----------------|----------------|
| The mayor came to visit | El alcalde vino de visita |
| Roses are pink | Las rosas son rosadas |

## Qué hay en cada carpeta?

- **data**: Carpeta donde se guardan los datos
- **docs**: Documentación del proyecto
- **notebooks**: Notebooks que usé para experimentar antes de escribir los scripts
- **reports**: Carpeta donde se guardan los outputs
- **scripts**: Carpeta donde se guardan los scripts
- **analizador_tweets_packages**: Aún no tengo nada planeado pa esta carpeta

## Activar el entorno
podés revisar las bibliotecas y dependencias a usar en el archivo *evironment.yalm*

- Si usás pip

crear un nuevo entorno para este proyecto usando virtualenv (env es el nombre del nuevo entorno, pero podría tener otro)

``` 
python3 -m venv env
```

activar el entorno


``` 
source env/Scripts/activate.bat
```
finalmente instalar las librerias:

``` 
pip install -r requirements.txt 
```

## Correr los scripts

simplemente hacer

```
python3 main.py
```

correrá todos los .py que estan en la carpeta scripts