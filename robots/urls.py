from django.urls import path
from . import views

urlpatterns = [path('get_excel', views.get_excel, name='get_excel'),
               ]
