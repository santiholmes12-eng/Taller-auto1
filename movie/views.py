from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.

def home(request): 
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title_icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})
   #return HttpResponse ('<h1>Welcome to home page<h1>')
  #return render(request,'home.html')
 #return render(request,'home.html',{'name':'Santiago Holguin'})
movies = Movie.objects.all()

def about(request):
    # Pasar Datos.
    return HttpResponse('<h1>Welcolme to about page</h1>')
