import requests

class CityInfo():
    def get_city_name(self):
        city = input("Enter city to get info: ")
        # upper za svaku riječ
        city = city.strip().title()
        return city


    # dohvati info s apija
    def get_city_info(self, city:str):
        url_city = "https://en.wikipedia.org/api/rest_v1/page/summary/" + city
        city_info_response = requests.get(url_city).json()
        if city_info_response["cod"] != 200:
            print("Incorrect city name entered, couldn't find any information.")
            return None
        else:
            city_info = city_info_response["extract"]
            return city_info


    def get_city_temperature(self, city:str):
        API_key="147323e89fb4fafc5df25189348f23e7"
        url_vrijeme = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}"
        response_vrijeme = requests.get(url_vrijeme).json()
        if response_vrijeme["cod"] != 200:
            print("Incorrect city name entered, couldn't find any information.")
            return None
        else:
            current_temp = response_vrijeme["main"]["temp"]
            return current_temp


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
    if city_info and city_temperature:        
        ci.write_to_file(city_name, city_temperature, city_info)
