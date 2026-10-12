#pip install requestsz
import requests
import csv
import time

BASE_URL = "https://pokeapi.co/api/v2/pokemon?limit=10000"

response = requests.get(BASE_URL).json()
pokemon_list = response["results"]

data = []

for p in pokemon_list:
    url = p["url"]
    details = requests.get(url).json()
    
    name = details["name"]
    
    types = [t["type"]["name"] for t in details["types"]]
    types_str = ", ".join(types)
    
    speed = next(stat["base_stat"] for stat in details["stats"] if stat["stat"]["name"] == "speed")
    
    sprite = details["sprites"]["front_default"]
    
    data.append([name, types_str, speed, sprite])
    
    time.sleep(0.1)  # be nice to API

# Save to CSV
with open("C:/Users/chito/OneDrive/Desktop/Downloads/pokemon_dataset.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "types", "base_speed", "sprite"])
    writer.writerows(data)

print("Dataset created!")
