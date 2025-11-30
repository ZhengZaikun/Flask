from flask import Flask

app = Flask(__name__)

def convert_celsius_to_fahrenheit(celsius_float):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = celsius_float * 9 / 5 + 32
    return fahrenheit

@app.route('/')
def hello_world():
    """View functions for the website's root directory."""
    return '<h1>Hello World!</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """A view function that displays a personalized greeting."""
    if name:
        return f"<h1>Hello {name}!</h1>"
    else:
        return "<h1>Hello!</h1>"

@app.route('/f/<float:celsius_value>')
def convert_fahren(celsius_value):
    """Receives the Celsius value from the URL and returns the converted Fahrenheit value."""
    fahrenheit = convert_celsius_to_fahrenheit(celsius_value)
    return f"<h1>{celsius_value}°C is {fahrenheit:.2f}°F</h1>"

if __name__ == '__main__':
    app.run()