"""
import csv

data =[
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

with open  ("data.csv", "w") as file:
    writer = csv.writer(file)

    for x in data:
        writer.writerow(x)

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(" | ".join(row))
        
try:
    n = int(input("Enter a number: "))
    y= 10 / n
    print("Result:", y)
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Operation completed successfully.")
finally:
    print("Execution finished.")

import requests


def get_weather(city_name):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=9d58bb0b773b008e17834bb6f24413f7"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
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
    


import sqlite3

conn = sqlite3.connect("db1.db")
# conn.execute('''CREATE TABLE IF NOT EXISTS 
#             users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                 name VARCHAR(100),
#                 pass VARCHAR(100)
#             )'''
#             )

conn.execute('INSERT INTO users VALUES (1,"Alice", "password123")')

import pywhatkit as pyw

pyw.sendwhatmsg("+1234567890", "Hello, this is a test message!", 17, 42)  # Sends a WhatsApp message at 17:42
"""