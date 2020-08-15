from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.logout, name='logout'),
    path('user_detail/', views.user_detail, name='user_detail'),
]