from django.contrib import admin

# Register your models here.
from .models import Home,AboutUs,contact,carousels,headers ,Images,Products
from  django.contrib.auth.models  import  Group
admin.site.site_header  =  "RAGHAV SITE DASHBOARD"  
admin.site.site_title  =  "ADMIN SITE"
admin.site.index_title  =  ""

class headersAdmin(admin.ModelAdmin):
    list_diaplay=("LOGO" ,"E-MAIL","INSTAGRAM","FACEBOOK","TWITTER")
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

    
class ImagesAdmin(admin.ModelAdmin):
    pass
        
class HomeAdmin(admin.ModelAdmin):
     def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

class ProductsAdmin(admin.ModelAdmin):
    pass

class AboutUsAdmin(admin.ModelAdmin):
     def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

class contactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

class carouselAdmin(admin.ModelAdmin):
    pass
admin.site.unregister(Group)
admin.site.register(headers,headersAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Home,HomeAdmin)
admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(contact,contactAdmin)
admin.site.register(carousels,carouselAdmin)
admin.site.register(Products,ProductsAdmin)

