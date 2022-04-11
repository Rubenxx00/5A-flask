'''scrivi una funzione che crei e restituisca un tag HTML a partire da nome tag e contenuto, entrambi passati come parametro

crea_tag('i', 'Python') -> '<i>Python</i>'
crea_tag('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
'''
def crea_tag(tipo, contenuto):
    tag = '<' + tipo + '>' + contenuto + '<' + tipo + '/>'
    return tag
    #return f'<{tipo}>{contenuto}</{tipo}>' versione one line

print(crea_tag('h1', 'titolo 1'))
print(crea_tag('p', 'paragrafo con testo'))
print(crea_tag('i', 'Python'))

'''scrivi una funzione che, dato un url, scomponga le sue componenti e stampi le informazioni contenute: protocollo, dominio del sito, dominio di primo livello, path

es:
https://www.w3resource.com/pythonexercises
'''

def scomponi(url):
    print() # completare
