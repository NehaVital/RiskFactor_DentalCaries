import numpy as np
import pickle
import streamlit as st


# Load the saved Random Forest Classifier model
loaded_model = pickle.load(open("C:/Users/preet/Downloads/trained_model_RFDC.sav",'rb'))

# Function to make predictions
def RFDC_Prediction(input_data):

    input_array = np.asarray(input_data)
    input_reshaped = input_array.reshape(1, -1)

    prediction = loaded_model.predict(input_reshaped)

    if prediction == 0:
        st.write("No Risk")
    else:
        st.write("There is a Risk")

# Streamlit app
def main():
    # Set the title and a short description for your app
    st.title("Dental Caries Risk Prediction")
    st.write("Enter the following information to predict the risk of dental caries.")

    # Input fields for various features
    age = st.text_input("Age")
    height_cm = st.text_input("Height (cm)")
    weight_kg = st.text_input("Weight (kg)")
    waist_cm = st.text_input("Waist (cm)")
    eyesight_right = st.text_input("Eyesight (right)")
    hearing_left = st.text_input("Hearing (left)")
    hearing_right = st.text_input("Hearing (right)")
    systolic = st.text_input("Systolic")
    relaxation = st.text_input("Relaxation")
    triglyceride = st.text_input("Triglyceride")
    hdl = st.text_input("HDL")
    hemoglobin = st.text_input("Hemoglobin")
    serum_creatinine = st.text_input("Serum Creatinine")
    ast = st.text_input("AST")
    alt = st.text_input("ALT")
    gtp = st.text_input("GTP")
    smoking = st.text_input("Smoking")

    # Create a list with the input data
    input_data = [age, height_cm, weight_kg, waist_cm, eyesight_right, hearing_left, hearing_right,
                  systolic, relaxation, triglyceride, hdl, hemoglobin,
                  serum_creatinine, ast, alt, gtp, smoking]

    prediction = ''
    # Predict the risk of dental caries
    if st.button("Predict"):
        prediction = RFDC_Prediction(input_data)
        

if __name__ == "__main__":
    main()
