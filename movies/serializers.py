from rest_framework import serializers
from .models import Movie, MovieStar, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieStar
        fields = ['star']

class MovieSerializer(serializers.ModelSerializer):
    movie_stars = MovieStarSerializer(many=True, write_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
