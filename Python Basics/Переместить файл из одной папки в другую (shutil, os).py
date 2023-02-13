import shutil
import os

"""
Сделать сортировщик файлов.
К примеру, загружается какой-то файл с любого сайта, допустим в формате .png.
Ваш скрипт должен распределить данный файл в отдельную директорию.

"""
folder_downloads = r'C:\Users\WM Reply\Downloads'  # папка для отслеживания файлов
folder_move = r'C:\Users\WM Reply\Desktop'  # папка куда файлы будут переноситься (+ папка для конкретного файла)
pdf_format = "pdf"  # файл с форматом pdf
jpg_format = "jpg"  # файл с форматом jpg
office_format = ["doc", "docx", 'xlsx', 'txt']  # список с офисными форматами
files = os.listdir(folder_downloads)  # Получаем список всех файлов в нашей папке Downloads
for i in files:  # Запускаем цикл по всем файлам
    extension = i.split(".")  # разделяем строку по точке и записываем в переменную extension (расширение)
    # Если длина переменную extension больше 1 и последний элемент списка равен jpg_format, то
    if len(extension) > 1 and extension[-1].lower() == jpg_format:
        file = folder_downloads + "/" + i  # Создаем переменную и присваиваем ей путь к файлу
        # Создаем переменную и присваиваем ей путь в папку, куда мы хотим файл перенести
        new_dir = folder_move + "/Photos/" + i
        shutil.move(file, new_dir)  # Переносим файл из расположения "file" в расположение "new_dir"
    if len(extension) > 1 and extension[-1].lower() in office_format:  #
        file = folder_downloads + "/" + i  # Создаем переменную и присваиваем ей путь к файлу
        # Создаем переменную и присваиваем ей путь в папку, куда мы хотим файл перенести
        new_dir = folder_move + "/Office/" + i
        shutil.move(file, new_dir)  # Переносим файл из расположения "file" в расположение "new_dir"
    if len(extension) > 1 and extension[-1].lower() == pdf_format:  #
        file = folder_downloads + "/" + i  # Создаем переменную и присваиваем ей путь к файлу
        # Создаем переменную и присваиваем ей путь в папку, куда мы хотим файл перенести
        new_dir = folder_move + "/PDF/" + i
        shutil.move(file, new_dir)  # Переносим файл из расположения "file" в расположение "new_dir"
