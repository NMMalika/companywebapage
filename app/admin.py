from django.contrib import admin
from app.models import GeneralInfo,Service

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name','location','email','phone','video_url','facebook','twitter','linkedin','instagram']
# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['icon','title','description']
    search_fields = ['title','description']
    

