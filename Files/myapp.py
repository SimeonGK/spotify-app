from scipy.sparse import data
import streamlit as st
import locale
from main import *
from PIL import Image
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


image = Image.open('spotifypredictor.png')
st.image(image)

st.title(""" Welcome to the Spotify predictor """)
st.write("""  An artist or a producer can try this app to get a prediction of the amount of streams his song will get compared to the existing songs on Spotify.""")
st.write("""This app uses a prediction algtorithm based on a data set of spotify songs.
        To make a valid prediction we need a little bit information about the song:\n
        - Artist's number of followers on Spotify
        - Tempo of the song
        - Duration of the song in ms""")

st.header("Criterias")
st.write("Please give an input to all of the following:\n  ")
st.write("(The less information provided the less precise the prediction will be. So please try to answer all of the fields!)")
#inputs
name_song = st.text_input('Name of the song:',)
followers = st.number_input("Artist's number of followers: (ex. 4953667)",step=1, value=4953667)
tempo = st.number_input('Tempo of the song: (ex. 142)',step=1, value=142)
duration = st.number_input('Duration of the song in ms: (ex. 155453)',step=1, value=155453)
#def show_plot():
#    data
app = SpotifyApp('spotify_dataset.csv')

if st.button('Predict'):
    with st.spinner("Training ongoing"):
        streams, datas = app.predict_streams(followers,tempo,duration)
        st.header(f'Following our predicition algorithm we estimated that {name_song} will reach {round(streams[0])} streams!')
#plot
df = pd.read_csv("clean.csv") #get csv file
st.header ('Scatter Plot') #tittle
st.write('To get a better understanding of the prediction we have provided a scatterplot of the data set.  ')
st.write('The X and Y value can be changed using the selectboxes at the sidebar on the left.')
st.write('We have also provided a local regression line to help us see the relationship between the axes. ')
x_options = ['Artist Followers','Duration (ms)','Streams','Tempo'] #selectbox options
x_axis = st.sidebar.selectbox('Select X-as', x_options)
y_options = ['Streams','Duration (ms)','Artist Followers','Tempo']
y_axis = st.sidebar.selectbox('Select Y-as', y_options,key="a")
fig = px.scatter(df, 
        x=x_axis,
        y=y_axis,
        hover_name='Streams',
        title=f'{y_axis} compared to {x_axis}',
        color = "Tempo",
        trendline="lowess")
#creating a scatter plot 
st.plotly_chart(fig)

#outputs: plot, than the evaluaded streams
#st.plotly_chart(SpotifyApp.data)


#confirming
#st.balloons()
#st.success('NICEEEE')
#print(kaas)