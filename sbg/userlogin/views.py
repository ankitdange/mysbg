from django.shortcuts import render ,redirect
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib.messages import constants as messages

def index(request):
    username = password=''
    if request.POST:
        username =request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username,password=password)
        if  user is not  None:
            login(request,user)
            return HttpResponseRedirect('dashbord/')
    return render (request,'registration/index.html')
   




def logout(request):
    auth.logout(request)
    return render(request,'registration/index.html')
    