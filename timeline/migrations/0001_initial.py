# Generated by Django 4.2.1 on 2023-08-05 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pointer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='timelineevents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtype', models.CharField(choices=[('NEWS', 'news'), ('EVENT', 'event'), ('INFORMATION', 'information'), ('REPORT', 'report'), ('PERSON', 'person'), ('VEHICLE', 'vehicle'), ('ORGANIZATION/BUSINESS', 'organization/business'), ('POLITICAL PARTY', 'political party')], default='INFORMATION', max_length=255)),
                ('createddate', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('showingraph', models.BooleanField(default=True)),
                ('nodetitle', models.CharField(max_length=255)),
                ('nodedescription', models.TextField(blank=True, default='', null=True)),
                ('nodecolor', models.CharField(default='#0000FF', max_length=80)),
                ('newstitle', models.CharField(blank=True, max_length=255, null=True)),
                ('newspublisher', models.CharField(blank=True, max_length=255, null=True)),
                ('newscategory', models.CharField(choices=[('LOCAL POLITICS', 'Local Politics'), ('SPORTS', 'Sports'), ('ENTERTAINMENT', 'Entertainment'), ('REPORT', 'report'), ('Global Politics', 'Global Politics'), ('CRIME', 'Crime'), ('FIRE', 'Fire'), ('INCIDENT', 'Incident'), ('OTHER', 'Other')], default='OTHER', max_length=255)),
                ('newslink', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('eventname', models.CharField(blank=True, max_length=255, null=True)),
                ('eventsponsor', models.CharField(blank=True, max_length=255, null=True)),
                ('eventdate', models.DateField(blank=True, null=True)),
                ('eventlocation', models.CharField(blank=True, max_length=255, null=True)),
                ('eventlatitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('eventlongitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('showinmap', models.BooleanField(blank=True, default=True, null=True)),
                ('infoname', models.CharField(blank=True, max_length=255, null=True)),
                ('infodescription', models.CharField(blank=True, max_length=255, null=True)),
                ('infosource', models.CharField(blank=True, max_length=255, null=True)),
                ('reportnumber', models.CharField(blank=True, max_length=255, null=True)),
                ('reporttitle', models.CharField(blank=True, max_length=255, null=True)),
                ('reportdate', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['createddate'],
            },
        ),
    ]
