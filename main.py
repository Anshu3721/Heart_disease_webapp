import pickle
import numpy as np
import streamlit as st

loaded_model = pickle.load(open('Diabetes_model.sav', 'rb'))


def heart_disease_prediction(input_data):
    # input_data = (0, 47, 25, 0.00, 1, 1, 304.00, 102.24, 24.56, 97.45, 67.54)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # prediction = loaded_model.predict(input_data_reshaped)
    # print(prediction)
    #
    # if prediction[0] == 0:
    #     print('The person has low risk of heart stroke.')
    # else:
    #     print('The person has high risk of heart stroke.')

    return input_data_as_numpy_array


def main():
    # giving a title
    st.title("Heart Disease Prediction Web App")

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


    # Code for prediction
    diagnosis = ''

    # Creating a button for prediction
    if st.button("Result"):
        heart_disease_prediction(
            ['Gender', 'age', 'cigsPerDay', 'BPMeds', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'BMI',
             'heartRate', 'glucose'])

    st.success(diagnosis)


if __name__ == '__main__':
    main()
