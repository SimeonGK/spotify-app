from matplotlib.pyplot import step
from scipy.sparse import data
import streamlit as st
import locale
from main import *
from PIL import Image
from scipy import stats

image = Image.open('predictor.png')
st.image(image)

st.header(""" Welcome to the Spotify-app """)
st.write("""This app allows an artist or producer to predict the amount of streams they will get on a song \n
        The user has to input a few details about the song that they want to predict. These are:
        - Amount of followers the artist has
        - The tempo of the song
        - The duration of the song in ms""")

st.header("Input field")
st.write("We ask you input a few values. You need to know all of the following to make a prediction.")

#inputs
name_song = st.text_input('Here the name of the song:',)
followers = st.number_input('Amount of followers: (ex. 4953667)',step=1, value=4953667)
tempo = st.number_input('Tempo of the song: (ex. 142)',step=1, value=142)
duration = st.number_input('Duration of the song in ms.: (ex. 155453)',step=1, value=155453)

#def show_plot():
#    data


if st.button('Train model'):
    with st.spinner("Training ongoing"):
        app = SpotifyApp('spotify_dataset.csv')
        streams, datas = app.predict_streams(followers,tempo,duration)
        st.header(f'{name_song} will have an estimation of {round(streams[0])} streams!')
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        plt.xlabel('Streams')
        plt.ylabel('Artist Followers')
        plt.scatter(datas['Streams'], datas['Artist Followers'])
        st.write(fig)

    

#outputs: plot, than the evaluaded streams
#st.plotly_chart(SpotifyApp.data)


#confirming
#st.balloons()
#st.success('NICEEEE')
#print(kaas)