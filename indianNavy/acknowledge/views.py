from django.db import models
from django.conf import settings
from .models import ack_subStandardsmenu, ack_Navyname, ack_subNavy_Orderssmenu, ack_subGuidelinesmenu,ack_Standardsname,  graphDetail,ack_guidelinesname,  ack_subMenuPolicyFile, ack_subNavy_Instructionssmenu,graphDetailUsed,  ack_subpublicationmenu, ack_publicationname, acknoledge_menu,acknowledge_parent_menu,ack_submenu, ack_policyname, ack_policypolicyfile, ack_publicationfile
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
#from users.models import CustomUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from application.views import BasicPagination
from rest_framework.pagination import PageNumberPagination 
from application.views import PaginationHandlerMixin
from django.http import Http404,HttpResponse
from rest_framework import status
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView , View
from django.shortcuts import render, redirect
from users.models import User

pagination_ob = settings.PAGINATION_SIZE


class policyViewobjApi(APIView):
	def get_object(self):
		try:
			return ack_policyname.objects.all()

		except ack_policyname.DoesNotExist:
			return Http404
	def get(self,request,id,sm_id):
		
		policy_name =  ack_policyname.objects.filter(parent_ob_id=id)
		serializer = serializers.AckenowledgePolicynameSerializer(policy_name,many=True)
		return Response(serializer.data)



class policyViewApi(APIView):
	def get_object(self):
		try:
			return ack_policyname.objects.all()

		except ack_policyname.DoesNotExist:
			return Http404

	def sub_child(self,id,lists=None):
		
		policy = ack_publicationname.objects.filter(parent_ob_id__in=id).count()
		
	def get_all_children(self,id,menubar,lists=None):
		
		policy_name =  menubar.objects.filter(id=id ).values()
		
		
		for pli in policy_name:
			if lists is None:
				polilistss=[]
				#print("############",)
				polilistss.append(pli['id'])
			else:
				polilistss= lists
				polilistss.append(pli['id'])
			#policy_names =  menubar.objects.filter(parent_ob_id=pli['id'] ).values()
			policy_data =  menubar.objects.filter(parent_ob_id=pli['id'] ).values('id')
			
			
			for policy_obj in policy_data:
				
				self.get_all_children(policy_obj['id'],menubar,lists=polilistss)


		 		

		
		
		return polilistss
		
	    

	def get(self,request, id,format=None):
		#print("###",request.GET.get('menubar'))
		if request.GET.get('menubar') == 'Publications':
			policy_name =  ack_subpublicationmenu.objects.filter(parent_id=id).values()
			policy_Id = self.get_all_children(id,ack_subpublicationmenu)
			subpolicy = self.sub_child(policy_Id)
			

			#policy_name =  ack_subpublicationmenu.objects.filter(id__in=policy_Id)
			policy_name =  ack_subpublicationmenu.objects.filter(parent_ob_id__in=id)
			
			
			serializer = serializers.AckenowledgepublicationSubmenuSerializer(policy_name,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_publicationname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckenowledgePublicationMenuSerializer(policy_file, many=True)
			data_record['obj']  = data_obj.data
			

		elif request.GET.get('menubar') == 'Navy_Instructions':
			policy_Id = self.get_all_children(id,ack_subNavy_Instructionssmenu)
			
			policy_name =  ack_subNavy_Instructionssmenu.objects.filter(id__in=policy_Id)
			
			serializer = serializers.AckNavyInstmenuSerializer(policy_name,many=True)



		elif request.GET.get('menubar') == 'Guidelines':
			policy_Id = self.get_all_children(id,ack_subGuidelinesmenu)
			#policy_name =  ack_subGuidelinesmenu.objects.filter(id__in=policy_Id) #ack_guidelinesname
			policy_name =  ack_subGuidelinesmenu.objects.filter(parent_ob_id__in=id)
			serializer = serializers.AckenowledgeGuidelinesSubmenuSerializer(policy_name,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_guidelinesname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckguideLineSerializer(policy_file, many=True)
			data_record['obj']  = data_obj.data



		elif request.GET.get('menubar') == 'Navy Orders':
			policy_Id = self.get_all_children(id,ack_subNavy_Orderssmenu)
			#policy_name =  ack_subGuidelinesmenu.objects.filter(id__in=policy_Id) #ack_guidelinesname
			policy_name =  ack_subNavy_Orderssmenu.objects.filter(parent_ob_id__in=id)
			serializer = serializers.Ack_subNavy_OrderssmenuSerializer(policy_name,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_Navyname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckenowledgeNavyOrdersSerializer(policy_file, many=True)
			data_record['obj']  = data_obj.data

			
		elif request.GET.get('menubar') == 'Standards':
			policy_Id = self.get_all_children(id,ack_subStandardsmenu)
			#policy_name =  ack_subStandardsmenu.objects.filter(id__in=policy_Id)
			policy_name =  ack_subStandardsmenu.objects.filter(parent_ob_id__in=id)
			serializer = serializers.AckenowledgeStandardsSerializer(policy_name,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_Standardsname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckStandardSerializer(policy_file, many=True)
			data_record['obj']  = data_obj.data
			
		else:

			
			policy_name =  ack_submenu.objects.filter(id=id ).values()# | ack_submenu.objects.filter(parent_ob_id=id ).values()
			policy =[]

			policyId =  self.get_all_children(id,ack_submenu)
			
			policy_name =  ack_submenu.objects.filter(id__in=policyId )
			policy_file = ack_subMenuPolicyFile.objects.filter(parent_ob_id=id)
			#print("::::::::::::::",policy_file.values())


			
			serializer = serializers.AckenowledgeSubmenuSerializer(policy_name,many=True)
			data_record = {"policy": serializer.data}
			data_obj = serializers.ack_subMenuPolicyFileSubmenuSerializer(policy_file, many=True)
			
			data_record['obj']  = data_obj.data
			#print("@@@@@@@@@@@@@@@@@@@@:::::::::::::::",data_record)
			
			
		return Response(data_record)

class policynewViewApi(APIView):
	def get(self,request,id,sm_id):
		
		policy_name =  ack_policyname.objects.filter(parent_ob_id=id,folder_type=2)
		
		serializer =serializers.AckenowledgePolicynameSerializer(policy_name,many=True)


		return Response(serializer.data)



class AcknowledgeAPI(APIView):
 	def get_object(self):
 		try:

 			return acknoledge_menu.objects.all()
 		except acknoledge_menu.DoesNotExist:
 			return Http404

 	def get(self, request,  format=None):
 		ack_menu = self.get_object()
 		serializer = serializers.AckenowledgeSerializer(ack_menu,many=True)
 		return Response(serializer.data)


class AxknowledgePublicAPI(APIView):
	def get_object(self):
		try:
			return ack_subpublicationmenu.objects.all()

		except ack_subpublicationmenu.DoesNotExist:
			return Http404
	def get(self, request,  format=None):
		ack_menu = self.get_object()
		serializer = serializers.AckenowledgepublicationSubmenuSerializer(ack_menu,many=True)
		return Response(serializer.data)


class AckpolicyAPI(APIView):
	def get(self,request, id):
		
		if request.GET.get('menubar') == 'Policy Letters':

			submenu = ack_submenu.objects.filter(parent_ob_id=id,folder_type=2).values()
			
			serializer = serializers.AckenowledgeSubmenuSerializer(submenu,many=True)
		elif request.GET.get('menubar') == 'Navy_Instructions':
			
			submenu = ack_subNavy_Instructionssmenu.objects.filter(parent_ob_id=id,folder_type=2)
			serializer = serializers.AckNavyInstmenuSerializer(submenu,many=True)
		elif request.GET.get('menubar') == 'Guidelines':
			
			submenu = ack_subGuidelinesmenu.objects.filter(parent_ob_id=id,folder_type=2)
			serializer = serializers.AckenowledgeGuidelinesSubmenuSerializer(submenu,many=True)

		elif request.GET.get('menubar') == 'Standards':
			submenu = ack_subStandardsmenu.objects.filter(parent_ob_id=id,folder_type=2)
			serializer = serializers.AckenowledgeStandardsSerializer(submenu,many=True)
			
		elif request.GET.get('menubar') == 'Navy Orders':
			submenu = ack_subNavy_Orderssmenu.objects.filter(parent_ob_id=id,folder_type=2)
			serializer = serializers.Ack_subNavy_OrderssmenuSerializer(submenu,many=True)

		else:
			submenu = ack_subpublicationmenu.objects.filter(parent_ob_id=id)
			serializer = serializers.AckenowledgepublicationSubmenuSerializer(submenu,many=True)

		#print(":::::::::",serializer.data)
		return Response(serializer.data)


# class AckpolicypubAPI(APIView):

# 	def get(self,request)







class acknowledgeViews(TemplateView):
	template_name = "acknowledge/policy.html"
	def get(self, request, id=None):

		context_data = {}
		policy_obj = ack_policypolicyfile.objects.all().values().order_by("-id")
		paginator = Paginator(policy_obj,pagination_ob)
		if request.GET.get('page')==None:
			page =1
		else:
			page = int(request.GET.get('page'))
		try:
			users = paginator.page(page)
		except PageNotAnInteger :
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)

		
		context_data['policy'] = users
		program_numpages = paginator.num_pages
		program_numpages = program_numpages+1
		context_data['PAGINATION_COUNT'] = range(1,program_numpages)
		

		return render(request, self.template_name, context_data)




class acknowledgeViews(TemplateView):
	template_name = "acknowledge/policy.html"

	def get_all_child(self, menubar,menutype,mainfile,lists=None):
		policy_name =  menubar.objects.filter(parent_ob_id=None).values('id')
		#print(menutype,"!!!!!!!!!!!!!", policy_name)
		policylist = []
		for pli in policy_name:
			
			policy_data =  mainfile.objects.filter(parent_ob_id=pli['id'] ).values()
			
			for obj in policy_data:
				policylist.append(obj)
		return policylist



		
	def get(self, request, id=None):
		
		context_data = {}
		#print("@@@",id)
		#policy_data = ack_submenu.objects.all()
		menu_id = graphDetail.objects.get(menu_detail=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id).id
		
		graph_obj = graphDetailUsed.objects.create(menu_detail_id=menu_id, menu_user=User.objects.get(username=request.user.username))

		#graphuser = graphDetailUsed.objects.create(menu_detail_id=menu_id, menu_user=User.objects.get(username=request.user.username))
		if request.GET.get('menutype') =='Policy Letters' :
			
			policy_data = ack_submenu.objects.filter(parent_ob_id=None, parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
			
			
			

			policy_obj = ack_submenu.objects.filter(parent_ob_id=None)
			policy_Id = self.get_all_child(ack_submenu,request.GET.get('menutype'),ack_subMenuPolicyFile)
			#context_data['idd'] = int(request.GET.get('array'))
			
		elif request.GET.get('menutype') =='Publications' :
			policy_data = ack_subpublicationmenu.objects.filter(parent_ob_id=None,parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
			#menuobj= request.GET.get('array').split(",")

			policy_obj = ack_subpublicationmenu.objects.all().order_by("-id")
			policy_Id = self.get_all_child(ack_subpublicationmenu,request.GET.get('menutype'),ack_publicationname)
		elif request.GET.get('menutype') =='Guidelines' :
			policy_data = ack_subGuidelinesmenu.objects.filter(parent_ob_id=None,parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
			#menuobj= request.GET.get('array').split(",")

			policy_obj = ack_subGuidelinesmenu.objects.all().order_by("-id")
			policy_Id = self.get_all_child(ack_subGuidelinesmenu,request.GET.get('menutype'),ack_guidelinesname)

		elif request.GET.get('menutype') =='Standards' :
			policy_data = ack_subStandardsmenu.objects.filter(parent_ob_id=None,parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
			policy_obj = ack_subStandardsmenu.objects.all().order_by("-id")

			policy_Id = self.get_all_child(ack_subStandardsmenu,request.GET.get('menutype'),ack_Standardsname)


		elif request.GET.get('menutype') =='Navy_Instructions' :
			policy_data = ack_subNavy_Instructionssmenu.objects.filter(parent_ob_id=None,parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
			policy_obj = ack_subNavy_Instructionssmenu.objects.all().order_by("-id")

			policy_Id = self.get_all_child(ack_subNavy_Instructionssmenu,request.GET.get('menutype'),ack_Standardsname)

		elif request.GET.get('menutype') =='Navy Orders' :
			policy_data = ack_subNavy_Orderssmenu.objects.filter(parent_ob_id=None,parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
			policy_obj = ack_subNavy_Orderssmenu.objects.all().order_by("-id")

			policy_Id = self.get_all_child(ack_subNavy_Orderssmenu,request.GET.get('menutype'),ack_Navyname)

		else:
			policy_obj = ack_policyname.objects.all().values().order_by("-id")
		# pagination_ob = 5

		paginator = Paginator(policy_obj,pagination_ob)
		if request.GET.get('page')==None:
			page = 1
		else:
			page = int(request.GET.get('page'))	
		
			

		try:
			users = paginator.page(page)
		except PageNotAnInteger :
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)

		
		context_data['policy'] = users
		program_numpages = paginator.num_pages
		program_numpages = program_numpages+1
		context_data['PAGINATION_COUNT'] = range(1,program_numpages)
		context_data['sub_menu'] = policy_data
		context_data['menu_bar'] = request.GET.get('menutype')
		

		return render(request, self.template_name, context_data)




class policyViews(TemplateView):
	def get(self, request, drink_name,string_name):
		template_name = string_name
		context_data = {}
		return render(request, template_name, context_data)


class ack_menudetail(TemplateView):
	template_name = "acknowledge/publication_menu.html"
	def get(self, request, id=None):
		context_data = {}
		ack_menu = acknoledge_menu.objects.all().values()
		menu_obj = []
		menu_count = []
		for menu in ack_menu:
			
			menu_obj.append(menu['menu_name'])
			manu_cnt = ack_submenu.objects.filter(parent_id=menu['id']).count()
			menu_count.append(manu_cnt)
		
		context_data['data'] = menu_obj
		context_data['labels'] = menu_count


		
		return render(request, self.template_name, context_data)




class acknowledgepublicationViews(TemplateView):
	template_name = "acknowledge/publication.html"
	def get(self, request, id=None):
		context_data = {}
		policy_obj = ack_publicationfile.objects.all().values().order_by("-id")
		paginator = Paginator(policy_obj,pagination_ob)
		if request.GET.get('page')==None:
			page =1
		else:
			page = int(request.GET.get('page'))
		try:
			users = paginator.page(page)
		except PageNotAnInteger :
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)

		
		context_data['policy'] = users
		program_numpages = paginator.num_pages
		program_numpages = program_numpages+1
		context_data['PAGINATION_COUNT'] = range(1,program_numpages)
		

		return render(request, self.template_name, context_data)




from .models import City

def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')[:5]

    for city in queryset:
        labels.append(city.name)
        data.append(city.population)
    print(":::::::::::::::::::::",labels)

    return render(request, 'acknowledge/pie_chart.html', {
        'labels': labels,
        'data': data,
    })


from django.http import JsonResponse

def send_json(request):
	ack_menu = acknoledge_menu.objects.all().values()
	ack_menus = ack_submenu.objects.filter(parent_id=1).count()
	ack_publication = ack_submenu.objects.filter(parent_id=2).count()
	ack_guidleines = ack_submenu.objects.filter(parent_id=3).count()
	menu_objs = []
	menu_objt = {}
	menn = []
	menncount = {}
	count = []
	guidline = []
	guidline_count = []

	for menu_name in ack_menu:
		guidline.append(menu_name['menu_name'])
		ack_menuscount = ack_submenu.objects.filter(parent_id=menu_name['id']).count()
		guidline_count.append(ack_menuscount)

		# if menu_name['menu_name'] == 'Policy':
		# 	menu_obj = {"policy":menu_name['menu_name'],'count':ack_menus}
		# 	menu_objs.append(menu_obj)
		# 	menn.append(menu_name['menu_name'])
		# 	count.append(ack_menus)
			
		# if menu_name['menu_name'] == 'Publication':
		# 	menu_obj = {"publication":menu_name['menu_name'],'count':ack_publication}
		# 	menu_objs.append(menu_obj)
		# 	menn.append(menu_name['menu_name'])
		# 	count.append(ack_publication)
		# if menu_name['menu_name'] == 'GuideLines':
		# 	menu_obj = {"publication":menu_name['menu_name'],'count':ack_guidleines}
		# 	menn.append(menu_name['menu_name'])
		# 	count.append(ack_guidleines)
	menncount['data'] = guidline
	menncount['count'] = guidline_count
	#print(menu_objs)
	

	data = menncount
	return JsonResponse(data,safe=False)


	
    




