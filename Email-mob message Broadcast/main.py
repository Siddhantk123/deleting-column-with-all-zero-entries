import pandas as pd
import smtplib as sm


#reading email from files
col=pd.read_csv('book.csv')
#print(col)



dict={}
for (columnName, columnData) in col.iteritems():
    #print('ColumnContents : ', columnData.values)
    sum=0
    #print(columnData)
    if(isinstance(columnData[0], str) == False):
        for i in range(0,len(columnData)):
            sum=sum+ columnData[i]       
        dict[columnName] = sum
#print(dict)
for key,value in dict.items():
    if(value == 0):
        col = col.drop(columns=[key])
print(col)