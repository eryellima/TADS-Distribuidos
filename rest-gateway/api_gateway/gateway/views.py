from django.http import JsonResponse

def gateway(request):
    # Implemente aqui a lógica do gateway para fazer as chamadas à sua API REST
    # Use a biblioteca requests ou qualquer outra biblioteca de sua preferência para fazer as requisições
    
    # Exemplo de resposta para um cliente:
    response_data = {
        'message': 'API Gateway - Endpoint de gateway'
    }
    
    return JsonResponse(response_data)
