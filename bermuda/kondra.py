#KONDRA LIBRARY

# Controllo di precisione universale

def definisci_iterazioni(cifre):
    n = 0
    while True:
        term = 1 / factoriale(2*n + 1)
        if term < 10**(-cifre):
            return n + 1
        n += 1

ITERAZIONI = definisci_iterazioni(5) #default

def factoriale(n):
    if n < 0:
        raise ValueError("Factoriale non definito per numeri negativi")
    risultato = 1
    for i in range(2, n+1):
        risultato *= i
    return risultato

def pi_greco():
    return 16 * arctan(1/5) - 4 * arctan(1/239)

def vabs(x):
    return x if x >= 0 else x*(-1)


def seno(x): #serie di Maclaurin
    risultato = 0.0
    numeratore = x
    denominatore = 1
    segno = 1
    for n in range(ITERAZIONI):
        risultato += segno * numeratore / denominatore
        numeratore *= x * x
        denominatore *= (2*n+2) * (2*n+3)
        segno *= -1
    return risultato

def coseno(x): #serie di Maclaurin
    risultato = 0.0
    numeratore = 1.0
    denominatore = 1
    segno = 1
    for n in range(ITERAZIONI):
        risultato += segno * numeratore / denominatore
        numeratore *= x * x
        denominatore *= (2*n+1) * (2*n+2)
        segno *= -1
    return risultato

def tangente(x):
    seno_x = seno(x)
    coseno_x = coseno(x)
    if coseno_x == 0:
        raise ValueError("La tangente non è definita per questo angolo.")
    return seno_x / coseno_x

def cotangente(x):
    seno_x = seno(x)
    coseno_x = coseno(x)
    if seno_x == 0:
        raise ValueError("La cotangente non è definita per questo angolo.")
    return coseno_x / seno_x

def arcseno(x): #serie di Taylor
    risultato = 0.0
    numeratore = x
    for n in range(ITERAZIONI):
        coeff = 1.0
        for k in range(1, n+1):
            coeff *= (2*k - 1) / (2*k)
        termine = coeff * numeratore / (2*n + 1)
        risultato += termine
        numeratore *= x * x
    return risultato

def arccoseno(x):
    return (pi_greco() / 2) - arcseno(x)

def arctan(x):
    oper = x if vabs(x) <= 1 else 1/x
    risultato = 0.0
    segno = 1
    potenza = oper
    x2 = oper * oper
    for n in range(ITERAZIONI):
        risultato += segno * potenza / (2*n + 1)
        potenza *= x2
        segno *= -1
    if vabs(x) <= 1:
        return risultato
    elif x > 0:
        return pi_greco()/2 - risultato
    else:
        return (-1)*pi_greco()/2 - risultato

def arccot(x):
    if x == 0:
        return pi_greco() / 2
    if x > 0:
        return arctan(1/x)
    return arctan(1/x) + pi_greco()


def rdqrt(a): # Metodo di Newton-Raphson
    if a < 0:
        raise ValueError("Impossibile calcolare la radice quadrata di un numero negativo.")
    if a == 0:
        return 0
    x = a
    for i in range(ITERAZIONI):
        x = 0.5 * (x + a / x)
    return x

def grad_rad(x): # converte gradi in radiani
    return (pi_greco()/180) * x

def rad_grad(x): # converte radiani in gradi
    return (180/pi_greco()) * x
