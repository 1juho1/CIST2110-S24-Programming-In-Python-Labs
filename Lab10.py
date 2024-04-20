# Lab 10
# Name: Justin Hoang

"""_summary_

This lab is designed to create a simple web application using streamlit and create a simple Date counter using datetime
"""

# 1. We will first need to active and install streamlit.
# pip install streamlit from within out venv

# 2. Import streamlit as st and datetime as dt
import streamlit as st
from datetime import datetime as dt

# 3. Create a title for your web application. Streamlit has a function for this called title
st.title("Date Counter")

# 4. Create a subheader for your web application. Streamlit has a function for this called subheader
st.subheader("This is a simple date counter")

# 5. Create a date input for the user to enter a date. Streamlit has a function for this called date_input
# make sure to store this date in a variable called date
date = st.date_input("Enter a Date")

# 6. Create a button for the user to Click. Streamlit has a function for this called button
# make sure to store this button in a variable called button
button = st.button("Calculate")

# 7. Create a function that will calculate the number of days until the date entered by the user.
# You will need to use the datetime module to get the current date and subtract the date entered by the user.
def calculate_days(target_date):
    try:
        today = dt.today().date()
        days_until = (target_date - today).days
        return days_until
    except Exception as e:
        st.error(f"Error: {e}")


# 8. Create a app function that will run the web application.
def app():
    if button:
        days_until = calculate_days(date)
        if days_until is not None:
            st.write(f"Days until {date}: {days_until}")
# Check if the button has been clicked, then call the calculate_days function and pass in the date entered by the user. Use a try except block to catch any errors.
# Save the result into a variable.
# Print out the result.


# 9. Run the web application by typing streamlit run Lab10.py in the terminal. Enter a date in the format of YYYY-MM-DD and click the button. Check to see if the number of days until the date entered is correct. If the number of days is correct, then you have completed the lab. If the number of days is incorrect, then you will need to debug your code.


if __name__ == "__main__":
    app()
