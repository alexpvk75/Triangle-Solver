# 0 - valori lati (AB, BC, AC)
# 1 - valori angoli (C, A, B)
# 2 - area, perimetro
import math
L = [0, 0, 0] # Lati del triangolo
A = [0, 0, 0] # Angoli del triangolo
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
    def carnot(x, L):
        y = int(((x%2)*(x+1)+(1-(x%2))*(1-(x/2))))
        z = int((1-(x%2))*(2-(x/2)))
        cos = (L[y]**2 + L[z]**2 - L[x]**2) / (2 * L[y] * L[z])
        angolo = math.degrees(math.acos(cos))
        if angolo % 1 == 0:
            return int(angolo)
        else:
            return float(angolo)      
    for x in range(3):
        A[x] = carnot(x, L)
    print(f"\nRISULTATI\nArea: {area}\nPerimetro: {perimetro}\nAngoli: C={A[0]}, A={A[1]}, B={A[2]}")