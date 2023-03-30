import uuid
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from users.models import Users
from subjects.models import Subject

class Book(models.Model):
    subject = models.ForeignKey(Subject, related_name="subject+", on_delete=models.CASCADE)
    title = models.CharField(_("Book Title"), max_length=80, unique=True)
    copies = models.IntegerField(default=1)
    shelved_on = models.DateTimeField(default=timezone.now)
    shelved_by = models.ForeignKey(Users, related_name="subject_shelved_by", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"