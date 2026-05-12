from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <body>
            <h1>Currículo</h1>

            <h2>Informações Pessoais</h2>
            <ul>
                <li><strong>Nome:</strong> Lorenzo Nunes</li>  
                <li><strong>Email:</strong> 12402133@aluno.cotemig.com.br</li>
                <li><strong>Telefone:</strong> (11) 99999-9999</li>
            </ul>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)