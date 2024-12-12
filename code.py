import scipy;
import tkinter as tk
import requests
import time
def getWeather():
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=1cfbbb9271a529a0475c64be49b6688d"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] -273.15)
    min_temp = int(json_data['main']['temp_min'] -273.15)
    max_temp = int(json_data['main']['temp_max'] -273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) +"\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.config(bg='sky blue')
f = ("poppins", 15, "bold")
t = ("poppins", 30, "bold")
label3 = tk.Label(canvas,text='Enter city :',font=f,bg='sky blue')
label3.pack(pady=10)
textfield = tk.Entry(canvas, font = t)
textfield.pack(padx = 100)
B = tk.Button(canvas, text ="Search")
B.pack(pady=10)
B.config(command= getWeather)
label1 = tk.Label(canvas, font =t,bg='sky blue')
label1.pack()
label2 = tk.Label(canvas, font=f,bg='sky blue')
label2.pack()
canvas.mainloop()