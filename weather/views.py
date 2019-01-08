from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import City
from .form import CityForm
def history(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8cd5cfb744611240e0c17b0b7d872b23'
    cities = City.objects.all()
    form = CityForm()
    weather_data = []
    
    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : ((city_weather['main']['temp']-32)*5/9).__int__,
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

        context = {'weather_data' : weather_data, 'form' : form}    
   
    return render(request, 'weather/history.html',context)
def delete(self):
    City.objects.all().delete()
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8cd5cfb744611240e0c17b0b7d872b23' ''
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save()
    form = CityForm
    city = City.objects.last()
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    weather = {
            'city' : city,
            'temperature' : ((city_weather['main']['temp']-32)*5/9).__int__,
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
    }
    context = {'weather':weather,'form':form}
    return render(request,'weather/index.html',context)   