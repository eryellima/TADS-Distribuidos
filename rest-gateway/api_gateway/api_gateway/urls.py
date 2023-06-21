from django.contrib import admin
from django.urls import include, path
from gateway import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gateway.urls')),
    path('gateway/', views.gateway, name='gateway'),
]
