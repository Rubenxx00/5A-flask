def conta_dispari(lista):
    conta = 0
    for el in lista:
        if el % 2 != 0:
            conta += 1
    return conta

def estrai_dispari(lista):
    li = []
    #oppure li = list()
    for el in lista:
        if el % 2 != 0:
            li.append(el)
    return li

def estrai_dispari2(lista):
    return [x for x in lista if x % 2]

def elimina_vuote(lista):
    # implementare
    pass

li = [0, 5, 2, 1, 9]
print(conta_dispari(li))
print(estrai_dispari(li))
