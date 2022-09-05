from re import template
from django import urls
from django.contrib import admin
from django.urls import URLPattern, path,include
from . import views as v1
from django.views.generic import TemplateView
urlpatterns=[
    path('',v1.dash.as_view()),
    path('login',v1.login.as_view(template_name='login.html'),name='login'),
    path('register',v1.login.as_view(template_name="register.html"),name="register"),
    path('Edit',v1.Edit.as_view(template_name="Edit.html"),name="Edit"),
    path("home", v1.dash.as_view(), name="home"),
    path('mails',v1.mails,name="mails")

]