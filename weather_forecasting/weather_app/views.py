from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import AddressForm
import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Create your views here.



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AddressForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            template=loader.get_template('main.html')
            name=form.cleaned_data['address']
            url = f"https://open-weather13.p.rapidapi.com/city/{name}/EN"
            print(url)
            headers = {
	                "x-rapidapi-key": os.getenv('x-rapidapi-key'),
	                "x-rapidapi-host":os.getenv('x-rapidapi-host')
                    }
            
            response =requests.get(url, headers=headers)
            if response.status_code==200:
                output=response.json()
                # Extract weather data
                city_name = output.get('name', 'Unknown City')
                weather_description = output['weather'][0]['description']
                temp_celsius = round(output['main']['temp'], 2)  # Convert Kelvin to Celsius
                temp_feels_like = round(output['main']['feels_like'], 2)
                temp_min = round(output['main']['temp_min'], 2)
                temp_max = round(output['main']['temp_max'] , 2)
                humidity = output['main']['humidity']
                wind_speed = output['wind']['speed']
                wind_deg = output['wind']['deg']
                cloudiness = output['clouds']['all']
                
                # Convert UNIX timestamp to human-readable time for sunrise and sunset
                sunrise_time = datetime.utcfromtimestamp(output['sys']['sunrise']).strftime('%H:%M:%S')
                sunset_time = datetime.utcfromtimestamp(output['sys']['sunset']).strftime('%H:%M:%S')

                # Prepare the weather data for display
                weather_data = {
                    'city_name': city_name,
                    'weather_description': weather_description,
                    'temp_celsius': temp_celsius,
                    'temp_feels_like': temp_feels_like,
                    'temp_min': temp_min,
                    'temp_max': temp_max,
                    'humidity': humidity,
                    'wind_speed': wind_speed,
                    'wind_deg': wind_deg,
                    'cloudiness': cloudiness,
                    'sunrise_time': sunrise_time,
                    'sunset_time': sunset_time
                }
            
            #to again show the address bar where we can submit our address
            form=AddressForm()
            return render(request,"main.html",{'form':form,"name":name,"weather_data":weather_data,'output':output})            
    else:
        form=AddressForm()
        return render(request,"master.html",{'form':form})            

