frase = 'il nome "Alessandro" significa...' # virgolette alternate per non terminare la stringa
frase = "il nome \"Alessandro\" significa..." # uso l'escape

frase = "the pen is on the table\nsecond row"
frase = 'the pen is on the table'

print(len(frase))

# contare quante lettere 'a' ci sono in questa stringa
conta = 0
for lettera in frase:
    if lettera == 'a':
        conta += 1

# contare quante parole ci sono nella stringa
conta_spazi = 1
for lettera in frase:
    if lettera == ' ':
        conta_spazi += 1

print(frase.upper())
print(frase.lower())

lista_parole = frase.split(" ")
print(len(lista_parole))

'''
Write a Python function that accepts a hyphen-separated sequence of words as input and returns the list of words after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : ['black', 'green', 'red', 'white', 'yellow']'''

lista = [5,1,0,9,2]
lista_ordinata = sorted(lista)
print(lista_ordinata)

#oppure
print(sorted(lista))

