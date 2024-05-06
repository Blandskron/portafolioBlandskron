from django.urls import path
from webportfolioapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('softskills/', views.softskills, name='softskills'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_message, name='success_message'),
]