from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('add-project/',views.add_project, name='add-project'),
]
