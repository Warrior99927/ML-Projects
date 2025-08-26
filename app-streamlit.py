import streamlit as st
st.title("Simple Streamlit App")
st.sidebar.header("User Input")

# Input from user
name = st.sidebar.text_input("Enter your name:", "Anjali")
age = st.sidebar.slider("Select your age:", 1, 100, 25)

if st.sidebar.button("Greet Me"):
    st.success(f"Hello, {name}! You are {age} years old.")

# Image
st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)

# Markdown
st.markdown("## Features")
st.markdown("- Easy user input via sidebar")
st.markdown("- Real-time interaction")
st.markdown("- Great for dashboards, ML apps, and data visualization")