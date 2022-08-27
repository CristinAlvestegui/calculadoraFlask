from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)#Referência ao objeto Flask, crinado uma variavel APP que guarda os elementos do Flask
@app.route("/")#Pagina index - priemira página de qualquer site

def homepage():
    return render_template("index.html")

@app.route("/soma", methods=['POST','GET'])
def soma():
    if request.method == 'POST':
        num1 = request.form['num1']#dentro do [] vai o nome da variavel, name no HTML
        num2 = request.form['num2']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
