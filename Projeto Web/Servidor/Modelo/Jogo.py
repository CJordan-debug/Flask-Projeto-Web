"""
  Classe Jogo que tem a responsabilidade de representar um jogo do mundo real
"""
class Jogo(object):
    """
        construtor da classe com os seguintes parâmetros
        nomeJogo  : string,
        categoria : string,
        idadeMinima: número,
        imagem : string,
        descricao: string
    """
    def __init__(self,codigo = 0, nomeJogo = "", categoria="", idadeMinima=0, imagem="",descricao=""):
        super().__init__()
        #atributos da classe Jogo são privados
        self.__codigo = codigo
        self.__nomeJogo = nomeJogo
        self.__categoria = categoria
        self.__idadeMinima = idadeMinima
        self.__imagem = imagem
        self.__descricao = descricao

    #Métodos que irão proporcionar o acesso aos atributos da classe
    #Ou seja, métodos get e set

    #get e set para o codigo do jogo
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novoCodigo):
        self.__codigo = novoCodigo


    #get e set para o nome do jogo
    @property
    def nomeJogo(self):
        return self.__nomeJogo

    @nomeJogo.setter
    def nomeJogo(self, novoNome):
        self.__nomeJogo = novoNome

    #get e set para a categoria
    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, novaCategoria):
        self.__categoria = novaCategoria


    #get e set para a idadeMinima
    @property
    def idadeMinima(self):
        return self.__idadeMinima

    @idadeMinima.setter
    def idadeMinima(self, novaIdadeMinima):
        self.__idadeMinima = novaIdadeMinima

    #get e set para a imagem
    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, novaImagem):
        self.__imagem = novaImagem

    #get e set para a descrição
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, novaDescricao):
        self.__descricao = novaDescricao

    def __str__(self):
        return "\nCodigo: " + str(self.__codigo) + \
               "\nJogo: " + self.__nomeJogo + \
               "\nCategoria: " + self.__categoria + \
               "\nIdade Mínima: " + str(self.__idadeMinima) + \
               "\nLocalização da Imagem: " + self.__imagem + \
               "\nDescrição: " + self.__descricao + "\n"