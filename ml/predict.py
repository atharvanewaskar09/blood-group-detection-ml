import cv2
import pickle
import numpy as np
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
IMAGE_SIZE = 64

with open(MODEL_PATH, "rb") as f:
    model, encoder = pickle.load(f)

def predict_blood_group(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
    img = img.flatten().reshape(1, -1)

    prediction = model.predict(img)[0]
    label = encoder.inverse_transform([prediction])[0]

    return label