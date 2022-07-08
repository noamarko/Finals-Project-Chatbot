import json 
import pickle
import numpy as np
from tensorflow import keras
# import keras

with open('C:/Users/noama/Desktop/GitHub/Finals-Project-Chatbot/server/models/chat_model/intents.json') as file:
    data = json.load(file)

# # Change the path to intents.json file
# with open('D:/Development/Final_Project_Chatbot/Finals-Project-Chatbot/server/models/chat_model/intents.json') as file:
    # data = json.load(file)

def load_model():
    # load trained model
    model = keras.models.load_model('C:/Users/noama/Desktop/GitHub/Finals-Project-Chatbot/server/models/chat_model/chat_model')
    # load tokenizer object 
    with open('C:/Users/noama/Desktop/GitHub/Finals-Project-Chatbot/server/models/chat_model/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    # Change the path to chat_model directory
    # model = keras.models.load_model('D:/Development/Final_Project_Chatbot/Finals-Project-Chatbot/server/models/chat_model/chat_model')

    # # Change the path to tokenizer.pickle file
    # # load tokenizer object
    # with open('D:/Development/Final_Project_Chatbot/Finals-Project-Chatbot/server/models/chat_model/tokenizer.pickle', 'rb') as handle:
    #     tokenizer = pickle.load(handle)

    # Change the path to label_encoder.pickle file
    # load label encoder object
    with open('C:/Users/noama/Desktop/GitHub/Finals-Project-Chatbot/server/models/chat_model/label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)
    
    return model, tokenizer, lbl_encoder

model, tokenizer, lbl_encoder = load_model()

def answer(inp):
    try:
        # parameters
        print(inp)
        max_len = 20
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                                truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])
        for i in data['intents']:
                if i['tag'] == tag:
                    return np.random.choice(i['responses'])
    except Exception as e:
        return str(e)

