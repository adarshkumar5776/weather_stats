from django.shortcuts import render
from django.http import HttpResponse
import csv
import os
from ingest.models import weather_records
from ingest.models import yield_records
from django.db.models import Sum
from django.db.models import Avg
from django.shortcuts import redirect
import datetime
from ingest.models import result
from ingest.models import result1
from ingest.models import result2




# Create your views here.
def prints(request):
     return render(request,'front.html')

def Avg_max(request):
     
    if request.method=="POST":
     start_date=request.POST.get('start')
     end_date=request.POST.get('end')
    
     
     listItems=weather_records.objects.all()
     listItems=listItems.filter(dates__range=[start_date,end_date])
     
     a=listItems.aggregate(Avg('Max_temp'))
     
    #  a=weather_records.objects.filter().values('dates').order_by('dates').annotate(sum=Sum('Max_temp'))
    #  a = weather_records.objects.filter(sampledate__gte=datetime.date(2011, 1, 1),
    #                              sampledate__lte=datetime.date(2011, 1, 31)).aggregate(Avg('Max_temp'))
    
  
     a_new=a.get("Max_temp__avg")
     result.objects.create(Max_temp=a_new,start_date=start_date,end_date=end_date)
     maxTrue=True
    #  print(a_new)
     return render(request,'avg_temp.html',{'a_new':a_new,'maxTrue':maxTrue})

def Avg_min(request):
    if request.method=="POST":
     
     start_date1=request.POST.get('start1')
     end_date1=request.POST.get('end1')
     
     listItems1=weather_records.objects.all()
     listItems1=listItems1.filter(dates__range=[start_date1,end_date1])
     a1=listItems1.aggregate(Avg('Min_temp'))
    #  a1=weather_records.objects.filter(dates__range=[start_date,end_date]).aggregate(Avg('Min_temp'))
     print(a1)
     a_new1=a1.get("Min_temp__avg")
     result1.objects.create(Min_temp=a_new1,start_date=start_date1,end_date=end_date1)
     minTrue=True
    #  print(a_new)
     return render(request,'avg_temp.html',{'a_new1':a_new1,'minTrue':minTrue})

def Sum_pre(request):
    if request.method=="POST":
     
     start_date2=request.POST.get('start2')
     end_date2=request.POST.get('end2')
     listItems2=weather_records.objects.all()
     print(start_date2)
     listItems2=listItems2.filter(dates__range=[start_date2,end_date2])
     a2=listItems2.aggregate(Sum('Precipitation'))
    #  a2=weather_records.objects.aggregate(Sum('Precipitation'))
     print(a2)
     a_new2=a2.get("Precipitation__sum")
     a_new2=int(a_new2/10)
     result2.objects.create(Precipitation=a_new2,start_date=start_date2,end_date=end_date2)
     preTrue=True
    #  print(a_new)
     return render(request,'avg_temp.html',{'a_new2':a_new2,'preTrue':preTrue})
    
     
def load(request):
    # weather_records.objects.create(date='2022-11-10',Max_temp='345',Min_temp='543',Precipitation='6543')
 if request.method=="POST":
    path1=request.POST.get('path')
    new_string = path1.replace("\ ","/")
    file=open(new_string)
    read_file=csv.reader(file)
    
    count=1
    weather_records.objects.all().delete()
    for record in read_file:
        if count==1:
            pass
        else:
            weather_records.objects.create(dates=record[0],Max_temp=record[1],Min_temp=record[2],Precipitation=record[3])
        
        count=count+1

        
    records=weather_records.objects.all()
    return render(request,'front.html',{'records':records})
 else:
    return render(request,'front.html')


def load1(request):
    # weather_records.objects.create(date='2022-11-10',Max_temp='345',Min_temp='543',Precipitation='6543')
 if request.method=="POST":
    path=request.POST.get('path1')
    new_string = path.replace("\ ","/")
    file=open(new_string)
    read_file=csv.reader(file)
    
    count=1
    yield_records.objects.all().delete()
    for record in read_file:
        if count==1:
            pass
        else:
            yield_records.objects.create(yield_year=record[0],yield_data=record[1])
        
        count=count+1

        
    records=yield_records.objects.all()
    return render(request,'front1.html',{'records':records})
 else:
    return render(request,'front1.html')