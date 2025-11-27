from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.

@app.route('/soma')
def soma():
    v1 = int(request.args.get('valor1'))
    v2 = int(request.args.get('valor2'))
    return f'{v1} + {v2} = {v1+v2}'


@app.route('/subtrair')
def subtrair():
    v1 = int(request.args.get('valor1'))
    v2 = int(request.args.get('valor2'))
    return f'{v1} - {v2} = {v1-v2}'

@app.route('/multiplicar')
def multiplicar():
    v1 = int(request.args.get('valor1'))
    v2 = int(request.args.get('valor2'))
    return f'{v1} X {v2} = {v1*v2}'

@app.route('/dividir')
def dividir():
    v1 = int(request.args.get('valor1'))
    v2 = int(request.args.get('valor2'))
    if v2 == 0:
        return 'Erro. Divisão por zero não é permitida.'
    return f'{v1} / {v2} = {v1/v2}'


if __name__ == "__main__":
    app.run(debug=True)
