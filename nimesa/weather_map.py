import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather(date):
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for forecast in data["list"]:
            if forecast["dt_txt"].startswith(date):
                temperature = forecast["main"]["temp"]
                print(f"Temperature on {forecast['dt_txt']}: {temperature} K")
                return
        print("No weather data available for the specified date.")
    else:
        print("Failed to retrieve weather data.")

def get_wind_speed(date):
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for forecast in data["list"]:
            if forecast["dt_txt"].startswith(date):
                wind_speed = forecast["wind"]["speed"]
                print(f"Wind Speed on {forecast['dt_txt']}: {wind_speed} m/s")
                return
        print("No weather data available for the specified date.")
    else:
        print("Failed to retrieve weather data.")

def get_pressure(date):
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for forecast in data["list"]:
            if forecast["dt_txt"].startswith(date):
                pressure = forecast["main"]["pressure"]
                print(f"Pressure on {forecast['dt_txt']}: {pressure} hPa")
                return
        print("No weather data available for the specified date.")
    else:
        print("Failed to retrieve weather data.")

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            get_weather(date)
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            get_wind_speed(date)
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            get_pressure(date)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
