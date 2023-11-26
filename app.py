"""CP1404 practical 10 - Flask Web Framework"""
from flask import Flask

app = Flask(__name__)


def calc_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def calc_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9.0
    return celsius


@app.route('/')  # 'decorator'
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius='0.0'):
    fahrenheit = calc_fahrenheit(float(celsius))
    return f"Result: {fahrenheit}°F<br>Calculated from {celsius}°C"


@app.route('/c')
@app.route('/c/<fahrenheit>')
def c(fahrenheit='0.0'):
    celsius = calc_celsius(float(fahrenheit))
    return f"Result: {celsius}°C<br>Calculated from {fahrenheit}°F"


if __name__ == '__main__':
    app.run()
