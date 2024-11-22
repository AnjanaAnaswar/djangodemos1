from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required



def register(request):

    if(request.method=='POST'):
        u=request.POST['us']
        p1=request.POST['pa']
        p2=request.POST['pass']
        e=request.POST['em']
        f=request.POST['fi']
        l=request.POST['la']
        if(p1==p2):
            r=User.objects.create_user(username=u,password=p1,email=e,first_name=f,last_name=l)
            r.save()
        else:
            return HttpResponse('Both passwords should be same')
        
        return redirect('shop:categories')

    return render(request,'register.html')


def signin(request):

    if(request.method=='POST'):
        u=request.POST['us']
        p=request.POST['pa']
        user_object=authenticate(username=u,password=p)
        
        if(user_object):
            login(request,user_object)
            return redirect('shop:categories')
        else:
            return HttpResponse('invalid credentials')

    return render(request,'login.html')


@login_required
def signout(request):
    logout(request)
    return redirect('shop:categories')