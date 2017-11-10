import os
import numpy as np
import pandas as pd
import lightgbm as lgb
os.chdir('D:/Kaggle/reco_music/data')


train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
songs = pd.read_csv('songs_processed.csv')
members = pd.read_csv('members_processed.csv')
songs_extra = pd.read_csv('songs_extra_processed.csv')

train_merged = pd.merge(train, songs, on='song_id',how='left')
test_merged = pd.merge(test, songs, on='song_id', how='left')

train_merged = train_merged.merge(songs_extra, on='song_id', how='left')
test_merged = test_merged.merge(songs_extra, on='song_id', how='left')

train_merged = train_merged.merge(members, on='msno', how='left')
test_merged = test_merged.merge(members, on='msno', how='left')

train_merged.drop('name', axis=1, inplace=True)
test_merged.drop('name', axis=1, inplace=True)


def check_missing_values(df):
    print (df.isnull().values.any())
    if (df.isnull().values.any() == True):
        columns_with_Nan = df.columns[df.isnull().any()].tolist()
    print(columns_with_Nan)
    for col in columns_with_Nan:
        print("%s : %d" % (col, df[col].isnull().sum()))


# process missing values in train_merged
train_merged['source_system_tab'].fillna(-1, inplace=True)
train_merged['source_screen_name'].fillna(-1, inplace=True)
train_merged['source_type'].fillna(-1, inplace=True)
train_merged['song_length'].fillna(train_merged['song_length'].mean(axis=0), inplace=True)
train_merged['artist_name'].fillna("no_artist", inplace=True)
train_merged['composer'].fillna("no_composer", inplace=True)
train_merged['lyricist'].fillna("no_lyricist", inplace=True)
train_merged['language'].fillna(-1, inplace=True)
train_merged['issue_year'].fillna(-1, inplace=True)


# process missing values in test_merged
test_merged['source_system_tab'].fillna(-1, inplace=True)
test_merged['source_screen_name'].fillna(-1, inplace=True)
test_merged['source_type'].fillna(-1, inplace=True)
test_merged['song_length'].fillna(test_merged['song_length'].mean(axis=0), inplace=True)
test_merged['artist_name'].fillna("no_artist", inplace=True)
test_merged['composer'].fillna("no_composer", inplace=True)
test_merged['lyricist'].fillna("no_lyricist", inplace=True)
test_merged['language'].fillna(-1, inplace=True)
test_merged['issue_year'].fillna(-1, inplace=True)

# check_missing_values(train_merged)
# check_missing_values(test_merged)
train_merged.to_csv("train_merged.csv", index=False, sep=',')
test_merged.to_csv("test_merged.csv", index=False, sep=',')
del train_merged
del test_merged









