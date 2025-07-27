"""
Jessie Miers
7-26-25
Module 9.2

This program is based off the tutorial for APIs
modified to run a different API. Pulls a random fact
and outputs the raw API JSON and then cleanly prints the fact.
"""


import requests

#API url
url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

#API request
response = requests.get(url)

#Connect test results
print(response.status_code)

#Raw output of API
print(response.json())

#Prints JSON Structure 
import json

#Create a formatted string of the Python JSON object
def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

jprint(response.json())

#Clean Output for Fact
fact_output = response.json()
print(f"\n***Random Fact***\n{fact_output['text']}")