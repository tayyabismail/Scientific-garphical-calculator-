import streamlit as st
import math

# Functions for the scientific calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def sqrt(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Streamlit app title
st.title("Scientific Calculator")

# Select operation
operation = st.selectbox(
    "Choose operation",
    ("Add", "Subtract", "Multiply", "Divide", "Square Root", "Power (x^y)", "Sine", "Cosine", "Tangent")
)

# For operations that require two numbers
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power (x^y)"]:
    num1 = st.number_input("Enter first number", format="%.2f")
    num2 = st.number_input("Enter second number", format="%.2f")

    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Power (x^y)":
            result = power(num1, num2)

        st.write(f"The result is: {result}")

# For square root (only requires one number)
elif operation == "Square Root":
    num = st.number_input("Enter the number", format="%.2f")

    if st.button("Calculate"):
        result = sqrt(num)
        st.write(f"The result is: {result}")

# For trigonometric functions (requires one angle in degrees)
elif operation in ["Sine", "Cosine", "Tangent"]:
    angle = st.number_input("Enter angle in degrees", format="%.2f")

    if st.button("Calculate"):
        if operation == "Sine":
            result = sine(angle)
        elif operation == "Cosine":
            result = cosine(angle)
        elif operation == "Tangent":
            result = tangent(angle)

        st.write(f"The result is: {result}")
