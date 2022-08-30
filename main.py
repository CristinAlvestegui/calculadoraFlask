from crypt import methods
import re
from unittest import result
from flask import Flask, render_template #Importando bibliotecas Flask
from flask import request, redirect
from operacoes import operacoes #importanto nossa classe operações
import this


app = Flask(__name__)#Referência ao objeto Flask, crinado uma variavel APP que guarda os elementos do Flask
ope = operacoes()#nossa chave para abrir o classe operacoes

this.resultadoFinal = ""

@app.route("/")#Pagina index - priemira página de qualquer site, tipo uma rota para uma pagina
def homepage():
    return render_template("index.html")

@app.route("/soma", methods=['POST','GET']) #aqui estamos fazendo um rota para a página /soma, com os métodos GET ou POST
def soma():
    if request.method == 'POST':
        numero1 = request.form['num1']#dentro do [] vai o nome da variavel, name no HTML
        numero2 = request.form['num2']
        this.resultadoFinal = ope.somar(numero1,numero2)
    return render_template("soma.html", titulo="Soma", resultado=this.resultadoFinal)

@app.route("/subtrair", methods=['POST', 'GET'])
def subt():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = ope.subtrair(numero1, numero2)
    return render_template("subtrair.html", titulo="Subtração", resultado=this.resultadoFinal)

@app.route("/multi", methods=['POST', 'GET'])
def mult():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = ope.multiplicar(numero1, numero2)
    return render_template("multi.html", titulo="multiplicar", resultado=this.resultadoFinal)

@app.route("/dividir", methods=['POST', 'GET'])
def divir():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = ope.dividir(numero1, numero2)
    return render_template("dividir.html", titulo="dividir", resultado=this.resultadoFinal)

@app.route("/potencia", methods=['POST', 'GET'])
def poten():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = ope.potencia(numero1, numero2)
    return render_template("potencia.html", titulo="Potência", resultado=this.resultadoFinal)

@app.route("/raiz", methods=['POST', 'GET'])
def raizes():
    if request.method == 'POST':
        numero1 = request.form['num1']
        this.resultadoFinal = ope.rais(numero1)
    return render_template("raiz.html", titulo="Raiz", resultado=this.resultadoFinal)

@app.route("/tabuada", methods=['POST', 'GET'])
def tabu():
    if request.method == 'POST':
        numero1 = request.form['num1']
        this.resultadoFinal = ope.tabuada(numero1)
    return render_template("tabuada.html", titulo="Tabuada", resultado=this.resultadoFinal)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
