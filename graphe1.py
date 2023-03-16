import matplotlib.pyplot as plt

# Créer un dictionnaire pour stocker le nombre de montants par nom_gare
montants_par_gare = {}

# Ouvrir le fichier contenant les données et lire chaque ligne
with open("C:\\Users\\bmanaa\\Documents\\GitHub\\HadoopSoutenance\\result.txt") as fichier:
    for ligne in fichier:
        # Séparer chaque valeur de la ligne
        valeurs = ligne.split(",")
        nom_gare = valeurs[0]
        montant = int(valeurs[-1])
        
        # Ajouter le montant à la somme pour cette gare dans le dictionnaire
        if nom_gare in montants_par_gare:
            montants_par_gare[nom_gare] += montant
        else:
            montants_par_gare[nom_gare] = montant

# Trier les gares par ordre décroissant de montants
gares = sorted(montants_par_gare, key=montants_par_gare.get, reverse=True)

# Créer les listes de noms de gares et de montants correspondants pour le graphique
noms = []
montants = []
for gare in gares:
    noms.append(gare)
    montants.append(montants_par_gare[gare])

# Créer le graphique à barres horizontales
fig, ax = plt.subplots()
ax.barh(noms, montants)
ax.invert_yaxis()  # Inverser l'ordre des gares pour que les plus grandes soient en haut
ax.set_xlabel("Montants")
ax.set_ylabel("Gares")
ax.set_title("Nombre de montants par nom_gare")

plt.show()