from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
import ticketSales
# Create your views here.


def login_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse(ticketSales.views.timeView))
        else:
            context = {
                'username' : username,
                'errorMessage' : 'کاربری با این مشخصات پیدا نشد!'
            }
            return render(request,'accounts/login.html',context)
    else:
        return render(request,'accounts/login.html',{})