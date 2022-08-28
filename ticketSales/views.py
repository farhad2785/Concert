from multiprocessing import context
from django.http import HttpResponse,HttpResponseRedirect
from urllib import request
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
# import accounts
from accounts.views import login_view
from django.contrib.auth.decorators import login_required
# import concert
from . import models,forms
import ticketSales

# Create your views here.

def concertListView(request):

    search_form = forms.SearchFrom(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        concerts = models.ConcertModel.objects.filter(name__contains=search_text)

    else:
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
        'search_form' : search_form,
    }
    return render(request,'ticketSales/concert_list.html',context)


@login_required
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



@login_required
def timeView(request):

    # if request.user.is_authenticated and request.user.is_active:
    times = models.TimeModel.objects.all()
    context = {
        'timelist': times,
    }
    return render(request,'ticketSales/time_list.html',context)   
    # else:
    #     return HttpResponseRedirect(reverse(accounts.views.login_view)) 



def concertEditView(request,concert_id):

    concert = models.ConcertModel.objects.get(pk=concert_id)

    if request.method=='POST':
        concert_form = forms.ConcerForm(request.POST, request.FILES, instance=concert)
        if concert_form.is_valid:
            concert_form.save()
            return HttpResponseRedirect(reverse(ticketSales.views.concertListView))
    else:
        concert_form = forms.ConcerForm(instance=concert)

    
    context = {
        'concert_form': concert_form,
        'poster_image' : concert.poster
    }
    return render(request,'ticketSales/concert_edit.html',context)