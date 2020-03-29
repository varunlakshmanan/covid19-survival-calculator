from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('update/', views.update_databases, name='update_databases')
]
