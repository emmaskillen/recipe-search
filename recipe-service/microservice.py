import json
from flask import Flask, jsonify
import requests
from requests.auth import HTTPBasicAuth
 
app = Flask(__name__)

# This function sends a parameters to microservice.py 

# cuisine, intolerances, diet, includeIngredients, excludeIngredients, type (meal type)
json_str = '{ "cuisine":"italian", "intolerances": "dairy", "diet":"Vegan", "includeIngredients":"wheat", "excludeIngredients":"butter", "type":"dinner"}'

@app.route("/")
def get_parameters():
    json_str = '{"cuisine":"italian", "intolerances": "dairy"}'
    parameter_dict = json.loads(json_str)
    
    headers = {
        'x-api-key': '23953f4c6a9f4412b033cebb01836514'
    }
    url = "https://api.spoonacular.com/recipes/complexSearch"
    
    recipes = requests.get(url, headers=headers, params=parameter_dict)
    recipes = recipes.json()    # turn into json object


    return recipes['results'][0]    # return first recipe


if __name__ == "__main__":
    app.run(port=8003)