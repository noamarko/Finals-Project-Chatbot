from importlib.metadata import requires
from inspect import getargs
from msilib.schema import Error
from cv2 import VideoCapture
from itsdangerous import base64_decode
import numpy as np
import pandas
from flask import Flask, request
from flask_cors import CORS, cross_origin
import random
from PIL import Image
from io import BytesIO
import torch
import torch.optim as optim
import cv2 as cv
import torchvision.models as models
import json
import time
import load_model_and_predict
from flask_socketio import SocketIO, emit
import threading
import sched
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)


bot_convo = {"intents": [
    {"tag": "greeting",
     "patterns": ["Hi", "Hey", "Is anyone there?", "Hello", "Hay"],
     "responses": ["Hello", "Hi", "Hi there"]
    },
    {"tag": "goodbye",
     "patterns": ["Bye", "See you later", "Goodbye"],
     "responses": ["See you later", "Have a nice day", "Bye! Come back again"]
    },
    {"tag": "thanks",
     "patterns": ["Thanks", "Thank you", "That's helpful", "Thanks for the help"],
     "responses": ["Happy to help!", "Any time!", "My pleasure", "You're most welcome!"]
    },
    {"tag": "about",
     "patterns": ["Who are you?", "What are you?", "Who you are?" ],
     "responses": ["I.m Joana, your bot assistant", "I'm Joana, an Artificial Intelligent bot"]
    },
    {"tag": "name",
    "patterns": ["what is your name", "what should I call you", "whats your name?"],
    "responses": ["You can call me Joana.", "I'm Joana!", "Just call me as Joana"]
    },
    {"tag": "help",
    "patterns": ["Could you help me?", "give me a hand please", "Can you help?", "What can you do for me?", "I need a support", "I need a help", "support me please"],
    "responses": ["Tell me how can assist you", "Tell me your problem to assist you", "Yes Sure, How can I support you"]
    },
    {"tag": "createaccount",
    "patterns": ["I need to create a new account", "how to open a new account", "I want to create an account", "can you create an account for me", "how to open a new account"],
    "responses": ["You can just easily create a new account from our web site", "Just go to our web site and follow the guidelines to create a new account"]
    },
    {"tag": "complaint",
    "patterns": ["have a complaint", "I want to raise a complaint", "there is a complaint about a service"],
    "responses": ["Please provide us your complaint in order to assist you", "Please mention your complaint, we will reach you and sorry for any inconvenience caused"]
    }
]
}


def get_args(req, args):
    args_list = []
    print("getting args")
    for arg in args:
        args_list.append(req.args.get(arg))
    print("got all args")
    return args_list

@app.route("/get_analysis")
@cross_origin()
def get_analysis():
    # image = get_args(request, ['image'])
    try:
        
        return "Got it"
    except Exception as e:
        return f"Falied due to {e}"


def check_input(input):
    try:
        length = len(bot_convo["intents"][0]['responses'])
        print(length)
        random_index = random.randint(0, length-1)
        for greeting in bot_convo["intents"][0]['patterns']:
            if greeting.lower() == input.lower():
                return bot_convo["intents"][0]['responses'][random_index]
        for goodbye in bot_convo["intents"][1]['patterns']:
            if goodbye.lower() == input.lower():
                return bot_convo["intents"][1]['responses'][random_index]
    except Exception as e:
        print(e) 


@app.route("/")
def main():
    try:
        input = get_args(request, ['input'])
        print(input)
        bot_input = check_input(input[0])
        print(bot_input)
        return bot_input
            
    except Exception as e:
        print(e)
        return "Hello, World!"

@app.route('/analyze')
def analyze():
    try:
        cam = VideoCapture(0)
        result, image = cam.read()
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faceCascade = cv.CascadeClassifier('./haarcascade_frontalface_default.xml')
        faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )
#     Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            face_only = image[y:y+h, x:x+w]

        if result:
            cv.imwrite("myImage.jpeg", face_only)
            emotion_result = load_model_and_predict.load_and_predict()
            return emotion_result
        else:
            print("Error in loading something")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print("Running")
    try:
        app.run(port=5000, host='0.0.0.0')
    except:
        print("Problem ")