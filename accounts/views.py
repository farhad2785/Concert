from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from accounts import models,views
import ticketSales
from concert import settings
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
# Create your views here.


def login_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            else:
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {
                'username' : username,
                'errorMessage' : 'کاربری با این مشخصات پیدا نشد!'
            }
            return render(request,'accounts/login.html',context)
    else:
        return render(request,'accounts/login.html',{})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse(ticketSales.views.concertListView))

@login_required
def profile_view(request):
    profile = request.user.profile
    context = {
        'profile' : profile
    }

    return render(request,'accounts/profile.html',context)

def registerView(request):
    
    if request.method=='POST':
        registerForm = forms.RegisterForm(request.POST, request.FILES) #, instance=concert)
        if registerForm.is_valid():
            user = User.objects.create_user(username= registerForm.cleaned_data['username'],
                                            email= registerForm.cleaned_data['email'],
                                            password= registerForm.cleaned_data['password'],
                                            first_name= registerForm.cleaned_data['first_name'],
                                            last_name= registerForm.cleaned_data['last_name']
                                            )
            user.save()
            profileModel= models.ProfileModel(user=user, profile_pic= registerForm.cleaned_data['profile_pic'],
                                        gender= registerForm.cleaned_data['gender'],
                                        credit= registerForm.cleaned_data['credit'],
                                         )
            profileModel.save()
            return HttpResponseRedirect(reverse(ticketSales.views.concertListView))
    else:
        registerForm = forms.RegisterForm()
    context = {
    'form_data' : registerForm
    }
    return render(request,'accounts/register.html',context)


def profileEditView(request):
    if request.method == 'POST':
        profileEditForm= forms.ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        userEditForm= forms.UserEditForm(request.POST, instance= request.user)
        if profileEditForm.is_valid and userEditForm.is_valid:
            profileEditForm.save()
            userEditForm.save()
            return HttpResponseRedirect(reverse(views.profile_view))
    else:
        profileEditForm= forms.ProfileEditForm(instance=request.user.profile)
        userEditForm= forms.UserEditForm(instance= request.user)
    
    context = {
        'profileEditForm' : profileEditForm,
        'userEditForm' : userEditForm,
        'profile_pic' : request.user.profile.profile_pic
    }
    return render(request,'accounts/profile_edit.html',context)