#Imports Modules
import csv
from itertools import zip_longest as z

import re
#A - Input Search Term
#B - Opens File and Imports Table creating Lists
#C - Checks whether Search Word appears in Sentence, add Text to List if does
#X - Creates and Exports a Data File


#A - Input Search Term

print('''Input Search Word
Input Month as three letter abbreviation''')
searchWord = input()
foundEmails = []
foundEmails = foundEmails + [searchWord]

print(' ')
print('If searching for Client input 1, if searching Email input 2, if searching for Month input 3')
searchType = int(input())


#B - Opens File and Imports Data for Searching

with open('EmailList.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')
    
    dataList = []
        
    for row in readCSV:
        reference = row[0]
        client = row[1]
        email = row[2]
        subject = row[3]
        contents = row[4]
        date =row[5]

        text = []
        textList =[]
        
        if searchType == 1:
            textString = str(client) + str(email)
        elif searchType == 2:
            textString = str(subject) + str(contents)
            print
        elif searchType == 3:
            textString = str(date)
        
        text = text + [reference] + [client] + [email] + [subject] + [contents] + [date]
        textList = textList + [text]
               
#C - Checks whether Search Term appears in Sentence, add Text to List if does

        searchTerm = re.compile(r'(' + searchWord + ')')

        keyCode = re.findall(searchTerm, textString)
        
        if keyCode == foundEmails:
            dataList = dataList + textList


#X - Creates and Exports a Data File

exportReference = ['Reference']
exportClient = ['Client']
exportEmail = ['Email Address']
exportSubject = ['Subject']
exportContent = ['Content']
exportDate = ['Date']

length = len(dataList)

for row in range(0,length):
    
    exportReference = exportReference + [dataList[row][0]]
    exportClient = exportClient + [dataList[row][1]]
    exportEmail = exportEmail + [dataList[row][2]]
    exportSubject = exportSubject + [dataList[row][3]]
    exportContent = exportContent + [dataList[row][4]]
    exportDate = exportDate + [dataList[row][5]]

newData = [exportReference, exportClient, exportEmail, exportSubject, exportContent, exportDate]

exportData = z(*newData, fillvalue = '')

with open('C:/Users/Peter/Documents/Peter - Toshiba/Python Project/Discovery Emails/Output.csv', 'w', newline ='') as newFile:
      writer = csv.writer(newFile)
      writer.writerows(exportData)
      newFile.close()
    
print('All Done')
  
