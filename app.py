import streamlit as st

# Define calculator functions
def calculate(x, y, operation):
    if operation == "Add":
        return x + y
    elif operation == "Subtract":
        return x - y
    elif operation == "Multiply":
        return x * y
    elif operation == "Divide":
        return "Error! Division by zero." if y == 0 else x / y

# Streamlit UI
st.title("Simple Calculator")

# User inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)
operation = st.selectbox("Choose operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate and display result
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"The result is: {result}")
