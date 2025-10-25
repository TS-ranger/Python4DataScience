import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")
age = st.slider("Select your age: ", 0, 100, 25)

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language: ", options)

data = {
    "Name": ["Tushar", "Sukanya", "Rohit", "Dhritiraj"],
    "Age": [22, 23, 21, 21],
    "Address": ["Bongaigaon", "Sarthebari", "Bongaigaon", "Guwahati"] 
}
df = pd.DataFrame(data)

uploaded_file = st.file_uploader("Choose a CSE file", type = "csv")

st.header("Output")

if name:
    st.write(f"Hello! {name}")

st.write(f"Your age is: {age}")
st.write(f"Your favorite language is: {choice}")
st.write(df)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)