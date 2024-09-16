from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome: str, categoria: str, console: str):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)

jogo1: Jogo = Jogo(nome="God of War", categoria="Ação", console="PS4")
jogo2: Jogo = Jogo("Skyrim", "RPG", "PS4")
jogo3: Jogo = Jogo("Fifa 21", "Esportes", "PS4")
    
lista: list[Jogo] = [jogo1, jogo2, jogo3]

@app.route("/inicio")
def ola() -> str:
    
    return render_template("lista.html", titulo="Jogos", jogos=lista)

@app.route("/novo")
def novo() -> str:
    return render_template("novo.html", titulo="Novo Jogo")

@app.route("/criar", methods=["POST"])
def criar() -> str:
    nome: str = request.form["nome"]
    categoria: str = request.form["categoria"]
    console: str = request.form["console"]
    
    jogo: Jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return render_template("lista.html", titulo="Jogos", jogos=lista)

app.run(debug=True)