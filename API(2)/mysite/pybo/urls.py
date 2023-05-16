
from django.urls import path
from django.template import *
from . import views

app_name = 'green'

urlpatterns = [
    path('', views.start, name='start'),
    path('main/', views.main, name='main'),
    path('page1/', views.farm_nm1, name='farm_nm1'),
    path('page2/', views.farm_nm2, name='farm_nm2'),
    path('page2_1/', views.back, name='back'),
   
    
]