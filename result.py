import pandas as pd
import numpy
import csv
outputfile ='lstm.csv'
#outputfile ="naivebayes.csv"
testfile ='trainingandtestdata/testdataset.csv'
df = pd.read_csv(outputfile, names=['id', 'value' ]) 
pos =0
neg =0
sentiment  =df['value']
count = len(df)-1
i=0
value =[]
for line in sentiment:
    if(i==0):
        i=1
        continue
    else:
        value.append(line)  
        if(line=='1'):
            pos=pos+1
        else:
            if(line =='0'):
                neg=neg+1    
df1 = pd.read_csv(testfile , names =['id' ,'value','prediction'])
df1['prediction']= value
print("\nPositive tweets:",(pos/count)*100 , '%')
print("\nNegative tweets:",(neg/count)*100,'%')
df1.to_csv('lstm1.csv')

