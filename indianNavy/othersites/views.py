from django.shortcuts import render, redirect
from django.views.generic import TemplateView , View

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from othersites.models import other_sites_parent_menu, other_sites_menu
from django.views.generic import TemplateView , View
from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from . import serializers
from django.template.loader import get_template
from django.contrib.auth import authenticate,login,logout



class OthersiterApiView(APIView):
	def get_queryset(self):
		return other_sites_menu.objects.all()

	def get(self, request,*args, **kwargs):

		try:
			queryset = other_sites_parent_menu.objects.all()

			#queryset = application_parent_menu.objects.filter(menu_type=1)


			serializer = serializers.ParentotherMenuerializer(queryset,many=True)
			data = serializer.data
		except:
			data = {}
		
		return Response(data)