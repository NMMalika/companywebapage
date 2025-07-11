import os
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from app.models import GeneralInfo,Service,Testimonial,FAQs,ContactFormLog,Blog,Author
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.
def index(request):
     general_info = GeneralInfo.objects.first()
     
     services=Service.objects.all()
     
     testimonials=Testimonial.objects.all()
     
     faqs=FAQs.objects.all()
     
     recent_blogs=Blog.objects.all().order_by('-created_at')[:3]
     
     default_value = ""
    
     context={
          "company_name":getattr(general_info, "company_name", ""),
          "location":getattr (general_info,"location", ""),
          "email":getattr(general_info,"email", ""),
          "phone":getattr(general_info,"phone", ""),
          "video_url":getattr(general_info,"video_url", ""),
          "facebook":getattr(general_info,"facebook", ""),
          "twitter":getattr(general_info,"twitter", ""),
          "linkedin":getattr(general_info,"linkedin", ""),
          "instagram":getattr(general_info,"instagram", ""),
        
         
           "services":services,
           "testimonials":testimonials,
           "faqs":faqs,
           "recent_blogs":recent_blogs,
     }
     
     return render(request, "index.html", context)

def contact_form(request):
     
     if request.method =="POST":
        print ("\nuser has submitted the form\n")
        print (f"request.POST: {request.POST}")
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        
        
        
        context={
          "name":name,
          "email":email,
          "subject":subject,
          "message":message,
        }
        html_content= render_to_string ("email.html", context)
        
        is_success=False
        is_error=False
        error_message=""
     try:  
          send_mail(
               subject=subject,
               message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
               html_message=html_content,
              from_email=settings.EMAIL_HOST_USER,
               recipient_list=[settings.EMAIL_HOST_USER],
               fail_silently=False,
         )
     except Exception as e:
          is_error=True
          error_message=str(e)
          messages.error(request, "An error occurred while sending the email")  
          return redirect("home")
     else:
          is_success=True
          messages.success(request, "Emairecent_blogs:Blog.objects.all().order_by('-created_at')[:2]l has been sent successfully")
          ContactFormLog.objects.create(name=name,email=email,subject=subject,message=message,is_success=is_success,is_error=is_error,error_message=error_message,action_time=timezone.now())
     return redirect("home")

def blog_detail(request,blog_id):
     blog=Blog.objects.get(id=blog_id)
     
     recent_blogs=Blog.objects.all().exclude(id=blog_id).order_by('-created_at')[:3]
     
     context={
          "blog":blog,
          "recent_blogs":recent_blogs,
          
     }
     return render(request, "blog_detail.html", context)
def blogs(request):
    all_blogs = Blog.objects.all().order_by('-created_at')  # Fetch all blogs

    paginator = Paginator(all_blogs, 3)  
    page = request.GET.get("page")  
    try:
        blogs = paginator.page(page)  # Get the blogs for the requested page
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

    context = {
        "blogs": blogs,  # Use the paginated blogs
    }
    return render(request, "blogs.html", context)