# ripasso liste

# lista vuota
li = list()
li = []

li.append(1)
li.append(2)
li.append(3)
li.insert(3, 4)
#li.pop() # toglie e restituisce l'ultimo elemento

print(li)

if 3 in li:
    print('valore 3 presente')

# sintassi -> start:end:step
print(li[0]) # primo elemento
print(li[:3]) # primi 3 elementi (indici 0,1,2)
print(li[3:]) # elementi dall'indice 3 in poi
print(li[:-2]) # elementi fino al penultimo (escluso)

print(li[::2]) # scorro incrementando con passo 2
print(li[::-1]) # scorro al contrario
