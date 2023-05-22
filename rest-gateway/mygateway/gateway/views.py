from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse

def get_movies(request, movie_id):
    response = requests.get(f"http://localhost:8000/api/movies/{movie_id}/")
    return JsonResponse(response.json())

def get_tasks(request, task_id):
    response = requests.get(f"http://localhost:8000/api/tasks/{task_id}/")
    return JsonResponse(response.json())
