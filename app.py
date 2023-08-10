import openai
from flask import Flask, jsonify
from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
import gpt
import yelp
import UserRepository

app = Flask(__name__)

allUsers = UserRepository.AllCurrentUsers()
user1 = UserRepository.User("Aali", "20", "singing, drawing, watching tv, playing video games", "chinese", "halal")
user2 = UserRepository.User("Huz", "17", "Singing, driving, cooking, art", "Thai", "halal")
user3 = UserRepository.User("Hanz", "23", "Cycling, Rock Climbing, watching movies, painting", "Mederteranian", "None")
allUsers.addUser(user1)
allUsers.addUser(user2)
allUsers.addUser(user3)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/getActivity")
def activity():
   mood = "exiting day out"
   print(allUsers.toString(mood))
   if mood != "food":
        term = True
        if(term):
            resp = gpt.gpt_response(f'suggest one generic activity that all of these user will enojoy doing together and keep their ages in mind. The users are in the mood for {mood} {allUsers.toString(mood)}. Give the response as the generic search term to use for a yelp search do not include anything else in the response')
        else:
            resp = ""
        resp += f'. For ages {allUsers.youngest()} and up'
        catagories = gpt.gpt_response(f'Give me a list of catgories that all of these users might enjoy doing together. Give the response in the format [category1, catgory2,...] limit the number of items to 5 ')
   print(catagories)
   print(resp)
   acts = yelp.get_locations(resp,'plano', catagories)
   return jsonify(acts)



if __name__ == '__main__':
    app.run(debug=True, port=8003)
    