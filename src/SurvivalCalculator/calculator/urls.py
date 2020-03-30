from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('update/', views.update, name='update')
]
