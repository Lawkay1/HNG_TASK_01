from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)


@app.route('/')
def get_slack():
    slackUsername = 'ibukun Lawson'
    age = int(25)
    backend = True
    bio = 'I am an highly dedicated software engineer. Scaling leaps and bounds is my second nature'

    data = {
        'bio': bio,
        'backend': backend,
        'age': age,
        'slackUserName': slackUsername,

    }

    return jsonify(data), 200
