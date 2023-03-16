import matplotlib.pyplot as plt
import csv

data = {}

# Read data from CSV file
with open('result.txt', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header
    for row in reader:
        tranche_horaire = row[7]
        montants = int(row[8])
        if tranche_horaire not in data:
            data[tranche_horaire] = montants
        else:
            data[tranche_horaire] += montants

# Create pie chart
labels = list(data.keys())
values = list(data.values())
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Nombre de montants par tranche horaire')
plt.show()