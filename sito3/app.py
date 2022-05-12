from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__) # creazione app

@app.route("/login")
def login():
    data_corrente = datetime.now().date()
    return render_template('login.html', data=data_corrente)


@app.route("/valuta_login")
def valuta_login():
    # qualcosa...
    
    return "Pagina che validerà le credenziali"


if __name__ == "__main__":
    app.run(debug=True)