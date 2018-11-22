from PrintedMaterial import PrintedMaterial

class Book(PrintedMaterial):
    def __init__(self, newTitle = "undefined", newAuthor = "undefined", newStyle = "undefined", newCost = 0):
        super().__init__("book", newTitle, newAuthor, newCost)
        self.style = newStyle
    
    def SetStyle(self, newStyle):
        self.style = newStyle

    def SetItem(self, newTitle, newAuthor, newStyle, newCost):
        super().__init__(newTitle, newAuthor, newCost)
        self.style = newStyle

    def GetStyle(self):
        return self.style

    def GetItem(self):
        return ( "Книга \"" + self.title + "\", " + self.author + ", " + self.style + ", $" + str(self.cost))