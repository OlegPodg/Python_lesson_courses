import csv

exampleFile = open("output.csv", "w", encoding="UTF-8", newline="")
exampleWriter = csv.writer(exampleFile, delimiter=';')
exampleData = [['05.04.2015 13:34', 'Яблоки', '73'], ['05.04.2015 3:41', 'Вишни', '85'],
               ['06.04.2015 12:46', 'Груши', '14']]
for row in exampleData:
    exampleWriter.writerow(row)
exampleFile.close()
