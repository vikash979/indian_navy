from rest_framework import serializers

from .models import other_sites_parent_menu,other_sites_menu


class OthersiteMenuobjSerializer(serializers.ModelSerializer):
	#application_submenu = ApplicationSerializer(many=True)
	class Meta:
		model = other_sites_menu
		#fields = ['id','menu_name','parent','parent_ob','menu_type','parent_ob']
		fields = '__all__'



class ParentotherMenuerializer(serializers.ModelSerializer):
	#application_menu = ApplicationMenuobjSerializer(many=True)

	othersiteParent_menu = serializers.SerializerMethodField()
	class Meta:
		model = other_sites_parent_menu
		fields = '__all__'

	def get_othersiteParent_menu(self,obj):
		hh =other_sites_menu.objects.filter(parent_id=obj.id,menu_type=1,parent_ob_id=None).values()
		return OthersiteMenuobjSerializer(hh,many=True).data