from PrintedMaterial import PrintedMaterial
from Book import Book
from Textbook import Textbook
from Magazine import Magazine
from Library import Library

lib = Library()

book2 = Book()

book3 = Book()
book3.SetAuthor("Gogol")

book4 = Textbook("Геология", "Джон Локк", "Геология", 9, 20)

book5 = Magazine("Капкан", "Охота", "10/03/18", 20)

lib.Add(book2)
lib.Add(book3)
lib.Add(book4)
lib.Add(book5)

running = True

while(running):
    print("Доступные операции:")
    print("1. Вывести список всех печатных изданий")
    print("2. Вывести список всех книг")
    print("3. Вывести список всех журналов")
    print("4. Вывести список всех учебников")
    print("5. Добавить печатное издание в библиотеку")
    print("6. Удалить печатное издание из библиотеки")
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
    
    elif (key == "0"):
        running = False
    

    