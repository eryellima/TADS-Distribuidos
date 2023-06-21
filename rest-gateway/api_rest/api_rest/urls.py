from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from api.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    
]
