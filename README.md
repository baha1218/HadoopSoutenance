

# Soutenance Hadoop

Dans cette documentation vous trouverez la procedure pour monter la maquette que je présenterais lors de ma soutenance.



## Prérequis

- Git

- Docker Engine

- Docker Compose

- [Cluster Hadoop](https://github.com/baha1218/HadoopCluster)

- [Datanode distant](https://github.com/baha1218/HadoopDatanode)

- [Datanode distant](https://github.com/baha1218/HadoopPython)

## 🛠 Configuration

### Sur le Namenode : 

Nous allons telecharger des données et les push dans notre cluster.
Télechargez et renommez les données.

```bash
wget https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/comptage-voyageurs-trains-transilien/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B
mv csv\?lang\=fr sncf.csv
```

Poussez les données dans votre cluster
```bash
hadoop fs -put sncf.csv
```
Créer un fichier [sncf.py](https://github.com/baha1218/HadoopSoutenance/blob/main/file/sncf.py) et executez le.
```bash
nano test_spark.py
python3 test_spark.py
```

Affichez les données géneré dans le cluster
```bash
hadoop fs -cat /user/output/filename
```
Attention ! Votre fichier a surement un nom différent. Vous pouvez vérifier sur le webui ou avec un `hadoop fs -ls /user/output/`

Copiez l'output et créez un fichier [result.txt](https://github.com/baha1218/HadoopSoutenance/blob/main/file/result.txt).

### Windows 

Nous ne pouvons pas visualiser ces données sans interface graphique donc j'ai transféré mon fichier [result.txt](https://github.com/baha1218/HadoopSoutenance/blob/main/file/result.txt) sur mon windows avec python d'installer. Un fichier [sncf.py](https://github.com/baha1218/HadoopSoutenance/blob/main/file/sncf.py) doit aussi etre créer dans le meme repertoire que vos 3 scripts pour graphique ([graphe1.py](https://github.com/baha1218/HadocopSoutenance/blob/main/file/graphe1.py), [graphe2.py](https://github.com/baha1218/HadocopSoutenance/blob/main/file/graphe2.py), [graphe3.py](https://github.com/baha1218/HadocopSoutenance/blob/main/file/graphe3.py)).

Rendez vous avec le `cmd` dans l'emplacement où se trouve vos fichiers.
Vous devez avoir installer Python sur windows. N'oubliez pas d'installer matplotlib.
```bash
pip install matplotlib
```
Pour finir, affichez votre graphique.
```bash
python3 graphe1.py
```
