import graphene
import grpc
import champion_pb2
import champion_pb2_grpc
from graphene.types.generic import GenericScalar
import asyncio
import websockets

class Champion(graphene.ObjectType):
    name = graphene.String()
    class_ = graphene.String()
    origin = graphene.String()
    abilities = graphene.List(graphene.String)

class Query(graphene.ObjectType):
    champion = graphene.Field(Champion, name=graphene.String())

    def resolve_champion(self, info, name):
        channel = grpc.insecure_channel('localhost:50051')
        stub = champion_pb2_grpc.ChampionServiceStub(channel)

        response = stub.GetChampionByName(champion_pb2.ChampionNameRequest(name=name))
        if response.name:
            return Champion(
                name=response.name,
                class_=response.class_,
                origin=response.origin,
                abilities=response.abilities,
            )
        return None

schema = graphene.Schema(query=Query)

async def send_graphql_query():
    url = "ws://localhost:8000/graphql"

    # Consulta GraphQL que você deseja enviar para o servidor
    query = "{ champion(name: \"Aatrox\") { name class origin abilities } }"

    async with websockets.connect(url) as websocket:
        # Envia a consulta GraphQL para o servidor
        await websocket.send(query)

        # Recebe a resposta do servidor e imprime no console
        response = await websocket.recv()
        print(response)

if __name__ == '__main__':
    asyncio.run(send_graphql_query())
