import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8908',
    port='3306',
    database='flightsale'
)
mycursor = mydb.cursor()

#CLASS FOR PERSON
class Person:
    def __init__(self, secname, name, personage, idcard, genra, house, number):
        self.secondName = secname
        self.PersonName = name
        self.personBirth = personage
        self.Id = idcard
        self.gen = genra
        self.direction = house
        self.phone = number

#SETTER
    def setPersonName(self, name):
        self.PersonName = name

    def setsecName(self, secondname):
        self.secondName = secondname

    def setPersonBirth(self, personage):
        self.personBirth = personage

    def setId(self,idperson):
        self.Id = idperson

    def setGender(self, genra):
        self.gen = genra

    def setDirection(self, house):
        self.direction = house

    def setNumber(self, number):
        self.phone = number

#GETTER
    def getPersonName(self):
        return self.PersonName

    def getsecName(self):
        return self.secondName

    def getPersonBirth(self):
        return self.personBirth

    def getPersonId(self):
        return self.Id

    def getGender(self):
        return self.gen

    def getDirection(self):
        return self.direction

    def getPhone_Number(self):
        return self.phone

#METHOD FOR QUESTIONS TO THE PERSON
    def askPersonalInfo(self):
        self.setsecName(input("Insert your second name: "))
        self.setPersonName(input("Insert your name: "))
        self.setPersonBirth(input("Insert your birthDate *yyyy-mm-dd*: "))
        self.setId(int(input("Insert your ID: ")))
        self.setGender(input("Insert your gender: "))
        self.setDirection(input("Where do you live?: "))
        self.setNumber(int(input("Digit your phone number: ")))

#EXECUTE THE TABLE OF PERSON QUERY
    def sendPerson(self):
        insert = ("INSERT INTO person(idPerson, Name, SecondName,BirthDate , Gender, HouseDirection, PhoneNumber) VALUES (%s,%s,%s,%s,%s,%s,%s)")
        datos = (self.getPersonId(), self.getPersonName(), self.getsecName(), self.getPersonBirth(), self.getGender(), self.getDirection(), self.getPhone_Number())
        mycursor.execute(insert, datos)
        mydb.commit()
        print("Data Inserted")










