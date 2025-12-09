# Fase Inizializzazione
import math
import os
os.makedirs("files", exist_ok=True)
L = [0, 0, 0] # Lati del triangolo (AB, BC, AC)
A = [0, 0, 0] # Angoli del triangolo (C, A, B)
perimetro = 0
area = 0
# Fase Input
for i in range(3):
    while True:
        insert = input(f"Inserisci il valore del lato {["AB", "BC", "AC"][i]}: ").strip().upper()
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
    area = math.sqrt(semiper * (semiper - L[0]) * (semiper - L[1]) * (semiper - L[2]))
    A = [0, 0, 0]     
    for x in range(3):
        cos = (L[(x+1)%3]**2 + L[(x+2)%3]**2 - L[x]**2) / (2 * L[(x+1)%3] * L[(x+2)%3])
        A[x] = math.degrees(math.acos(cos))
    # Fase Output
    def fmt(num, cifre=3):
        return f"{num:.{cifre}f}".rstrip('0').rstrip('.')
    text = {
        '.txt': [
            'Soluzione:\n',
            f'Lati: AB = {fmt(L[0])}, BC = {fmt(L[1])}, AC = {fmt(L[2])}\n',
            f'Perimetro: AB + BC + AC = {fmt(perimetro)}\n',
            f'Area: sqrt(p(p-AB)(p-BC)(p-AC))\n',
            f'p = (AB+BC+AC)/2 = {fmt(semiper)}\n',
            f'Area: sqrt({fmt(semiper)}({fmt(semiper)}-{L[0]})({fmt(semiper)}-{L[1]})({fmt(semiper)}-{L[2]}))'
            f' = {fmt(area)}\n'],
        '.md': [
            '## Soluzione:\n',
            f'$$Lati: AB = {fmt(L[0])}, BC = {fmt(L[1])}, AC = {fmt(L[2])}$$\n',
            f'$$Perimetro: AB + BC + AC = {fmt(perimetro)}$$\n',
            f'$$Area: \\sqrt{{p(p-AB)(p-BC)(p-AC)}}$$\n',
            f'$$p = \\frac{{AB+BC+AC}}{{2}} = {fmt(semiper)}$$\n',
            f'$$Area: \\sqrt{{{fmt(semiper)}({fmt(semiper)}-{L[0]})({fmt(semiper)}-{L[1]})({fmt(semiper)}-{L[2]})}}'
            f' = {fmt(area)}$$\n',
        ]
    }
    for x in range(3):
        text['.txt'].append(
            f'{["C", "A", "B"][x]} = arccos(({["AB", "BC", "AC"][(x+1)%3]}^2 + {["AB", "BC", "AC"][(x+2)%3]}^2 - {["AB", "BC", "AC"][x]}^2) '
            f'/ (2 * {["AB", "BC", "AC"][(x+1)%3]} * {["AB", "BC", "AC"][(x+2)%3]})) '
            f'= arccos(({L[(x+1)%3]}^2 + {L[(x+2)%3]}^2 - {L[x]}^2) / (2 * {L[(x+1)%3]} * {L[(x+2)%3]}))'
            f' = {fmt(A[x])}\n'
        )
        text['.md'].append(
            f'$$ {["C", "A", "B"][x]} = arccos\\frac{{{["AB", "BC", "AC"][(x+1)%3]}^2 + {["AB", "BC", "AC"][(x+2)%3]}^2 - {["AB", "BC", "AC"][x]}^2}}'
            f'{{2 \\times {["AB", "BC", "AC"][(x+1)%3]} \\times {["AB", "BC", "AC"][(x+2)%3]}}} '
            f'= arccos\\frac{{{L[(x+1)%3]}^2 + {L[(x+2)%3]}^2 - {L[x]}^2}}{{2 \\times {L[(x+1)%3]} \\times {L[(x+2)%3]}}}'
            f' = {fmt(A[x])} $$\n'
        )
    def scrivere(name, format, content, dir):
        with open(os.path.join(dir, "".join(name + format)), "w") as file:
            file.writelines(content[format])
    scrivere("soluzione", ".txt", text, "files")
    scrivere("soluzione", ".md", text, "files")
    print(f'\nPerimetro: {fmt(perimetro)}\nArea: {fmt(area)}\n')