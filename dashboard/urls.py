"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from timeline.views import  searchevent, deleteevent, map_view,homeview, feed, addevent, WeatherAPI, map_view_beta, add_pointer, delete_pointer, eventgraph, graphjson
from users.views import loginview, logoutview, edit_profile
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview, name='home'),

    path('map/', map_view, name='map'),
    path('map/<str:location>', map_view_beta, name='maplocation'),
    path('add_pointer/', add_pointer),
    path('delete_pointer/', delete_pointer),
    
    path('feed/', feed, name='feed'),
    



    path('weather/', login_required(WeatherAPI.as_view()), name='weather'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('edit_user/', edit_profile, name='edituser'),
    path('graph/', eventgraph, name='graph'),
    path('jsongraph/', graphjson, name='jsongraph')

]

htmx = [

 path('addevent/', addevent, name='addevent'),
path('deleteevent/<id>', deleteevent, name='deleteevent'),
path('search/', searchevent, name='searchevent'),
  


]

urlpatterns += htmx