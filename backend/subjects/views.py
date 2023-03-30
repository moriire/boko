from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from users.models import Users

from .models import Subject, SubjectSerializer
class SubjectsView(ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer