# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 17:06:49 2025

@author: HP
"""

import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Load model and scaler
load = open('model.pkl', 'rb')
model = pickle.load(load)


def predict(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    prediction = model.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])
    return prediction

st.title("Titanic Survival Prediction")
st.write("Enter passenger details below:")
Pclass = st.selectbox("Ticket Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
Sex = st.selectbox("Sex", ['male', 'female'])
Age = st.slider("Age", 1, 100, 25)
SibSp = st.number_input("Siblings/Spouses aboard", 0, 10, 0)
Parch = st.number_input("Parents/Children aboard", 0, 10, 0)
Fare = st.number_input("Fare", 0.0, 600.0, 30.0)
Embarked = st.selectbox("Embarked", ['S', 'C', 'Q'])
    

# Encode categorical
Sex = 0 if Sex == 'male' else 1
Embarked = {'S': 2, 'C': 0, 'Q': 1}[Embarked]

    
if st.button('Predict'):
    result = predict(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
    if result==0:
        st.success("Survived")
    else:
        st.success("Did not Survived")
    
