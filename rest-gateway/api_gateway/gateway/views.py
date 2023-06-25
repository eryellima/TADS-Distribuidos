import requests
from django.http import JsonResponse

def Champion_list(request):
    api_rest_url = 'http://localhost:8001/api/champions/'
    response = requests.get(api_rest_url)
    champions_data = response.json()
    return JsonResponse(champions_data, safe=False, json_dumps_params={'ensure_ascii': False})

def Champion_detail(request, pk):
    api_rest_url = f'http://localhost:8001/api/champions/{pk}/'
    response = requests.get(api_rest_url)
    champion_data = response.json()
    return JsonResponse(champion_data, json_dumps_params={'ensure_ascii': False})

def Origem_list(request):
    api_rest_url = 'http://localhost:8001/api/origens/'
    response = requests.get(api_rest_url)
    champions_data = response.json()
    return JsonResponse(champions_data, safe=False, json_dumps_params={'ensure_ascii': False})

def Origem_detail(request, pk):
    api_rest_url = f'http://localhost:8001/api/origens/{pk}/'
    response = requests.get(api_rest_url)
    champion_data = response.json()
    return JsonResponse(champion_data, json_dumps_params={'ensure_ascii': False})

def Classe_list(request):
    api_rest_url = 'http://localhost:8001/api/classes/'
    response = requests.get(api_rest_url)
    champions_data = response.json()
    return JsonResponse(champions_data, safe=False, json_dumps_params={'ensure_ascii': False})

def Classe_detail(request, pk):
    api_rest_url = f'http://localhost:8001/api/classes/{pk}/'
    response = requests.get(api_rest_url)
    champion_data = response.json()
    return JsonResponse(champion_data, json_dumps_params={'ensure_ascii': False})

def ItemBasico_list(request):
    api_rest_url = 'http://localhost:8001/api/itensBasicos/'
    response = requests.get(api_rest_url)
    champions_data = response.json()
    return JsonResponse(champions_data, safe=False, json_dumps_params={'ensure_ascii': False})

def ItemBasico_detail(request, pk):
    api_rest_url = f'http://localhost:8001/api/itensBasicos/{pk}/'
    response = requests.get(api_rest_url)
    champion_data = response.json()
    return JsonResponse(champion_data,json_dumps_params={'ensure_ascii': False})

def ItemReceita_list(request):
    api_rest_url = 'http://localhost:8001/api/itensReceitas/'
    response = requests.get(api_rest_url)
    champions_data = response.json()
    return JsonResponse(champions_data, safe=False, json_dumps_params={'ensure_ascii': False})

def ItemReceita_detail(request, pk):
    api_rest_url = f'http://localhost:8001/api/itensReceitas/{pk}/'
    response = requests.get(api_rest_url)
    champion_data = response.json()
    return JsonResponse(champion_data,json_dumps_params={'ensure_ascii': False})

def ItemCompleto_list(request):
    api_rest_url = 'http://localhost:8001/api/itensCompletos/'
    response = requests.get(api_rest_url)
    champions_data = response.json()
    return JsonResponse(champions_data, safe=False, json_dumps_params={'ensure_ascii': False})

def ItemCompleto_detail(request, pk):
    api_rest_url = f'http://localhost:8001/api/itensCompletos/{pk}/'
    response = requests.get(api_rest_url)
    champion_data = response.json()
    return JsonResponse(champion_data, json_dumps_params={'ensure_ascii': False})

def Melhoria_list(request):
    api_rest_url = 'http://localhost:8001/api/melhorias/'
    response = requests.get(api_rest_url)
    champions_data = response.json()
    return JsonResponse(champions_data, safe=False, json_dumps_params={'ensure_ascii': False})

def Melhoria_detail(request, pk):
    api_rest_url = f'http://localhost:8001/api/melhorias/{pk}/'
    response = requests.get(api_rest_url)
    champion_data = response.json()
    return JsonResponse(champion_data,json_dumps_params={'ensure_ascii': False})