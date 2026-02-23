import datetime

import streamlit as st
st.title("welcome to basic streamlit form")
f_name =st.text_input("enter your name")
l_name =st.text_input("enter your last_name")
date = st.date_input(
    "Select date",
    value=datetime.date(2005, 1, 1),
    min_value=datetime.date(2005, 1, 1),
    max_value=datetime.date(2030, 12, 31)
)
age =st.slider("select your age",1,100)
city =st.selectbox("select your city name:",["delhi","mumbai","nashik","pune"])

if st.button("show the details"):
    st.write("age",age)
    st.write("city",city)
    st.write("fname",f_name)
    st.write("lname",l_name)
    st.write("dob",date)
    
st.markdown("""
<style>
        .stButton > button
        {
            background-color:green;
            color:yellow;
            border-radius:50%;
        } 
        .stApp {
            background-color:yellow;
        }
       
</style>
""",unsafe_allow_html=True)
