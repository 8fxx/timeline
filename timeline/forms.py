from django import forms
from .models import timelineevents
from django.forms.widgets import TextInput
class addeventform(forms.ModelForm):
    class Meta:
        model = timelineevents
        fields = [
            'eventtype',
            'showingraph',
            'nodetitle',
            'nodecolor',
            'relatedevents',

            'newstitle',
            'newspublisher',
            'newscategory',
            'newslink',
            'image',

            'eventname',
            'eventsponsor',
            'eventdate',
            'eventlocation',
            'eventlatitude',
            'eventlongitude',
            'showinmap',

            'infoname',
            'infodescription',
            'infosource',

            'reportnumber',
            'reporttitle',
            'reportdate',
            'reportdepartment',

            ]
        
        labels = {
            'eventtype': 'Item Type',
            'showingraph' : 'Show in Graph',
            'nodetitle' : 'Node Title (Required)*',
            'nodedescription': 'Node Description',
            'nodecolor': 'Node Color',
            'relatedevents': 'Related Items',

            'newstitle': 'News Title',
            'newspublisher': "News Publisher",
            'newscategory': 'News Category',
            'newslink': 'News URL',
            'image': 'Image URL',
            'orientation': 'Orientation',

            'eventname': 'Event Name',
            'eventsponsor': 'Event Sponsor',
            'eventdate' : 'Event Date',
            'eventlocation': 'Event Location',
            'eventlatitude': 'Event Latitude',
            'eventlongitude': 'Event Longitude',
            'showinmap': 'Show in Map',

            'infoname': 'Title for Information',
            'infodescription': 'Description of Information',
            'infosource': 'Information Source',

            'reportnumber': 'Report Number',
            'reporttitle': 'Report Title',
            'reportdate': 'Report Date',
            'reportdepartment': 'Report Department',

        }
        widgets = {
                   'nodecolor': TextInput(attrs={'type': 'color'}),
                   }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # nodes
        # self.fields['eventtype'].widget.attrs.update({'class':'eventtype form-select m-1', 'placeholder':'Select a type'})
        # self.fields['nodetitle'].widget.attrs.update({'class':'form-control m-1', 'placeholder':'Enter Node Title'})
        # # self.fields['showingraph'].widget.attrs.update({'class':'form-check-input m-1'})
        # self.fields['relatedevents'].widget.attrs.update({'class':'form-select m-1'})
        # self.fields['relatedevents'].widget.attrs.update({'style':'z-index:2; width:200px'})
        

        #news
        self.fields['newstitle'].widget.attrs.update({'class':'form-control m-1','placeholder':'Enter News Title'})
        self.fields['newspublisher'].widget.attrs.update({'class':'form-control m-1', 'placeholder':'Enter News Publisher'})
        self.fields['newscategory'].widget.attrs.update({'class':'form-select m-1'})
        self.fields['newslink'].widget.attrs.update({'class':'form-control m-1','placeholder':'Enter URL'})
        self.fields['image'].widget.attrs.update({'class':'form-control m-1','placeholder':'News Image URL'})

        #event
        self.fields['eventname'].widget.attrs.update({'class':'form-control m-1','placeholder':'Enter Event name'})
        self.fields['eventsponsor'].widget.attrs.update({'class':'form-control m-1','placeholder':'Enter Sponsor Name'})
        self.fields['eventdate'].widget.attrs.update({'class':'form-control m-1 datepicker','placeholder':'YYYY-MM-DD'})
        self.fields['eventlocation'].widget.attrs.update({'class':'form-control m-1','placeholder':'Enter Location'})
        self.fields['eventlatitude'].widget.attrs.update({'class':'form-control m-1','placeholder':'Latitude'})
        self.fields['eventlongitude'].widget.attrs.update({'class':'form-control m-1','placeholder':'Longitude'})
        # self.fields['showinmap'].widget.attrs.update({{'class':'form-check-input m-1'}})

        #information
        self.fields['infoname'].widget.attrs.update({'class':'form-control m-1','placeholder':'Information title'})
        self.fields['infodescription'].widget.attrs.update({'class':'form-control m-1','placeholder':'Information description'})
        self.fields['infosource'].widget.attrs.update({'class':'form-control m-1','placeholder':'Source'})

        #report
        self.fields['reportnumber'].widget.attrs.update({'class':'form-control m-1','placeholder':'Information title'})
        self.fields['reporttitle'].widget.attrs.update({'class':'form-control m-1','placeholder':'Information description'})
        self.fields['reportdate'].widget.attrs.update({'class':'form-control m-1','placeholder':'YYYY-MM-DD'})
        self.fields['reportdepartment'].widget.attrs.update({'class':'eventtype form-select m-1', 'placeholder':'Select Department'})

