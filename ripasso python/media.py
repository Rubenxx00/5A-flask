# caricare da input N elementi,
# stamparne la media

from cgi import print_arguments


n = int(input("Inserisci N: "))
somma = 0

# ...
for i in range(n):
    num = int(input("Inserisci il prossimo numero: "))
    somma = somma + num

media = somma / n

print(media)

li = ...

print(li[0])
print(li[:3])
print(li[3:])
print(li[:-1])

print(li[::-1])
