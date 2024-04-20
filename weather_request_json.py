import requests
import json


OPEN_WEATHER_API_KEY = 'aebf204b101c8b173750b669ce15b279';

url = "http://api.openweathermap.org/data/2.5/""weather?" \
          "q={}&" \
          "appid={}&" \
          "units=metric&" \
          "lang=ru".format("Томск", OPEN_WEATHER_API_KEY)

weather_data = json.loads(requests.get(url).text)
file = open('weather_data.json', 'w', encoding='utf-8')
json.dump(weather_data, file, indent=2, ensure_ascii=False)

print(f'''Добрый день
Сейчас температура в {weather_data['name']} {weather_data['main']['temp']}
На улице  {weather_data['weather'][0]['description']}
Скорость ветра {weather_data['wind']['speed']}''')

# print(weather_data['name'])
# print(weather_data['weather'][0]['description'])
# print(weather_data['main']['temp'])
# print(weather_data['wind']['speed'])
