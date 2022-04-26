from math import sqrt
from flask import Flask # modulo in minuscolo, oggetto (classe) Flask in maiuscolo

app = Flask(__name__) # creazione app

'''definizione routes e pagine'''

@app.route("/")
def home():
    return "Pagina iniziale (root del sito)"

@app.route("/pagina1")
def pagina1():
    return "<p>Hello World!</p>"

@app.route("/pagina2")
def pagina2():
    # costruisce il contenuto della pagina, creando una stringa
    contenuto = "<p>Ciao sono la pagina 2</p>" # racchiuso in un tag p
    contenuto = contenuto + '<p>Calcolo la radice di 121: ' + str(sqrt(121)) + '</p>' # aggiungere un paragrafo che riporti la radice quadrata di 121
    return contenuto

# definire pagina 3 che riporti:
#       titolo "i primi 10 numeri pari"
#       paragrafo contenente i primi 10 numeri pari (calcolati al momento)

# serve a eseguire direttamente il file corrente, lancia la webapp creata e definita prima
if __name__ == "__main__":
    app.run()