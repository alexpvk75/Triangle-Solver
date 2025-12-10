import math

def calcola_triangolo():
    t_max = 4
    t = 0
    a, b, c = 0, 0, 0 
    
    while t < t_max:
        t += 1
        print(f"Tentativo {t} di {t_max}")
        
        try:
            a = float(input("Inserisci la lunghezza del lato a: "))
            b = float(input("Inserisci la lunghezza del lato b: "))
            c = float(input("Inserisci la lunghezza del lato c: "))

            if a <= 0 or b <= 0 or c <= 0:
                print("Errore: tutti i lati del triangolo devono avere lunghezze positive.")
                continue  

            if (a + b <= c) or (a + c <= b) or (b + c <= a):
                print("Errore: le lunghezze fornite non possono formare un triangolo (Disuguaglianza triangolare).")
                continue
            
            break 

        except ValueError:
            print("Errore: assicurati di inserire valori numerici validi (es. 3, 5.7).")
            continue 

    if t == t_max and (a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0):
        print("Limite tentativi superato. Fine programma.")
        return 


    def calcola_ang(lato1, lato2, lato3):
        try:
            cos_ang = (lato2**2 + lato3**2 - lato1**2) / (2 * lato2 * lato3)
        except ZeroDivisionError:
            return 0 

        cos_ang = max(-1.0, min(1.0, cos_ang)) 
        ang = math.acos(cos_ang)
        return math.degrees(ang)

    ang_a = round(calcola_ang(a, b, c), 2)
    ang_b = round(calcola_ang(b, a, c), 2)
    ang_c = round(180.0 - (ang_a + ang_b), 2)

    def t_ang(x, y, z):
        tolleranza = 1e-6 
        if abs(x - 90) < tolleranza or abs(y - 90) < tolleranza or abs(z - 90) < tolleranza:
            return "Rettangolo"
        elif x > 90 or y > 90 or z > 90:
            return "Ottusangolo"
        else:
            return "Acutangolo"
            
    def t_lati(l1, l2, l3):
        tolleranza = 1e-6
        if abs(l1 - l2) < tolleranza and abs(l2 - l3) < tolleranza:
            return "Equilatero"
        elif abs(l1 - l2) < tolleranza or abs(l1 - l3) < tolleranza or abs(l2 - l3) < tolleranza:
            return "Isoscele"
        else:
            return "Scaleno"
            
    tip_lati = t_lati(a, b, c)
    tip_angoli = t_ang(ang_a, ang_b, ang_c)
    
    P = a + b + c
    SP = P / 2
    A = math.sqrt(SP * (SP - a) * (SP - b ) * (SP - c))
    
    print(f"Il perimetro è {round(P, 2)}")
    print(f"L'area è {round(A, 2)}")
    print(f"Il triangolo è {tip_angoli} {tip_lati}")
    
if __name__ == "__main__":
    calcola_triangolo()