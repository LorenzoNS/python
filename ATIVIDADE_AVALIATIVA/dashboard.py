from flask import Blueprint, render_template
from models import Sessao

cinema_bp = Blueprint("dashboard", __name__)

@cinema_bp.route("/")
def index():
    return render_template("index.html", sessoes = Sessao.listar_com_detalhes())