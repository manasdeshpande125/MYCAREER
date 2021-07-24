from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="shopHome"),
    path("about/",views.about,name="Aboutus"),
    path("search/",views.search,name="Search"),
    path('form/', views.index2,name="index2"),
    path('startup/', views.enter,name="startup"),
    path('jobs/', views.work,name="jobs"),
    path('mba/', views.mba,name="mba"),
    path('mtech/', views.mtech,name="mtech"),
    path('gre/', views.gre,name="gre"),
    path('upsc/', views.upsc,name="upsc"),
    path('inter/', views.inter,name="inter")

]
