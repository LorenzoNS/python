from . import db


class Operacao(db.Model):
    """Model — dados e acesso ao banco (tabela operacoes)."""

    __tablename__ = "operacoes"

    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Float, nullable=False)
    num2 = db.Column(db.Float, nullable=False)
    operacao = db.Column(db.String(120), nullable=False)
    etapas = db.Column(db.String(120), nullable=False)
    resultado = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)


#   CRIAR A TABELA COM datetime AQUI
        

    @classmethod
    def salvar(cls, num1, num2, operacao, etapas, resultado, date):
        registro = cls(
            num1=num1,
            num2=num2,
            operacao=operacao,
            etapas=etapas,
            resultado=str(resultado),
            date=date
        )
        db.session.add(registro)
        db.session.commit()
    #  ADICIONAR E FAZER O COMMIT AQUI
        return registro

    @classmethod
    def listar_recentes(cls, limite=10):
        return (
            cls.query.order_by(cls.date.desc()).limit(limite).all()
        )

    def __repr__(self):
        return f"<Operacao {self.id}: {self.etapas}>"
