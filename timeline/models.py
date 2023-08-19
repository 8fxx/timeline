from django.db import models
import datetime
from django.conf import settings
from django.db import models
from users.models import DEPARTMENT_CHOICES

EVENT_CHOICES = [
  
    ("NEWS", 'News'),
    ("EVENT", 'Event'),
    ("INFORMATION", 'Information'),
    ("REPORT", 'Report'),
    ("PERSON", 'Person'),
    ("VEHICLE", 'Vehicle'),
    ("ORGANIZATION/BUSINESS", 'Organization/Business'),
    ("POLITICAL PARTY", 'Political Party'),
]

NEWS_CHOICES = [
    ("LOCAL POLITICS", 'Local Politics'),
    ("SPORTS", 'Sports'),
    ("ENTERTAINMENT", 'Entertainment'),
    ("REPORT", 'report'),
    ("Global Politics", 'Global Politics'),
    ("CRIME", 'Crime'),
    ("FIRE", 'Fire'),
    ("INCIDENT", 'Incident'),
    ("OTHER", 'Other'),
]


# Create your models here.
class timelineevents(models.Model):
    eventtype = models.CharField(max_length=255, choices=EVENT_CHOICES,default='')
    createddate = models.DateTimeField(default=datetime.datetime.now, editable=False)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='User', default='id')
    showingraph = models.BooleanField(default=True)

    # nodes
    nodetitle = models.CharField(max_length=255)
    nodedescription = models.TextField(default='', null=True, blank=True)
    nodecolor = models.CharField(max_length=80, default='#0000FF')
    relatedevents = models.ManyToManyField('self', blank=True, symmetrical=False)

    # news
    newstitle = models.CharField(null=True, blank=True, max_length=255)
    newspublisher = models.CharField(null=True, blank=True, max_length=255)
    newscategory = models.CharField(choices = NEWS_CHOICES, default='OTHER', max_length=255)
    newslink = models.CharField(max_length=255,null=True, blank=True)
    image = models.CharField(max_length=255,null=True,blank=True)

    #event
    eventname = models.CharField(max_length=255, null=True, blank=True)
    eventsponsor = models.CharField(max_length=255, null=True, blank=True)
    eventdate = models.DateField(null=True, blank=True)
    eventlocation = models.CharField(max_length=255, null=True, blank=True)
    eventlatitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    eventlongitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    showinmap = models.BooleanField(default=True, blank=True)

    #information
    infoname = models.CharField(max_length=255, null=True, blank=True)
    infodescription = models.CharField(max_length=255, null=True, blank=True)
    infosource = models.CharField(max_length=255, null=True, blank=True)

    #report
    reportnumber = models.CharField(max_length=255, null=True, blank=True)
    reporttitle = models.CharField(max_length=255, null=True, blank=True)
    reportdate = models.DateField(default=datetime.datetime.now)
    reportdepartment = models.CharField(choices = DEPARTMENT_CHOICES, max_length=255, null=True, blank=True)




    class Meta:
        ordering = ['createddate']
    def __str__(self):
        return self.eventtype + ' - ' + self.nodetitle

    
class Pointer(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.TextField(null=True)

    def __str__(self):
        return self.title