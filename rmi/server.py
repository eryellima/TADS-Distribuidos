import Pyro4

# Origens
origemAdmin = "Origem: ADMINISTRADOR\n 4 Champions\n O ADMIN programa uma configuração personalizada por jogador em cada jogo.\n 2-Inicializar causa e efeito\n 4-Adicione outro efeito ao programa\n 6-Aumente o nível anterior 180%\n Champions: Blitzcrank, Camille, Leblanc, Ashe"

#origemEsqAnima = "Origem: Esquadrão Anima\n 6 Champions\n Os membros do Esquadrão Anima ganham fama por marcar abates de campeões. Quando eles param para comemorar uma morte, eles ganham permanentemente 6 de Vida máxima por ponto de fama. A fama beneficia imediatamente todo o Anima Squad. Anima Squad também ganha:\n 3-15%' de dano de ataque e 15 de poder de habilidade\n 5-35%' de dano de ataque e 35 de poder de habilidade\n 55%' de dano de ataque e 55 de poder de habilidade\n Champions: Nasus, Sylas, Jinx, Riven, Vayne, Miss Fortune"

#origemCivil = "Origem Civil\n 3 Champions\n Se houver um Civil vivo, sua equipe se inspira a protegê-lo ganhando Mana a cada 2 segundos.\n 1-2 de mana\n 2-4 de mana\n 3-10 de mana\n Champions: Galio, Sivir, Janna"

#origemCorrompido = "Origem: Corrompido\n 1 Champion\n 1-Início do combate: fique adormecido enquanto absorve as almas dos aliados que morrem. Ganhe 40 de Poder de Habilidade para cada alma. Uma vez por combate com 60%' de saúde (ou quando seu time morrer), ganhe vida e lute.\n Champions: Fiddle"

#origemGadGeteen = "Origem: GadGeteen\n 5 Champions\n Gadgeteens criam armas modificadas aleatoriamente com efeitos poderosos. Qualquer campeão pode equipar os itens, mas eles se desfazem após 1 rodada.\n 3-crie 1 item a cada rodada\n 5-crie 2 itens a cada rodada\n Champions: Lulu, Poppy, Zoe, Annie, Nunu"



# Champions
blitz = "Blitazcrank\n Origem: ADMINISTRADOR\n Habilidade: Defesas Estáticas (ativo)\n Blitzcrank cria um campo poderoso ao seu redor, reduzindo todo o dano recebido por 4 segundos.\n Redução de dano: 45%/55%/65%\n Build: Gargolitica, Sunfire, Warmog\n Custo: 1"

#camille = "Camille\n Origem: ADMINISTRADOR\n Habilidade: Varredura Tática (ativo)\n Camille varre com a perna, causando dano físico e desarmando os inimigos atingidos por alguns segundos. Desarmar: o alvo não pode se mover ou atacar\n Porcetagem de Dano de Ataque: 180%/200%/225%\n Dano Bônus: 60/75/100\n Duração do desarme: 1,5/1,6/1,75\n Build: Sedenta, Gume, Titanica\n Custo: 2"

#leblanc = "Leblanc\n Origem ADMINISTRADOR\n Habilidade: Sigilo da Malícia (ativo)\n Leblanc dispara sigilos em seu alvo, cada um causando dano mágico. Se o alvo morrer, ela completa o lançamento dos sigilos restantes no inimigo mais próximo, mas adiciona mais 1 sigilo.\n Dano: 80/100/130\n Número de sigilos 5/6/8\n Build: Blue, Gigantes, Manopla de Joias\n Custo: 3"

#soraka = "Soraka\n Origem: ADMINISTRADOR\n Habilidade: Chamado Estelar (ativo)\n Soraka lança uma estrela em seu alvo, que causa dano mágico e cura Soraka em 10%' de sua saúde máxima. A cada 3 lançamentos, ela lança estrelas em cada um dos inimigos mais próximos.\n Dano: 225/340/750\n Estrelas Fortalecidas: 3/3/5\n Build: Blue, Gigantes, Manopla de Joias\n Custo: 4"

#nasus = "Nasus\n Origem: Anima Squad\n Habilidade: Bonk! (ativo)\n Nasus bate seu cajado em seu alvo, causando dano físico e 40%' de resfriamento por 3 segundos. Chill: reduz a velocidade de ataque\n Dano Bõnus: 60/90/135\n Build: Sedenta, Canhão, Titanica\n Custo: 1"



# Itens
gargolitica = "Placa de Pedra Gárgula\n MR + 20, Armor +20\n Conceda 15 de Armadura e 15 de Resistência Mágica para cada inimigo mirando no portador."

#gume = "Gume do Infinito\n AD +10, Crit +20%\n Concede 15%' de bônus de chance de acerto Crítico. O dano de uma habilidade pode atingir criticamente."

#sedenta = "Sedenta por Sangue\n AD +10, MR+20\n Conceda 20%' de Ominvamp. Uma vez por combate com 40%' de Vida, ganhe um escudo máximo de 25%' de Vida que dura até 5 segundos."

#sunfire = "Capa de Fogo Solar\n Vida +150, Armor +20\n Conceda 150 bônus de Saúde. A cada 2 segundos, um inimigo dentro de 2 hexágonos é 10% queimado e 33%' ferido por 10 segundos. [Único - apenas 1 por campeão] Queimadura: causa um pouco da Vida máxima do alvo como dano verdadeiro Ferimento: reduz a cura recebida"

#titanica = "Resolução de Titã\n AS +10%, Armor +20\n Concede 2%' de Dano de Ataque e 2 de Poder de Habilidade ao atacar ou receber dano, acumulando até 25 vezes. Em pilhas completas, conceda 25 de Armadura e Resistência Mágica."



@Pyro4.expose
class TFT(object):
    def sistemas(self):
        return "Estes são aprimoramentos específicos do campeão que são divididos em duas categorias. Cada campeão terá um aumento de suporte e transporte. Uma vez por jogo, você terá que escolher um aprimoramento de Herói entre três opções. Como acontece com os aumentos regulares, você também poderá rolar novamente suas escolhas uma vez por jogo."

    def caracteristicas(self):
        return origemAdmin #, origemCivil, origemGadGeteen, origemCorrompido, origemEsqAnima

    def champions(self):
        return blitz #, camille, leblanc, nasus, soraka

    def itens(self):
        return gargolitica #, gume, sedenta, sunfire, titanica

    def aprimoramentos(self):
        return "função ainda não adicionada"


daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
# register the greeting maker as a Pyro object
uri = daemon.register(TFT)
# register the object with a name in the name server
ns.register("example.champion", uri)

print("Server ready.")
# start the event loop of the server to wait for calls
daemon.requestLoop()
