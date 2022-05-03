from math import sqrt
from flask import Flask # modulo in minuscolo, oggetto (classe) Flask in maiuscolo

app = Flask(__name__) # creazione app

'''definizione routes e pagine'''

@app.route("/")
def home():
    return "Pagina iniziale (root del sito)  "

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
@app.route("/pagina3")
def pagina3():
    contenuto = "<ul style='list-style-type: square;'>"
    for i in range(1,21):
        if i % 2 == 0:
            contenuto += "<li>" + str(i) + "</li>"
    contenuto += "</ul>"
    return contenuto

@app.route("/pagina4")
def pagina4():
    nomi = ['Chris', 'Dennis', 'Sarah']
    età = [18, 22, 25]
    contenuto = '''<table border="2">
                        <tr>
                            <th>Person</th>
                            <th>Age</th>
                        </tr>'''

    # genero le righe
    for i in range(len(nomi)):
        contenuto += "<tr>"
        contenuto += "<td>" + nomi[i] + "</td>" 
        contenuto += "<td>" + str(età[i]) + "</td>"
        contenuto += "</tr>"

    contenuto += "</table>" # chiude tabella
    return contenuto

# serve a eseguire direttamente il file corrente, lancia la webapp creata e definita prima
if __name__ == "__main__":
    app.run(debug=True)