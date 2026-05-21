from flask import Flask, request, render_template_string

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuarios = ["lorenzo", "janaina", "dolga", "antonio"]
    senhas = ["12402133", "cotemig2026", "cotemig2026", "cotemig2026"]

    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario in usuarios:
        if senha == senhas[usuarios.index(usuario)]:
            return f"<h1>Bem-vindo(a), {usuario}!</h1>"
        else:
            return "<h1>Login inválido</h1>"
    else:
        return "<h1>Login inválido</h1>"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)