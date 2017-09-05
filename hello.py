from flask import Flask, flash, request, jsonify
from flask_cors import CORS

import random
import pickle

import datetime
import copy
app = Flask(__name__)

CORS(app)
app.config['DEBUG'] = False 

users = {}

@app.route('/')
def main():
   
    print(users)
    user = request.cookies.get('user')
    if not user in users:
       new = True
       user = str(random.random())
       users[user] = {"photoIds":[], "friends":[]}
    if random.random() > -1:
        print("saved")
      
        pickle.dump(users, open("users.pickle", "wb"))
    response = app.make_response(open("index.html", "r").read())
    response.set_cookie("user", value = user, expires = datetime.datetime(9999, 1, 1))
    return response

@app.route('/post', methods=['POST'])
def bet():
    user = request.cookies.get('user')
    if not user in users:
        return "derp"
    print(request.files)
    return "went well"

@app.route('/takepot')
def takepot():
    user = request.cookies.get('user')
    if not user in users:
        return "derp"
    
    game = pokergames[users[user]["gameId"]]
    oldstate = copy.deepcopy(game[-1])
    
    oldstate["money"][user] += oldstate["pot"]
    oldstate["pot"] = 0
    oldstate["actor"] = user
    

    game.append(oldstate)
    return "went well"




if __name__ == '__main__':

    app.run(host = "0.0.0.0", port = 8788)

