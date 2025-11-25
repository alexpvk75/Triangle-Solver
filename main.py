# Inizializzazione del dizionario per i dati del triangolo
import math
triangolo = {
    'L0': {'E': 0, 'V': None, 'N': None}, #base
    'L1': {'E': 0, 'V': None, 'N': None}, #primo lato adjacente
    'L2': {'E': 0, 'V': None, 'N': None}, #secondo lato adjacente
    'A0': {'E': 0, 'V': None, 'N': None, 'R': None}, #angolo opposto alla base
    'A1': {'E': 0, 'V': None, 'N': None, 'R': None}, #primo angolo adiacente
    'A2': {'E': 0, 'V': None, 'N': None, 'R': None}, #secondo angolo adiacente
    'H': {'E': 0, 'V': None}, #altezza
    'AREA': {'V': None} #area
}
lati = ["AB", "BC", "AC"]
constrlati = [None, None, None]
angoli = ["C", "A", "B"]
# Inizializzazione della base e della althezza
while True:
    base_input = input('\033[36m' + "Quale lato viene considerato come la base (AB/BC/AC): " + '\033[0m').strip().upper()
    if base_input in lati:
        L_root = lati.index(base_input)
        break
    print('\033[91m' + "Input non valido! Inserisci AB, BC o AC" + '\033[0m')
constrlati[0] = int(2*(L_root%2)+(1 - (L_root%2))*(1 - ((2-L_root)/2)))
constrlati[1] = int((constrlati[0] % 2) * (constrlati[0] + 1) + (1 - (constrlati[0] % 2)) * (1 - ((constrlati[0])/2)))
constrlati[2] = int((1 - (constrlati[0] % 2)) * (2 - constrlati[0]/2))
for lato in lati:
    triangolo[f'L{constrlati[lati.index(lato)]}']['N'] = lato
for angolo in angoli:
    triangolo[f'A{constrlati[angoli.index(angolo)]}']['N'] = angolo
if input('\033[36m' + "Si conosce l'altezza relativa alla base? (S/N): "+ '\033[0m').strip().upper() == "S":
    triangolo['H']['E'] = 1
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
    triangolo[f'L{chiave}']['V'] = convlato(input(f"Inserisci il valore del lato {triangolo[f'L{chiave}']['N']} (inserisci 'X' se sconosciuto): "))
    triangolo[f'L{chiave}']['E'] = 1 if triangolo[f'L{chiave}']['V'] != None else 0
for chiave in range(0, 3):
    triangolo[f'A{chiave}']['V'] = convangolo(input(f"Inserisci il valore dell'angolo {triangolo[f'A{chiave}']['N']} (inserisci 'X' se sconosciuto): "))
    triangolo[f'A{chiave}']['E'] = 1 if triangolo[f'A{chiave}']['V'] != None else 0
    triangolo[f'A{chiave}']['R'] = math.radians(float(triangolo[f'A{chiave}']['V'])) if triangolo[f'A{chiave}']['V'] != None else None

if triangolo['H']['E'] == 1:
    triangolo['H']['V'] = convlato(input(f"Inserisci il valore di altezza H relativa a {triangolo['L0']['N']} (inserisci 'X' se sconosciuto): "))
print(triangolo)