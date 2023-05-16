from django.core.checks import messages
from django.urls import path
from . import views
app_name = 'green'
urlpatterns = [
    path('', views.start, name="Initialize"),
    path('Jog/', views.home, name="Jog"),
    path('Spindle/', views.home1, name="Spindle"),
    path('Maintenance/', views.home6, name="Maintenance"),
    path('Tool/', views.home7, name="Tool"),
    
]


