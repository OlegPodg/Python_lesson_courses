import shutil  # shutil (для высокоуровневого взаимодействия с объектами системы)
import os  # os (для получения информации о файлах)

"""
Сделать сортировщик файлов.
К примеру, загружается какой-то файл с любого сайта, допустим в формате .png.
Ваш скрипт должен распределить данный файл в отдельную директорию.

"""


def move_files():
    folder_downloads = r'C:\Users\...\Downloads'  # папка для отслеживания файлов
    folder_move = r'C:\Users\...\Desktop'  # папка куда файлы будут переноситься (+ папка для конкретного файла)
    pdf_format = "pdf"  # файл с форматом pdf
    jpg_format = "jpg"  # файл с форматом jpg
    office_format = ["docx", 'xlsx', 'txt']  # список с офисными форматами
    files = os.listdir(folder_downloads)  # Получаем список всех файлов в нашей папке Downloads
    for i in files:  # Запускаем цикл по всем файлам
        extension = i.split(".")  # разделяем строку по точке и записываем в переменную extension (расширение)
        if extension[-1].lower() == jpg_format:  # Если последний элемент списка равен jpg_format, то
            file = folder_downloads + "/" + i  # Создаем переменную и присваиваем ей путь к файлу
            # Создаем переменную и присваиваем ей путь в папку, куда мы хотим файл перенести
            new_dir = folder_move + "/Photos/" + i
            shutil.move(file, new_dir)  # Переносим файл из расположения "file" в расположение "new_dir"
        if extension[-1].lower() in office_format:  # Если последний элемент списка равен jpg_format, то
            file = folder_downloads + "/" + i  # Создаем переменную и присваиваем ей путь к файлу
            # Создаем переменную и присваиваем ей путь в папку, куда мы хотим файл перенести
            new_dir = folder_move + "/Office/" + i
            shutil.move(file, new_dir)  # Переносим файл из расположения "file" в расположение "new_dir"
        if extension[-1].lower() == pdf_format:  # Если последний элемент списка равен jpg_format, то
            file = folder_downloads + "/" + i  # Создаем переменную и присваиваем ей путь к файлу
            # Создаем переменную и присваиваем ей путь в папку, куда мы хотим файл перенести
            new_dir = folder_move + "/PDF/" + i
            shutil.move(file, new_dir)  # Переносим файл из расположения "file" в расположение "new_dir"


move_files()
