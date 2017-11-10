# Notice: this file costs a big big amount of time(about two hours) !
# just contact me if you need "songs_with_complete_genre.csv"

import os
import pandas as pd
# os.chdir('...')  # replace with your work path
os.chdir('D:/Kaggle/reco_music/data')


# replace genre nulls with the most possible id (in songs)
def complete_songs_genre(df):
    df['genre_ids'].fillna(-1, inplace=True)
    artist_needed = list(set(df[df['genre_ids'] == -1]['artist_name']))
    most_genre = {}
    for artist in artist_needed:
        most_genre[artist] = df[df['artist_name'] == artist]['genre_ids'].value_counts().idxmax()
    for i in range(df.shape[0]):
        if df.iloc[i, 2] == -1:
            a = df.iloc[i, 3]
            df.iloc[i, 2] = most_genre[a]


songs = pd.read_csv("songs.csv")

complete_songs_genre(songs)

songs.to_csv("songs_with_complete_genre.csv", index=False, sep=',')
