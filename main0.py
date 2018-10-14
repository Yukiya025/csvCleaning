import csv

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