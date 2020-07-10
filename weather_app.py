from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os

import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

api_key = '9544da1b5b36a32fd74c1b155da84715'


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_max = json['main']['temp_max']
        temp_min = json['main']['temp_min']
        temp_h = (temp_max - 273.15)
        temp_l = (temp_min - 273.15)
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        humid = json['main']['humidity']
        desc = json['weather'][0]['description']
        final = (city, country, temp_h, temp_l, icon, weather, humid, desc)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = 'City: {}'.format(weather[0])
        location_lbl1['text'] = 'Country: {}'.format(weather[1])
        temp_lbl['text'] = 'Temperature:   Max: {:.2f}°C;  Min: {:.2f}°C'.format(weather[2], weather[3])
        weather_lbl['text'] = 'Weather: {}'.format(weather[5])
        humid_lbl['text'] = 'Humidity: {}%'.format(weather[6])
        desc_lbl['text'] = 'Description: {}'.format(weather[7])
    #    panel.config(image='')
        i = 'weather_icons/' + weather[4] + '.png'
        img = Image.open(i)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(app, image=img)
        panel.image = img
        #panel.place(relwidth=1, relheight=1)
        panel.pack()
    else:
        messagebox.showerror('Error.', 'Cannot find city {}'.format(city))


app = Tk()
app.title("Weather App")
app.geometry('700x350')

#canvas = Canvas(app,height=350, width=700)
#canvas.pack()

#background_image = PhotoImage(file=r"C:\Users\91700\Downloads\bg.png")
#background_label = Label(image=background_image)
#background_label.place(relwidth=1, relheight=1)


city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search Weather', width=12, command=search, bg='lightblue')
search_btn.pack()

location_lbl = Label(app, text='', font=('bold', 20))
location_lbl.pack()

location_lbl1 = Label(app, text='', font=('bold', 20))
location_lbl1.pack()

temp_lbl = Label(app, text='')
temp_lbl.pack()

humid_lbl = Label(app, text='')
humid_lbl.pack()

weather_lbl = Label(app, text='')
weather_lbl.pack()

desc_lbl = Label(app, text='')
desc_lbl.pack()

#global panel
#icon= Label(app, image = None)

app.mainloop()
