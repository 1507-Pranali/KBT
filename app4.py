import streamlit as st
st.title("chatbot")
s=st.text_input("ask me anything")
if st.button("send"):
    st.write("you asked",s)
    st.write("chatbot is processes i wil reply soon")