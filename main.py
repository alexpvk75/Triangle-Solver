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
    semiper = int(semiper) if semiper % 1 == 0 else float(semiper)
    area = math.sqrt(semiper * (semiper - L[0]) * (semiper - L[1]) * (semiper - L[2]))
    area = int(area) if area % 1 == 0 else float(area)
    A = [0, 0, 0]     
    for x in range(3):
        cos = (L[(x+1)%3]**2 + L[(x+2)%3]**2 - L[x]**2) / (2 * L[(x+1)%3] * L[(x+2)%3])
        angolo = math.degrees(math.acos(cos))
        A[x] = int(angolo) if angolo % 1 == 0 else float(angolo)
    def format(num, cifre=2):
        if num % 1 == 0:
            return str(num)
        else:
            return f"{num:.{cifre}f}"
    text = {
        '.txt': [
            'Soluzione:\n',
            f'Lati: AB = {format(L[0])}, BC = {L[1]}, AC = {L[2]}\n',
            f'Perimetro: AB + BC + AC = {perimetro}\n',
            f'Area: sqrt(p(p-AB)(p-BC)(p-AC))\n',
            f'p = (AB+BC+AC)/2 = {semiper}\n',
            f'Area: sqrt({semiper}({semiper}-{L[0]})({semiper}-{L[1]})({semiper}-{L[2]})) = {area}\n',
            f'C = arccos((BC^2 + AC^2 - AB^2) / (2 * BC * AC)) = {A[0]}\n',
            f'A = arccos((AB^2 + AC^2 - BC^2) / (2 * AB * AC)) = {A[1]}\n',
            f'B = arccos((AB^2 + BC^2 - AC^2) / (2 * AB * BC)) = {A[2]}\n'
        ],
        '.md': [
            '## Soluzione:\n',
            f'- $$Lati: AB = {L[0]}, BC = {L[1]}, AC = {L[2]}$$\n',
            f'- $$Perimetro: AB + BC + AC = {perimetro}$$\n',
            f'- $$Area: \\sqrt{{p(p-AB)(p-BC)(p-AC)}}$$\n',
            f'- $$p = \\frac{{AB+BC+AC}}{{2}} = {semiper}$$\n',
            f'- $$Area: \\sqrt{{{semiper}({semiper}-{L[0]})({semiper}-{L[1]})({semiper}-{L[2]})}} = {area}$$\n',
            f'- $$C = arccos(\\frac{{BC^2 + AC^2 - AB^2}}{{2 \\times BC \\times AC}}) = {A[0]}$$\n',
            f'- $$A = arccos\\frac{{AB^2 + AC^2 - BC^2}}{{2 \\times AB \\times AC}} = {A[1]}$$\n',
            f'- $$B = arccos\\frac{{AB^2 + BC^2 - AC^2}}{{2 \\times AB \\times BC}} = {A[2]}$$\n'
        ]
    }

    def scrivere(name, format, content):
        with open("".join(name + format), "w") as file:
            file.writelines(content[format])
    scrivere("soluzione", ".txt", text)
    scrivere("soluzione", ".md", text)
    print(f'\nPerimetro: {perimetro}\nArea: {area}\n')
