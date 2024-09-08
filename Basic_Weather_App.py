from tkinter import *
import requests
import json

def get_weather_data(api_key, city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    weather_data = response.json()
    return weather_data

def show_weather():
    api_key = "d5dbcb664bda207f09eda9034baede4e"  # Replace with your OpenWeatherMap API key
    city = city_value.get()
    
    try:
        weather_data = get_weather_data(api_key, city)
        
        if weather_data["cod"] != "404":
            main_data = weather_data["main"]
            temperature = main_data["temp"]
            humidity = main_data["humidity"]
            weather_description = weather_data["weather"][0]["description"]
            
            weather_now = Label(root, text = "The Weather is: ", font = 'arial 12 bold').pack(pady=10)
            tfield = Text(root, width=46, height=10)
            tfield.pack()
            tfield.insert(INSERT, f"Weather in {city}:")
            tfield.insert(INSERT, f"\nTemperature: {temperature}°C")
            tfield.insert(INSERT, f"\nHumidity: {humidity}%")
            tfield.insert(INSERT, f"\nWeather Description: {weather_description}")
        else:
            weather_now = Label(root, text = "The Weather is: ", font = 'arial 12 bold').pack(pady=10)
            tfield = Text(root, width=46, height=10)
            tfield.pack()
            tfield.insert(INSERT, f"City not found. Please try again.")
    except requests.exceptions.RequestException as e:
        weather_now = Label(root, text = "The Weather is: ", font = 'arial 12 bold').pack(pady=10)
        tfield = Text(root, width=46, height=10)
        tfield.pack()
        tfield.insert(INSERT, f"An error occurred: {e}")
    except Exception as e:
        weather_now = Label(root, text = "The Weather is: ", font = 'arial 12 bold').pack(pady=10)
        tfield = Text(root, width=46, height=10)
        tfield.pack()
        tfield.insert(INSERT, f"An unexpected error occurred: {e}")

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Weather App - AskPython.com")

city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10)
city_value = StringVar()
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()

Button(root, command = show_weather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

root.mainloop()