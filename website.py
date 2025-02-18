import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



### Data flow and button ###
pressed = st.button("press me")
print('frist:', pressed)
pressed2 = st.button("press me again")
print('second:', pressed2)

## Text Element ###
st.title("My Website")  
st.header("Welcome to the website")
connect= st.subheader("Have you connected to your server")
if connect: 
    pressed = (st.button("Yes, _connect_"))
    print('frist:', pressed)
else: 
    pressed2 = (st.button("Not, _connect_"))
    print('frist:', pressed2)   
st.markdown("This is a _markdown_")
st.caption("small text")

code_example = """
def greet(name):
    print('hello', name)
"""

st.code(code_example, language='python')
st.divider()
st.image(os.path.join(os.getcwd(), "static", "A.jpg"))

## Data elements ###
st.sidebar.title("Sidebar")

st.title("Data Frame structure")
st.subheader("DataFrame")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie","David"],
    "Age": [25, 30, 28,24],
    "Occupation": ["Engineer", "Doctor", "Artist", "Chef"]
})
st.dataframe(df)
## Data editor section (Editable dataframe)
st.subheader("Data Editer")
edittable_df = st.data_editor(df)
print(edittable_df)

## static table section ###
st.subheader("Static Table")
st.table(df)

## Metrics section ###
st.subheader("Metrics")
st.metric(label= "Total Rows", value= len(df))
st.metric(label= "Average Age", value=round(df['Age'].mean(), 1))

##Json and Dictionary sections ###

st.subheader("Json and Dictionary")
simple_dict = {
    "name": "Abhishek Thasal",
    "age": 25,
    "Skill": ["Python","SQL","Data Science","Machine Learning",
              "Equty management","Portfolio mangement"]
}
st.write(simple_dict)

st.write("Dictionary view", simple_dict)

## CHART ELEMENT ###

st.title("Streamlit charts Demo")
# generate sample data
