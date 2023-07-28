import grpc
import champion_pb2
import champion_pb2_grpc
from concurrent import futures



class ChampionServiceServicer(champion_pb2_grpc.ChampionServiceServicer):
    def GetChampionByName(self, request, context):
        if request.name == "Aatrox":
            return champion_pb2.Champion(
                name="Aatrox",
                classe="Fighter",
                origin="Darkin",
                abilities=["The Darkin Blade", "Infernal Chains", "Umbral Dash", "World Ender"]
            )
        elif request.name == "Ahri":
            return champion_pb2.Champion(
                name="Ahri",
                classe="Mage",
                origin="Vastaya",
                abilities=["Orb of Deception", "Fox-Fire", "Charm", "Spirit Rush"]
            )
        else:
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

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    champion_pb2_grpc.add_ChampionServiceServicer_to_server(ChampionServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("O servidor está rodando na porta 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
