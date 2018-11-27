from django.shortcuts import render
from django.shortcuts import HttpResponse
from demoApp import models
# Create your views here.

user_list = [
    {"user": "JACK3", "pwd": "123"},
    {"user": "TOMS3", "pwd": "456"},
]

def login_view(request):
    return render(request, "index.html", {"data": user_list})

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        cityName = request.POST.get('cityname')
        cityAdd = request.POST.get('cityadd')
        models.UserInf.objects.create(user=name, pwd=pwd)
        models.CityInf.objects.create(CityName=cityName, CityAdd=cityAdd)
    user_list = models.UserInf.objects.all()
    city_list = models.CityInf.objects.all()
    employ_list = models.Employee.objects.all()
    #return HttpResponse(message)
    return render(request, "index.html", {"data": user_list,"data1": city_list,"data2": employ_list})