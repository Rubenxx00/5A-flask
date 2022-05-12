from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__) # creazione app

@app.route("/login")
def login():
    data_corrente = datetime.now().date()
    return render_template('login.html', data=data_corrente)


@app.route("/valuta_login", methods=['GET', 'POST'])
def valuta_login():
    dati = request.values # dati del form
    if dati["username"] == "admin" and dati["password"] == "ciao":
        return "Accesso eseguito"
    else:
        return "Utente non riconosciuto"


if __name__ == "__main__":
    app.run(debug=True)