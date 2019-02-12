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

    def ConvertToJSON(self):
        printedMaterial = {}
        printedMaterial["type"] = self.GetType()
        printedMaterial["title"] = self.GetTitle()
        printedMaterial["author"] = self.GetAuthor()
        printedMaterial["cost"] = self.GetCost()
        printedMaterial["style"] = self.GetStyle()
        return printedMaterial

    def ParseFromJSON(self, pmJSON):
        self.type = pmJSON["type"]
        self.title = pmJSON["title"]
        self.author = pmJSON["author"]
        self.cost = pmJSON["cost"]
        self.style = pmJSON["style"]