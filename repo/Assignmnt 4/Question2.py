import requests

def get_weather(city_name):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=9d58bb0b773b008e17834bb6f24413f7"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
    if data.get("cod") != 200:
        print(f"Error: {data.get('message')}")
        return None
    
    print(f"City: {data['name']}")
    print(f"Temperature: {(data['main']['temp']-273.15):.2f}C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f'Wind Speed :{data["wind"]["speed"]*3.6} km/h')
city = input("Enter city name: ")
get_weather(city)
print("Weather data fetched successfully.")