from PIL import Image
from io import BytesIO
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow

import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


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


def get_city_weather_screen(city):
    api_key = '745fb1f9f05d9447185ec6e2868e1ca5'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&mode=html'
    get_screenshot_html(url)


def get_html(response):
    with open("current_weather.html", 'w') as file:
        file.writelines(response.text)


def get_screenshot_html(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(url)

    element = driver.find_element(By.TAG_NAME, 'body')
    location = element.location
    png = driver.get_screenshot_as_png()
    driver.quit()

    im = Image.open(BytesIO(png))
    left = 0
    top = 0
    right = location['x'] + 130
    bottom = location['y'] + 135

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('screenshot.png')  # saves new cropped image


get_city_weather_screen('kyiv')


