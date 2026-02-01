import streamlit as st

st.title("text input")

name=st.text_input("enter your name")

age=st.slider("select your age",0,100,25)

st.write(f"your age is ",{age})

if name:
    st.write(f"hello ,{name}")