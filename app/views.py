from django.shortcuts import render

from app.models import *
from django.db.models.functions import Length

def display_country(request):
    QSC=Country.objects.all()
    QSC=Country.objects.all().order_by('Country_Name')


    d={'country':QSC}
    return render(request,'display_country.html',d)

def display_cap(request):
    QSCA=Cap.objects.all()
    QSCA=Cap.objects.all().order_by('Country_Name')
    QSCA=Cap.objects.all().order_by('-Country_Name')
    QSCA=Cap.objects.filter(Country_Name='India').order_by('Cap_name')#ASC
    QSCA=Cap.objects.filter(Country_Name='India').order_by('-Cap_name')#DESC
    QSCA=Cap.objects.exclude(Country_Name='India').order_by('Cap_name')#ASC
    QSCA=Cap.objects.exclude(Country_Name='India').order_by('-Cap_name')#DESC
    QSCA=Cap.objects.all().order_by(Length('Cap_name'))
    QSCA=Cap.objects.all().order_by(Length('Cap_name').desc())[:5]#Top % colums
    QSCA=Cap.objects.exclude(Country_Name='India').order_by(Length('num_states'))[::-2]

    d={'cap':QSCA}
    return render(request,'display_cap.html',d)
    