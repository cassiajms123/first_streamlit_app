import streamlit
import pandas
import requests

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


streamlit.title('My Parents New Healthy Dinner!') # adding an exlamation mark

streamlit.header('Breakfast Menu') 
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.title('🍌🥭 Build Your Own Fruit Smoothie')

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page 
streamlit.dataframe(fruits_to_show)

# Display fruityvice api response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# Display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

# Display fruityvice api response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# Take the json version of the response and normalize it 
fruitvice_normalized = panda.json_normalized(fruityvice_response.json())

# Output it the screen as a table
streamlit.dataframe(fruityvice_normalized)


