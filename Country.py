import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8908',
    port='3306',
    database='flightsale'
)
mycursor = mydb.cursor()


#CLASS FOR COUNTRY
class Country:
    def __init__(self, country, count_id):
        self.countryName = country
        self.countryId = count_id

#SETTERS
    def setCountryName(self, country):
        self.countryName = country

    def setCountryId(self, coun_id):
        self.countryId = coun_id

#GETTERS
    def getCountryName(self):
        return self.countryName

    def getCountryId(self):
        return self.countryId

#SET THE COUNTRY ID
    def askCount_Id(self):
        self.setCountryId(int(input("Insert your country Id: ")))

#METHOD TO SEARCH THE COUNTRYID BY FLIGHTID
    def searchCountryId(self, flighId):
        mycursor.execute("SELECT CountryId FROM flights INNER JOIN destinys as d ON flights.DestinyCode = d.DestinyCode WHERE FlightId = '%s' " % flighId)
        spc = mycursor.fetchone()
        self.setCountryId(int(spc[0]))
