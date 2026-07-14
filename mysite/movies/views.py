from django.shortcuts import render
from rest_framework import viewsets
from.serializers import MovieSerializer
from .models import MovieData
from django.views.generic import TemplateView
from rest_framework import filters


# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "typ","rating","duration"]
    
class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comedy')
    serializer_class = MovieSerializer


class HomeView(TemplateView):
    template_name = "movies/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = MovieData.objects.all()
        return context
        