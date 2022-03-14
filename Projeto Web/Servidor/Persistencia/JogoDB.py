from Servidor.Modelo.Jogo import Jogo
import sqlite3

caminhoBanco = "./Persistencia/dados/BancoDeDados.db"

class JogoDB(object):
    def __init__(self):
        self.__conexao = sqlite3.connect(caminhoBanco)
        with self.__conexao as conn:
            conn.execute("""
                            CREATE TABLE IF NOT EXISTS Jogo(
                                codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                categoria TEXT NOT NULL,
                                idadeMin INTEGER NOT NULL,
                                imagem TEXT NOT NULL,
                                descricao TEXT NOT NULL
                            ) 
                         """)
            conn.commit()

    def incluir(self, jogo):
        if isinstance(jogo, Jogo):
            with self.__conexao as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Jogo(nome, categoria, idadeMin," + \
                               " imagem, descricao) values (?,?,?,?,?)",
                               (jogo.nomeJogo, jogo.categoria, jogo.idadeMinima, jogo.imagem, jogo.descricao))
                jogo.codigo = cursor.lastrowid #pega o valor do código gerado pelo banco de dados
                conn.commit()

    def apagar(self, jogo):
        if isinstance(jogo, Jogo):
            with self.__conexao as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Jogo WHERE codigo = ?",(jogo.codigo,))
                conn.commit()

    def atualizar(self, jogo):
        if isinstance(jogo,Jogo):
            with self.__conexao as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE Jogo SET nome = ?, categoria = ? " + \
                               " idadeMin = ?, imagem = ?, descricao = ? " + \
                               "WHERE codigo = ?",
                               (jogo.nomeJogo, jogo.categoria, jogo.idadeMinima,
                                jogo.imagem, jogo.descricao, jogo.codigo)
                               )
                conn.commit()

    def consultar(self,termo=""):
        if isinstance(termo,int):
            with self.__conexao as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Jogo WHERE codigo=?",[termo])
                resultado = cursor.fetchone()
                if resultado:
                    return Jogo(resultado[0], #codigo
                                resultado[1], #nome
                                resultado[2], #categoria
                                resultado[3], #idadeMinima
                                resultado[4], #imagem
                                resultado[5]) #descricao
                else:
                    return None
        else: #a busca deverá ser realizada pelo nome do Jogo
            with self.__conexao as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Jogo WHERE nome LIKE ?", ["%" + termo + "%"])
                resultados = cursor.fetchall()
                if resultados:
                    jogos = []
                    for resultado in resultados:
                        jogo = Jogo(resultado[0], #codigo
                                    resultado[1], #nome
                                    resultado[2], #categoria
                                    resultado[3], #idadeMinima
                                    resultado[4], #imagem
                                    resultado[5]) #descricao
                        jogos.append(jogo)
                    return jogos
                else:
                    return None



















