from PrintedMaterial import PrintedMaterial
from Book import Book
from Textbook import Textbook
from Magazine import Magazine

class Library():
    def __init__(self):
        self.storage = []
    
    def Add(self, item):
        self.storage.append(item)

    def Remove(self, position):
        self.storage.remove(self.storage[position])

    def Show(self):
        id = 0
        for item in self.storage:
            print(str(id) + ". " + item.GetItem())
            id += 1
    
    def ShowBooks(self):
        id = 1
        for item in self.storage:
            if (item.GetType() == "book"):
                print(str(id) + ". " + item.GetItem())
            id += 1
    
    def ShowTextbooks(self):
        id = 1
        for item in self.storage:
            if (item.GetType() == "textbook"):
                print(str(id) + ". " + item.GetItem())
            id += 1
    
    def ShowMagazines(self):
        id = 1
        for item in self.storage:
            if (item.GetType() == "magazine"):
                print(str(id) + ". " + item.GetItem())
            id += 1