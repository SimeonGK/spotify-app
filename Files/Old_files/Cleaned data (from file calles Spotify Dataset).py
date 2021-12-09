import pandas as pd
import numpy as np
import seaborn as sns
import os, sys
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/bnkoz/AppData/Local/GitHubDesktop/app-2.9.3/spotify-app/Files/spotify_dataset.csv')
df = df.iloc[:1000]
data_defin = df[['Index','Highest Charting Position','Streams','Artist Followers','Genre','Tempo','Duration (ms)' ]]

#data_defin["Streams"] = pd.to_numeric(data_defin["Streams"],errors = 'coerce')
data_defin["Streams"] = data_defin["Streams"].str.replace(',','').astype(np.float64)
data_defin["Artist Followers"] = pd.to_numeric(data_defin["Artist Followers"],errors = 'coerce')
data_defin["Tempo"] = pd.to_numeric(data_defin["Tempo"],errors = 'coerce')
data_defin["Duration (ms)"] = pd.to_numeric(data_defin["Duration (ms)"],errors = 'coerce')
print(data_defin.info())

#print('Choose one of the options you would like to compare:')
for chooseCol in data_defin.columns:
        print(chooseCol)
#colInput1 = input()
print('And:/n')
#colInput2 = input()
print(data_defin)

#print(data_defin.mean())
sns.regplot(x="Highest Charting Position", y="Streams", data=data_defin, fit_reg = False, scatter_kws={"alpha": 0.9})
sns.jointplot(x="Highest Charting Position", y="Streams", data=data_defin, kind = 'kde')