import requests
from random import choice

print("Cat fact:")

url = 'https://cat-fact.herokuapp.com/facts/'
response = requests.get(url)
response_dict = response.json()

fact = choice(response_dict)
cat_fact = fact['text']
print(cat_fact)