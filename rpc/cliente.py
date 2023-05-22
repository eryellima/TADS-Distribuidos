import xmlrpc.client

print('\tCLIENTE')

IP = input('- Digite o IP do Servidor: ')
PORTA = int(input('- Digite a PORTA: '))

servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(IP, PORTA))

nome = "Eryel"

while(nome != 'sair'):
	nome = input('\n- Digite o nome de uma pessoa: ')
	numeroTelefonico = servidor.agenda(nome.lower())

	if numeroTelefonico == '1':
		print('\nNão Existe contatos para esse nome!')

	elif numeroTelefonico == '0':
		print('\nSaindo da Aplicação...')
	else:
		print('\nContato de '+nome.upper())
		print('-'*18)
		print('|'+ numeroTelefonico +'|')
		print('-'*18)