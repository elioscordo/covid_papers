from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Paper
from .serializers import PaperSerializer


class PaperListView(generics.ListAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'cord_uid': ['exact'],
        'publish_date': ['exact','lte','gte'],
        'publish_time': ['exact'], 
    }
    search_fields = ['title']