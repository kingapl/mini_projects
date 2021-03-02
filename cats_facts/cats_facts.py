import requests
from random import choice


def get_cat_fact():
    url = 'https://cat-fact.herokuapp.com/facts/'
    response = requests.get(url)
    response_dict = response.json()

    fact = choice(response_dict)
    cat_fact = fact['text']
    
    return cat_fact


cat_fact = get_cat_fact()
print(f"Cat fact: {cat_fact}")