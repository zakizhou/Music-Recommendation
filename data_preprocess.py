import os
os.chdir('D:/Kaggle/reco_music/data')


# print col with nulls and the exact number
def check_columns_isnull(df):
    if df.isnull().values.any():
        columns_with_nan = df.columns[df.isnull().any()].tolist()
        print("columns with nulls:")
        for col in columns_with_nan:
            print("%s:%d" % (col, df[col].isnull().sum()))
    print("\n")


