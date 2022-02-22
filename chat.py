
import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from train import train
import random
import pickle

back_up = open("5220119712", 'a')

with open("intents1.json") as file:
    data1 = json.load(file)
    
with open("intents.json") as file:
    data = json.load(file)
    
if data['intents'] != data1['intents']:
    data1 = open("intents1.json", "w")
    json.dump(data, data1)
    train()

# load trained model
model = keras.models.load_model('chat_model')

    # load tokenizer object
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

    # load label encoder object
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

    # parameters
max_len = 20
    
    #basics intents 
basics = ["greeting", "How_are_you", "goodbye", "I_m_fine", "yes_you", "Flatterie", "insults","complaint", "help", "name", "about", "thanks", "T_es_con", "How_to_reserve"]
    

def predict_class(inp):
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    return tag    

def get_response(tag):
    if tag in basics: 
        for i in data['intents']:
            if i['tag'] == tag:
                return np.random.choice(i['responses'])
                                
    elif tag == "":
        for i in data['intents']:
            if i['tag'] == tag:
                break          
        return np.random.choice(i['responses'])