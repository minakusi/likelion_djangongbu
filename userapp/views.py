from django.shortcuts import render, redirect
from .models import Userinfo
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method =='POST':
        ID = request.POST['ID']
        PW = request.POST['PW']
        user = auth.authenticate(request, username = ID, password = PW)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error':'아이디 혹은 패스워드가 틀렸습니다.'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method =='POST':
        if request.POST['PW'] == request.POST['PW2']:
            user = User.objects.create_user(username = request.POST['ID'], password = request.POST['PW'])
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def user_detail(request):
    return render(request, 'user_detail.html')
