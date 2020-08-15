from django.urls import path
from . import views

urlpatterns = [
    path('', views.postings, name='postings'),
    path('write/', views.write, name='write'),
]