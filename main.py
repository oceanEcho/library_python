import json

from PrintedMaterial import PrintedMaterial
from Book import Book
from Textbook import Textbook
from Magazine import Magazine
from Library import Library

defaultFilePath = "default.json"

lib = Library()

lib.ReadFromFile(defaultFilePath, 0)

running = True

while(running):
    print("Доступные операции:")
    print("1. Вывести список всех печатных изданий")
    print("2. Вывести список всех книг")
    print("3. Вывести список всех журналов")
    print("4. Вывести список всех учебников")
    print("5. Добавить печатное издание в библиотеку")
    print("6. Удалить печатное издание из библиотеки")
    print("7. Считать из файла")
    print("8. Записать в файл")
    print("0. Выход. ")

    key = input("Ваше действие: ")

    if (key == "1"):
        lib.Show()
    elif (key == "2"):
        lib.ShowBooks()
    elif (key == "3"):
        lib.ShowMagazines()
    elif (key == "4"):
        lib.ShowTextbooks()
    elif (key == "5"):
        print("1. Книга")
        print("2. Журнал")
        print("3. Учебник")

        newKey = input("Ваше действие: ")

        if (newKey == "1"):
            title = input("Введите название: ")
            author = input("Введите автора: ")
            style = input("Введите жанр: ")
            cost = float(input("Введите стоимость: "))
            lib.Add(Book(title, author, style, cost))
        elif (newKey == "2"):
            title = input("Введите название: ")
            theme = input("Введите тематику: ")
            date = input("Введите дату выпуска: ")
            cost = float(input("Введите стоимость: "))
            lib.Add(Magazine(title, theme, date, cost))
        elif (newKey == "3"):
            title = input("Введите название: ")
            author = input("Введите автора: ")
            subject = input("Введите предмет: ")
            stage = float(input("Введите класс: "))
            cost = float(input("Введите стоимость: "))
            lib.Add(Textbook(title, author, subject, stage, cost))
    
        print("Издание добавлено в библиотеку.")

    elif (key == "6"):
        item = int(input("Введите номер издания для удаления: "))
        lib.Remove(item)
        print("Издание удалено из библиотеки.")

    elif (key == "7"):
        file = str(input("Введите имя файла: "))
        isBinary = input("Считать бинарно(1 - да, 0 - нет)? ")
        print(int(isBinary))
        if int(isBinary) == 0:
            isBinary = False
        else:
            isBinary = True
        lib.ReadFromFile(file, isBinary)

    elif (key == "8"):
        file = str(input("Введите имя файла: "))
        isBinary = input("Записать бинарно(1 - да, 0 - нет)? ")
        print(int(isBinary))
        if int(isBinary) == 0:
            isBinary = False
        else:
            isBinary = True
        lib.WriteToFile(file, isBinary)

    elif (key == "0"):
        running = False
