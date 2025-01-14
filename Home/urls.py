from django.urls import path
from .views import Home,filter_projects,About_us,Services,Esg,contact_view
from . import views
urlpatterns=[
    path('',Home.as_view(),name="homepage"),
     path('filter-projects/', filter_projects, name='filter_projects'),
     path('about-us/',About_us,name="about_us"),
     path('services/',Services,name="services"),
     path('esg/',Esg,name="esg"),
      path("contact/", contact_view, name="contact"),
      
    path('blogs/', views.blog_list_view, name='blog_list'),
    path('blogs/<slug:slug>/', views.blog_detail_view, name='blog_detail'),

]