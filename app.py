import streamlit as st
import joblib

vectorizer = joblib.load("vectorizer.joblib")
model = joblib.load("model.joblib")

st.title("Email Spam Detection")

input_sms = st.text_area("Enter Email Message")

if st.button("Predict"):

    transformed_sms = vectorizer.transform([input_sms])

    result = model.predict(transformed_sms)[0]

    if result == 1:
        st.success("Spam Email")
    else:
        st.success("Not Spam Email")