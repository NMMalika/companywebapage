from django.db import models

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