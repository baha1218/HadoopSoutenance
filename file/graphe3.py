import matplotlib.pyplot as plt
import csv

# On crée des listes pour stocker les années et le nombre de montants par année
annees = []
montants_par_annee = {}

# On ouvre le fichier CSV et on lit les données ligne par ligne
with open('result.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        # On récupère l'année et le montant de la ligne
        annee = int(row[3])
        montant = int(row[8])
        
        # On ajoute l'année à la liste des années si elle n'est pas déjà présente
        if annee not in annees:
            annees.append(annee)
        
        # On ajoute le montant à la liste des montants par année
        if annee not in montants_par_annee:
            montants_par_annee[annee] = 0
        montants_par_annee[annee] += montant

# On trie la liste des années dans l'ordre chronologique
annees.sort()

# On crée un graphique de courbe avec les données
plt.plot(annees, [montants_par_annee[a] for a in annees])

# On ajoute un titre et des labels d'axe
plt.title('Nombre de montants par année')
plt.xlabel('Année')
plt.ylabel('Montants')

# On affiche le graphique
plt.show()