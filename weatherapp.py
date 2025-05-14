from tkinter import *
from tkinter import ttk
import urllib.request
import json


def get_weather():
    city = city_name.get()
    if not city:
        return

    api_key = "06cb784d0db003e738f4de1026391216"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            w_label1.config(text=data["weather"][0]["main"])
            wd_label1.config(text=data["weather"][0]["description"])
            temp_celsius = data["main"]["temp"] - 273.15
            temp_label1.config(text=f"{temp_celsius:.2f} °C")
            P_label1.config(text=f"{data['main']['pressure']} hPa")
    except:
        w_label1.config(text="N/A")
        wd_label1.config(text="N/A")
        temp_label1.config(text="N/A")
        P_label1.config(text="N/A")


# GUI setup
win = Tk()
win.title("WEATHER APP")
win.config(bg="green")
win.geometry("500x500")

name_label = Label(win, text="Weather App", font=("Times New Roman", 30, "bold"), bg="green", fg="white")
name_label.place(x=25, y=20, height=50, width=450)

city_name = StringVar()
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
    "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
    "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh",
    "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"
]

com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 14), state="readonly", textvariable=city_name)
com.place(x=25, y=90, height=40, width=450)

label_width = 200
value_width = 250

w_label = Label(win, text="Weather Climate:", font=("Times New Roman", 14), bg="green", fg="white")
w_label.place(x=25, y=210, height=30, width=label_width)
w_label1 = Label(win, text="", font=("Times New Roman", 14), bg="white", fg="green")
w_label1.place(x=230, y=210, height=30, width=value_width)

wd_label = Label(win, text="Weather Desc:", font=("Times New Roman", 14), bg="green", fg="white")
wd_label.place(x=25, y=250, height=30, width=label_width)
wd_label1 = Label(win, text="", font=("Times New Roman", 14), bg="white", fg="green")
wd_label1.place(x=230, y=250, height=30, width=value_width)

temp_label = Label(win, text="Temperature:", font=("Times New Roman", 14), bg="green", fg="white")
temp_label.place(x=25, y=290, height=30, width=label_width)
temp_label1 = Label(win, text="", font=("Times New Roman", 14), bg="white", fg="green")
temp_label1.place(x=230, y=290, height=30, width=value_width)

P_label = Label(win, text="Pressure:", font=("Times New Roman", 14), bg="green", fg="white")
P_label.place(x=25, y=330, height=30, width=label_width)
P_label1 = Label(win, text="", font=("Times New Roman", 14), bg="white", fg="green")
P_label1.place(x=230, y=330, height=30, width=value_width)

done_button = Button(win, text="Done", font=("Times New Roman", 16, "bold"), command=get_weather)
done_button.place(x=200, y=150, height=40, width=100)

win.mainloop()
