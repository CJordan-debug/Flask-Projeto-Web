from Servidor.Modelo.Jogo import Jogo
from Servidor.Persistencia.JogoDB import JogoDB

jogoDB = JogoDB()
jogo1 = jogoDB.consultar(1)
print(jogo1)
jogoMinecraft = jogoDB.consultar("Mine")
print(jogoMinecraft[0])

print("------Todos os jogos-----------")
todosJogos = jogoDB.consultar("")
for jogo in todosJogos:
    print(jogo)

# jogo1 = Jogo(0,"Battlefield","FPS",16,'./imagens/battlefield.png',"Um jogo emocionante...")
# jogo2 = Jogo(0,"Super Mario Bros","CASUAL",3,'./imagem/mario.png',"Nostalgia...")
# jogo3 = Jogo(0,"Minecraft","SANDBOX",3,'./imagem/minecraft',"Blocos...")
#
# jogoDB = JogoDB()
#
# jogoDB.incluir(jogo1)
# print("Jogo " + jogo1.nomeJogo + " incluido com sucesso com o código " + str(jogo1.codigo))
# jogoDB.incluir(jogo2)
# print("Jogo " + jogo2.nomeJogo + " incluido com sucesso com o código " + str(jogo2.codigo))
# jogoDB.incluir(jogo3)
# print("Jogo " + jogo3.nomeJogo + " incluido com sucesso com o código " + str(jogo3.codigo))