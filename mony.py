import warnings
warnings.filterwarnings('ignore')
import os  # Importing the os module for interacting with the operating system
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import logging
logging.getLogger('tensorflow').disabled = True
from tensorflow.keras.models import load_model # type: ignore
import os
import cv2
import tensorflow as tf
import numpy as np


model = load_model(os.path.join("models", "model.h5"))

def cash_detector(image_bytes):
    np_array = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    resize = tf.image.resize(img, (224, 224))  # Resize Image
    
    class_names = ['1' , '10' , '10 (new)' , '100' , '20' , '20 (new)' , '200' , '5' , '50']  # List of class names

    
    prediction = model.predict(np.expand_dims(resize, 0))
    predicted_label = np.argmax(prediction)
    predicted_class = class_names[predicted_label]  # Get the corresponding class name
    return predicted_class

