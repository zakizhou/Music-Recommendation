import csv
import os
os.chdir('D:/Kaggle/kkbox_music_recommendation/')

#just a test
with open('result.csv','wb') as csvfile:
    writer = csv.writer(csvfile, delimiter = ' ')
    writer.writerow(['spam', 'love', 'badworm'])