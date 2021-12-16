import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

submit=st.button('Scatter') #creating a submit button

if submit: #submit button needs tweaking doesnt work if an as in the selectbox has been chosen
    st.write(""" # My first app Hello *sheeesh*""")

    df = pd.read_csv("clean.csv") #get csv file
    st.title ('Scatter Plot') #tittle
    x_options = ['Artist Followers','Duration (ms)','Streams','Tempo'] #selectbox options
    x_axis = st.sidebar.selectbox('Select X-as', x_options)
    y_options = ['Artist Followers','Duration (ms)','Streams','Tempo']
    y_axis = st.sidebar.selectbox('Select Y-as', y_options,key="a")
    fig = px.scatter(df, 
                x=x_axis,
                y=y_axis,
                hover_name='Streams',
                title=f'{y_axis} compared to {x_axis}')
    #creating a scatter plot 
    st.plotly_chart(fig)
  

