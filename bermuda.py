triangolo = [[False, False, False, False, False, False, False],
    [None, None, None, None, None, None, None],
    [0, 0, 0, 0, 0, 0, 0],
    [False, 0, 0],
    [False, 0, 0]]
while True:
    base_input = input("Quale lato viene considerato come la base (AB/BC/AC): ").strip().upper()
    if base_input in ["AB", "BC", "AC"]:
        triangolo[1][0] = base_input
        break
    print("Input non valido! Inserisci AB, BC o AC")
triangolo[1][1] = "BC" if triangolo[1][0] == "AB" else "AC" if triangolo[1][0] == "BC" else "AB"
triangolo[1][2] = "AC" if triangolo[1][0] == "AB" else "AB" if triangolo[1][0] == "BC" else "BC"
for i in range(0, 3):
    triangolo[1][i+3] = ["C", "A", "B"][["AB", "BC", "AC"].index(triangolo[1][i])]
# input dei dati
for i in range(0, 3):
    while True:
        insert = input(f"Inserisci il valore del lato {triangolo[1][i]}: ").strip().upper()
        if insert <= 0:
            print("Il valore non può essere minore o uguale a 0")
        else:
            triangolo[2][i] = float(insert) if insert != 'X' else 0
            triangolo[0][i] = True if insert != 'X' else False
            break
for i in range(3, 6):
    while True:
        insert = input(f"Inserisci il valore del angolo {triangolo[1][i]}: ")
        if not (0< insert < 180):
            print("Il valore non può essere minore a 0 o maggiore a 180")
        else:
            triangolo[2][i] = float(insert) if insert != 'X' else 0
            triangolo[0][i] = True if insert != 'X' else False
            break
while True:
    insert = input(f"Inserisci il valore dell'altezza: ")
    if insert < 0:
        print("Il valore non può essere minore a 0")
    else:
        triangolo[2][6] = float(insert) if insert != 'X' else 0
        triangolo[0][6] = True if insert != 'X' else False
        break