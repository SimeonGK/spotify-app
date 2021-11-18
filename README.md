# spotify-app
This project is meant for the Software Development course of the 2nd year Bachelor students at Leiden university. This repository is for group 1

## Project Description
Dataset: Spotify_dataset.csv
Goal: making a product which has the following abilities:

Predicting streams with amount of subs/genre/release date
input genre - input subs - inputs release date
Predicting amount of subs with streams
Predicting how long tune will be on highest charts
Correlation of valence with release date and streams
Construct a modified chart list from given entries.

## Project Installation
To run the software, you need to install the following tools:
* Python
* pandas
* numpy
* matplotlib
* PyQt5

### (For developers:)

To load the needed tools automatically, run the project using virtual environemnt as the following steps:

#### For windows:
```
1. Set virtual environment (only once):
pip3 install virtualenv
python -m venv ./venv
2. Go to activate folder: (every time)
cd venv/Scripts
activate
3. Install the packages from requirements.txt
pip3 install -r Files/requirements.txt`
```
#### For Linux:
```
1. Set virtual environment (only once):
pip3 install virtualenv
virtualenv venv
source venv/bin/activate   (every time)
2. Install the packages from requirements.txt
pip3 install -r Files/requirements.txt
```
for new added packages, they can be added to requirements:

`pip3 freeze > requirements.txt`

### Run
To run the project:
1. Open project directory: 'Files' in your command line
2. Run the command: 
    * for windows: `python SpotifyDataset.py` 
    * for linux:   `python3 SpotifyDataset.py`
