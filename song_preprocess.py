import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
# os.chdir('...')  # replace with your work path
os.chdir('D:/Kaggle/reco_music/data')


# read & process songs
songs = pd.read_csv('songs_with_complete_genre.csv')
songs['language'].fillna(31, inplace=True)  # only one NaN, manually find its language
songs['composer'].fillna("no_composer", inplace=True)
songs['lyricist'].fillna("no_lyricist", inplace=True)  # over half without lyricist info


# process songs genre using one hot encoding
ids = songs['genre_ids']
splits = ids.apply(lambda x: x.split("|"))
# NOTE(zakizhou)
# this is for choosing subset of songs for testing algorithm, do not delete
# songs_subset = songs.iloc[2296295:2296312, [0, 1, 2]]
# songs_subset_genre_ids = songs_subset['genre_ids'].apply(lambda x: x.split("|"))

tolist = splits.values.tolist()
# get all ids, in unordered str
all_ids = list(set([item for sublist in tolist for item in sublist]))
# convert to unordered int
all_ids = map(int, all_ids)
# convert to ordered str
all_ids.sort()
all_ids = map(str, all_ids)

cv = CountVectorizer(vocabulary=all_ids, tokenizer=lambda x: x.split("|"))
genre_ids = cv.fit_transform(songs['genre_ids'])

one_hot = genre_ids.toarray()
one_hot_df = pd.DataFrame(one_hot, columns=all_ids)
songs_with_genre_encoding = pd.concat([songs, one_hot_df], axis=1)
songs_with_genre_encoding.drop("genre_ids", axis=1, inplace=True)

songs_with_genre_encoding.to_csv("songs_processed.csv", index=False, sep=',')
'''
# as a ref, manually find the language corresponding to each number 
language = {52: "English", -1:"pure_music", 3:"Chinese", 17:"Japanese",
            24: " Cantonese", 31: "Korean", 10:"Chinese", 45:"Dai language"
            59:"Chinese", 38:"baby_song"}
'''