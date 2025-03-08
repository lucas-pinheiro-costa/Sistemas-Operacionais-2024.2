import requests

response = requests.get('http://servidor:8000')
print(response.text)
