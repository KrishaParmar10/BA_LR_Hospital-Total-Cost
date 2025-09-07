import streamlit as st 
import pickle 
import numpy as np 

# Load the saved model 
model = pickle.load(open('linear_reg.sav', 'rb')) 
st.title('Hospital Total Cost Prediction App') 

# Input features 
TOTAL_AMOUNT_BILLED_TO_THE_PATIENT = st.number_input('TOTAL_AMOUNT_BILLED_TO_THE_PATIENT', min_value=0.0) 
CONCESSION = st.number_input('CONCESSION', min_value=0.0) 
ACTUAL_RECEIVABLE_AMOUNT = st.number_input('ACTUAL_RECEIVABLE_AMOUNT', min_value=0.0) 
TOTAL_LENGTH_OF_STAY = st.number_input('TOTAL_LENGTH_OF_STAY', min_value=0.0) 
LENGTH_OF_STAY_ICU = st.number_input('LENGTH_OF_STAY_ICU', min_value=0.0) 
LENGTH_OF_STAY_WARD = st.number_input('LENGTH_OF_STAY_WARD', min_value=0.0) 
COST_OF_IMPLANT = st.number_input('COST_OF_IMPLANT', min_value=0.0) 

# Make prediction 
if st.button('Predict Hospital Total Cost'): 
    input_data = np.array([[TOTAL_AMOUNT_BILLED_TO_THE_PATIENT, CONCESSION, ACTUAL_RECEIVABLE_AMOUNT, TOTAL_LENGTH_OF_STAY, LENGTH_OF_STAY_ICU, LENGTH_OF_STAY_WARD, COST_OF_IMPLANT]]) 
    prediction = model.predict(input_data)[0] 
    st.success(f'Predicted Hospital Cost: {prediction:.2f}')