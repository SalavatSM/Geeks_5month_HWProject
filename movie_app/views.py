from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieStarSerializer
from .models import Director, Movie, Review
from rest_framework import generics


@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(instance=directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_item_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movies_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movies_item_api_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movies, many=False).data
    return Response(data=data)


@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def reviews_item_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(reviews, many=False).data
    return Response(data=data)


class MovieReviewListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = ReviewSerializer


@api_view(['GET'])
def movie_star_review(request):
    movies = Movie.objects.all()
    data = MovieStarSerializer(instance=movies, many=True).data
    return Response(data=data)

