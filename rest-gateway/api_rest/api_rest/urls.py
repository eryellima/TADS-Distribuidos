from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import ChampionViewSet, OrigemViewSet, ClasseViewSet, ItemBasicoViewSet, ItemReceitaViewSet, ItemCompletoViewSet, MelhoriaViewSet

#from api.views import TaskViewSet, LivroViewSet

router = routers.DefaultRouter()
router.register(r'champion', ChampionViewSet)
router.register(r'origen', OrigemViewSet)
router.register(r'classe', ClasseViewSet)
router.register(r'itemBasico', ItemBasicoViewSet)
router.register(r'itemReceita', ItemReceitaViewSet)
router.register(r'itemCompleto', ItemCompletoViewSet)
router.register(r'melhoria', MelhoriaViewSet)

#router.register(r'tasks', TaskViewSet)
#router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]