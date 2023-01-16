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
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please, select a fruit would you like to get information.")
  else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalize)
      
except URLError as e:
  streamlit.error()

# Display fruityvice api response
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# Display fruityvice api response
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# streamlit.write('The user entered ', fruit_choice)
# streamlit.text(fruityvice_response.json())


# write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized)
#streamlit.stop()
# Querying Our Trial Account Metadata
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("select * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.text("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

# add a second text Entry Box
#add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
#streamlit.write('The user entered ', add_my_fruit)
#streamlit.write('Thanks for adding', add_my_fruit)
#my_cur.execute("Insert into fruit_load_list values ('from streamlit')")
