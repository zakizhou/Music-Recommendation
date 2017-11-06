import csv
with open('D:/Kaggle/kkbox_music_recommendation/code/result.csv','wb') as csvfile:
    writer = csv.writer(csvfile, delimiter = ' ')
    writer.writerow(['spam', 'love', 'badworm'])