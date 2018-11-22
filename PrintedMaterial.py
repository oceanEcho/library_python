class PrintedMaterial:
    def __init__(self, newType = "default", newTitle = "undefined", newAuthor = "undefined", newCost = 0):
        self.type = newType
        self.title = newTitle
        self.author = newAuthor
        self.cost = newCost

    def SetTitle(self, newTitle):
        self.title = newTitle

    def SetAuthor(self, newAuthor):
        self.author = newAuthor
    
    def SetCost(self, newCost):
        self.cost = newCost

    def SetItem(self, newTitle, newAuthor, newCost, newStyle):
        self.type = "default"
        self.title = newTitle
        self.author = newAuthor
        self.cost = newCost
    
    def GetType(self):
        return self.type

    def GetTitle(self):
        return self.title

    def GetAuthor(self):
        return self.author
    
    def GetCost(self):
        return self.cost

    def GetItem(self):
        return ( "\"" + self.title + "\", " + self.author + ", $" + str(self.cost))
