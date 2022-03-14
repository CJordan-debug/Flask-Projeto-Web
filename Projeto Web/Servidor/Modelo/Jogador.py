class Jogador(object):

    def __init__(self, nome="", nickName="", avatar="", dataNasc="", email=""):
        self.__nome = nome
        self.__nickName = nickName
        self.__avatar = avatar
        self.__dataNasc = dataNasc
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome

    @property
    def nickName(self):
        return self.__nickName

    @nickName.setter
    def nickName(self, novoNickName):
        self.__nickName = novoNickName

    @property
    def avatar(self):
        return self.__avatar

    @avatar.setter
    def avatar(self, novoAvatar):
        self.__avatar = novoAvatar

    @property
    def dataNasc(self):
        return self.__dataNasc

    @dataNasc.setter
    def dataNasc(self, novoDataNasc):
        self.__dataNasc = novoDataNasc

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novoEmail):
        self.__email = novoEmail