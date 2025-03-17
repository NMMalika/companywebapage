import os
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from app.models import GeneralInfo,Service,Testimonial,FAQs
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages


# Create your views here.
def index(request):
     general_info = GeneralInfo.objects.first()
     
     services=Service.objects.all()
     
     testimonials=Testimonial.objects.all()
     
     faqs=FAQs.objects.all()
    
     context={
          "company_name":general_info.company_name,
          "location":general_info.location,
          "email":general_info.email,
          "phone":general_info.phone,
          "video_url":general_info.video_url,
          "facebook":general_info.facebook,
          "twitter":general_info.twitter,
          "linkedin":general_info.linkedin,
          "instagram":general_info.instagram,
         
         
           "services":services,
           "testimonials":testimonials,
           "faqs":faqs,
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
     try:  
          send_mail(
               subject=subject,
               message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
               html_message=html_content,
              #from_email=settings.EMAIL_HOST_USER,
               recipient_list=[settings.EMAIL_HOST_USER],
               fail_silently=False,
         )
     except Exception as e:
          messages.error(request, "An error occurred while sending the email")  
          return redirect("home")
     else:
          messages.success(request, "Email sent successfully")
     return redirect("home")


