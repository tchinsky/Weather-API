# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:36:25 2019

@author: Tyler Chinsky

@description: API caller to accuweather.com to get weather based off
inputted zipcode. Returns many weather data points seen below.

"""
#import required modules
import requests, json

#Takes in the wanted zipcode and calls accuweather's API and returns the key
#value for that zipcode to be implemented in the forcast function
def getWeatherZip(zipcode,api_key):

    #postal_url variable to store url
    postal_url = "http://dataservice.accuweather.com/locations/v1/postalcodes/search?"

    #compiles various parts of the url from above into a complete url to request
    complete_postal_url = postal_url +"apikey="+api_key+"&q="+zipcode

    #get method of requests module
    #return postal_data object
    postal_data = requests.get(complete_postal_url)

    #json method of postal_data object
    #convert json format data into
    #python format data
    post = postal_data.json()

    #Return the location key for forcasting data request
    key = post[0]["Key"]

    return key

#Takes the key output from the zipcode function and outputs the weather after
#an API call to accuweather
def getForcastWeather(key,api_key):
    #forcast_url variable to store url
    forcast_url = "http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/"

    #compiles various parts of the url from above into a complete url to request
    complete_forcast_url = forcast_url+key+"?apikey="+api_key+"&details=true"

    #get method of requests module
    #return forcast_data object
    forcast_data = requests.get(complete_forcast_url)

    #json method of forcast_data object
    #convert json format data into python format data
    x = forcast_data.json()

    #store the weather_description and current_temp from corresponding keys in x
    weather_description = x[0]["IconPhrase"]
    current_temp = x[0]["Temperature"]["Value"]

    #store the wind_speed, wind_direction_deg, and wind_direction_eng
    #from corresponding keys in x
    wind_speed = x[0]["Wind"]["Speed"]["Value"]
    wind_direction_deg = x[0]["Wind"]["Direction"]["Degrees"]
    wind_direction_eng = x[0]["Wind"]["Direction"]["Localized"]

    #store the wind_gust from corresponding key in x
    wind_gust = x[0]["WindGust"]["Speed"]["Value"]

    #store the humidity from corresponding key in x
    humidity = x[0]["RelativeHumidity"]

    #store the visibility from corresponding key in x
    visibility = x[0]["Visibility"]["Value"]

    #store the precip_probability, rain_probability, snow_probability, and
    #ice_probability from corresponding key in x
    precip_probability = x[0]["PrecipitationProbability"]
    rain_probability = x[0]["RainProbability"]
    snow_probability = x[0]["SnowProbability"]
    ice_probability = x[0]["IceProbability"]

    #store the total_liquid from corresponding key in x
    total_liquid = x[0]["TotalLiquid"]["Value"]

    #store rain_level from corresponding key in x
    rain_level = x[0]["Rain"]["Value"]

    #store snow_level from corresponding key in x
    snow_level = x[0]["Snow"]["Value"]

    #store ice_level from corresponding key in x
    ice_level = x[0]["Ice"]["Value"]


    #print following values
    print("\nCurrent Weather:\n",weather_description,"\n")
    print("Temperature: ",current_temp," F\n")
    print("Wind Speed and Direction:\n",wind_speed," mph ",wind_direction_eng,
          "\n\n(",wind_direction_deg," degrees)\n\nGusting: ",wind_gust," mph\n")
    print("Humidity: ",humidity,"%\n")
    print("Precipitation Probabilities: \n\nOverall: ",precip_probability,"%\n")
    print("Rain Probability: ",rain_probability,"%\n")
    print("Snow Probability: ",snow_probability,"%\n")
    print("Ice Probability: ",ice_probability,"%\n")
    print("Total Precipitation Amounts: \n\nOverall: ",total_liquid," in\n")
    print("Rain: ",rain_level," in\n")
    print("Snow: ",snow_level," in\n")
    print("Ice: ",ice_level," in\n")
    print("Visibility: ",visibility," mi\n")



def main():
    #Enter your api key for accuweather here
    api_key = "***Enter API key here***"

    #Enter the zipcode you want weather for
    zipcode = input("Enter the city zipcode:\n")

    key = getWeatherZip(zipcode,api_key)
    getForcastWeather(key,api_key)
