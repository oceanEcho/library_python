from PrintedMaterial import PrintedMaterial

class Textbook(PrintedMaterial):
    def __init__(self, newTitle = "undefined", newAuthor = "undefined", newSubject = "undefined", newStage = 0, newCost = 0):
        super().__init__("textbook", newTitle, newAuthor, newCost)
        self.subject = newSubject
        self.stage = newStage
    
    def SetStage(self, newStage):
        self.stage = newStage
    
    def SetSubject(self, newSubject):
        self.subject = newSubject

    def SetItem(self, newTitle, newAuthor, newSubject, newStage, newCost):
        super().__init__(newTitle, newAuthor, newCost)
        self.subject = newSubject
        self.stage = newStage

    def GetStage(self):
        return self.stage
    
    def GetSubject(self):
        return self.subject

    def GetItem(self):
        return ( "Учебник \"" + self.title + "\", " + self.author + ", " + self.subject + ", " + str(self.stage) + " класс, $" + str(self.cost))