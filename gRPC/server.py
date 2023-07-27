import graphene
import grpc
import time
import lol_champions_pb2
import lol_champions_pb2_grpc
from concurrent import futures



# Implementa o serviso definido no arquivo '.proto'
class ChampionService(lol_champions_pb2_grpc.ChampionServiceServicer):
    # Retonrna informações sobre alguns Champions do LoL com base no nome.
    def GetChampionInfo(self, request, context):
        champion_name = request.name.lower()
        if champion_name == 'aatrox':
            return lol_champions_pb2.ChampionResponse(
                name='Aatrox',
                role='Top Lane',
                difficulty=3,
                abilities=['The Darkin Blade', 'Infernal Chains', 'Umbral Dash', 'World Ender']
            )
        else:
            return lol_champions_pb2.ChampionResponse(
                name='Campeão Desconhecido',
                role='Desconhecido',
                difficulty=0,
                abilities=[]
            )



class ChampionType(graphene.ObjectType):
    name = graphene.String()
    role = graphene.String()
    difficulty = graphene.Int()
    abilities = graphene.List(graphene.String)


class Query(graphene.ObjectType):
    champion_info = graphene.Field(ChampionType, name=graphene.String())

    def resolve_champion_info(self, info, name):
        # Aqui você pode implementar a lógica para obter as informações do campeão
        # do LoL com base no nome fornecido.
        # Por enquanto, retornaremos algumas informações fictícias.
        if name.lower() == 'aatrox':
            return {
                'name': 'Aatrox',
                'role': 'Top Lane',
                'difficulty': 3,
                'abilities': ['The Darkin Blade', 'Infernal Chains', 'Umbral Dash', 'World Ender']
            }
        else:
            return {
                'name': 'Campeão Desconhecido',
                'role': 'Desconhecido',
                'difficulty': 0,
                'abilities': []
            }

schema = graphene.Schema(query=Query)


# Configurações do server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lol_champions_pb2_grpc.add_ChampionServiceServicer_to_server(ChampionService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor iniciado na porta 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

# Inicia o server
if __name__ == '__main__':
    serve()
