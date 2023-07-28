import grpc
import champion_pb2
import champion_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = champion_pb2_grpc.ChampionServiceStub(channel)

    # Solicitar informações de um campeão por nome
    campeao = input("Digite o nome do campeão que deseja consultar: ")

    response = stub.GetChampionByName(champion_pb2.ChampionNameRequest(name=campeao))
    if response.name:
        print("Nome:", response.name)
        print("Classe:", response.classe)
        print("Origem:", response.origin)
        print("Habilidades:", ', '.join(response.abilities))
    else:
        print("Campeão não encontrado.")

if __name__ == '__main__':
    run()
