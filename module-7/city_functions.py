"""
Jessie Miers
CSD325 
Module 7.2

This program was modified each time to add if statement that would 
allow it to pass the test used in test_cities.py. 
First only City and Country would pass the test, causing it to fail the 
test given in test_cities.py. Conditions were a added to allow each parameter
to be opitional after failing the test. 

"""

def city_country_function(city,country,language=None,population=None):
    #Return if popluation and language are provided.
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    #Return if population is provided.
    if population:
       return f"{city}, {country} - population {population}" 
    else:
        #Return original format, if only city and country are provided. 
        return f"{city}, {country}"
      
if __name__ == "__main__":
    
    #print(city_country_function("Tulsa", "United States" ,population=411894,language="English"))
    #print(city_country_function("Tokyo", "Japan", population=14180000, language="Japanese"))
    #print(city_country_function("Paris", "France", population= 2048472,language="French"))

    print(city_country_function("Tulsa", "United States"))
    print(city_country_function("Tokyo", "Japan", population=14180000))
    print(city_country_function("Paris", "France", population= 2048472,language="French"))