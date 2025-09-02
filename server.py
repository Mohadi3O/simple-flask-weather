

import argparse
from argparse import ArgumentParser
from flask import Flask, request, render_template
from weather import get_current_weather_data
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if  not bool(city.strip()):
        city = "algeria"

    weather_data = get_current_weather_data(city)

    if weather_data is None or weather_data.get('cod') != 200:
        return render_template('city_not_found.html')
      
    return render_template(
      'Weather.html',
      title= weather_data['name'],
      temp= f'{weather_data['main']['temp']:.1f}',
      status= weather_data['weather'][0]['description'].capitalize(),
      feels_like= f'{weather_data['main']['feels_like']:.1f}'

    )



# Argument parsing
def get_args() -> argparse.Namespace:
    """
    Parses command-line arguments to elect the type of running our app
    """
    parser = ArgumentParser(
        description="Weather application arguments")
    parser.add_argument("-t", "--type", metavar="type", type=str,
                        default="_", help="Enter your name between quotes (\" _ \")")

    args = parser.parse_args()
    return args




def run():
    '''
    this function is for starting the server \n
    there are two ways to running :\n
    1) by default flask run() function\n
    \t\tor\n
    2) using serve() function from waitress module\n
    >>> you can choose one of them by passing an argument in the command line
    if there "-t" or "--type" values are existed that meaning the first way is selected  so if not the second defiantly is selected

    '''
    args = get_args()
    if args.type:
        app.run(host="0.0.0.0", port=8000, debug=True)
    else:
        serve(app, host="0.0.0.0", port=8000)


if __name__ == '__main__':
        serve(app, host="0.0.0.0", port=8000)
    # run()
