from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.display_loads, name='display'),
    path('newload/', views.new_load, name='newload'),
    path('editsave/<pk>', views.edit_save, name='editsave'),
    path('delete/<pk>', views.delete_load, name='deleteload'),
    path('edit/<pk>', views.edit_load, name='editload'),
    path('history/', views.history, name='history'),
    path('todo/', views.todo_list, name='todo'),
    path('newtodo/', views.new_todo, name='newtodo'),
    #path('newtodo/', views.UserToDoList.as_view(), name='newtodoclass'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('todo/delete_todo/<pk>', views.delete_todo, name='deletetodo'),
    path('copy/<pk>', views.copy_load, name='copy'),
    path('todo/delete_from_mydesk/<pk>', views.delete_from_mydesk, name='deletefrommydesk'),
    path('cupboard/<pk>', views.copy_to_cupboard, name='copytocupboard'),
]
