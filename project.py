import redis
import requests
import json
import pprint

# pp = pprint.PrettyPrinter()

# #setting up redis client for caching.
# redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# url = "https://zillow56.p.rapidapi.com/search"
# print(response.text)

# zillow_data = 'test_zillow_data.json'
# with open(zillow_data, 'r') as file_obj:
#     data = json.load(file_obj)

# #pp.pprint(data)
# #start server (redis-server)
# redis_client.set('zillow_data', json.dumps(data))
# zillow_data = redis_client.get('zillow_data')

# if zillow_data:
#     print('yes')
#     pp.pprint(zillow_data)
# else: 
#     pass
    # querystring = {"location":"ann arbor, mi"}

#   headers = {
# 	"X-RapidAPI-Key": api_key,
# 	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# zillow_data = 'test_zillow_data.json'
# with open(zillow_data, 'r') as file_obj:
#     data = json.load(file_obj)

# #pp.pprint(data)
# #start server (redis-server)
# redis_client.set('zillow_data', json.dumps(data))
# zillow_data = redis_client.get('zillow_data')

#------load data for json ------

#------ tree ----
# class Rental():
#     def __init__(self, address, bedrooms, bathrooms, log, lat, url, json=None ):
#         if json:
#             self.address = json.get('streetAddress')
#             self.bedroom = json.get('bedrooms')
#             self.bathroom = json.get('bathrooms')
#             self.log = json.get('longitude')
#             self.lat = json.get('latitude')
#         else:
#             self.address = address
#             self.bedroom = bedrooms
#             self.bathroom = bathrooms
#             self.log = log
#             self.lat = lat
#             self.url = url

