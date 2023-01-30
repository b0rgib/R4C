from django.urls import path
from . import views


urlpatterns = [path('add', views.add, name='add'),
               path('get_excel', views.get_excel, name='get_excel'),
