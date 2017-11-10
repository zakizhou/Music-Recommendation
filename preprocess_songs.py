import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import os

NAN_PLACEHOLDER = "-1"

os.chdir('/media/windows98/C212E4F512E4EEFB/Users/Windows98/kaggle')
songs = pd.read_csv('songs.csv')
ids = songs['genre_ids']
ids.fillna(value=NAN_PLACEHOLDER, inplace=True)


splits = ids.apply(lambda x: x.split("|"))

# NOTE(zakizhou)
# this is for choosing subset of songs for testing algorithm, do not delete
# songs_subset = songs.iloc[2296295:2296312, [0, 1, 2]]
# songs_subset_genre_ids = songs_subset['genre_ids'].apply(lambda x: x.split("|"))

tolist = splits.values.tolist()

# get all ids, in unordered str
all_ids = list(set([item for sublist in tolist for item in sublist]))
# convert to unorder int
all_ids = map(int, all_ids)
# convert to ordered str
all_ids.sort()
all_ids = map(str, all_ids)

cv = CountVectorizer(vocabulary=all_ids, tokenizer=lambda x: x.split("|"))
genre_ids = cv.fit_transform(songs['genre_ids'])

# TODO(zakizhou) genre_ids is a sparse matrix/features, should be combined with
# normal feature, see document or example for details.