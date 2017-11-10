import os
import numpy as np
import pandas as pd
# os.chdir('...')  # replace with your work path
os.chdir('D:/Kaggle/reco_music/data')


# read & process songs
songs = pd.read_csv('songs_with_complete_genre.csv')
songs['language'].fillna(31, inplace=True)  # only one NaN, manually find its language
songs['composer'].fillna("no_composer", inplace=True)
songs['lyricist'].fillna("no_lyricist", inplace=True)  # over half without lyricist info


'''
# as a ref, manually find the language corresponding to each number 
language = {52: "English", -1:"pure_music", 3:"Chinese", 17:"Japanese",
            24: " Cantonese", 31: "Korean", 10:"Chinese", 45:"Dai language"
            59:"Chinese", 38:"baby_song"}
'''