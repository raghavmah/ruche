from django.db import models
import os 
from django.utils.safestring import mark_safe
# Create your models here.

PROJECT_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  
class Products(models.Model):
    name= models.CharField( max_length=64, unique=True,verbose_name="Enter the Categories Name")
    class  Meta:  #new
        verbose_name_plural  =  "PRODUCTS NAME" 
    def __str__(self):
        return f" {self.name}"

class Home(models.Model):
    pagetitle=models.CharField(max_length=60,verbose_name="Enter the Page Sub Heading")
    pagetext =models.CharField( max_length=1000,verbose_name="Enter Page  Description")
    class  Meta:  #new
        verbose_name_plural  =  "HOME PAGE TITLE AND DESCRIPTION" 
    def __str__(self):
        return f"PAGE TITLE:{self.pagetitle} AND PAGE TEXT:{self.pagetext}"

class AboutUs(models.Model):
    pagetitle=models.CharField(max_length=60,verbose_name="Enter the Page Sub Heading")
    pagetext =models.CharField( max_length=1000,verbose_name="Enter Page  Description")
    class  Meta:  #new
        verbose_name_plural  =  "ABOUT-US PAGE TITLE AND DESCRIPTION"   
    def __str__(self):
        return f"PAGE TITLE:{self.pagetitle} "
            

class contact(models.Model):
    pagetitle=models.CharField(max_length=60,verbose_name="Enter the Page Sub Heading")
    pagetext = models.CharField(max_length =1000, verbose_name="Enter Page  Description")
    class  Meta:  #new
        verbose_name_plural  =  "CONTACT PAGE TITLE AND DESCRIPTION" 
    def __str__(self):
        return f"PAGE TITLE:{self.pagetitle} "

class carousels(models.Model):
    Image = models.ImageField(upload_to=os.path.join(PROJECT_DIR, "frontend/img"), null = True,verbose_name="Enter The Image for carousel")
    Img_title = models.CharField(max_length=30, null=True,verbose_name="Enter The image title")
    Img_desc = models.CharField(max_length=500, null=True,verbose_name="Enter The image description",blank=True)
    class  Meta:  #new
        verbose_name_plural  =  "CAROUSELS IMAGES" 
    def __str__(self):
        return f"IMAGE : {self.Image}   TITLE:{self.Img_title} "
    def car_preview(self): #new
        return mark_safe(f'<img src = "{self.Image.url}" width = "100"/>')

class headers(models.Model):
    title_img=models.ImageField(upload_to=os.path.join(PROJECT_DIR, "frontend/img"),verbose_name="Enter The TITLE IMAGE")
    logo=models.ImageField(upload_to=os.path.join(PROJECT_DIR, "frontend/img"),verbose_name="Enter The Logo")
    email=models.EmailField(max_length=256,verbose_name="Enter The Email id",null=True,blank=True)
    insta=models.URLField(max_length=500,verbose_name="Enter The Instagram  Profile URl",null=True,blank=True)
    facebook=models.URLField(max_length=500,verbose_name="Enter The FaceBook Profile URl",null=True,blank=True)
    twitter=models.URLField(max_length=500,verbose_name="Enter The twitter  Profile URl",null=True,blank=True)
    class  Meta:  #new
        verbose_name_plural  =  "LOGO IMAGE AND SOCIAL MEDIA LINKS" 
    
    def __str__(self):
        return f" email: {self.email}; instagram : {self.insta}; facebook :{self.facebook}; twitter:{self.twitter}"
    
    def logo_preview(self): #new
        return mark_safe(f'<img src = "{self.logo.url}" width = "100"/>')
    def title_preview(self): #new
        return mark_safe(f'<img src = "{self.title_img.url}" width = "50"/>')


class Images(models.Model):
    title=models.CharField(max_length=30, null=True,verbose_name="Enter The image title")
    desp =models.CharField( max_length=250,verbose_name="Enter Image Description")
    image=models.ImageField(upload_to=os.path.join(PROJECT_DIR, "frontend/img"))
    des = models.ForeignKey(Products,on_delete=models.CASCADE )
    class  Meta:  #new
        verbose_name_plural  =  "PRODUCTS IMAGES" 
    
    def __str__(self):
        return f"IMAGE : {self.image} TITLE:{self.title} DESCRIPTION:{self.desp}  PRODUCT NAME:{self.des}"
    
    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')