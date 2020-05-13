
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .api import router


urlpatterns = [
    path('', include('cargos.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
