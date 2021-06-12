import requests

def get_weather_forcast_and_temp():
    apiKey = "dfd43713cf650e2f357ed4a4925afd8e"
    cityName="Chennai"
    Url ="http://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid="+apiKey+"&units=imperial"
    whether= requests.get(Url)
    json = whether.json()
    description = json.get("weather")[0].get("description")
    temp = json.get("main").get("temp_max") 
    return {"description":description,
            "temp":temp
           }

def main():
    wetherDetails=get_weather_forcast_and_temp()
    print("Todays Wheather in Chennai")
    print("Forcast : ",wetherDetails.get("description"))
    print("Temperature : ",wetherDetails.get("temp"),"*F")

main()
