from rest_framework import serializers
from .models import ack_NavyInstructionname, ack_Navyname,graphDetail, ack_publicationname,   ack_Standardsname,graphDetailUsed,  ack_guidelinesname , BRsmenu, ack_subGuidelinesmenu, ack_subpublicationmenu,acknoledge_menu,acknowledge_parent_menu,ack_submenu,ack_policyname,ack_policypolicyfile, ack_subStandardsmenu, ack_subNavy_Orderssmenu, ack_subNavy_Instructionssmenu ,ack_subNHQe_Librarylinesmenu, ack_subMenuPolicyFile




class AckenowledgepolicypolicyfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = ack_policypolicyfile
		fields = '__all__'

class AckenowledgePolicynameSerializer(serializers.ModelSerializer):
	ask_policyfile = AckenowledgepolicypolicyfileSerializer(many=True)
	class Meta:
		model = ack_policyname
		fields = '__all__'



class AckenowledgeNavyOrdersSerializer(serializers.ModelSerializer):
	class Meta:
		model = ack_Navyname
		fields = '__all__'



		

		

class AckguideLineSerializer(serializers.ModelSerializer):
	class Meta:
		model = ack_guidelinesname
		fields = '__all__'


class AckStandardSerializer(serializers.ModelSerializer):
	class Meta:
		model = ack_Standardsname
		fields = '__all__'
		


class ack_subMenuPolicyFileSubmenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = ack_subMenuPolicyFile
		fields = '__all__'

class AckenowledgeSubmenuSerializer(serializers.ModelSerializer):
	#ack_submenu_children = ack_subMenuPolicyFileSubmenuSerializer(many=True)
	class Meta:
		model= ack_submenu
		fields= '__all__'

class AckenowledgepublicationSubmenuSerializer(serializers.ModelSerializer):


	class Meta:
		model= ack_subpublicationmenu
		fields= '__all__'


class AckenowledgePublicationMenuSerializer(serializers.ModelSerializer):

	class Meta:
		model = ack_publicationname
		fields = '__all__'


class AckenowledgeGuidelinesSubmenuSerializer(serializers.ModelSerializer):
	#guidelines_name = AckguideLineSerializer(many=True)
	class Meta:
		model= ack_subGuidelinesmenu
		fields= '__all__'

class AckenowledgeStandardsSerializer(serializers.ModelSerializer):
	#standards_name = AckStandardSerializer(many=True)
	class Meta:
		model= ack_subStandardsmenu
		fields= '__all__'


class Ack_subNavy_OrderssmenuSerializer(serializers.ModelSerializer):
	navyOrders_name = AckenowledgeNavyOrdersSerializer(many=True)
	class Meta:
		model= ack_subNavy_Orderssmenu
		fields= '__all__'


class AckenowledgeNavyInstructionSerializer(serializers.ModelSerializer):
	class Meta:
		model = ack_NavyInstructionname
		fields = '__all__'

class AckNavyInstmenuSerializer(serializers.ModelSerializer):
	#navyinstruction_name = AckenowledgeNavyInstructionSerializer(many=True)
	class Meta:
		model= ack_subNavy_Instructionssmenu
		fields= '__all__'



class AckLibrarySerializer(serializers.ModelSerializer):
	class Meta:
		model= ack_subNHQe_Librarylinesmenu
		fields= '__all__'


class BRsmenuSerializer(serializers.ModelSerializer):
	class Meta:
		model= BRsmenu
		fields= '__all__'


class publicationMenuSerializer(serializers.ModelSerializer):
	class Meta:
		models = ack_publicationname
		fields = '__all__'


class graphDetailUsedSerializer(serializers.ModelSerializer):
	class Meta:
		model = graphDetailUsed
		fields = ['menu_detail']

class graphDetailUserSerializer(serializers.ModelSerializer):
	graph_detail = graphDetailUsedSerializer(many=True)
	

	class Meta:
		model = graphDetail
		fields = ['menu_detail','graph_detail']


class  AckenowledgeSerializer(serializers.ModelSerializer):
	#ask_subpublicationmenues = AckenowledgePublicationSerializer(many=True)
	ask_submenues = AckenowledgeSubmenuSerializer(many=True)
	ascsubmenu_count = serializers.SerializerMethodField()
	ask_subpublicationmenues = AckenowledgepublicationSubmenuSerializer(many=True)
	ascpublicationsubmenu_count = serializers.SerializerMethodField()
	ask_subguidelinesmenues = AckenowledgeGuidelinesSubmenuSerializer(many=True)
	ascguideleinessubmenu_count = serializers.SerializerMethodField()
	standards = serializers.SerializerMethodField()
	ask_substandardsmenues = AckenowledgeStandardsSerializer(many=True)
	ask_subnavy_ordersmenues = Ack_subNavy_OrderssmenuSerializer(many=True)
	navy_ordersCount = serializers.SerializerMethodField()
	navy_ordersCountall = serializers.SerializerMethodField()
	ask_subnavy_instructionmenues = AckNavyInstmenuSerializer(many=True)
	navyInstrctionCount = serializers.SerializerMethodField()
	navyInstrctionCountall = serializers.SerializerMethodField()
	ask_subnohqsmenues = AckLibrarySerializer(many=True)
	ask_libCount = serializers.SerializerMethodField()
	brsmenues = BRsmenuSerializer(many=True)
	brsCount = serializers.SerializerMethodField()

	ask_submenudetail = graphDetailUserSerializer(many=True)


	class Meta:
		model = acknoledge_menu
		fields = '__all__'

	def get_ascsubmenu_count(self,obj):
		
		#submenu = ack_submenu.objects.filter(parent_id=obj.id).order_by("-id")[:4]
		submenu  = ack_submenu.objects.all().order_by("-id")[:4]
		#return AckenowledgeSubmenuSerializer(submenu,many=True).data
		return AckenowledgeSubmenuSerializer(submenu,many=True).data

	def get_ascpublicationsubmenu_count(self,obj):
		#submenu = ack_subpublicationmenu.objects.filter(parent_id=obj.id).values().order_by("-id")[:4]
		submenu =  ack_subpublicationmenu.objects.all().order_by("-id")[:4]
		#return AckenowledgepublicationSubmenuSerializer(submenu,many=True).data
		return AckenowledgepublicationSubmenuSerializer(submenu,many=True).data

	def get_ascguideleinessubmenu_count(self,obj):
		submenu = ack_subGuidelinesmenu.objects.all().order_by("-id")[:4]
		guidelines= {'data':AckenowledgeGuidelinesSubmenuSerializer(submenu,many=True).data}
		guidelines['menu'] = ack_subGuidelinesmenu.objects.all().count()
		return guidelines

	def get_standards(self,obj):
		submenu = ack_subStandardsmenu.objects.all().order_by("-id")[:4]
		standard = {'data':AckenowledgeStandardsSerializer(submenu,many=True).data}
		standard['menu'] = ack_subStandardsmenu.objects.all().count()
		
		return standard

	def get_navy_ordersCount(self,obj):
		submenu = ack_subNavy_Orderssmenu.objects.all().order_by("-id")[:4]
		return Ack_subNavy_OrderssmenuSerializer(submenu,many=True).data

	def get_navy_ordersCountall(self,obj):
		submenu = ack_Navyname.objects.all()
		return AckenowledgeNavyOrdersSerializer(submenu,many=True).data

	def get_navyInstrctionCount(self,obj):
		submenu = ack_subNavy_Instructionssmenu.objects.all().order_by("-id")[:4]
		navy_instruction = {'data':AckNavyInstmenuSerializer(submenu,many=True).data}
		navy_instruction['menu'] = ack_subNavy_Instructionssmenu.objects.all().count()
		return navy_instruction


	def get_navyInstrctionCountall(self,obj):
		submenu = ack_NavyInstructionname.objects.all()
		return AckenowledgeNavyInstructionSerializer(submenu,many=True).data

	def get_ask_libCount(self,obj):
		submenu = ack_subNHQe_Librarylinesmenu.objects.filter(parent_id=obj.id).values().order_by("-id")[:4]
		return AckLibrarySerializer(submenu,many=True).data

	def get_brsCount(self,obj):
		submenu = BRsmenu.objects.all().order_by("-id")[:4]
		return BRsmenuSerializer(submenu,many=True).data






