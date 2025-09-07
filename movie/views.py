from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(request):
    searchTerm = request.GET.get('searchMovie')  # obtiene lo que escribas en el buscador
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)  # filtra por título
    else:
        movies = Movie.objects.all()  # si no se busca nada, lista todas
    return render(request, 'home.html', {
        'searchTerm': searchTerm,
        'movies': movies
    })