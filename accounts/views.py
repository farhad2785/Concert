import re
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
import ticketSales
from concert import settings
from django.contrib.auth.decorators import login_required
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