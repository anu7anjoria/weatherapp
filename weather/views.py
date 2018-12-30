from django.shortcuts import render
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8cd5cfb744611240e0c17b0b7d872b23'
    city = 'Patiala'
    city_weather = requests.get(url.format(city)).json() 

    weather = {
        #City Info
        'city' : city,
        'longitude' : city_weather['coord']['lon'],
        'latitude'  : city_weather['coord']['lat'],
       'country' : city_weather['sys']['country'],
       # 'sunrise' : ['sys']['sunrise'],
       # 'sunset' : ['sys']['sunset'],
        #Temprature
        'temperature' : city_weather['main']['temp'],
        'temp_min' : city_weather['main']['temp_min'],
        'temp_max' : city_weather['main']['temp_max'],
        'humidity' : city_weather['main']['humidity'],
        'pressure' : city_weather['main']['pressure'],
        'wind_speed' : city_weather['wind']['speed'],
        'wind_dir' : city_weather['wind']['deg'],
        'clouds' :city_weather['clouds']['all'],
       # 'visibilty' :city_weather['dt']['value'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],
       

    }
    return render(request, 'weather/index.html',{'weather':weather})