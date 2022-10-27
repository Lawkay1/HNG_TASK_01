from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
#app.config['JSON_SORT_KEYS']=False
@app.route('/')
def get_slack():
    slackUsername = 'ibukun Lawson'
    age = int(25)
    backend = True
    bio = 'I am an highly dedicated software engineer. Scaling leaps and bounds is my second nature'

    data = {
        'slackUserName': slackUsername,
        'backend': backend,
        'age': age,
        'bio': bio,




    }

    return json.dumps(data), 200
