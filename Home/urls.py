from django.urls import path
from .views import Home,filter_projects,About_us,Services,Esg,contact_view,OurMarkets,Solutions,JoinTeam,WhistleBlowing
from . import views
urlpatterns=[
    path('',Home.as_view(),name="homepage"),
     path('filter-projects/', filter_projects, name='filter_projects'),
     path('about-us/',About_us,name="about_us"),
     path('our-markets/',OurMarkets,name="our_markets"),  # custom view for our markets page
     path('services/',Services,name="services"),
     path('esg/',Esg,name="esg"),
      path("contact/", contact_view, name="contact"),
      path("solutions/", Solutions, name="solutions"),
      path("solutions/built-to-suit", Solutions, kwargs={'slug': 'built-to-suit'}, name="built-to-suit"),
      path("solutions/co-location", Solutions, kwargs={'slug': 'co-location'}, name="co-location"),
      path("solutions/ibs", Solutions, kwargs={'slug': 'ibs'}, name="ibs"),
      path("team/", JoinTeam, name="join_team"),
      path("whistle-blowing/", WhistleBlowing.as_view(), name="whistle_blowing"),
      
    path('blogs/', views.blog_list_view, name='blog_list'),
    path('blogs/<slug:slug>/', views.blog_detail_view, name='blog_detail'),
    

]