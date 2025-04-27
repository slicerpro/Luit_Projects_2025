import requests
import json

r = requests.get("http://api.open-notify.org/astros.json")
json = r.json()
for person in json['people']:
    print(person)


