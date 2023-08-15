from .views import HomeView ,ProductView ,AboutView,ContactView
from django.urls import path
app_name="rugs"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<str:des>/',ProductView.as_view(),name='products'),
    path('aboutus', AboutView.as_view(),name='about'),
    path('contact',ContactView.as_view(),name='contact'),

    
]