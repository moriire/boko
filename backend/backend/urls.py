"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from subjects.views import SubjectsView
from books.views import BooksView
from users.views import GetUserView
from django.shortcuts import render
from rest_framework.routers import DefaultRouter

def homepage(request):
    return render(request, "index.html", {})

def others(request, **kw):
    return render(request, "index.html", {})

router = DefaultRouter()
router.register("subject", SubjectsView)
router.register("book", BooksView)
router.register("get-user", GetUserView)

urlpatterns = [
    path('', homepage, name="index"),
    path('<str:f>', others, name="index1"),
    path('v1/api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('v1/api/auth/', include('dj_rest_auth.urls')),
    path('v1/api/auth/signup/', include('dj_rest_auth.registration.urls')),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)