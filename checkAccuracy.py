import csv
import pandas as pd
import numpy

linecount =0

interesting_cols = [0, 1]

""" with open("lstm.csv", 'r') as file1, open("trainingandtestdata/dataset-processed.csv", 'r') as file2:

    reader1, reader2 = csv.reader(file1), csv.reader(file2)

    for line1, line2 in zip(reader1, reader2):
        equal = all(x == y
            for n, (x, y) in enumerate(zip(line1, line2))
            if n in interesting_cols
        )
        print(equal) """

df = pd.read_csv('trainingandtestdata/testdata.manual.2009.06.14-processed.csv', names=['id', 'value', 'tweet'])  
df1 = pd.read_csv('lstm.csv', names=['id', 'value'])  
count =df['id'].count()
count1 =df1['id'].count()
""" idvalue = []
idvalue1 =[]
value =[]
value1 =[] """
idvalue = df['id']
idvalue1 =df1['id']
valuearray =df['value']
value1array =df1['value']
print(df, df1)
for i in range(count):
    for j in range(count1):
       
        if ((idvalue[i]==idvalue1[j]) and (valuearray[i]==value1array[j])):
            linecount=linecount+1
            print(linecount)
percentage = linecount/count
print(percentage)                  