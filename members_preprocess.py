import os
import numpy as np
import pandas as pd
# os.chdir('...')  # replace with your work path
os.chdir('D:/Kaggle/reco_music/data')


# extract year, month, day from register_init_time & expire_date (in members)
def extract_from_date(df, col, str1, str2, str3):
    df[str1] = df[col].apply(lambda x: int(str(x)[0:4]))
    df[str2] = df[col].apply(lambda x: int(str(x)[4:6]))
    df[str3] = df[col].apply(lambda x: int(str(x)[6:]))
    df.drop(col, axis=1, inplace=True)


# detect age outliers (in members)
def detect_outlier(x):
    if np.abs(x - 45) <= 35:  # regard age out of 10~80 as outlier
        return x
    else:
        return np.nan


# process age info (in members)
def process_age(df):
    df['bd'] = df['bd'].apply(detect_outlier)
    mask = np.abs(df['bd'] - 45) <= 35
    mean_without_outlier = int(df['bd'][mask].mean())  # compute mean out of outliers
    df['bd'].fillna(mean_without_outlier, inplace=True)


# process gender info (in members)
def process_gender(df):
    df["gender"] = df["gender"].replace({'male': 1, 'female': 0})
    df["gender"].fillna(-1, inplace=True)


# read & process members
members = pd.read_csv('members.csv')

extract_from_date(members, "registration_init_time", "reg_year", "reg_month", "reg_day")
extract_from_date(members, "expiration_date", "expire_year", "expire_month", "expire_day")

process_age(members)
process_gender(members)

# members.to_csv("...")  # your output path
members.to_csv("members_processed.csv", index=False, sep=',')
