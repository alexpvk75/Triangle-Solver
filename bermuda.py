# Inizializzazione del dizionario per i dati del triangolo
import moduli.sheva as sheva
import moduli.kondra as kondra
import moduli.malev as malev
cifre_const = 15
kondra.ITERAZIONI = kondra.definisci_iterazioni(cifre_const)
lang = 0 #0 - inglese, 1 - italiano, 2 - ucraino
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
    'P1': superTriangolo['L0']['E']*superTriangolo['H']['E'],
    'P2': superTriangolo['L0']['E']*superTriangolo['L1']['E']*superTriangolo['L2']['E'],
    'P3': superTriangolo['L1']['E']*superTriangolo['L2']['E']*superTriangolo['A0']['E'] or superTriangolo['L0']['E']*superTriangolo['L2']['E']*superTriangolo['A1']['E'] or superTriangolo['L0']['E']*superTriangolo['L1']['E']*superTriangolo['A2']['E']
}
paradigmi = {
    'P1': {
        'STEPS': {
            '0': ['', '#comment'],
            '1': ['', '#comment']
        },
    }
}
# Inizializzazione della base e della althezza
while True:
    radice = input('\033[1;36m' + "Quale lato viene considerato come la base (AB/BC/AC): " + '\033[0m').strip().upper()
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
    superTriangolo[f'A{chiave}']['R'] = kondra.grad_rad(float(superTriangolo[f'A{chiave}']['V'])) if superTriangolo[f'A{chiave}']['V'] != None else None

if superTriangolo['H']['E'] == 1:
    superTriangolo['H']['V'] = convlato(input(f"Inserisci il valore di altezza H relativa a {superTriangolo['L0']['N']} (inserisci 'X' se sconosciuto): "))
print(superTriangolo)