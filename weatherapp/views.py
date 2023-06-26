from django.shortcuts import render
import requests
import datetime
import random
# Create your views here.
'''
weather = {
    "sun" : "fa-solid fa-sun",
    "sun-cloud" : "fa-solid fa-cloud-sun",
    "sun-rain" : "fas fa-cloud-sun-rain",
}'''
weather2 = ["fas fa-sun", "fas fa-cloud-sun", "fas fa-cloud-sun-rain", 
            "fas fa-cloud", "fas fa-cloud-showers-heavy", 
            "fas fa-moon", "fas fa-cloud-moon"]

weathermap = {
    "sunny" : "fas fa-sun",
    "cloudy" : "fas fa-cloud",
    "rainy" : "fas fa-cloud-showers-heavy",
}

sunny = [1000]
cloudy = [1003, 1006, 1009, 1030, 1063, 1066, 1069, 1072, 1087]
rain = [1114, 1117, 1135, 1147, 1150, 1153, 1168, 1171, 1180, 1183, 1186, 1189, 1192, 1195, 1198, 1201, 1204, 1207, 1210, 1213, 1216, 1219, 1222, 1225, 1237, 1240, 1243, 1246, 1249, 1252, 1255, 1258, 1261, 1264, 1273, 1276, 1279, 1282]

#APINinja exercise API variables
APINinjaKey = 'dV9FTqWfYRGojBtO5zA2fA==NYSICiGYwfHsZ4dq'
APINinjaHeaders = {'X-Api-Key' : APINinjaKey}
APINinjaEndPt = 'https://api.api-ninjas.com/v1/weather?city=london'

#WeatherAPI direction dictionary
dir = {
    'NW':'North-West',
    'N':'North',
    'NE':'North-East',
    'E':'East',
    'SE':'South-East',
    'S':'South',
    'SW':'South-West',
    'W':'West'
}


#View for homepage
def weather(request):
    context = {}
    '''icon = random.randint(0, 6)
    context['icon'] = weather2[icon]
    response = requests.get(APINinjaEndPt, headers=APINinjaHeaders)
    if response.status_code == requests.codes.ok:
        print(response.text)
        json = response.json()
        context['weather'] = json
        try:
            context['sunset'] = datetime.datetime.fromtimestamp(json['sunset'])
            context['sunrise'] = datetime.datetime.fromtimestamp(json['sunrise'])
        except:
            pass
    else:
        print("Error:", response.status_code, response.text)'''
    
    #WeatherAPI data getter
    weatherResponse = requests.get('http://api.weatherapi.com/v1/current.json?key=fc05229c81164c538f8194512232406&q=Afghanistan&aqi=no')
    json = weatherResponse.json()
    print(json)
    try:    #Try to format wind direction nicely
        windDir = dir[json['current']['wind_dir']]
    except: #Not in pre-def dictionary? Keep as-is
        windDir = json['current']['wind_dir']
    
    context = {'location':(json['location']['name'] + ", " + json['location']['country']),
               'condition':json['current']['condition']['text'],
               'temp':json['current']['temp_c'],
               'feelslike':json['current']['feelslike_c'],
               'wind_mph':json['current']['wind_mph'],
                'wind_dir':windDir,
               'vis':json['current']['vis_miles'],
               'time':(json['location']['localtime']),
     }
    
    if(json['current']['condition']['code'] == 1000):
        cond = "sunny"
    elif(json['current']['condition']['code'] in cloudy):
        cond = "cloudy"
    elif(json['current']['condition']['code'] in rain):
        cond = "rainy"
    else:
        cond = "n/a"

    print(cond)
    print(1006 in cloudy)
    
    icon = random.randint(0, 6)
    try:
        context['icon'] = weathermap[cond]
    except:
        context['icon'] = ""
    context['cond'] = cond

    context['day'] = json['current']['is_day']
    if(json['current']['is_day'] == 0):
        context['icon'] = "fas fa-moon"
    #Render with context
    return render(request, 'weatherapp/weather.html', context)