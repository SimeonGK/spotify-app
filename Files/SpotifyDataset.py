# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:55:00 2021

@author: bnkoz
"""

"Software development"

import pandas as pd
import numpy as np
import seaborn as sns
import os, sys
import matplotlib.pyplot as plt
sns.set(color_codes=True)


df = pd.read_csv('C:/Users/bnkoz/AppData/Local/GitHubDesktop/app-2.9.3/spotify-app/Files/spotify_dataset.csv')
df = df.iloc[:500]



selection = df.iloc[:500,:2]
selection.columns = ['X', 'y']
#print(df['Highest Charting Position'])

print('Choose one of the options you would like to compare:')
for chooseCol in df.columns:
        print(chooseCol)
colInput1 = input()
print('And:/n')
colInput2 = input()



print(df[[colInput1, colInput2]].corr)

plt.scatter(df[colInput1], df[colInput2], marker='o')
plt.xlabel([0, 100])
plt.show()



#spfy = FirstPart['Highest Charting Position']
#spfy2 = FirstPart['Valence']
#print("Highest Charting Position", spfy, "Valence", spfy2)
#print(spfy, spfy2)
#plt.plot(spfy, spfy2, color='red', scalex=True, scaley=True)
#plt.show()