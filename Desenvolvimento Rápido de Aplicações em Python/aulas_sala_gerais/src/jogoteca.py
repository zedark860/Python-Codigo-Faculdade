from flask import Flask, render_template

app = Flask(__name__)

@app.route("/inicio")
def ola():
    lista: list[str] = ["God of war", "Super Mario", "GTA V"]
    
    return render_template("lista.html", titulo="Jogos", jogos=lista)

app.run(debug=True)