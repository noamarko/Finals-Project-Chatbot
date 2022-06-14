# Check out the README file before


# model
import time
import torch
import torch.nn as nn
import torchvision.models as models

# image
import numpy as np
import cv2 as cv
import albumentations as A
from albumentations.pytorch import ToTensorV2


NUM_OF_CLASSES = 7
model = models.resnext50_32x4d(pretrained=True)
dim_in = model.fc.in_features
model.fc = nn.Linear(dim_in, NUM_OF_CLASSES)
optimizer = torch.optim.Adam(model.parameters(), lr = 5e-5)
Emotions = ['disgust', 'happy', 'fear', 'angry', 'sad', 'surprise', 'neutral']
# print(model)
def load_model(path, model, optimizer):
    checkpoint = torch.load(path)
    model.load_state_dict(checkpoint['model_state_dict'])
    # optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    # epoch = checkpoint['epoch']
    # loss = checkpoint['loss']
    # return epoch, loss

# path to the model
# CHANGE TO YOUR PATH
MODEL_PATH = "C:/Users/noama/Desktop/GitHub/Finals-Project-Chatbot/server/best_model_cpu"


# MODEL_PATH = "C:/Users/noama/Desktop/GitHub/Finals-Project-Chatbot/server/best_model_cpu"

load_model(MODEL_PATH, model, optimizer)

# Loading image and predict

IMG_SIZE = 256
test_transform = A.Compose([
        A.Normalize(
              mean=[0.485, 0.456, 0.406],
              std=[0.229, 0.224, 0.225],
        ),
        ToTensorV2(),
])

# CHANGE TO YOUR PATH
def load_and_predict():
    img_path = "C:/Users/noama/Desktop/GitHub/Finals-Project-Chatbot/server/myImage.jpeg"
    # img_path = "C:/Users/noama/Desktop/GitHub/Finals-Project-Chatbot/server/myImage.jpeg"
    # read img
    img = cv.imread(img_path) 
    # resize
    img = cv.resize(img, (IMG_SIZE, IMG_SIZE))
    # required transformations
    img = test_transform(image = img)['image']
    # predicting
    # adding new axis, because the model waiting for 4 dim input
    output = model(img[np.newaxis, :, :])
    # applying softmax to get the probabilities
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    emotion = Emotions[np.argmax(probabilities.detach().numpy())]
    return emotion






