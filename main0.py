import csv
import pandas as pd

def onlyEn():
    with open('original.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        no_ques = []
        for row in reader:
            if (r"?" in row[1]) == False:
                no_ques.append([row[0], row[1]])

        print(no_ques)
    with open('OnlyEn.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(no_ques)

def del_dup():
    on_en = pd.read_csv('OnlyEn.csv')
    sorted_onen = on_en.sort_values(['user_id', 'comment'],
                                     ascending=[1, 0])
    # print(sorted_onen)
    # print(len(on_en))

    df = pd.DataFrame(sorted_onen)
    print(df)
    ans = df.groupby('user_id')['comment'].apply(lambda x: ','.join(x))
    print(ans)

    ans.to_csv('final.csv', header = 'user_id')


