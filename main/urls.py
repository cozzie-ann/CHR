from django.urls import path, re_path
from . import views
from .converters import FloatConverter


app_name = 'pricing' 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('services/', views.services, name='services'),

    re_path(r'^inquiry/(?P<plan_name>[^/]+)/(?P<plan_amount>\d+(\.\d+)?|)/$', views.pricing_inquiry, name='pricing_inquiry'),
    path('base/', views.base, name='base'),

    

]