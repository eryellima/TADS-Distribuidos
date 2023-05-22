from xmlrpc.server import SimpleXMLRPCServer

print("\tSERVIDOR")

IP = '127.0.0.1'
PORTA = 8080

def agenda(nome):
	if nome == "eryel":
		return "(84) 99912-1057"
	elif nome == "maria":
		return "(84) 99914-4420"
	elif nome == "joao":
		return "(84) 99915-9644"
	elif nome == "joaomaria":
		return "(84) 99914-9644"
	elif nome == "sair":
		return "0"
	else:
		return "1"

print('\nAVISO: O não escrever no servidor.')

print('\nEsperando por clientes: ')

servidor = SimpleXMLRPCServer((IP,PORTA))

servidor.register_function(agenda, "agenda")

servidor.serve_forever()