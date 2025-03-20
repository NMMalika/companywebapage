from django.db import models
from django.utils import timezone
# Create your models here.
class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=100 , default='Nimcity Enterprises')
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    video_url = models.URLField(blank=True,null=True)
    facebook = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    

    def __str__(self):
        return self.company_name
    
class Service(models.Model):
    icon=models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50,unique=True)
    description= models.TextField()
    
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    user_image=models.CharField(max_length=100, blank=True, null=True)
    stars_counts=(
        (1,'1 Star'),
        (2,'2 Star'),
        (3,'3 Star'),
        (4,'4 Star'),
        (5,'5 Star'),
    )
    rating=models.IntegerField(choices=stars_counts)
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    review=models.TextField()
    
    def __str__(self):
        return f'{self.name} - {self.designation}'
class FAQs(models.Model):
    question=models.CharField(max_length=100)
    answer=models.TextField()
    
    def __str__(self):
        return self.question
    
class ContactFormLog(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    action_time=models.DateTimeField(auto_now_add=True)
    is_success=models.BooleanField(default=False)
    is_error=models.BooleanField(default=False)
    error_message=models.TextField(blank=True,null=True)
  
    def __str__(self):
        return self.email
class Blog(models.Model):
    blog_image=models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    facebook = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    joined_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name