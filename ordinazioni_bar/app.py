from flask import Flask, redirect, render_template, request
from datetime import datetime

global utenti
ordini = []

app = Flask(__name__) # creazione app

@app.route("/ordina")
@app.route("/")
def iscrizione():
    return render_template('form_ordina.html')


@app.route("/inserimento", methods=['POST'])
def inserimento():
    dati = request.values # dati del form
    nuovo_ordine = (dati['classe'], dati['piano'], dati['prod'])
    ordini.append(nuovo_ordine)
    return "ordine inserito"

@app.route("/visualizza_ordini")
def visualizza_iscritti():
    dati = request.values # dati del form
    global ordini
    if "sort" in dati:
        criterio = dati["sort"]
        if criterio == "classe":
            ordini = sorted(ordini, key=lambda el: el[0])
        elif criterio == "piano":
            ordini = sorted(ordini, key=lambda el: el[1])
        elif criterio == "articolo":
            ordini = sorted(ordini, key=lambda el: el[2])


    return render_template('ordini.html', ordini=ordini)


if __name__ == "__main__":
    app.run(debug=True)