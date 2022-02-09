from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('add-project/',views.add_project, name='add-project'),
    path('delete-project/<int:pk>',views.delete_project, name='delete-project'),
    path('read-project/<int:pk>',views.read_project, name='read-project'),
    path('update-project/<int:pk>',views.update_project, name='update-project'),
]
