
from threading import active_count
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

user = 'llfxwees'
password = 'QF7I9SRL2Fmh48-sT89sy4rz7dZHaNE3'
host = 'tuffi.db.elephantsql.com'
database = 'llfxwees'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Alunos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    sexo = db.Column(db.String)
    email = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String)
    contato = db.Column(db.String(20))
    descricao = db.Column(db.String)
    ativo = db.Column(db.Boolean)

    def __init__(self, nome, sexo, email, img_url, contato, descricao, ativo=True):
        self.nome = nome
        self.sexo = sexo
        self.email = email
        self.img_url = img_url
        self.contato = contato
        self.descricao = descricao
        self.ativo = ativo

    @staticmethod
    def listar():
        return Alunos.query.all()

    @staticmethod
    def aluno(aluno_id):
        return Alunos.query.get(aluno_id)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/listar')
def listar():
    alunos = Alunos.listar()
    return render_template("listar.html", alunos=alunos)


@app.route('/aluno/<aluno_id>')
def aluno(aluno_id):
    aluno = Alunos.aluno(aluno_id)
    return render_template('aluno.html', aluno=aluno)


@app.route('/criar', methods=['GET', 'POST'])
def create():
    id_atribuido = None
    if request.method == "POST":
        form = request.form
        aluno = Alunos(form['nome'], form['sexo'], form['email'],
                       form['img_url'], form['contato'], form['descricao'])
        db.session.add(aluno)
        db.session.commit()
        id_atribuido = aluno.id

    return render_template('create.html', id_atribuido=id_atribuido)


if __name__ == '__main__':
    app.run(debug=True)
