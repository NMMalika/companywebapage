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