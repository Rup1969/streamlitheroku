import streamlit as st

st.title("Simple multiplication Table")

value1=st.number_input("Enter your first Number") 
value2=st.number_input("Enter your second Number")

st.text("The resultant number is")
st.write(value1*value2)

