import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

# Titles & Headers
streamlit.title('My Parents New Healthy Dinner!') 

# Breakfast Menu 
streamlit.header('Breakfast Menu') 
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
