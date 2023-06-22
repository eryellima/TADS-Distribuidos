import requests
from django.shortcuts import render
from django.http import HttpResponse

def gateway(request):
    # Lógica para receber a requisição do front-end e encaminhar para a API
    # por exemplo, se a requisição for um GET para /api/tasks/, você pode fazer algo como:
    if request.method == 'GET' and request.path == '/gateway/api/tasks/':
        response = requests.get('http://localhost:8001/tasks/')
        return HttpResponse(response.content)
    
    # Implemente a lógica para outros métodos HTTP e URLs do front-end aqui
    
    # Se nenhuma correspondência for encontrada, retorne uma resposta de erro
    return HttpResponse('URL não encontrada', status=404)
