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
    ja = com.encode("ascii", "replace").decode("ascii")
    print(ja)
    ja_l.append(ja)

print(ja_l)

for index, row in csv_ori.iterrows():
    csv_ori['comment'][index] = ja_l[index]

csv_ori.to_csv('original.csv', index=False)

"""
LINE12
Depending on circumstances, use them
ja = re.sub('[亜-熙ぁ-んァ-ヶ]', 'None', com) 日本語であればNoneにする
ja = com.encode("ascii","ignore").decode("ascii") 日本語以外の文字も消し去る
ja = com.encode("ascii","replace").decode("ascii") 日本語、ロシア語の文字は?に変換される

"""