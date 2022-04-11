def sort_words(frase):
    return sorted(frase.split('-'))

def ordina_parole(frase):
    lista_parole = frase.split('-')
    lista_ordinata = sorted(lista_parole)
    return lista_ordinata

frase = 'green-red-yellow-black-white'
print(ordina_parole(frase))

