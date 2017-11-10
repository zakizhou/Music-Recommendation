import os
import numpy as np
import pandas as pd
# os.chdir('...')  # replace with your work path
os.chdir('D:/Kaggle/reco_music/data')


# get the issue year from isrc (in songs_extra)
def isrc_to_year(isrc):
    if type(isrc) == str:
        if int(isrc[5:7]) > 17:
            return 1900 + int(isrc[5:7])
        else:
            return 2000 + int(isrc[5:7])
    else:
        return -1


# read & process songs_extra
songs_extra = pd.read_csv('song_extra_info.csv')
songs_extra["issue_year"] = songs_extra["isrc"].apply(isrc_to_year)
songs_extra.drop("isrc", axis=1, inplace=True)

songs_extra.to_csv("songs_extra_processed.csv", index=False, sep=',')


'''
# insights from Kernel
# visualize the issue year for songs in train set and test set
# find the train set and test set have a chronological order
# maybe we can split the last N samples in train set as validation set

import seaborn as sns 
train_set = pd.read_csv("train.csv")
test_set = pd.read_csv("test.csv")
col = ["song_id", "issue_year"]
train_with_isrc = pd.merge(train_set, songs_extra[col], on="song_id", how="left")
test_with_isrc = pd.merge(test_set, songs_extra[col], on="song_id", how="left")

train_with_isrc["2017_rolling_mean"] = (train_with_isrc["issue_year"]==2017).rolling(window=5000, center=True).mean()
test_with_isrc["2017_rolling_mean"] = (test_with_isrc["issue_year"] == 2017).rolling(window=5000,center=True).mean()

ax = sns.countplot(x="issue_year", data=train_with_isrc)
ax2 = sns.countplot(x="issue_year", data=test_with_isrc)
'''