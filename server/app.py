from cv2 import VideoCapture
from flask import Flask, request
from flask_cors import CORS, cross_origin
import urllib.request, json
import random
import cv2 as cv
import load_model_and_predict
import chat_model

app = Flask(__name__)
CORS(app)

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



@app.route("/")
def main():
    try:
        input = get_args(request, ['input'])
        if(not input[0].isdigit()):
            bot_input = chat_model.answer(input[0])
            print(bot_input)
            return bot_input
        else:
            raise Exception("Need to send only words or sentences")
    except Exception as e:
        print(e)
        return "An error has occured, please try again"

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
            bot_output = chat_model.answer(emotion_result)
            print(bot_output)
            return bot_output
        else:
            return "Error in loading something"
    except Exception as e:
        return e

if __name__ == '__main__':
    print("Running")
    try:
        app.run(port=5000, host='0.0.0.0')
    except:
        print("Problem ")