from django.shortcuts import render
from app.models import GeneralInfo

# Create your views here.
def index(request):
     general_info = GeneralInfo.objects.first()
     print(f"general_info: {general_info.location}")
     
     
     context={
          "company_name":general_info.company_name,
          "location":general_info.location,
          "email":general_info.email,
          "phone":general_info.phone,
          "video_url":general_info.video_url,
          "facebook":general_info.facebook,
          "twitter":general_info.twitter,
          "linkedin":general_info.linkedin,
          "instagram":general_info.instagram
         
     }
     print(f"context: {context}")
     return render(request, "index.html", context)
