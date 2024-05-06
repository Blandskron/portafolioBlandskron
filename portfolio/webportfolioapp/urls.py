from django.urls import path
from webportfolioapp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_message, name='success_message'),
]