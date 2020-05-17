from django.contrib import admin

# Register your models here.
from .models import other_sites_parent_menu,other_sites_menu
admin.site.register(other_sites_parent_menu)
admin.site.register(other_sites_menu)