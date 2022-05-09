from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__) # creazione app

@app.route("/pagina1")
def pagina1():
    contenuto = render_template('base.html', titolo="Pagina di benvenuto", nome="Ruben")

    return contenuto

@app.route("/orario")
def orario():
    adesso = datetime.now()

    data_adesso = adesso.date()
    ora_adesso = adesso.time()

    return render_template('base.html', titolo="Pagina ora corrente", data=data_adesso, ora=ora_adesso)

# serve a eseguire direttamente il file corrente, lancia la webapp creata e definita prima
if __name__ == "__main__":
    app.run(debug=True)