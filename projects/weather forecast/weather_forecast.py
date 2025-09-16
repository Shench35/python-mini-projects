import customtkinter as ctk
import requests
from customtkinter import CTkLabel

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Weather App")

username_entry = ctk.CTkEntry(app , placeholder_text ="Enter the place here")
username_entry.pack(pady=20)

api_code = "876ab756797235e3c7a340462a6c7408"

def weather():
    place = username_entry.get()
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=5&appid={api_code}"

    try:
        response = requests.get(url, timeout=5)  # timeout helps avoid hanging
        response.raise_for_status()
    except requests.exceptions.RequestException:
        result_label.configure(text="No internet connection")
        return

    weather_data = response.json()
    if not weather_data:   # city not found
        result_label.configure(text="City not found")
        return

    x = weather_data[0]["lat"]
    y = weather_data[0]["lon"]

    url_1 = f'https://api.openweathermap.org/data/2.5/weather?lat={x}&lon={y}&appid={api_code}'
    try:
        response = requests.get(url_1, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        result_label.configure(text="No internet connection")
        return

    data = response.json()
    temp = round(data["main"]["temp"] - 273.15, 1)  # Kelvin → °C
    condition = data["weather"][0]["description"]
    result_label.configure(text=f"{place}: {temp}°C, {condition}")


check_button = ctk.CTkButton(app , text="Check", command=weather)
check_button.pack(pady=20)

result_label = CTkLabel(app , text="Result", font=("Arial", 18))
result_label.pack(pady=20)

app.mainloop()
