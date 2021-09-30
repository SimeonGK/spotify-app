# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:55:00 2021

@author: bnkoz
"""

"Software development"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('spotify_dataset.csv')
df.head()

CorA = ['Highest Charting Position', 'Valence']
FirstPart = df.iloc[:500,:]
SecondPart = df.iloc[500:,:]
spfy = FirstPart['Highest Charting Position']
spfy2 = FirstPart['Valence']
print("Highest Charting Position", spfy, "Valence", spfy2)
plt.plot(spfy, spfy2, color='red', scalex=True, scaley=True)

plt.show()