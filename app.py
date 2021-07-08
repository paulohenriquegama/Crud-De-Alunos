from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

user = os.environ.get("user")
password = os.environ.get("password")
host = os.environ.get("host")
database = os.environ.get("database")

app = Flask(__name__)


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


@app.route('/alterar/<aluno_id>', methods=['GET', 'POST'])
def alterar(aluno_id):
    alterado = None
    aluno = Alunos.query.get(aluno_id)
    if request.method == 'POST':
        form = request.form
        aluno.nome = form['nome']
        aluno.sexo = form['sexo']
        aluno.email = form['email']
        aluno.img_url = form['img_url']
        aluno.contato = form['contato']
        aluno.descricao = form['descricao']
        db.session.commit()
        alterado = aluno.id
        return render_template('alterar.html', alterado=alterado)
    return render_template('alterar.html', aluno=aluno)


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


@app.route('/delete/<aluno_id>')
def delete(aluno_id):
    alunos = Alunos.aluno(aluno_id)

    return render_template('deletar.html', alunos=alunos)


@app.route('/delete/<aluno_id>/confirmed')
def delete_confirmed(aluno_id):
    sucesso = None

    alunos = Alunos.aluno(aluno_id)

    if alunos:
        db.session.delete(alunos)
        db.session.commit()
        sucesso = True

    return render_template('deletar.html', alunos=alunos, aluno_id=aluno_id, sucesso=sucesso)


if __name__ == '__main__':
    app.run(debug=True)
