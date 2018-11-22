from PrintedMaterial import PrintedMaterial

class Magazine(PrintedMaterial):
    def __init__(self, newTitle = "undefined", newTheme = "undefined", newDate = "00/00/00", newCost = 0):
        super().__init__("magazine", newTitle, "undefined", newCost)
        self.theme = newTheme
        self.date = newDate
    
    def SetTheme(self, newTheme):
        self.theme= newTheme

    def SetDate(self, newDate):
        self.date = newDate

    def SetItem(self, newTitle, newTheme, newDate, newCost):
        super().__init__(newTitle, "undefined", newCost)
        self.theme = newTheme
        self.date = newDate

    def GetDate(self):
        return self.date

    def GetTheme(self):
        return self.theme

    def GetItem(self):
        return ( "Журнал \"" + self.title + "\", " + self.theme + ", " + self.date + ", $" + str(self.cost))