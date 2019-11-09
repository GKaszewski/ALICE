#TODO: Do this today. (Metric to Imperial, Fahrenheit to Celsius and Kelvin to Celcius and vice-versa, same with Fahrenheit and Kelvin)
from unit_converter.converter import convert

def feetsToInches(feets):
    return convert(str(feets)+'foot' 'inch')

def feetsToMeters(feets):
    return convert(str(feets)+'foot', 'm')

def feetsToCentimeters(feets):
    return convert(str(feets)+'foot', 'cm')

def inchesToFeets(inches):
    return convert(str(inches)+'inch', 'foot')

def inchesToCentimeters(inches):
    return convert(str(inches)+'inch', 'cm')

def inchesToMeters(inches):
    return convert(str(inches)+'inch', 'm')