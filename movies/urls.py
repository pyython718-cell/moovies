from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/top/', views.top_movies),
    path('movies/<int:pk>/', views.movie_detail),
]
