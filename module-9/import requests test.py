import requests
response = requests.get('https://uselessfacts.jsph.pl/')

print(response.status_code)