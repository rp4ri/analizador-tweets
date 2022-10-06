# analizador-tweets

- **By:** Rodrigo Pari

- **Contact:** rodrigo.parisusao25201@gmail.com

Proyecto con scripts básicos para analizar tweets en general.

## Licence


This project has not a license file


## Directories Distribution
```
├── LICENCE
├── README.md
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
│   ├── figures
│   │   ├── 3d-scatter-plot.html
│   │   └── wordcloud.png
├── requirements.txt
├── scripts
│   ├── 0_analisis-sentimientos.py
│   ├── 1_
│   ├── 2_
│   ├── 3_
│   ├── 4_
│   └── 5_
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

- Crear un nuevo entorno con conda:

```
conda env create -f environment.yml
activate analizador_tweets
```

- Si usás pip

crear un nuevo entorno para este proyecto (env es el nombre del entorno, pero podría tener otro nombre)  

``` 
python3 -m venv env
```

activar el entorno


``` 
source env/bin/activate
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
