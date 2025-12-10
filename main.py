# Fase Inizializzazione
import math
precisione = 3
L = [0, 0, 0] # Lati del triangolo (AB, BC, AC)
A = [0, 0, 0] # Angoli del triangolo (C, A, B)
perimetro = 0
area = 0
# Fase Input
for i in range(3):
    while True:
        insert = input(f"Inserisci il valore del lato {["AB", "BC", "AC"][i]}: ")
        try:
            valore = float(insert)
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
    # Fase Elaborazione
    perimetro = (L[0] + L[1] + L[2])
    semiper = perimetro / 2
    area = round(math.sqrt(semiper * (semiper - L[0]) * (semiper - L[1]) * (semiper - L[2])), precisione)
    A = [0, 0, 0]     
    for x in range(3):
        cos = (L[(x+1)%3]**2 + L[(x+2)%3]**2 - L[x]**2) / (2 * L[(x+1)%3] * L[(x+2)%3])
        A[x] = round(math.degrees(math.acos(cos)), precisione)
    # Fase Output
    def fmt(num, cifre=precisione):
        if num % 1 == 0:
            return f'{int(num)}'
        else:
          return f"{num:.{cifre}f}"
    def tipologia(A, L):
        tipo_A = 0
        tipo_L = 0
        if A[0] == 90 or A[1] == 90 or A[2] == 90:
            tipo_A = "rettangolo"
        elif A[0] > 90 or A[1] > 90 or A[2] > 90:
            tipo_A = "ottusangolo"
        else:
            tipo_A = "acutangolo"
        if L[0] == L[1] == L[2]:
            tipo_L = "equilatero"
        elif L[0] == L[1] or L[1] == L[2] or L[0] == L[2]:
            tipo_L = "isoscele"
        else:
            tipo_L = "scaleno"
        if tipo_A==0:
            return f'{tipo_L}'
        elif tipo_L==0:
            return f'{tipo_A}'
        else:
            return f'{tipo_A} e {tipo_L}'
    text = [
            'Soluzione:\n',
            f'Lati: AB = {fmt(L[0])}, BC = {fmt(L[1])}, AC = {fmt(L[2])}\n',
            f'Perimetro: AB + BC + AC = {fmt(perimetro)}\n',
            f'Area: sqrt(p(p-AB)(p-BC)(p-AC))\n',
            f'p = (AB+BC+AC)/2 = {fmt(semiper)}\n',
            f'Area: sqrt({fmt(semiper)}({fmt(semiper)}-{L[0]})({fmt(semiper)}-{L[1]})({fmt(semiper)}-{L[2]}))'
            f' = {fmt(area)}\n']
    for x in range(3):
        text.append(
            f'{["C", "A", "B"][x]} = arccos(({["AB", "BC", "AC"][(x+1)%3]}^2 + {["AB", "BC", "AC"][(x+2)%3]}^2 - {["AB", "BC", "AC"][x]}^2) '
            f'/ (2 * {["AB", "BC", "AC"][(x+1)%3]} * {["AB", "BC", "AC"][(x+2)%3]})) '
            f'= arccos(({L[(x+1)%3]}^2 + {L[(x+2)%3]}^2 - {L[x]}^2) / (2 * {L[(x+1)%3]} * {L[(x+2)%3]}))'
            f' = {fmt(A[x])}\n'
        )
        text.append(f'Tipologia del triangolo: {tipologia(A, L)}\n')
    with open("soluzione.txt", "w") as file:
            file.writelines(text)
    print(f'\nPerimetro: {fmt(perimetro)}\nArea: {fmt(area)}\n')
    print(f'Angoloi:\nC = {fmt(A[0])}\nA = {fmt(A[1])}\nB = {fmt(A[2])}\n')
    print(f'Tipologia del triangolo: {tipologia(A, L)}\n')