from django.contrib import admin
from app.models import GeneralInfo,Service

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name','location','email','phone','video_url','facebook','twitter','linkedin','instagram']

    def __str__(self):  
        return self.company_name    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['icon','title','description']
    search_fields = ['title','description']
    
def __str__(self):
        return self.title
