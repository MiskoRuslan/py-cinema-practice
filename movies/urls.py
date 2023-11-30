from django.urls import path
from .views import MovieListView, MovieDetailView

app_name = "movies"

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]
