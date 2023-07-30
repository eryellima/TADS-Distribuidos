import grpc
import champion_pb2
import champion_pb2_grpc
from concurrent import futures



class ChampionServiceServicer(champion_pb2_grpc.ChampionServiceServicer):
    def GetChampionByName(self, request, context):
        if request.name == "Ashe":
            return champion_pb2.Champion(
                name="Ashe",
                classe="Atirador",
                origin="Freljord",
                abilities=[
                            "Tiro Congelado (Passiva): Os ataques de Ashe reduzem a velocidade do alvo e fazem com que ela cause mais dano a ele. Os Acertos Críticos de Ashe não causam dano adicional, mas reduzem ainda mais a velocidade do alvo.\n",
                            "Concetração (Habilidade Q): Ashe acumula Foco ao atacar. Quando o Foco chega ao máximo, Ashe pode conjurar Concentração para consumir todos os acúmulos de Foco, aumentando temporariamente sua Velocidade de Ataque e transformando seu ataque básico em uma poderosa rajada de ataques pela duração do efeito.\n",
                            "Rajada (Habilidade W): Ashe dispara flechas em cone, causando dano aumentado. Também aplica Tiro Congelado.\n",
                            "Olhar do Falcão (Habilidade E): Ashe envia seu Espírito do Falcão em uma missão de exploração em qualquer ponto do mapa.\n",
                            "Flecha de Cristal Encatada ( Habilidade R): Ashe dispara um projétil de gelo em linha reta. Se a flecha colidir com um Campeão inimigo, ela causa dano e o atordoa. A duração do atordoamento depende da distância percorrida pela flecha. Além disso, unidades inimigas próximas recebem dano e lentidão."]
            )
        elif request.name == "Blitz":
            return champion_pb2.Champion(
                name="Blitzcrank",
                classe="Tanque",
                origin="Zaun",
                abilities=[
                            "Barreida de Mana (Passiva): Blitzcrank recebe um Escudo com base em seu Mana ao ficar com a Vida baixa.\n",
                            "Puxão Biônica (Habilidade Q): Blitzcrank dispara a mão direita para pegar um inimigo no trajeto, causando dano e puxando-o em sua direção.\n",
                            "Turbo (Habilidade W): Blitzcrank sobrecarrega-se para aumentar drasticamente suas Velocidades de Ataque e de Movimento. Após o fim do efeito, sofre Lentidão temporariamente.\n",
                            "Punho do Poder (Habilidade E): Blitzcrank carrega seu punho para fazer com que o próximo Ataque cause o dobro de dano e arremesse o alvo ao ar.\n",
                            "Campo Estático (Habilidade R): Inimigos atacados por Blitzcrank são marcados e sofrem dano de eletricidade após 1s. Ele também pode ativar esta habilidade para remover escudos de inimigos próximos, causar dano e silenciá-los brevemente."]
            )
        elif request.name == "Barum":
            return champion_pb2.Champion(
                name="Braum",
                classe="Suporte",
                origin="Freljord",
                abilities=[
                            "Golpes Concussivos (Passiva): Os ataques básicos de Braum aplicam Golpes Concussivos. Uma vez que o primeiro acúmulo é aplicado, os ataques básicos de aliados também acumulam Golpes Concussivos. Ao atingir 4 acúmulos, o alvo é atordoado e sofre Dano Mágico. Pelos próximos segundos, ele não pode receber acúmulos, mas recebe Dano Mágico adicional dos ataques de Braum.\n",
                            "Mordida do Inverno (Habilidade Q): Braum dispara rajadas congelantes de seu escudo, causando Dano Mágico e redução de velocidade. Aplica um acúmulo de Golpes Concussivos.\n",
                            "Eu te Protejo (Habilidade W): Braum salta à frente de um Campeão ou tropa aliada alvo. Ao aterrissar, ele e o aliado recebem Armadura e Resistência Mágica por alguns segundos..\n",
                            "Inquebrável (Habilidade E): Braum levanta seu escudo em uma direção por muitos segundos, interceptando todos os projéteis e fazendo com que o atinjam e sejam destruídos. Ele nega completamente o dano do primeiro ataque e reduz o dano de todos os ataques seguintes provenientes da mesma direção.\n",
                            "Fissura Glacial (Habilidade R): Braum golpeia o chão, arremessando ao ar inimigos próximos e em linha reta à sua frente. Uma fissura é deixada no caminho, causando redução de velocidade nos inimigos."]
            )
        elif request.name == "Cait":
            return champion_pb2.Champion(
                name="Caitlyn",
                classe="Atirador",
                origin="Piltover",
                abilities=[
                            "Bem na Mira (Passiva): A cada poucos ataques básicos, ou contra um alvo preso em uma armadilha ou rede, Caitlyn fará um disparo Bem na Mira causando dano adicional que escala com sua Chance de Acerto Crítico. Em alvos presos por armadilhas ou pela rede, o alcance de Bem na Mira de Caitlyn é dobrado.\n",
                            "Pacificadora de Piltover (Habilidade Q): Caitlyn prepara seu rifle por 1s para fazer um disparo penetrante que causa Dano Físico (causa menos dano a alvos subsequentes).\n",
                            "Armadilha Mecânica Yordle (Habilidade W): Caitlyn posiciona uma armadilha que, quando ativada, revela e imobiliza o Campeão inimigo por 1,5s e concede a Caitlyn um Bem na Mira fortalecido.\n",
                            "Rede Calibre 90 (Habilidade E): Caitlyn atira uma rede pesada para reduzir a velocidade do seu alvo. O recuo projeta Caitlyn para trás.\n",
                            "Ás na Manga (Habilidade R): Caitlyn se concentra para fazer o disparo perfeito, causando dano drástico em um único alvo a uma longa distância. Campeões inimigos podem interceptar o projétil e tomar dano no lugar de seu aliado."]
            )
        elif request.name == "Darius":
            return champion_pb2.Champion(
                name="Darius",
                classe="Lutador",
                origin="Noxus",
                abilities=[
                            "Hemorragia (Passiva): Os Ataques e Habilidades de dano de Darius fazem os inimigos sangrarem, causando Dano Físico ao longo de 5s e acumulando até 5 vezes. Darius se enfurece e recebe uma grande quantidade de Dano de Ataque quando o alvo alcança o máximo de acúmulos.\n",
                            "Dizimar (Habilidade Q): Darius pega impulso e golpeia com seu machado em um movimento circular. Os inimigos atingidos pela lâmina recebem mais dano do que aqueles atingidos pelo cabo. Darius cura a si mesmo com base nos Campeões inimigos e monstros grandes atingidos pela lâmina.\n",
                            "Ataque Multilador (Habilidade W): O próximo ataque de Darius acerta uma artéria importante do inimigo. Enquanto a vítima sangra, a Velocidade de Movimento dela é reduzida.\n",
                            "Apreender (Habilidade E): Darius afia seu machado, fazendo com que seu Dano Físico ignore passivamente um percentual da Armadura do alvo. Quando ativado, Darius ataca seus inimigos com o gancho do seu machado e os puxa em sua direção.\n",
                            "Guilhotina de Noxus (Habilidade R): Darius salta na direção de um Campeão inimigo e o atinge com um golpe letal, causando Dano Verdadeiro. Este dano aumenta a cada acúmulo de Hemorragia no alvo. Se Guilhotina de Noxus causar o golpe final, seu Tempo de Recarga é zerado por um breve momento."]
            )
        elif request.name == "Kai'sa":
            return champion_pb2.Champion(
                name="Kai'sa",
                classe="Atirador",
                origin="Vazio",
                abilities=[
                            "Segunda Pele (Passiva): Os ataques básicos de Kai'Sa acumulam Plasma, causando Dano Mágico adicional crescente. Efeitos imobilizadores de aliados ajudam a acumular Plasma. Além disso, as aquisições de itens de Kai'Sa aprimoram suas habilidades básicas, deixando-as mais poderosas.\n",
                            "Chuva Icathiana (Habilidade Q): Kai'Sa dispara uma chuva de projéteis que correm atrás de alvos próximos. Arma Viva: Chuva Icathiana é aprimorada e lança mais mísseis.\n",
                            "Exploradora do Vazio (Habilidade W): Kai'Sa lança um projétil de longo alcance, marcando inimigos com sua passiva. Arma Viva: Exploradora do Vazio é aprimorada e aplica mais marcas passivas e tem o Tempo de Recarga reduzido ao acertar um Campeão.\n",
                            "Sobrecarga (Habilidade E): Kai'Sa aumenta brevemente sua Velocidade de Movimento, depois aumenta sua Velocidade de Ataque. Arma Viva: Sobrecarga é aprimorada e concede Invisibilidade por um breve momento.\n",
                            "Instinto Assassino (Habilidade R): Kai'Sa avança para perto de um Campeão inimigo."]
            )
        elif request.name == "Pyke":
            return champion_pb2.Champion(
                name="Pyke",
                classe="Suporte alkjdlkasdjhfalksdhflk",
                origin="Aguas de Sentina",
                abilities=[
                            " Dádiva dos Afogados (Passiva): Quando Pyke está escondido dos inimigos, ele regenera o dano recebido recentemente de Campeões. Pyke também não ganha Vida máxima adicional de nenhuma fonte, mas ganha DdA adicional.\n",
                            "Espero de Osso (Habilidade Q): Pyke esfaqueia um inimigo à sua frente ou puxa um inimigo em direção a si mesmo.\n",
                            " Mergulho Fantasma (Habilidade W): Pyke entra em camuflagem e ganha Velocidade de Movimento significativa que decai ao longo do tempo.\n",
                            "Ressaca Espectral (Habilidade E): Pyke avança e deixa para trás um fantasma, que avança até ele e atordoa os Campeões inimigos pelo caminho.\n",
                            "Morte das Profundezas (Habilidade R): Pyke teleporta até inimigos com Vida baixa e os executa, permitindo que ele conjure a habilidade novamente e concedendo ouro adicional ao aliado que der assistência."]
            )
        
        else:
            # Retorna um campeão vazio caso não seja encontrado nenhum campeão com o nome fornecido.
            return champion_pb2.Champion()
        

        def ListChampions(self, request, context):
            champions = [
                champion_pb2.Champion(
                    name="Aatrox",
                    class_="Fighter",
                    origin="Darkin",
                    abilities=["The Darkin Blade", "Infernal Chains", "Umbral Dash", "World Ender"]
                ),
                champion_pb2.Champion(
                    name="Ahri",
                    class_="Mage",
                    origin="Vastaya",
                    abilities=["Orb of Deception", "Fox-Fire", "Charm", "Spirit Rush"]
                ),
            ]

            return champion_pb2.ChampionList(champions=champions)

# Função que cria e inicializa o servidor gRPC.
def serve():
    # Cria um servidor usando ThreadPoolExecutor para lidar com as chamadas de procedimento remoto.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Adiciona o serviço ChampionServiceServicer ao servidor.
    champion_pb2_grpc.add_ChampionServiceServicer_to_server(ChampionServiceServicer(), server)
    # Adiciona uma porta para o servidor aceitar conexões (Neste caso, uma porta insegura).
    server.add_insecure_port('[::]:50051')
    print("O servidor está rodando na porta 50051...")
    # Inicia o servidor
    server.start()
    # Aguarda o término do servidor (isso evita que o programa saia imediatamente após iniciar o servidor).
    server.wait_for_termination()

# Bloco de código que executa a função 'serve()' somente se o script for executado diretamente.
if __name__ == '__main__':
    serve()
