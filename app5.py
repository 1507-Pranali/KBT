import streamlit as st
st.markdown("""
<style>
        .stButton > button
        {
            background-color:green;
            color:yellow;
            border-radius:50%;
        } 
</style>
""",unsafe_allow_html=True)












st.title("welcome to basic streamlit app")
name =st.text_input("enter your name")
age =st.slider("select your age",1,100)
city =st.selectbox("select your city name:",["delhi","mumbai","nashik","pune"])
if st.button("show the details"):
    st.write("age",age)
    st.write("city",city)
    st.write("name",name)
    
