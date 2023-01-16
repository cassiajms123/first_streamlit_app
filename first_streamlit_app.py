import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
# streamlit.stop()


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


streamlit.title('My Parents New Healthy Dinner!') # adding an exlamation mark

streamlit.header('Breakfast Menu') 
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.title('🍌🥭 Build Your Own Fruit Smoothie')

