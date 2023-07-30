# Importa as biblioteca necessárias
from spyne import Application, rpc, ServiceBase, Array, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import json
import requests

# URL base da API de Pokemons
base_url = "https://pokeapi.co/api/v2/"

# Define a classe do serviço que será exposto pelo servidor SOAP
class Pokemon(ServiceBase):
     # Define um método remoto chamado 'get_pokemon' que recebe o ID de um Pokémon e retorna informações sobre ele
    @rpc(Unicode, _returns=Unicode)
    def get_pokemon(self, pokemon_id):
        # Faz uma requisição HTTP GET à API de Pokémons para obter os dados do Pokémon
        response = requests.get(f"{base_url}/pokemon-form/{pokemon_id}")
        # Converte o JSON da resposta para um dicionário Python
        pokemon_data = response.json()

        # Extrai o nome do Pokémon do dicionário
        pokemon_name = pokemon_data.get("name", "")
        # Extrai os tipos do Pokémon do dicionário e cria uma lista com seus nomes
        types = [type_data["type"]["name"] for type_data in pokemon_data.get("types", [])]
         # Junta os nomes dos tipos em uma única string, separados por vírgula
        pokemon_type = ", ".join(types)

        # Cria uma string de resultado com o nome e tipo do Pokémon
        result = f"name: {pokemon_name}, Type: {pokemon_type}"
        return result
    

# Cria uma instância da aplicação SOAP e registra o serviço 'Pokemon' nela
soap_app = Application([Pokemon],
                       tns="soap.server",
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())


# Cria uma aplicação WSGI (Web Server Gateway Interface) a partir da aplicação SOAP
application = WsgiApplication(soap_app)


# Executa o servidor se o script estiver sendo executado diretamente
if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server

    # Configuração do nível de log para DEBUG
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    # Imprime as informações sobre o servidor na console
    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    # Cria um servidor WSGI na porta 8000 e o coloca para ouvir
    server = make_server('127.0.0.1', 8000, application)  
    server.serve_forever()
