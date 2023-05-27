import pickle
import numpy as np
import streamlit as st

loaded_model = pickle.load(open('Diabetes_model.sav', 'rb'))
st.title("Web App")

# Getting input data
Gender = st.text_input("Gender(m/f)")
age = st.text_input("Age of the patient")
cigsPerDay = st.text_input("No. of cigarettes smoked on average in one day.")
BPMeds = st.text_input("If the patient was on blood pressure medication (yes:1, no:0).")
prevalentHyp = st.text_input("If  the patient was hypertensive (yes:1, no:0).")
diabetes = st.text_input("If the patient had diabetes (yes:1, no:0).")
totChol = st.text_input("Total Cholesterol Level")
sysBP = st.text_input("systolic blood pressure")
BMI = st.text_input("Body Mass Index")
heartRate = st.text_input("Heart Rate")
glucose = st.text_input("Glucose level")


if Gender == 'm':
    Gender = 1
else:
    Gender = 0

input_data =  [Gender, age, cigsPerDay, BPMeds, prevalentHyp, diabetes, totChol, sysBP, BMI,heartRate, glucose]
input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

if st.button("predict"):
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0] == 0:
        st.write(prediction)
        st.write("The person has low risk of heart stroke.")
    else:
        st.write(prediction)
        st.write("The person has high risk of heart stroke.")