from flask import Flask


app = Flask(__name__)

@app.route('/decorator')
def decorator():
    return 'Em Python, o decorator é uma função que recebe como atributo outra função, que serve para executar uma função ao chamar outra. No Flask ele é utilizado para executar métodos no http.'

if __name__ == '__main__':
    app.run(debug=True)