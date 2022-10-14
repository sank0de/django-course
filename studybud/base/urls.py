from django.urls import path
from . import views # because views file is in the same folder

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
]