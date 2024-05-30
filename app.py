# app.py
import streamlit as st

st.title("Student Information") # Title of the app
student_name = st.text_input("Enter the student's name:") # Text input for student's name
student_age = st.slider("Select the student's age:", 1, 100) # Slider for student's age

# Button to display the input text and age
if st.button("Display Information"):
    st.write("Student's name: ", student_name)
    st.write("Student's age: ", student_age)
    if int(student_age) < 12:
        st.write("un mensonge, pouvez-vous SVP saisir votre âge")