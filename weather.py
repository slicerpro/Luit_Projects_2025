import pip._vendor.requests as r

url = 'http://api.weatherapi.com/v1/current.json?key=6745300ce17048c48bd42826252404&q=olathe&aqi=no+city'

response = r.get(url)

weather_json= response.json()

print(weather_json)

temp = weather_json.get('current').get('temp_f')

print(temp)
description = weather_json.get('current').get('condition').get('text')


