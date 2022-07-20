import requests


def get_city_weather(city):
    api_key = '745fb1f9f05d9447185ec6e2868e1ca5'
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
    response_json = response.json()
    if 'message' in response_json and response_json['message'] == 'city not found':
        return "Sorry, but I can't find the city. Please check the city name and try again."

    weather = {'temp': response_json['main']['temp'], 'feels_like': response_json['main']['feels_like'],
               'weather': response_json['weather'][0]['main'], 'wind': response_json['wind']['speed']}

    return f'In {city.title()} now {weather["weather"]}, the temperature is {weather["temp"]} Celsius, ' \
           f'feels like {weather["feels_like"]}, and winds {weather["wind"]} meters per second.'


