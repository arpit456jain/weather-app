from django.shortcuts import render,HttpResponse
import requests
# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        print(city)
        try:
            url = f'https://api.weatherapi.com/v1/current.json?key=f11d5b4a05064d81b2b162530221609&q={city}&aqi=yes'
            r = requests.get(url)
            data = r.json()
            # print(data,type(data))
            # print(data['location'])
            payload = {
                'status' : True,
                'city' : data['location']['name'],
                'region' : data['location']['region'],
                'country' : data['location']['country'],
                'lat' : data['location']['lat'],
                'lon' : data['location']['lon'],
                'time' : data['location']['localtime'],
                'temp' : data['current']['temp_c'],
                'wind_speed' : data['current']['wind_kph'],
                'humidity' : data['current']['humidity'],
                'pressure_mb' : data['current']['pressure_mb'],
            }
            
            # print(payload)
            return render(request,'home.html',payload)
        except:
            context = {'error' : True}
            return render(request,'home.html',context)
    else:
        return render(request,'home.html')