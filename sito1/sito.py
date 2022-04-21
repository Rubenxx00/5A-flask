from math import sqrt
from flask import Flask # modulo in minuscolo, oggetto (classe) Flask in maiuscolo

app = Flask(__name__) # creazione app

'''definizione routes e pagine'''

@app.route("/")
def home():
    return "Pagina iniziale (root del sito)"

@app.route("/pagina1")
def hello():
    return "<p>Hello World!</p>"

@app.route("/pagina2")
def hello2():
    contenuto =  "<p>Ciao sono la pagina 2</p>" # racchiuso in un tag p
    contenuto = contenuto + '<p>Calcolo la radice di 121: ' + str(sqrt(121)) + '</p>' # aggiungere un paragrafo che riporti la radice quadrata di 121
    return contenuto

# serve a eseguire direttamente il file corrente, lancia la webapp creata e definita prima
if __name__ == "__main__":
    app.run()