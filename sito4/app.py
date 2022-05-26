from flask import Flask, redirect, render_template, request
from datetime import datetime

global utenti
utenti = []

app = Flask(__name__) # creazione app

@app.route("/iscrizione")
def iscrizione():
    data_corrente = datetime.now().date()
    return render_template('iscrizione.html', data=data_corrente)


@app.route("/inserimento", methods=['POST'])
def inserimento():
    dati = request.values # dati del form
    utente = (dati['nome'], dati['cognome'], dati['nascita'], dati['sesso'])
    utenti.append(utente)
    return redirect('/visualizza_iscritti')

@app.route("/visualizza_iscritti")
def visualizza_iscritti():
    global utenti
    return render_template('iscritti.html', utenti=utenti)


if __name__ == "__main__":
    app.run(debug=True)