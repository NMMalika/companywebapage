from django.contrib import admin
from app.models import GeneralInfo,Service,Testimonial,FAQs

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name','location','email','phone','video_url','facebook','twitter','linkedin','instagram']

     

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['icon','title','description']
    search_fields = ['title','description']
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['user_image','display_rating','name','designation','review']
    search_fields = ['name','designation','review']
    
    def display_rating(self,obj):
        return "*" *obj.rating
    display_rating.short_description = 'Rating'
    
@admin.register(FAQs)
class FAQsAdmin(admin.ModelAdmin):
    list_display = ['question','answer']
    search_fields = ['question','answer']