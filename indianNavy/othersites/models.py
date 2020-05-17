from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from django.conf import settings

class other_sites_parent_menu(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    menu_name =  models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.menu_name

from django.core.validators import FileExtensionValidator
class other_sites_menu(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
    )
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    menu_name =  models.CharField(max_length=200,unique=True)
    parent = models.ForeignKey(other_sites_parent_menu,null=True, related_name ="othersiteParent_menu" , blank=True, on_delete=models.SET_NULL)
    ###############################late
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)
    #file = models.FileField(upload_to='study_material/notes/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    def __str__(self):
    	return self.menu_name