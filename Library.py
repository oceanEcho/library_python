import json
import pickle

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

    def WriteToFile(self, filePath, isBinary):
        convertedStorage = []
        if isBinary:
            for item in self.storage:
                convertedStorage.append(item.ConvertToJSON())
            with open(filePath, "wb") as fileHandler:
                pickle.dump(convertedStorage, fileHandler)
        else:
            for item in self.storage:
                convertedStorage.append(item.ConvertToJSON())
            with open(filePath, "w") as fileHandler:
                json.dump(convertedStorage, fileHandler)


    def ReadFromFile(self, filePath, isBinary):
        self.storage = []
        if isBinary:
            with open(filePath, "rb") as fileHandler:
                convertedStorage = pickle.load(fileHandler)
        else:
            with open(filePath, "r") as fileHandler:
                convertedStorage = json.loads(fileHandler.read())

        for item in convertedStorage:
            if item["type"] == "book":
                newBook = Book(item["title"], item["author"], item["style"], item["cost"])
            if item["type"] == "textbook":
                newBook = Textbook(item["title"], item["author"], item["subject"], item["stage"], item["cost"])
            if item["type"] == "magazine":
                newBook = Magazine(item["title"], item["theme"], item["date"], item["cost"])
            self.storage.append(newBook)
