import requests
import json
city = input("Enter City name: ")
url = f"https://api.weatherapi.com/v1/current.json?key=0bf287fa2ead41eebd6152759231904&q={city}"

response = requests.get(url)
data = response.text
# data = data.content['location']
try:
    json_data = json.loads(data)
    print(json_data)
    place = json_data['location']['name']
    region = json_data['location']['region']
    country = json_data['location']['country']
    time = json_data['location']['localtime']
    temp = json_data['current']['temp_c']
    wind = json_data['current']['wind_kph']
    print(f"Country: {country}  City : {place},{region} \nTime : {time} \nTemperature : {temp}\nWind : {wind} km/h")
except Exception as e:
    print("Please enter correct city name!")
