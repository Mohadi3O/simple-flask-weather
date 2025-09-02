
from dotenv import load_dotenv
from os import getenv
import requests as req
from pprint import pprint




def get_current_weather_data(city_name="biskra"):
    load_dotenv()
    API_KEY = getenv("OpenWeatherMap_API_KEY")
    # global API_KEY
    print('\n\n*** Get current weather conditions *** \n')
    # city_name = input('\n \t ==> Please enter city name:\t')

    requests_URL = f'''https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city_name}&units=imperial'''
    # print(f'\n \t ==> requests_URL= {requests_URL}\n')

    weather_Data = req.get(requests_URL).json()

    # pprint(f'\n \t ==> weather_Data= {weather_Data}\n')
    return weather_Data


if __name__ == "__main__":
    get_current_weather_data()
