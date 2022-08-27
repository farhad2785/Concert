from multiprocessing import context
from django.http import HttpResponse,HttpResponseRedirect
from urllib import request
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
import accounts

import concert
from . import models

# Create your views here.

def concertListView(request):
    concerts = models.ConcertModel.objects.all()
    # text = '''
    # <!DOCTYPE html>
    # <html>
    # <head>
    # <title>Page Title</title>
    # </head>
    # <body>
    #     <h1>لیست کنسرت ها</h1>
    #     <ul>
    #         {}
    #     </ul>
    # </body>
    # </html>
    # '''.format('\n'.join('<li>{}</li>'.format(concert) for concert in concerts))

    context = {
        'concertlist': concerts,
        'concertcount': concerts.count,
    }
    return render(request,'ticketSales/concert_list.html',context)


def locationListView(request):

    locations = models.LocationModel.objects.all()
    context = {
        'locationlist': locations,
    }
    return render(request,'ticketSales/location_list.html',context)


def concertdDtailsView(request, concert_id):
    concert = models.ConcertModel.objects.get(pk=concert_id)
    
    context = {
        'concertdetails' : concert
    }
    print(concert)
    return render(request,'ticketSales/concert_details.html',context)


def timeView(request):

    if request.user.is_authenticated and request.user.is_active:
        times = models.TimeModel.objects.all()
        context = {
            'timelist': times,
        }
        return render(request,'ticketSales/time_list.html',context)   
    else:
        return HttpResponseRedirect(reverse(accounts.views.login_view)) 