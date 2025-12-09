import math
L = [0, 0, 0] # Lati del triangolo (AB, BC, AC)
A = [0, 0, 0] # Angoli del triangolo (C, A, B)
perimetro = 0
area = 0
for i in range(3):
    while True:
        insert = input(f"Inserisci il valore del lato {["AB", "BC", "AC"][i]}: ").strip().upper()
        try:
            valore = float(insert)
            if valore % 1 == 0:
                valore = int(insert)
        except ValueError:
            print("Inserisci un numero valido")
            continue
        if valore <= 0:
            print("Il valore non può essere minore o uguale a 0")
            continue
        L[i] = valore
        break
def valido(L):
    return (L[0] + L[1] > L[2]) and (L[1] + L[2] > L[0]) and (L[0] + L[2] > L[1])

if(not valido(L)):
    print("I valori inseriti non possono formare un triangolo valido.")
else:
    perimetro = (L[0] + L[1] + L[2])
    perimetro = int(perimetro) if perimetro % 1 == 0 else float(perimetro)
    semiper = perimetro / 2
    erona = math.sqrt(semiper * (semiper - L[0]) * (semiper - L[1]) * (semiper - L[2]))
    area = int(erona) if erona % 1 == 0 else float(erona)
    A = [0, 0, 0]     
    for x in range(3):
        cos = (L[(x+1)%3]**2 + L[(x+2)%3]**2 - L[x]**2) / (2 * L[(x+1)%3] * L[(x+2)%3])
        angolo = math.degrees(math.acos(cos))
        A[x] = int(angolo) if angolo % 1 == 0 else float(angolo)
    print(f"\nRISULTATI\nArea: {area}\nPerimetro: {perimetro}\nAngoli: C={A[0]}, A={A[1]}, B={A[2]}")