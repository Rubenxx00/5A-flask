
# scrivere una funzione che stampi
# tutti i divisori di un numero
def stampa_divisori(n):
    for i in range(1, n+1):
        if n % i == 0: # se il resto della divisione n/i è 0
           print(i) 

# restituisce True se il numero è primo, False altrimenti
# numero è primo se è divisibile solo per 1 e per sè stesso
def controlla_primo(n):
    conta = conta_divisori(n)
    if conta == 2:
        return True
    else:
        return False

# restituisce il numero di divisori di n
def conta_divisori(n):
    conta = 0
    for i in range(1, n+1):
        if n % i == 0:
            conta += 1
    return conta

# utilizzo la funzione
numero = int(input("inserisci il numero di cui vuoi conoscere i divisori "))
stampa_divisori(numero)

numero = int(input("inserisci il numero da verificare "))
p = controlla_primo(numero)
print(p)
if p == True:
    print("primo")
else:
    print("non primo")
