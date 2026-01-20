from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_games, name='list_games'),
    path('<int:pk>/', views.detail_game, name='detail_game'),

]