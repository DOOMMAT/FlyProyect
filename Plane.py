import mysql.connector
import time
from Status import *
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8908',
    port='3306',
    database='flightsale'
)
mycursor = mydb.cursor()


#CLASS FOR PLANE
class Plane(Status):
    OnHold = 9
    Ready = 10
    Arrived = 11
    Damaged = 12
    Up = 13

    def __init__(self):
        print("")

    # Constructor of the plane
    def __init__(self, planecode, Sits, gasoline, Amount, weight, size):
        self.codePlane = planecode
        self.Sits = Sits
        self.GasolineType = gasoline
        self.Amount_Passengers = Amount
        self.plane_Weigth = weight
        self.planeSize = size

#Setters
    def setPlane_Code(self, planecode):
        self.codePlane = planecode

    def set_Sits(self, sits):
        self.Sits = sits

    def setGasoline(self, Gasoline):
        self.GasolineType = Gasoline

    def setPassengersAmount(self, Amount):
        self.Amount_Passengers = Amount

    def setplane_Weigth(self, weight):
        self.plane_Weigth = weight

    def setSize(self, size):
        self.planeSize = size

#Getters
    def getPlane_Code(self):
        return self.codePlane

    def getSits(self):
        return self.Sits

    def getGasoline(self):
        return self.GasolineType

    def getPassengerAmoun(self):
        return self.Amount_Passengers

    def getPlaneWeight(self):
        return self.plane_Weigth

    def getPlane_Size(self):
        return self .planeSize

    def storageSta(self):
        return

#METHOD TO CHECK ALL THE PLANES THAT ARE READY TO FLIGHT oR JUST ARRIVED
    def planesBy(self, StatId):
        mycursor.execute("SELECT * FROM plane WHERE StatusId = '%s'" % StatId)
        spc = mycursor.fetchall()
        for i in spc:
            print(i)

#METHOD TO CHECK THE PLAMES THAT ARE DELAYED
    def planesDelayed(self):
        print("-----------------------------------------------------------")
        mycursor.execute("SELECT p.PlaneCode, d.description, d.StarDate, d.FinishDate FROM plane AS p INNER JOIN flights AS f ON p.PlaneCode = f.PlaneCode INNER JOIN delay AS d ON f.FlightId = d.FlightId")
        spc = mycursor.fetchall()
        for i in spc:
            print(i)
        print("-----------------------------------------------------------")

#UPDATE THE SPACE OF THE PLANE
    def updatePlane(self, amount, FligId):
        select = "UPDATE plane as p INNER JOIN flights as f ON p.PlaneCode = f.PlaneCode SET Amount_Passengers= '%s' WHERE FlightId = '%s' "
        data = (amount, FligId)
        mycursor.execute(select, data)
        mydb.commit()
        print("Space Reserved")
#METHOD TO UPDATE THE STATUS OF THE PLANE WHEN IT'S FULL
    def updateStatusPlane(self, sta, FligId):
        select = "UPDATE plane as p INNER JOIN flights as f ON p.PlaneCode = f.PlaneCode SET p.StatusId= '%s' WHERE FlightId = '%s' "
        data = (sta, FligId)
        mycursor.execute(select, data)
        mydb.commit()
