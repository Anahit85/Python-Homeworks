"""Insertion Sort"""

# Beispiel-Liste (unsortiert)
data = [5, 3, 8, 2, 1]

# Funktion für Insertion Sort
def insertionSort(data):

    steps = 0  # Zählt wie viele Schritte gemacht werden

    # Wir starten beim zweiten Element (Index 1)
    for i in range(1, len(data)):

        # Speichert das aktuelle Element
        current = data[i]

        # Index für Vergleich mit vorherigen Elementen
        j = i - 1

        # Verschiebt größere Elemente nach rechts
        while j >= 0 and data[j] > current:
            data[j + 1] = data[j]
            j -= 1
            steps += 1

        # Setzt das aktuelle Element an die richtige Stelle
        data[j + 1] = current

    # Anzahl der Schritte ausgeben
    print("Schritte:", steps)

    # Sortierte Liste zurückgeben
    return data


# Funktion aufrufen
print("Sortierte Liste:", insertionSort(data))



"""Selection Sort"""
data = [5,2,7,4,1,3,6]

def selectionSort(data):
    steps = 0
    marker = 0

    while marker < len(data):
        steps += 1
        minIndex = marker   # Index des kleinsten Elements

        # Suche das kleinste Element im restlichen Array
        for i in range(marker, len(data)):
            steps += 1
            if data[i] < data[minIndex]:
                minIndex = i

        # Tausche aktuelles Element mit kleinstem Element
        data[marker], data[minIndex] = data[minIndex], data[marker]

        marker += 1

    print("Schritte:", steps)
    return data


print(selectionSort(data))

"""Bubble Sort"""


def bubbleSort(data):  # Funktion bubbleSort wird definiert. Sie bekommt eine Liste "data".

    steps = 0  # Variable zum Zählen der Schritte (Vergleiche / Durchläufe)

    swapped = True  # Startwert: True bedeutet, dass eventuell noch getauscht werden muss

    while swapped == True:  # Solange im letzten Durchlauf ein Tausch passiert ist,
        # läuft die Schleife weiter

        steps += 1  # Ein Schritt wird gezählt

        swapped = False  # Wir nehmen zuerst an: es gibt keinen Tausch

        for i in range(0, len(data) - 1):  # Schleife durch die Liste (bis vor das letzte Element)

            steps += 1  # Vergleichsschritt zählen

            if data[i] > data[i + 1]:  # Prüfen: ist das linke Element größer als das rechte?

                # Wenn ja → Elemente tauschen
                data[i], data[i + 1] = data[i + 1], data[i]

                swapped = True  # Es gab einen Tausch → wir müssen noch einmal prüfen

    print(steps)  # Anzahl der Schritte ausgeben

    return data  # Sortierte Liste zurückgeben


print(bubbleSort(data))  # Funktion ausführen und Ergebnis ausgeben




"""Quick Sort"""
def quickSort(data):                     # Funktion quickSort wird definiert. Sie sortiert eine Liste.

    if len(data) < 2:                    # Wenn die Liste weniger als 2 Elemente hat
        return data                      # ist sie bereits sortiert → zurückgeben

    pivot = data[len(data)//2]           # Pivot-Element auswählen (mittleres Element der Liste)

    part1 = []                           # Liste für Elemente kleiner als Pivot
    middle = []                          # Liste für Elemente gleich dem Pivot
    part2 = []                           # Liste für Elemente größer als Pivot

    for i in data:                       # Schleife durch alle Elemente der Liste
        if i < pivot:                    # Wenn Element kleiner als Pivot ist
            part1.append(i)              # → in Liste part1 speichern
        elif i == pivot:                 # Wenn Element gleich Pivot ist
            middle.append(i)             # → in Liste middle speichern
        else:                            # Wenn Element größer als Pivot ist
            part2.append(i)              # → in Liste part2 speichern

    # Rekursiv die Teil-Listen sortieren und zusammenfügen
    return quickSort(part1) + middle + quickSort(part2)


# Funktion ausführen und Ergebnis ausgeben
print(quickSort([5,4,3,2,1,5,7,8,9,6,66,22,0,-75]))



"""Merge Sort"""
def sort(part1, part2):            # Funktion zum Zusammenfügen (Merge) von zwei sortierten Listen
    result = []                    # Neue Liste für das Ergebnis
    i, j = 0, 0                    # Startindex für beide Listen

    # Solange beide Listen noch Elemente haben
    while i < len(part1) and j < len(part2):

        if part1[i] < part2[j]:    # Wenn Element aus part1 kleiner ist
            result.append(part1[i])# → in Ergebnisliste hinzufügen
            i += 1                 # Index von part1 erhöhen

        else:                      # Sonst ist Element aus part2 kleiner oder gleich
            result.append(part2[j])# → in Ergebnisliste hinzufügen
            j += 1                 # Index von part2 erhöhen

    # Falls noch Elemente in part2 übrig sind
    while j < len(part2):
        result.append(part2[j])    # Restliche Elemente anhängen
        j += 1

    # Falls noch Elemente in part1 übrig sind
    while i < len(part1):
        result.append(part1[i])    # Restliche Elemente anhängen
        i += 1

    return result                  # Zusammengeführte Liste zurückgeben



def devide(data):                  # Funktion zum Aufteilen der Liste
    if len(data) < 2:              # Wenn Liste weniger als 2 Elemente hat
        return data                # ist sie bereits sortiert

    else:
        middle = len(data)//2      # Mitte der Liste berechnen

        part1 = devide(data[:middle])  # Erste Hälfte rekursiv sortieren
        part2 = devide(data[middle:])  # Zweite Hälfte rekursiv sortieren

        return sort(part1, part2)      # Beide sortierten Hälften zusammenfügen


# Funktion ausführen
print(devide([1,45,20,24,47,65]))