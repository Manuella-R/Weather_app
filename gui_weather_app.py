import requests
city_name = 'Nairobi'
API_key = 'eb38ea9004f4d4995963f458e96d73f4'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'


response = requests.get(url)    
if response.status_code == 200:
    data = response.json()
    print('Weather is ', data['weather'][0]['description'])
    print('Temperature is ', data['main']['temp'])
    print('Current Temp feels like', data['main']['feels_like'])
    print('Humidity is ', data['main']['humidity'])
 
    print('it worked turn off pilot')
