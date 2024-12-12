from django.urls import path
from . import views
from .converters import FloatConverter


app_name = 'pricing' 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('inquiry/<str:plan_name>/<float:plan_amount>/', views.pricing_inquiry, name='pricing_inquiry'),
    path('base/', views.base, name='base'),

    

]