# Inizializzazione
import math
def valido(L):
    return (L[0] + L[1] > L[2]) and (L[1] + L[2] > L[0]) and (L[0] + L[2] > L[1])
def calc_area(perimetro, L):
    semiper = perimetro / 2
    return round(math.sqrt(semiper * (semiper - L[0]) * (semiper - L[1]) * (semiper - L[2])), 2)
def calc_angolo(x, L):
    cos = (L[(x+1)%3]**2 + L[(x+2)%3]**2 - L[x]**2) / (2 * L[(x+1)%3] * L[(x+2)%3])
    return round(math.degrees(math.acos(cos)), 2)
def fmt(num, cifre=2):
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
def scrivere(file, L, perimetro, area, A):
    semiper = perimetro / 2
    text = [
        'Soluzione:\n',
        f'Lati: AB = {fmt(L[0])}, BC = {fmt(L[1])}, AC = {fmt(L[2])}\n',
        f'Perimetro: AB + BC + AC = {fmt(perimetro)}\n',
        f'Area: sqrt(p(p-AB)(p-BC)(p-AC))\n',
        f'p = (AB+BC+AC)/2 = {fmt(perimetro/2)}\n',
        f'Area: sqrt({fmt(perimetro/2)}({fmt(semiper)}-{fmt(L[0])})({fmt(semiper)}-{fmt(L[1])})({fmt(semiper)}-{fmt(L[2])}))'
        f' = {fmt(area)}\n']
    for x in range(3):
        text.append(
            f'{["C", "A", "B"][x]} = arccos(({["AB", "BC", "AC"][(x+1)%3]}^2 + {["AB", "BC", "AC"][(x+2)%3]}^2 - {["AB", "BC", "AC"][x]}^2) '
            f'/ (2 * {["AB", "BC", "AC"][(x+1)%3]} * {["AB", "BC", "AC"][(x+2)%3]})) '
            f'= arccos(({fmt(L[(x+1)%3])}^2 + {fmt(L[(x+2)%3])}^2 - {fmt(L[x])}^2) / (2 * {fmt(L[(x+1)%3])} * {fmt(L[(x+2)%3])}))'
            f' = {fmt(A[x])}\n'
        )
    text.append(f'Tipologia del triangolo: {tipologia(A, L)}\n'.strip())
    with open(file, "w") as f:
            f.writelines(text)
def main():
    L = [0, 0, 0] # Lati del triangolo (AB, BC, AC)
    A = [0, 0, 0] # Angoli del triangolo (C, A, B)
    perimetro = 0
    area = 0
    # Fase Input
    for i in range(3):
        tentativi = 0
        while tentativi <= 3:
            tentativi +=1
            insert = input(f"Inserisci il valore del lato {["AB", "BC", "AC"][i]} (tentativo n. {tentativi}/3): ")
            try:
                valore = float(insert)
            except ValueError:
                print("Errore: assicurati di inserire valori numerici validi (es. 3, 5.7)")
                continue
            if valore <= 0:
                print("Errore: tutti i lati del triangolo devono avere lunghezze positive")
                continue
            L[i] = valore
            perimetro += L[i]
            break
        else:
            print("Limite tentativi superato. Fine programma.")
            exit()
    if(not valido(L)):
        print("Errore: le lunghezze fornite non possono formare un triangolo (Disuguaglianza triangolare)")
    else:
        # Fase Elaborazione
        perimetro = (L[0] + L[1] + L[2])
        area = calc_area(perimetro, L)
        for x in range(3):
            A[x] = calc_angolo(x, L)
        # Fase Output
        print(f'\nPerimetro: {fmt(perimetro)}\nArea: {fmt(area)}\n')
        print(f'Angoloi:\nC = {fmt(A[0])}\nA = {fmt(A[1])}\nB = {fmt(A[2])}\n')
        print(f'Tipologia del triangolo: {tipologia(A, L)}\n')
        scrivere("soluzione.txt", L, perimetro, area, A)
if __name__ == "__main__":
    main()