from Person import *
from flights import *
from Country import *
import random
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8908',
    port='3306',
    database='flightsale'
)
mycursor = mydb.cursor()


#CLASS FOR CLIENTS
class Clients(Person):

    def __init__(self):
        print("")

#CONSTRUCTOR FOR CLIENTS
    def __init__(self, secname, name, personage, idcard, genra, house, number, passport, sitNum):
        super().__init__(secname, name, personage, idcard, genra, house, number)
        self.personpassport = passport
        self.numSit = sitNum
#Setters

    def setpassport(self, passport):
        self.personpassport = passport

    def set_Sit(self, num):
        self.numSit = num
#Getters

    def getPassport(self):
        return self.personpassport

    def get_SitNum(self):
        return self.numSit

    def askInfo(self):
        self.setpassport(input("Insert Your Passport"))

    def staNum(self):
        numb = random.randrange(1000000)
        self.set_Sit(numb)

#QUERY FOR INSERT INTO THE DATABASE
    def insertPassenger(self, countId, FlightId):
        insert = "INSERT INTO passenger(Passport,idPerson, CountryId, SitNumber, FlightId) VALUES (%s,%s,%s,%s,%s)"
        datos = (self.getPassport(), self.getPersonId(), countId, self.get_SitNum(), FlightId)
        mycursor.execute(insert, datos)
        mydb.commit()
        print("Data Inserted")

#QUERY TO SHOW THE CLIENTS PER FLIGHT
    def clientsPerFligh(self):
        print("-----------------------------------------------------------------------")
        mycursor.execute("SELECT f.AirLine,pe.Name, pe.SecondName, pe.BirthDate, pe.Gender, p.SitNumber FROM flights as f INNER JOIN passenger AS p ON f.FlightId = p.FlightId INNER JOIN person as pe ON p.idPerson = pe.idPerson")
        spc = mycursor.fetchall()
        for i in spc:
            print(i)
        print("-----------------------------------------------------------------------")




