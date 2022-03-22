
# scrivere una funzione che stampi
# tutti i divisori di un numero
def stampa_divisori(n):
    for i in range(1, n+1):
        if n % i == 0: # se il resto della divisione n/i è 0
           print(i) 

# stampa "il numero è primo" oppure ...
# numero è primo se è divisibile solo per 1 e per sè stesso
def controlla_primo(n):
    # scrivere implementazione
    print("il numero è primo")

# utilizzo la funzione
numero = int(input("inserisci il numero di cui vuoi conoscere i divisori"))
stampa_divisori(numero)
