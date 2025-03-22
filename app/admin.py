from django.contrib import admin
from app.models import GeneralInfo,Service,Testimonial,FAQs,ContactFormLog,Blog,Author

admin.site.site_header = 'Nimcity Enterprises Admin'
admin.site.site_title = 'Nimcity Enterprises Admin'
admin.site.index_title = 'Nimcity Enterprises Admin Dashboard'


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
    
@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','is_success','is_error','action_time']
    search_fields = ['name','email','subject','message']
    
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','email','phone','joined_date']
    search_fields = ['first_name','email','phone']
    list_filter = ['joined_date']
    date_hierarchy = 'joined_date'
    list_per_page = 5
    list_max_show_all = 10
    list_editable = ['email','phone']
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_image','title','category','author','content','created_at']
    search_fields = ['title','category','author','content']
    list_filter = ['category','author','created_at']
    date_hierarchy = 'created_at'
    list_per_page = 5
    list_max_show_all = 10
    list_editable = ['category','author']
    

        