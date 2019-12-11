"""project_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'basic_view'
urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog'),
    path('mentee/', views.mentee, name='mentee'),
    path('mentor/', views.mentor, name='mentor'),
    path('author/', views.author, name='author'),
    path('blog/input_blog', views.input_blog, name='input_blog'),
    path('blog/update', views.update, name='input_content'),
    path('blog/<int:blog_id>/readmore', views.readmore, name='readmore')
]
