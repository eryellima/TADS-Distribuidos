import zeep
from zeep import Client

client = zeep.Client(wsdl='http://localhost:3000/tasks?wsdl')

task = {'title': 'Comprar leite', 'description': 'Comprar leite na loja'}

response = client.service.AddTask(task)

print(response)
