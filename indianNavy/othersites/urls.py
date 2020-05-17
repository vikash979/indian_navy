from django.urls import re_path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from othersites import views
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()

urlpatterns = [
	re_path(r'^menu_details/$', views.OthersiterApiView.as_view(), name="menu_details"),
]