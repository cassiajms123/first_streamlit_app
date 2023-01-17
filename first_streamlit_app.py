import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

# Titles & Headers
streamlit.title('My Parents New Healthy Dinner!') 

# Breakfast Menu 
streamlit.header('Breakfast Menu') 
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# IMPORTING DATA FROM A CSV PLACE IN AWS
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
# Customer choose fruits by name 
my_fruit_list = my_fruit_list.set_index('Fruit')

# Creating USER INTERACTION 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page
streamlit.dataframe(my_fruit_list)


# New section to display fruityvice api response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
