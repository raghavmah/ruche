
from .models import Products ,Images, Home,AboutUs, carousels, contact, headers
from django.http import HttpResponse
from django.views.generic import ListView,DetailView


class HomeView(ListView):
    http_method_names = ["get"]
    model=Home
    template_name ='rugs/dashboard.html'
    context_object_name = "home"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context[  'carousels' ] = carousels.objects.all()
        context[  'items' ] = Products.objects.all()
        context[  'head' ] = headers.objects.all()
        
        return context

class ProductView(ListView):
    template_name = 'rugs/products.html'
    context_object_name = 'product'
    model=Images
    slug_field="des"
    slug_url_kwarg="des"
   
    def get_queryset(self):
        return Images.objects.filter(des_id=self.kwargs['des'])
    
    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context[  'carousels' ] = carousels.objects.all()
        context[  'items' ] = Products.objects.all()
        context[  'head' ] = headers.objects.all()
        
        return context
    
    
class ContactView(ListView):
    http_method_names =["get"]
    model=contact
    template_name="rugs/contact.html"
    context_object_name = "contacts"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context[  'carousels' ] = carousels.objects.all()
        context[  'items' ] = Products.objects.all()
        context[  'head' ] = headers.objects.all()
        
        return context

class AboutView(ListView):
    http_method_names =["get"]
    model=AboutUs
    template_name="rugs/aboutus.html"
    context_object_name = "abouts"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context[  'carousels' ] = carousels.objects.all()
        context[  'items' ] = Products.objects.all()
        context[  'head' ] = headers.objects.all()
        
        return context