from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import book

# Create your views here.


class BookList(generics.ListCreateAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer
