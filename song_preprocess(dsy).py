import os
import numpy as np
import pandas as pd
# os.chdir('...')  # replace with your work path
os.chdir('D:/Kaggle/reco_music/data')


# replace genre nulls with the most possible id (in songs)
def complete_songs_genre(df):
    artist_needed = list(set(df[df['genre_ids'] == -1]['artist_name']))
    most_genre = {}
    for artist in artist_needed:
        most_genre[artist] = df[df['artist_name'] == artist]['genre_ids'].value_counts().idxmax()
    for i in range(df.shape[0]):
        if df.iloc[i, 2] == -1:
            a = df.iloc[i, 3]
            df.iloc[i, 2] = most_genre[a]


# read & process songs
songs = pd.read_csv('songs.csv')
songs['language'].fillna(31, inplace=True)  # only one NaN, manually find its language
songs['composer'].fillna("no_composer", inplace=True)
songs['lyricist'].fillna("no_lyricist", inplace=True)  # over half without lyricist info

songs['genre_ids'].fillna(-1, inplace=True)
complete_songs_genre(songs)

'''
# as a ref, manually find the language corresponding to each number 
language = {52: "English", -1:"pure_music", 3:"Chinese", 17:"Japanese",
            24: " Cantonese", 31: "Korean", 10:"Chinese", 45:"Dai language"
            59:"Chinese", 38:"baby_song"}
'''