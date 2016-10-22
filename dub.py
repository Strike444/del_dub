# Программа для удаления лишних файлов. Понадобилась для удаления задвоенных ромов
# version: 0.01
import os, sys, re
from pathlib import Path
# каталог для файлов
path = "c:\\Temp\\roms"
#Получаем список файлов в переменную files 
dirs = os.listdir(path) 
#Массив файлов
Files = []
for file in dirs:
    Files.append(file)
#len(Files) длинна массива
for i in range(0, len(Files)):
    #Берем подстроку из нужного нам количиства строк и сравниваем ее
    #по регулярному выражению с остальными файлами
    podstroka = Files[i][0:4]
    for j in range(i+1, len(Files)):
        if podstroka == Files[j][0:4]:
            file_for_del = path + "\\" + Files[j]
            my_file = Path(file_for_del)
            #проверка на существование файла
            if my_file.is_file():
                os.remove(file_for_del)
                print("Удален файл:  ", file_for_del)