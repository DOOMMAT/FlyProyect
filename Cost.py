import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8908',
    port='3306',
    database='flightsale'
)
mycursor = mydb.cursor()

#CLASS FOR THE COST OF THE FLIGHTS
class cost:
    def __init__(self, cost, money, curr):
        self.IdCost = cost
        self.Amount = money
        self.Currency = curr

#SETTERS
    def setIdCost(self, cost):
        self.IdCost = cost

    def setAmount(self, amoun):
        self.Amount = amoun

    def setCurr(self, curr):
        self.Currency = curr

#GETTERS
    def getIdCost(self):
        return self.IdCost

    def getAmount(self):
        return self.Amount

    def getCurrency(self):
        return self.Currency

#SELECT THE ID COST QUERY
    def getIdcost(self, flightId):
        mycursor.execute("SELECT idCost FROM cost WHERE FlightId = '%s'" % flightId)
        spc = mycursor.fetchone()
        self.setIdCost(int(spc[0]))
