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
# streamlit.dataframe(my_fruit_list)
# Customer choose fruits by name 
my_fruit_list = my_fruit_list.set_index('Fruit')

# Creating USER INTERACTION 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page
streamlit.dataframe(my_fruit_list)


# create the receptable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "fruit_choice")
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return streamlit.dataframe(fruityvice_normalized)

# New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
  
# don't run anything past here while we troubleshoot
streamlit.stop()

# Querying Our Trial Account Metadata
#streamlit.text("The fruit load list contains:")
# streamlit.dataframe(my_data_rows)
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# snowflake related functions 
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchone()
# Add a button 
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)



# Add a second entry box 
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit') 
streamlit.write('The user entered ', add_my_fruit)

# Will not work 
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
