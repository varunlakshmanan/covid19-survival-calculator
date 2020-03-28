from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ip/<str:ip>/', views.geolocate, name='geolocate'),
    path('mortality/<str:ip>/', views.get_mortality_rate, name='get_mortality_rate'),
    path('update/', views.update_databases, name='update_databases')
]
