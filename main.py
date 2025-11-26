# Inizializzazione del dizionario per i dati del triangolo
import math
superTriangolo = {
    'L0': {'E': 0, 'V': None, 'N': None}, #base
    'L1': {'E': 0, 'V': None, 'N': None}, #primo lato adiacente
    'L2': {'E': 0, 'V': None, 'N': None}, #secondo lato adiacente
    'A0': {'E': 0, 'V': None, 'N': None, 'R': None}, #angolo opposto alla base
    'A1': {'E': 0, 'V': None, 'N': None, 'R': None}, #primo angolo adiacente
    'A2': {'E': 0, 'V': None, 'N': None, 'R': None}, #secondo angolo adiacente
    'H': {'E': 0, 'V': None}, #altezza
    'AREA': {'V': None}, #area
    'PERIMETRO': {'V': None} #perimetro
}
primeTriangolo = {
    'ordine_lati': {
        "AB": ["AB", "BC", "AC"],
        "BC": ["BC", "AC", "AB"],
        "AC": ["AC", "AB", "BC"]
    },
    'ordine_angoli': {
        "AB": ["C", "A", "B"],
        "BC": ["A", "B", "C"],
        "AC": ["B", "C", "A"]
    }
}
subTriangolo = {
    'L0': {'V': None, 'S': None}, #base
    'L1': {'V': None, 'S': None}, #primo lato
    'L2': {'V': None, 'S': None}, #secondo lato
    'A0': {'V': None, 'S': None, 'R': None}, #angolo opposto alla base
    'A1': {'V': None, 'S': None, 'R': None}, #primo angolo
    'A2': {'V': None, 'S': None, 'R': None}, #secondo angolo
    'H': {'V': None}, #altezza
}
paradigmi = {
    'P1': {
        'STEPS': {
            '0': ['', '#comment'],
            '1': ['', '#comment']
        },
        'RESULT': {'AREA': None, 'PERIMETRO': None}
    }
}
# Inizializzazione della base e della althezza
while True:
    radice = input('\033[36m' + "Quale lato viene considerato come la base (AB/BC/AC): " + '\033[0m').strip().upper()
    if radice in primeTriangolo['ordine_lati']:
        break
    print('\033[91m' + "Input non valido! Inserisci AB, BC o AC" + '\033[0m')
for indice in range(0, 3):
    superTriangolo[f'L{indice}']['N'] = primeTriangolo['ordine_lati'][radice][indice]
for indice in range(0, 3):
    superTriangolo[f'A{indice}']['N'] = primeTriangolo['ordine_angoli'][radice][indice]

if input('\033[36m' + "Si conosce l'altezza relativa alla base? (S/N): "+ '\033[0m').strip().upper() == "S":
    superTriangolo['H']['E'] = 1
# Funzioni di conversione
def convlato(valore):
    if valore.upper() == "X":
        return None
    try:
        return float(valore)
    except ValueError:
        print('\033[91m' + "Valore non valido"+ '\033[0m')
        return None
def convangolo(valore):
    if valore.upper() == "X":
        return None
    try:
        return float(valore)
    except ValueError:
        print('\033[91m' + "Valore non valido"+ '\033[0m')
        return None
# Input dei dati
for chiave in range(0,3):
    superTriangolo[f'L{chiave}']['V'] = convlato(input(f"Inserisci il valore del lato {superTriangolo[f'L{chiave}']['N']} (inserisci 'X' se sconosciuto): "))
    superTriangolo[f'L{chiave}']['E'] = 1 if superTriangolo[f'L{chiave}']['V'] != None else 0
for chiave in range(0, 3):
    superTriangolo[f'A{chiave}']['V'] = convangolo(input(f"Inserisci il valore dell'angolo {superTriangolo[f'A{chiave}']['N']} (inserisci 'X' se sconosciuto): "))
    superTriangolo[f'A{chiave}']['E'] = 1 if superTriangolo[f'A{chiave}']['V'] != None else 0
    superTriangolo[f'A{chiave}']['R'] = math.radians(float(superTriangolo[f'A{chiave}']['V'])) if superTriangolo[f'A{chiave}']['V'] != None else None

if superTriangolo['H']['E'] == 1:
    superTriangolo['H']['V'] = convlato(input(f"Inserisci il valore di altezza H relativa a {superTriangolo['L0']['N']} (inserisci 'X' se sconosciuto): "))