from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Products ,Images, Home,AboutUs, carousels, contact, headers,banner_one,banner_two
from django.http import HttpResponse
from django.views.generic import ListView,DetailView

from django.shortcuts import render

class HomeView(ListView):
    http_method_names = ["get"]
    model=Home
    template_name ='rugs/dashboard.html'
    context_object_name = "home"
    def __str__(self):
      return str(self.id)
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context[  'carousels' ] = carousels.objects.all()
        context[  'items' ] = Products.objects.all()
        context[  'head' ] = headers.objects.all()
        context[  'pic']  = Images.objects.all()
        context[ 'banner1'] = banner_one.objects.all()
        context[ 'banner2'] = banner_two.objects.all()
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
    
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')




    
