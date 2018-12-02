from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.display_loads, name='display'),
    path('newload/', views.new_load, name='newload'),
    path('delete/<pk>', views.delete_load, name='deleteload'),
    path('edit/<pk>', views.edit_load, name='editload'),
    path('history/', views.history, name='history'),
    path('todo/', views.todo_list, name='todo'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
]
