# scrivere funzione che, dato in input un intero, restituisca True se è perfetto, False altrimenti

def perfetto(n):
    somma = 0
    for i in range(1, n):
        if n % i == 0:
            somma += i
    if n == somma:
        return True
    else:
        return False

n = int(input("inserisci il numero da verificare "))
if perfetto(n):
    print(f"{n} è un numero perfetto")
else:
    print(f"{n} non è un numero perfetto")
