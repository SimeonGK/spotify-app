from matplotlib.pyplot import step
from scipy.sparse import data
import streamlit as st
import locale
from main import *
from PIL import Image
from scipy import stats

app = SpotifyApp('spotify_dataset.csv')
streams, datas = app.predict_streams(4953667.0,142.169,155453.0)

datas = datas.iloc(['Highest Charting Position','Index', 'Genre'])
print(datas)
z_scores = stats.zscore(datas)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all
datas = datas[filtered_entries]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.xlabel('Streams')
plt.ylabel('Artist Followers')
plt.scatter(datas['Streams'], datas['Artist Followers'])
st.write(fig)