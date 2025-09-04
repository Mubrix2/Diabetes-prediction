import streamlit as st
import requests

API_URL = 'http://localhost:8000/predict'

st.title('Diabetics Prediction Model App')

st.subheader('Enter your details below')

Pregnancies = st.number_input('How many pregnancies have the patient gone through')
Glucose = st.number_input("What's your glucose level as tested")
BloodPressure = st.number_input("Enter your blood pressure as tested")
SkinThickness = st.number_input("Enter your skin thickness")
Insulin = st.number_input('Enter your insulin level')
BMI = st.number_input("Enter your BMI")
DiabetesPedigreeFunction = st.number_input("Enter your Diabetes Pedigree function")
Age = st.number_input("Enter your age")

if st.button("Predict"):
  input_data = {
    'Pregnancies': Pregnancies,
    'Glucose': Glucose,
    'BloodPressure': BloodPressure,
    'SkinThickness': SkinThickness,
    'Insulin': Insulin,
    'BMI': BMI,
    'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
    'Age': Age
  }

  try:
    responses = requests.post(API_URL, json=input_data)
    if responses.status_code == 200:
      result = responses.json()
      st.success(f'The patient is {result['message']}')
    else:
      st.error(f'API error: {responses.status_code} - {responses.text}')
  except requests.exceptions.ConnectionError:
    st.error('Could not connect to API server. Make sure it is connected to the localhost 8000')