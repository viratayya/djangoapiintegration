
from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('<slug:slug>/',views.PostComments.as_view()),
    path('',views.Post.as_view()),
]
