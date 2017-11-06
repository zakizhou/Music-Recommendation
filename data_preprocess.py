import os
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
os.chdir('D:/Kaggle/reco_music/data')

train_set = pd.read_csv('train.csv')
test_set = pd.read_csv('test.csv')
members = pd.read_csv('members.csv')
songs = pd.read_csv('songs.csv')
songs_extra = pd.read_csv('song_extra_info.csv')


def check_columns_isnull(df):
    if(df.isnull().values.any()):
        columns_with_nan = df.columns[df.isnull().any()].tolist()
        print("columns with nulls:")
        for col in columns_with_nan:
            print("%s:%d" % (col, df[col].isnull().sum()))
    print("\n")


def get_shape_columns_missingdata(df):
    print("shape:", df.shape)
    print("columns", df.columns)
    check_columns_isnull(df)
    print("\n")


get_shape_columns_missingdata(train_set)
get_shape_columns_missingdata(test_set)
get_shape_columns_missingdata(members)
get_shape_columns_missingdata(songs)
get_shape_columns_missingdata(songs_extra)

#merge
train_members = pd.merge(train_set, members, on='msno', how='inner')
train_merged = pd.merge(train_members, songs, on='song_id', how='inner')
print("before merge:", train_set.shape)
print("after merge members:", train_members.shape)
print("after merge songs:", train_merged.shape)

test_members = pd.merge(test_set, members, on='msno', how='inner')
test_merged = pd.merge(test_members, songs, on='song_id', how='inner')
print("before merge:", test_set.shape)
print("after merge members:", test_members.shape)
print("after merge songs:", test_merged.shape)

del train_set
del test_set
del songs
del members

check_columns_isnull(train_merged)
check_columns_isnull(test_merged)

#simplify dtype to save memory
train_set['target'] = train_set['target'].astype(np.int8)
test_set['id'] = test_set['id'].astype(np.int32)

members['city'] = members['city'].astype(np.int8)
members['bd'] = members['bd'].astype(np.int16)
members['registered_via'] = members['registered_via'].astype(np.int8)
members['registration_init_time'] = members['registration_init_time'].astype(np.int32)
members['expiration_date'] = members['expiration_date'].astype(np.int32)

#songs['song_length'] = songs['song_length'].astype(np.int32)













