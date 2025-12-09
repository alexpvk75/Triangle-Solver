# alternative branch
import bermuda
#triangolo: 0 - segnali di presenza dati
#           1 - nomi lati e angoli
#           2 - valori lati, angoli e altezza
#           3 - segnali: LEGAL, PARADIGM(AREA), SHIFT, RECOVERY
#           4 - area e perimetro
# H, L0, L1, L2, A0, A1, A2
triangolo = [[False, False, False, False, False, False, False],
    [None, None, None, None, None, None, None],
    [0, 0, 0, 0, 0, 0, 0],
    [False, 0, 0],
    [0, 0]]
while True:
    base_input = input("Quale lato viene considerato come la base (AB/BC/AC): ").strip().upper()
    if base_input in ["AB", "BC", "AC"]:
        triangolo[1][1] = base_input
        break
    print("Input non valido! Inserisci AB, BC o AC")
triangolo[1][2] = "BC" if triangolo[1][1] == "AB" else "AC" if triangolo[1][1] == "BC" else "AB"
triangolo[1][3] = "AC" if triangolo[1][1] == "AB" else "AB" if triangolo[1][1] == "BC" else "BC"
for i in range(1, 4):
    triangolo[1][i+3] = ["C", "A", "B"][["AB", "BC", "AC"].index(triangolo[1][i])]
# input dei dati
for i in range(1, 4):
    while True:
        insert = input(f"Inserisci il valore del lato {triangolo[1][i]}: ").strip().upper()
        if insert == 'X':
            triangolo[2][i] = 0
            triangolo[0][i] = False
            break
        try:
            valore = float(insert)
        except ValueError:
            print("Inserisci un numero valido o 'X' se sconosciuto")
            continue
        if float(insert) <= 0:
            print("Il valore non può essere minore o uguale a 0")
            continue
        triangolo[2][i] = float(insert)
        triangolo[0][i] = True
        break
for i in range(1, 4):
    while True:
        insert = input(f"Inserisci il valore del angolo {triangolo[1][i+3]}: ").strip().upper()
        if insert == 'X':
            triangolo[2][i+3] = 0
            triangolo[0][i+3] = False
            break
        try:
            valore = float(insert)
        except ValueError:
            print("Inserisci un numero valido o 'X' se sconosciuto")
            continue
        if not (0<valore<180):
            print("Il valore non può essere minore a 0 o maggiore a 180")
            continue
        triangolo[2][i+3] = float(insert)
        triangolo[0][i+3] = True
        break
while True:
    insert = input("Inserisci il valore dell'altezza: ").strip().upper()
    if insert == 'X':
        triangolo[2][0] = 0
        triangolo[0][0] = False
        break
    try:
        valore = float(insert)
    except ValueError:
        print("Inserisci un numero valido o 'X' se sconosciuto")
        continue
    if valore <= 0:
        print("Il valore non può essere minore o uguale a 0")
        continue
    triangolo[2][0] = float(insert)
    triangolo[0][0] = True
    break
bermuda.inspect(triangolo)
print(triangolo[3][1])