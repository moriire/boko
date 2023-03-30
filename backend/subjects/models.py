import uuid
from django.db import models
from users.models import Users
from django.utils.translation import gettext as _
from django.utils import timezone
from rest_framework.serializers import ModelSerializer

class Subject(models.Model):
    #user = models.ForeignKey(Users, related_name="user+", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

