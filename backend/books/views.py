from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from users.models import Users
import datetime as dt

from .models import Book, BookSerializer

class BooksView(ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

