import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8908',
    port='3306',
    database='flightsale'
)
mycursor = mydb.cursor()


#CLASS FOR THE DESTINYS
class Destinys:
    #CONSTRUCTOR FOR DESTINYS
    def __init__(self, desCode, name):
        self.destCode = desCode
        self.DestName = name

#SETTERS
    def setDestCode(self, code):
        self.destCode = code

    def setDestName(self, name):
        self.DestName = name

#GETTERS
    def getDestCode(self):
        return self.destCode

    def getDestName(self):
        return self.DestName

#SELECT THE CODE OF THE DESTINY
    def getDestId(self, countryId):
        mycursor.execute("SELECT DestinyCode FROM destinys WHERE CountryId = '%s'" % countryId)
        spc = mycursor.fetchone()
        self.setDestCode(int(spc[0]))
#SEARCH DESTINY NAME BY FLIGHT ID
    def searchDestName(self, flighId):
        mycursor.execute("SELECT DestName FROM flights INNER JOIN destinys as d ON flights.DestinyCode = d.DestinyCode WHERE FlightId = '%s' " % flighId)
        spc = mycursor.fetchone()
        self.setDestName(str(spc[0]))
