from django.shortcuts import render
import requests
import datetime
import random
# Create your views here.

weather = {
    "sun" : "fa-solid fa-sun",
    "sun-cloud" : "fa-solid fa-cloud-sun",
    "sun-rain" : "fas fa-cloud-sun-rain",
}
weather2 = ["fas fa-sun", "fas fa-cloud-sun", "fas fa-cloud-sun-rain", 
            "fas fa-cloud", "fas fa-cloud-showers-heavy", 
            "fas fa-moon", "fas fa-cloud-moon"]

#APINinja exercise API variables
APINinjaKey = 'dV9FTqWfYRGojBtO5zA2fA==NYSICiGYwfHsZ4dq'
APINinjaHeaders = {'X-Api-Key' : APINinjaKey}
APINinjaEndPt = 'https://api.api-ninjas.com/v1/weather?city=london'

#View for homepage
def weather(request):
    context = {}
    icon = random.randint(0, 6)
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
        print("Error:", response.status_code, response.text)
    #Render with context
    return render(request, 'weatherapp/weather.html', context)