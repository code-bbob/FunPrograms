#need to install requests module

import requests

def get_random_joke(category=None):
    url = "https://api.chucknorris.io/jokes/random"
    if category:
        url += f"?category={category}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        joke_data = response.json()
        return joke_data['value']
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

category = input("Enter a joke category (leave blank for any): ")
print(get_random_joke(category))
