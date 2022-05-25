import folium
from geopy.geocoders import OpenCage
import os
import webbrowser

location_name = input("Enter name of location: ")


geolocator = OpenCage(api_key="07589c2cfabf4baea61c8085ec6108f5")
location = geolocator.geocode(location_name)

if location:
    latitude = location.latitude
    longitude = location.longitude
    clcoding = folium.Map(location=[latitude, longitude], zoom_start=12)

    marker = folium.Marker([latitude, longitude], popup=location_name)
    marker.add_to(clcoding)


    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    map_file = os.path.join(downloads_folder, "map.html")

    clcoding.save(map_file)
    print(f"Map has been saved to: {map_file}")
    webbrowser.open("file://" + map_file)
else:
    print("Location not found. Try again.")
