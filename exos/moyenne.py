## Exercice avec les fichiers
## Calculer la moyenne des notes d'un fichier, une note par ligne
import statistics

notes = []
with open('notes.txt', 'r') as f:
    # pour chaque ligne du fichier
    for note in f:
        notes.append(int(note))

total = sum(notes)
moyenne = total / len(notes)
print(f"La moyenne des notes est {moyenne:.3}")

# ou avec la fonction 'mean' du module 'statistics'
moyenne = statistics.mean(notes)
print(f"La moyenne des notes est {moyenne:.3}")
