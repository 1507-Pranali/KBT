import streamlit as st 

st.title("basic calculator")

num1 = st.number_input("Enter first no:", step=1)
num2 = st.number_input("Enter second no:", step=1)


op = st.selectbox("choose operations",["add","sub","mul","div"])
if st.button("calculate"):
    if op == "add":
        st.write("you performed addition")
        st.write(num1 + num2)
    elif op == "sub":
        st.write("you performed subtraction")
        st.write(num1-num2)
    elif op == "mul":
        st.write("you performed multi")
        st.write(num1*num2)
    elif op == "div":
        if num2!=0:
            st.write(num1/num2)
        else:
            st.write("0 not alloowed")
    
    
