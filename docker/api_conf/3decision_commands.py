from api_python_3decision import api

# Structure endpoints:

response = api.get_structure('1uyd')
print(response.text)
