# app.py
import streamlit as st
import pandas as pd
import numpy as np

st.title("Student Information") # Title of the app
student_name = st.text_input("Enter the student's name:") # Text input for student's name
student_age = st.slider("Select the student's age:", 1, 100) # Slider for student's age

df_age = pd.DataFrame({'âge': list(range(1, 11)),'second column': np.arange(10, 101, 10)})


# Button to display the input text and age
if st.button("Display Information"):
    st.write("Student's name: ", student_name)
    st.write("Student's age: ", student_age)
    if int(student_age) < 12:
        st.write(student_name, "un mensonge, pouvez-vous SVP saisir votre âge")
    st.write(df_age)