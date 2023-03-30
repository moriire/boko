from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _
from django.utils import timezone
from .manager import UserManager
#from django.db.models.signals import post_save
#from django.dispatch import receiver
from rest_framework import serializers
import uuid
import os
ROLES =(
    ("A", "Librarian 1"),
    ("B", "Librarian 2"),
    ("C", "Librarian 3"),
    ("D", "Chief Librarian")
)
class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    full_name = models.CharField(max_length=80)
    email = models.EmailField(_("email address"), unique=True,)
    role = models.CharField(max_length=2, choices=ROLES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["full_name", "role"]
    
    def __str__(self):
        return self.role

from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.email = data.get('email')
        user.role = data.get("role")
        full_name = data.get("full_name")
        user.save()
        return user
    
class CustomLoginSerializer(LoginSerializer):
    username = None #serializers.CharField(required=False, allow_blank=True)
    #email = serializers.EmailField(required=False, allow_blank=True)
    #password = serializers.CharField(style={'input_type': 'password'})

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:   
        model = Users
        fields = ("pk", "email", "full_name", "role")

class CustomRegisterSerializer(RegisterSerializer):
    username = None
    #full_name = None
    #last_name=None
    #qrcode_link = serializers.ImageField(required=False)

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings  

from rest_framework_simplejwt.tokens import RefreshToken
class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField(read_only=True)
    token_class = RefreshToken

    def validate(self, attrs):
        refresh = self.token_class(attrs["refresh"])

        data = {"access": str(refresh.access_token)}
        

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()
            refresh.set_iat()

            data["refresh"] = str(refresh)
            data["pk"] = self.user.pk

        return data


    