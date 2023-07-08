from rest_framework import serializers
from .models import Director, Movie, Review
from django.db.models import Avg


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    # movie_reviews = ReviewSerializer(many=True)
    # director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = 'id title description duration director_name'.split()
        # fields = '__all__'


class MovieStarSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)
    # director = DirectorSerializer()
    stars_avg = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        # fields = 'id title movie_review'.split()
        fields = 'id title description duration director_name movie_reviews stars_avg'.split()

    def get_stars_avg(self, obj):
        return round(obj.movie_reviews.aggregate(avg_rating=Avg("stars"))["avg_rating"], 1)

