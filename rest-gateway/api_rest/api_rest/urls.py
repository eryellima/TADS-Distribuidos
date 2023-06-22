from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from api.views import TaskViewSet, LivroViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
