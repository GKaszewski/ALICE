"""
THIS FILE WILL BE CHANGED IN THE FUTURE.
FOR NOW THERE ARE SOME TESTING LINES. 
"""

from modules import uni_converter, weather, spotify, speech_recognition

print(str(uni_converter.feetsToMeters(6)) + ' m')
print(str(uni_converter.inchesToCentimeters(6)) + ' cm')

weather.get_weather('Gdansk')
