
import streamlit 
streamlit.title('my parents are beauty')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 kale,spinach & rocket smoothie')
streamlit.text('🐔hard-boiled free-range egg')
streamlit.text(' 🥑🍞avocado taste')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)





