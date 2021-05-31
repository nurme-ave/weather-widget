import requests
import wget

city = input('Enter your city: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=d77b3627841123cf3a6aca273de34e05'

res = requests.get(url)

data = res.json()

customer_city = data['name']
temp = data['main']['temp']
icon = data['weather'][0]['icon']
icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"


print(f'\nThe current temperature in {customer_city} is {temp} degrees.')
wget.download(icon_url, f'Icons/{icon}.png')
