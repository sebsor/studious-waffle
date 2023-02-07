# Fungerar inte av någon anledning
import requests

def get_weather_desc_and_temp() :
    api_key = "67da29cb91129f1a68c1c06c1be92daa"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&a"

    requests = requests.get(url)
    json = requests.json()

    description = json.get("weather") [0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description' : description, 
            'temp_min' : temp_min
            'temp_max' : temp_max}

def main() :
    weather_dict = get_weather_desc_and_temp()
    # Print the results
    print("Today's forecast is", weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'))
    print("The maximum temperature is", weather_dict.get('temp_max'))

main()

# import requests

# def get_weather():
# api_key = "<your api="" key="">"
# city = "<your city="">"
# state = "<your state's="" 3="" digit="" code="">"
# location = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + ","+ state + ",USA&limit=1&appid=" + api_key

# request = requests.get(location)
# ljson = request.json()

# jlat = ljson[0].get("lat")
# jlon = ljson[0].get("lon")

# url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(jlat) + "&lon=" + str(jlon) + "&appid=" + api_key + "&units=imperial"