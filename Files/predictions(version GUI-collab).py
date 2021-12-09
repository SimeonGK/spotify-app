# %%
#import dependencies/libraries
import numpy as np
import pandas as pd
import plotly.express as px

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR

# %%
data = pd.read_csv('spotify_dataset.csv')

# %% [markdown]
# ## Preprocesing

# %%
drop_list = ['Index', 'Highest Charting Position', 'Number of Times Charted',
       'Week of Highest Charting', 'Song Name', 'Artist', 'Chord',
     'Song ID', 'Release Date', 'Weeks Charted', 'Genre', 'Popularity'
     ]
data = data.drop(drop_list,axis=1)

# %%
def object_to_numeric(df):
    df = df.copy()
    for i, column in enumerate(df.columns,start=1):
        df[column] = pd.to_numeric(df[column],errors = 'coerce')
    return df

# %%
data["Streams"] = data["Streams"].str.replace(',','').astype(np.float64)
data = object_to_numeric(data)
data = data.dropna()
data.info()

# %%
data.info()

# %% [markdown]
# Split and Scaling

# %%
y = data.loc[:,'Streams']

X = data.drop('Streams', axis=1)

# %%
scaler = StandardScaler()

X = scaler.fit_transform(X)

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=20)

# %% [markdown]
# Modeling and Training

# %%
lin_model = LinearRegression()


# %%
lin_model.fit(X_train, y_train)


# %%
lin_acc = lin_model.score(X_test, y_test)

# %%
print("Lin Accuracy:",lin_acc )


