# Branch: Alex Pavlyk
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

def controllare(L):
    return (L[0] + L[1] > L[2]) and (L[1] + L[2] > L[0]) and (L[0] + L[2] > L[1])

if(not controllare(L)):
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
    fileTXT = [
        f"Lati: AB={L[0]}, BC={L[1]}, AC={L[2]}\n",
        f"C=arccos((AC^2+BC^2-AB^2)/(2*AC*BC))=arccos(({L[1]}^2+{L[2]}^2-{L[0]}^2)/(2*{L[1]}*{L[2]}))={A[0]}\n",
        f"A=arccos((AB^2+AC^2-BC^2)/(2*AB*AC))=arccos(({L[2]}^2+{L[0]}^2-{L[1]}^2)/(2*{L[2]}*{L[0]}))={A[1]}\n",
        f"B=arccos((AB^2+BC^2-AC^2)/(2*AB*BC))=arccos(({L[0]}^2+{L[1]}^2-{L[2]}^2)/(2*{L[0]}*{L[1]}))={A[2]}\n\n",
        f"Perimetro: AB+BC+AC={L[0]}+{L[1]}+{L[2]}={perimetro}\n",
        f"p=Perimetro/2={perimetro}/2={semiper}\n",
        f"Area: sqrt(p(p-AB)(p-BC)(p-AC))=sqrt({semiper}*({semiper}-{L[0]})*({semiper}-{L[1]})*({semiper}-{L[2]}))={area}\n"
    ]
    with open("soluzione.txt", "w") as file:
        file.writelines(fileTXT)