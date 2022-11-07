import requests
import os
from dotenv import load_dotenv

class CityInfo():
    def get_city_name(self):
        city = input("Enter city to get info: ")
        # upper za svaku riječ
        city = city.strip().title()
        return city


    # dohvati info s apija
    def get_city_info(self, city:str):
        url_city = f"https://en.wikipedia.org/api/rest_v1/page/summary/{city}"
        city_info_response = requests.get(url_city).json()
        if city_info_response["title"] == "Not found.":
            print("Incorrect city name entered, couldn't find any city information.")
            return {"code": 400}
        else:
            city_info = city_info_response["extract"]
            return {"code": 200, "info": city_info}


    def get_city_temperature(self, city:str): 
        load_dotenv()

        API_key = os.getenv('API_KEY')
        url_vrijeme = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}"
        response_vrijeme = requests.get(url_vrijeme).json()
        
        if response_vrijeme["cod"] == '404':
            print("Incorrect city name entered, couldn't find any weather information.")
            return {"code":response_vrijeme["cod"]}
        elif response_vrijeme["cod"] == 401:
            print("Invalid API key.")
            return {"code":response_vrijeme["cod"]}
        elif response_vrijeme["cod"] != 200:
            print("Error retrieving city weather info.")
            return {"code":response_vrijeme["cod"]}
        else:
            current_temp = response_vrijeme["main"]["temp"]
            return {"code": 200, "info": current_temp}


    def write_to_file(self, city:str, current_temp:int, city_info:str):
        # pisanje u datoteku
        recenica = f"Current temperature in {city} is {current_temp} degrees Celsius."
        with open(f"{city}", "w") as f:
            f.write(city_info + "\n")
            f.write(recenica)
            print("Writing to file successful")


if __name__ == "__main__":
    ci = CityInfo()
    city_name = ci.get_city_name()
    city_info = ci.get_city_info(city_name)
    city_temperature = ci.get_city_temperature(city_name)
    if city_info["code"] == 200 and city_temperature["code"] == 200:        
        ci.write_to_file(city_name, city_temperature["info"], city_info["info"])
    else:
        print("Not able to write data to file.")
