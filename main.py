# Branch: Alex Pavlyk
# 0 - valori lati (AB, BC, AC)
# 1 - valori angoli (C, A, B)
# 2 - area, perimetro
import math
triangolo = [[0, 0, 0],
             [0, 0, 0],
             [0, 0]]
for i in range(0, 3):
    while True:
        insert = input(f"Inserisci il valore del lato {['AB', "BC", "AC"][i]}: ").strip().upper()
        try:
            valore = float(insert)
        except ValueError:
            print("Inserisci un numero valido")
            continue
        if float(insert) <= 0:
            print("Il valore non può essere minore o uguale a 0")
            continue
        triangolo[0][i] = float(insert)
        break

def controllare(L):
    return (L[0] + L[1] > L[2]) and (L[1] + L[2] > L[0]) and (L[0] + L[2] > L[1])

if(not controllare(triangolo[0])):
    print("I valori inseriti non possono formare un triangolo valido.")
else:
    L = [triangolo[0][0], triangolo[0][1], triangolo[0][2]]
    semiper = (L[0] + L[1] + L[2]) / 2
    area = math.sqrt(semiper * (semiper - L[0]) * (semiper - L[1]) * (semiper - L[2]))
    triangolo[2][0] = area
    triangolo[2][1] = semiper * 2
    A = [0, 0, 0]
    A[0] = math.acos((L[1]**2+L[2]**2-L[0]**2)/(2*L[1]*L[2])) * (180/math.pi)
    A[1] = math.acos((L[0]**2+L[2]**2-L[1]**2)/(2*L[0]*L[2])) * (180/math.pi)
    A[2] = 180 - A[0] - A[1]
    for i in range(0, 3):
        triangolo[1][i] = A[i]
    print(f"Area: {triangolo[2][0]}\nPerimetro: {triangolo[2][1]}\nAngoli: C={triangolo[1][0]}, A={triangolo[1][1]}, AB={triangolo[1][2]}")