from django.urls import path
from . import views

urlpatterns = [
    path("api/movies/<int:movie_id>/", views.get_movies),
    path("api/tasks/<int:task_id>/", views.get_tasks),
]
