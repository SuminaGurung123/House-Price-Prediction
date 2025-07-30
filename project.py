import streamlit as st
import pickle
import numpy as np

st.title("Fish species Predictor")

# Select model
model_choice = st.selectbox("Select Model", ["Baseline Model", "Fine-tuned Model"])

# Load selected model
model_path = "projectfish.pkl" if model_choice == "Baseline Model" else "projectfish2.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Inputs
weight = st.number_input("weight ")
Length1 = st.number_input("Length 1", step=1)
Length2  = st.number_input("Length 2", step=1)
Length3 = st.number_input("Length 3",  step=1)
Height = st.number_input("Height",  step=1)
Width = st.number_input("Width",  step=1)
# Predict
if st.button("Predict Species"):
    features = np.array([[weight,Length1,Length2,Length3,Height,Width]])
    prediction = model.predict(features)
    st.write(f"Predicted Species: {int(prediction[0])}")
    st.write("0=Bream 1=parkki  2=perch 3=pike 4=Roach 5=smelt 6=Whitefish")