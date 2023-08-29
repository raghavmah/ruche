from django.contrib import admin

# Register your models here.
from .models import Home,AboutUs,contact,carousels,headers ,Images,Products
from  django.contrib.auth.models  import  Group
admin.site.site_header  =  "RAGHAV SITE DASHBOARD"  
admin.site.site_title  =  "ADMIN SITE"
admin.site.index_title  =  ""

class headersAdmin(admin.ModelAdmin):
    readonly_fields=['logo_preview', 'title_preview']
    list_display =("title_preview","logo_preview" ,"email","insta","facebook","twitter")
    list_display_links =("title_preview","logo_preview" ,"email","insta","facebook","twitter")
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True
    
    
class ImagesAdmin(admin.ModelAdmin):
    readonly_fields=['img_preview']
    list_display =("des","img_preview" ,"title","desp")
    list_display_links =("des","img_preview" ,"title","desp")
    list_filter = (
        ('des', admin.RelatedOnlyFieldListFilter),
    )
        
class HomeAdmin(admin.ModelAdmin):
     list_display=("pagetitle","pagetext")
     list_display_links=("pagetitle","pagetext")
     def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

class ProductsAdmin(admin.ModelAdmin):
    list_display=("name",)

class AboutUsAdmin(admin.ModelAdmin):
     list_display=("pagetitle","pagetext")
     list_display_links=("pagetitle","pagetext")
     def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

class contactAdmin(admin.ModelAdmin):
    list_display=("pagetitle","pagetext")
    list_display_links=("pagetitle","pagetext")
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

class carouselAdmin(admin.ModelAdmin):
    readonly_fields=['car_preview']
    list_display =("car_preview" ,"Img_title","Img_desc")
    list_display_links  =("car_preview" ,"Img_title","Img_desc")
admin.site.unregister(Group)
admin.site.register(headers,headersAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Home,HomeAdmin)
admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(contact,contactAdmin)
admin.site.register(carousels,carouselAdmin)
admin.site.register(Products,ProductsAdmin)

