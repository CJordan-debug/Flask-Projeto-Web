from flask import Flask, render_template, request, redirect, url_for
from Servidor.Utilitarios import validarDadosJogo
from Servidor.Modelo.Jogo import Jogo
from Servidor.Persistencia.JogoDB import JogoDB

import datetime
import os

def create_app():
    app = Flask(__name__)
    @app.route('/saudacao',methods=['GET'])
    def saudacao():
        nome=request.args.get('nome')
        idade=request.args.get('idade')
        hora = datetime.datetime.now().time().hour
        return render_template('saudacao.html',nome=nome, hora=hora, idade=idade)

    @app.route('/',methods=['GET'])
    def raiz():
        return redirect(url_for('index'))

    @app.route('/index',methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/games',methods=["GET","POST"])
    def games():
        return render_template('games.html')

    @app.route('/cadastrarJogos',methods=["GET","POST"])
    def cadastrarJogos():
        cwd = os.getcwd()
        print(cwd)
        jogoDB = JogoDB()
        #recuperando todos os jogos cadastrados
        listaJogos = jogoDB.consultar("")

        if request.method == "GET":
            return render_template('cadastrarJogos.html',listaJogos = listaJogos)
        elif request.method == "POST":
            nomeJogo  = request.form["nomeJogo"]
            categoria = request.form["categoria"]
            idadeMin  = int(request.form["idadeMin"])
            foto = request.files['foto']
            caminho='./static/imagens/SemImagem.png'
            if foto and foto.filename:
                caminho ='./static/imagens/' + foto.filename
                foto.save(caminho)

            descricao = request.form["descrição"]

            #Retorna o cadastro de Jogos após uma ação cadastrar
            if validarDadosJogo(nomeJogo,categoria,idadeMin,caminho,descricao):
                jogo = Jogo(0,nomeJogo,categoria,idadeMin,caminho,descricao)
                jogoDB.incluir(jogo)
                return render_template('cadastrarJogos.html', listaJogos = listaJogos)
            else:
                return render_template('cadastrarJogos.html', nomeJogo=nomeJogo,
                                                              categoria=categoria,
                                                              idadeMin=idadeMin,
                                                              foto=caminho,
                                                              descricao=descricao,
                                                              listaJogos = listaJogos)
        else:
            return redirect(url_for("index"))



    return app

meuApp = create_app()
print(os.path)
meuApp.run('0.0.0.0',5000);