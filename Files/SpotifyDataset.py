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

class Spotifyapp:
    

    def initialize_column(self):
        print('Choose one of the options you would like to compare:')

        for columns in df.columns:
            print(columns)
        
        col_input_one = input()
        print('And:/n')
        col_input_two = input()
        
        return str(col_input_one), str(col_input_two)


x = Spotifyapp()
variable_one = x.initialize_column()

print(" x is ", variable_one)

