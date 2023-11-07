'''
(c) 2023, Charles Ide
This application will create a webpage and display the weather in a sepcified city using the OpenWeatherMap API
'''
import requests
from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_city = request.form.get('city')
        
        if new_city:
            new_city_obj = City(name=new_city)

            db.session.add(new_city_obj)
            db.session.commit()

    #cities = City.query.all()
    cities = ['Boston', 'Las Vegas'] 

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b91b86148c8617a364e0f4e6ec2ca5b3'

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature_f' : int(r['main']['temp']),
            'temperature_c' : int((r['main']['temp'] - 32) / 1.8),
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(weather)


    return render_template('weather.html', weather_data=weather_data)

if __name__ =='__main__':
    app.run(debug=True)