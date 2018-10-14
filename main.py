import csv
import re # Regular expression
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

csv_ori = pd.read_csv('original.csv', sep=",")
ja_l = []
for i, index in csv_ori.iterrows():
    print('i: ' + str(i))
    com = csv_ori.iloc[i]["comment"]
    ja = re.sub('[亜-熙ぁ-んァ-ヶ]', 'None', com)
    print(ja)
    ja_l.append(ja)

print(ja_l)

for index, row in csv_ori.iterrows():
    csv_ori['comment'][index] = ja_l[index]

csv_ori.to_csv('original.csv', index=False)