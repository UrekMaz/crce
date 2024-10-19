import streamlit as st

# Title and description
st.title("Welcome to My Streamlit App")
st.write("This is a basic Streamlit app for demonstration purposes.")

# Input section
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=120)

# Button to display input
if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")

# Add a select box (dropdown)
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])

# Display the selected option
st.write(f"You selected: {option}")

# Add a slider
slider_value = st.slider("Select a value", 0, 100)
st.write(f"Slider value: {slider_value}")

# Add a checkbox
if st.checkbox("Check me"):
    st.write("Checkbox is checked!")
