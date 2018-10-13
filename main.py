import csv
import re # Regular expression
import pandas as pd
csv_ori = pd.read_csv('original.csv', sep=",")
# csv_ori = open('original.csv', 'r')
print(csv_ori['comment'][0])

"""
for index in csv_ori.iterrows():
    ori = csv_ori['comment'][index]
    # if csv_ori['comment'][index] == '[^\x01-\x7E]'
    # ori = re.sub('[^\x01-\x7E]', '', ori)
    print(ori)
"""