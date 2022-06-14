from cv2 import VideoCapture
from flask import Flask, request
from flask_cors import CORS, cross_origin
import urllib.request, json
import random
import cv2 as cv
import load_model_and_predict
import chat_model
import nltk
nltk.download('punkt')
app = Flask(__name__)
CORS(app)


# bot_convo = {"intents": [
#     {"tag": "greeting",
#      "patterns": ["Hi", "Hey", "Is anyone there?", "Hello", "Hay"],
#      "responses": ["Hello", "Hi", "Hi there"]
#     },
#     {"tag": "goodbye",
#      "patterns": ["Bye", "See you later", "Goodbye"],
#      "responses": ["See you later", "Have a nice day", "Bye! Come back again"]
#     },
#     {"tag": "how ",
#      "patterns": ["Thanks", "Thank you", "That's helpful", "Thanks for the help"],
#      "responses": ["Happy to help!", "Any time!", "My pleasure", "You're most welcome!"]
#     },
#     {"tag": "about",
#      "patterns": ["Who are you?", "What are you?", "Who you are?" ],
#      "responses": ["I.m Joana, your bot assistant", "I'm Joana, an Artificial Intelligent bot"]
#     },
#     {"tag": "name",
#     "patterns": ["what is your name", "what should I call you", "whats your name?"],
#     "responses": ["You can call me Joana.", "I'm Joana!", "Just call me as Joana"]
#     },
#     {"tag": "weather",
#     "patterns": ["How's the weather over there?", "What's the weather right now?", "Is the sun up yet?", "It's raining cats and dogs!"],
#     "responses": ["Tell me how can assist you", "Link to forecast sight", "Yes Sure, How can I support you"]
#     },
#     {"tag": "season",
#     "patterns": ["What is your favorite season", "Summer is the best", "Can't stand the rain", "I have so many allergies right now"],
#     "responses": ["Winter is the season I prefer", "I love the rain and snow", "I don't care, as long as I don't get rusty"]
#     },
#     {"tag": "complaint",
#     "patterns": ["have a complaint", "I want to raise a complaint", "there is a complaint about a service"],
#     "responses": ["Please provide us your complaint in order to assist you", "Please mention your complaint, we will reach you and sorry for any inconvenience caused"]
#     }
# ]
# }


def get_args(req, args):
    args_list = []
    print("getting args")
    for arg in args:
        args_list.append(req.args.get(arg))
    print("got all args")
    return args_list


def check_which_response_to_send(sentence):
    sentence = ' '.join(sentence)
    print(sentence)
    
    
    


# def check_input(input):
#     try:
#         # input_breakdown = nltk.sent_tokenize(input)
#         # response = check_which_response_to_send(input_breakdown)
#         length = len(bot_convo["intents"][0]['responses'])
#         print(length)
#         random_index = random.randint(0, length-1)
#         for greeting in bot_convo["intents"][0]['patterns']:
#             if greeting.lower() == input.lower():
#                 return bot_convo["intents"][0]['responses'][random_index]
#         for goodbye in bot_convo["intents"][1]['patterns']:
#             if goodbye.lower() == input.lower():
#                 return bot_convo["intents"][1]['responses'][random_index]
#     except Exception as e:
#         print(e) 


@app.route("/")
def main():
    try:
        input = get_args(request, ['input'])
        # bot_input = check_input(input[0])
        bot_input = chat_model.answer(input[0])
        # print(bot_input)
        return bot_input
            
    except Exception as e:
        print(e)
        return "Hello, World!"

@app.route('/analyze')
def analyze():
    print("Analyzing face reaction")
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

            return emotion_result #get_response(emotion_result)
        else:
            return "Error in loading something"
    except Exception as e:
        return e

def get_response(emotion):
    if emotion == 'sad':
        url = 'https://v2.jokeapi.dev/joke/Any?type=single'
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        # resp = "You look sad. maybe this will cheer you up:\n"
        # resp += dict['joke']
        return dict['joke'] #resp
    else:    
        return emotion


if __name__ == '__main__':
    print("Running")
    try:
        app.run(port=5000, host='0.0.0.0')
    except:
        print("Problem ")