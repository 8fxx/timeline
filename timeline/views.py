from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from timeline.models import timelineevents
from django.contrib.sessions.models import Session
import datetime
from django.views.generic import View
from django import template
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Pointer
from django.core import serializers
import requests
from django.contrib.auth.decorators import login_required
from .forms import addeventform
from django.db.models import Q
from django.contrib import messages

@login_required(login_url='/login/')
def homeview(request):
    show_search_bar = False  # You can replace this with your logic
    return render(request, 'index.html', {'show_search_bar': show_search_bar,})
    
@login_required(login_url='/login/')
def feed(request):
    form = addeventform()
    show_search_bar = True
    feedsearch = True
    data = timelineevents.objects.order_by('-createddate')
    return render(request,'timeline.html', {'form':form,'show_search_bar': show_search_bar,'feedsearch': feedsearch,'object_list':data})

@login_required(login_url='/login/')
def addevent(request):
    feedsearch = True
    show_search_bar = True
    if request.method == 'POST':
        form = addeventform(request.POST)
        if form.is_valid():
            form.instance.createdby = request.user
            form.save()
            data = timelineevents.objects.order_by('-createddate')
            success = True
            return render(request, 'partials/feedlist.html',{'object_list':data,'form':form, 'success':success})
        else:
            form = addeventform(request.POST)
            data = timelineevents.objects.order_by('-createddate')
            return render(request, 'partials/feedlist.html',{'object_list':data,'form_errors':form.errors})

def eventdetail(request, id):
    pass

@login_required(login_url='/login/')
def deleteevent(request, id):
    timelineevents.objects.filter(id=id).delete()
    data = timelineevents.objects.order_by('-createddate')
    success = True 
    return render(request,'partials/feedlist.html',{'object_list':data,'added':success})

@login_required(login_url='/login/')
def searchevent(request):
    if request.method == 'POST':
            searched = request.POST['searched']
            lookup = (
            Q(nodetitle__icontains=searched) |
            Q(eventtype__icontains=searched) |
            Q(createdby__username__icontains=searched) |
            Q(showingraph__icontains=searched) |
            Q(nodedescription__icontains=searched) |
            Q(nodecolor__icontains=searched) |
            Q(relatedevents__nodetitle__icontains=searched) |
            Q(newstitle__icontains=searched) |
            Q(newspublisher__icontains=searched) |
            Q(newscategory__icontains=searched) |
            Q(newslink__icontains=searched) |
            Q(image__icontains=searched) |
            Q(eventname__icontains=searched) |
            Q(eventsponsor__icontains=searched) |
            Q(eventdate__icontains=searched) |
            Q(eventlocation__icontains=searched) |
            Q(eventlatitude__icontains=searched) |
            Q(eventlongitude__icontains=searched) |
            Q(showinmap__icontains=searched) |
            Q(infoname__icontains=searched) |
            Q(infodescription__icontains=searched) |
            Q(infosource__icontains=searched) |
            Q(reportnumber__icontains=searched) |
            Q(reporttitle__icontains=searched) |
            Q(reportdate__icontains=searched) |
            Q(reportdepartment__icontains=searched)
            )
            data =  timelineevents.objects.filter(lookup).order_by('-createddate')
            return render(request, 'partials/feedlist.html',{'object_list':data})
    else:
        return render(request,'search.html',{})
    
class WeatherAPI(View):
    def get(self, request):
        currenturl = 'https://api.openweathermap.org/data/2.5/weather?q=Male&units=metric&appid=213a104a394f779313b8e2bd41d33121'
        forecasturl = "https://api.openweathermap.org/data/2.5/forecast?lat=4.1748&lon=73.5089&appid=213a104a394f779313b8e2bd41d33121"
        currentrespone = requests.get(currenturl)
        forecastrespone = requests.get(forecasturl)
        currentdata = currentrespone.json()
        forecastdata = forecastrespone.json()
        sunrise = datetime.datetime.fromtimestamp(currentdata['sys']['sunrise']/1000).strftime('%H:%M')
        sunset = datetime.datetime.fromtimestamp(currentdata['sys']['sunset']/1000).strftime('%H:%M')
        return render(request, 'weatherdash.html', {'current':currentdata,'forecast':forecastdata, 'sunrise':sunrise, 'sunset':sunset})
    
def liveweather(request):
    pass

@login_required(login_url='/login/')
def map_view(request):
    return render(request, 'maphome.html')


@login_required(login_url='/login/')
def map_view_beta(request, location):
    pointers = Pointer.objects.all()
    pointers_json = serializers.serialize('json', pointers)
    return render(request, 'map.html', {'pointers': pointers_json, 'location': location})

@login_required(login_url='/login/')
def add_pointer(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        title = request.POST.get('title')
        description = request.POST.get('description')
        icon = request.POST.get('icon')
        pointer = Pointer(latitude=latitude, longitude=longitude, title=title, description=description, icon = icon)
        pointer.save()
        print('added', request.POST.get('PointerID'))
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
    
@login_required(login_url='/login/') 
def delete_pointer(request):
    if request.method == 'POST':
        if request.POST.get('PointerID') != 'map':
            pointerid = request.POST.get('PointerID')
            pointer = get_object_or_404(Pointer, pk=pointerid)
            pointer.delete()
            print('Deleted',pointerid)
            return JsonResponse({'success': True})   
    else:
        return None
    
@login_required(login_url='/login/') 
def eventgraph(request):
    show_search_bar = True
    graphsearch = True
    now = datetime.datetime.now()
    return render(request, 'graph.html',{'show_search_bar': show_search_bar, 'graphsearch':graphsearch})

@login_required(login_url='/login/')
def graphjson(request):
    events = timelineevents.objects.filter(showingraph=True)
    nodes = [{'id': event.id, 'title': event.nodetitle, 'color': event.nodecolor} for event in events]
    links = []
    for event in events:
        for related_event in event.relatedevents.filter(showingraph=True):
            links.append({'source': event.id, 'target': related_event.id})
    data = {'nodes': nodes, 'links': links}
    return JsonResponse(data, content_type="application/json")



    



    







