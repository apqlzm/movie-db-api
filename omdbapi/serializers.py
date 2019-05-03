from rest_framework import serializers

from .models import Movie, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            'id',
            'source',
            'value',
        )


class MovieSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'year',
            'rated',
            'released',
            'runtime',
            'genre',
            'director',
            'writer',
            'actors',
            'plot',
            'language',
            'country',
            'awards',
            'poster',
            'metascore',
            'imdbrating',
            'imdbvotes',
            'imdbid',
            'type_picture',
            'dvd',
            'boxoffice',
            'production',
            'website',
            'totalseasons',
            'ratings'
        )
