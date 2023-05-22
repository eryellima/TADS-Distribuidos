from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import TaskViewSet
from movies.views import MovieList


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'movies', MovieList, basename='movie')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
