from django.db.models import F
from rest_framework import generics
from rest_framework.response import Response
from .models import Movie, MovieStar
from .serializers import MovieSerializer


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.annotate(rank=F('id')).order_by('rank')[:10]
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)

    def perform_create(self, serializer):
        serializer.save()


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
