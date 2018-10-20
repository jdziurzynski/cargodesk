from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_loads, name='display'),
    path('newload/', views.new_load, name='newload'),
]
