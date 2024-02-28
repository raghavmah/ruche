from .views import HomeView,ProductView ,AboutView,ContactView,ResetPasswordView
from django.urls import path
from . import views
app_name="rugs"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<str:des>/',ProductView.as_view(),name='products'),
    path('aboutus', AboutView.as_view(),name='about'),
    path('contact',ContactView.as_view(),name='contact'),
   path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
 
]