from keras.models import Model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import load_model
import streamlit as st
import pickle

max_words = 1000
max_len = 150
model = load_model('model_1.joblib')

st.title('Spam or Ham')

sample_texts = st.text_input('Enter text you want to classify: ')

with open('kbest_feature.pickle', 'rb') as handle:
    tok = pickle.load(handle)

txts = tok.texts_to_sequences([sample_texts])
txts = pad_sequences(txts, maxlen=max_len)
preds = model.predict(txts)

if st.button('Predict'):
    if (result==0):
        sms = 'SMS Normal'
    elif (result==1):
        sms = 'SMS Fraud'
    else:
        sms = 'SMS Promo'