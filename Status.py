class Status:
    def __init__(self, id, descrip, sign):
        self.StatusId = id
        self.Description = descrip
        self.letter = sign

#SETTERS
    def set_Status(self, id):
        self.StatusId = id

    def set_Description(self, descrip):
        self.Description = descrip

    def set_letter(self, sign):
        self.letter = sign

#GETTERS
    def get_StatusId(self):
        return self.StatusId

    def get_Description(self):
        return self.Description

    def get_letter(self):
        return self.letter

    def searchForId(self):
        self.set_Status(int(input("Insert Status")))
