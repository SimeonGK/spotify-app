import pandas as pd
import numpy as np
import seaborn as sns
import os, sys
import matplotlib.pyplot as plt
sns.set(color_codes=True)

"""
SpotifyApp class:
constructor input: filepath
cleans code
multiple prediction functions
"""
class SpotifyApp:
    
    #Load dataset into SpotifyApp and clean it
    def __init__(self, file) -> None:
        # load data set
        self.file = pd.read_csv(file)
        #load first 500 for developing
        self.file = self.file.iloc[:500]
        # clean data set
        self.data = self.file[['Index','Highest Charting Position','Streams','Artist Followers','Genre','Tempo','Duration (ms)' ]]
        self.data["Streams"] = self.data["Streams"].str.replace(',','').astype(np.float64)
        self.data["Artist Followers"] = pd.to_numeric(self.data["Artist Followers"],errors = 'coerce')
        self.data["Tempo"] = pd.to_numeric(self.data["Tempo"],errors = 'coerce')
        self.data["Duration (ms)"] = pd.to_numeric(self.data["Duration (ms)"],errors = 'coerce')
    
    def predict_streams(self, followers, tempo, duration):
        pass
    def predict_highest_chart(self, followers, tempo, duration, streams):
        pass

#create instance of SpotifyApp class app
app = SpotifyApp('spotify_dataset.csv')
print(app.data.info())