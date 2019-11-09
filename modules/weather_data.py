from datetime import datetime

class Weather():
    status = ''
    temperature = 0
    max_temperature = 0
    min_temperature = 0
    humidity = 0
    wind_speed = 0
    sunrise = 0
    sunset = 0

    def __init__(self, status = '', temperature = 0, max_temperature = 0, min_temperature = 0, humidity = 0, wind_speed = 0, sunrise = 0, sunset = 0):
        self.status = status
        self.temperature = temperature
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.sunrise = sunrise
        self.sunset = sunset

    def __str__(self):
        return status
    
    def timestampToDate(self, timestamp):
        return datetime.fromtimestamp(timestamp)

    def printData(self):
        print('Status: {}, \nTemp: {}, \nMax temp: {}, \nMin temp: {}, \nHumidity: {}, \nWind speed: {}, \nSunrise: {}, \nSunset: {}'.format(self.status, self.temperature, self.max_temperature, self.min_temperature, self.humidity, self.wind_speed, self.timestampToDate(self.sunrise), self.timestampToDate(self.sunset)))