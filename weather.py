import requests
import json

def get_weather(city):
	api_key = "e677d98fa74c8df1e3c57d849436e76c"
	base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
	
	response = requests.get(base_url)
	data = json.loads(response.text)

	if data["cod"] == "404":
		print("Not Found A City")
	else:
		try:
			main_data = data["main"]
			temperature = main_data["temp"]
			humidity = main_data["humidity"]
			description = data["weather"][0]["description"]
   
			temperature = int((temperature - 273.15) * 9/5 + 32)

			print(f"Weather in {city}:")
			print(f"Temperature: {temperature} F")
			print(f"Humidity: {humidity}%")
			print(f"Description: {description}")
		except KeyError:
			print("Invalid response from the weather API.")

city_name = input("Enter City Name: ")
get_weather(city_name)
