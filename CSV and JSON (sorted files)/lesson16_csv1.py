import csv

with open('example.csv', encoding='UTF-8') as csv_file:
    exampleReader = csv.reader(csv_file, delimiter=';')
    # print(list(exampleReader))
    for row in exampleReader:
        string = 'Строка #' + str(exampleReader.line_num) + ' '
        # line_num - для вывода номера строки
        for value in row:
            string += value + ' '
        print(string)
