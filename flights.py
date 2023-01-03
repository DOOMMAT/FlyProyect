from Plane import *
import time
import ctypes
import mysql.connector
import multiprocessing
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8908',
    port='3306',
    database='flightsale'
)
mycursor = mydb.cursor()


#CLASS FOR FLIGHTS
class flights(Plane):
    flighNames = []
    flighList = []
    destNameList = []

    def __init__(self):
        print("")

#CONSTRUCTOR FOR THE FLIGHTS
    def __init__(self, flightId, name, planeCode, Sits, gasoline, Amount, weight, size, start_hour, arrive_hour, countryid, status):
        super().__init__(planeCode, Sits, gasoline, Amount, weight, size)
        self.st_hour = start_hour
        self.arr_hour = arrive_hour
        self.flightId = flightId
        self.country_Id = countryid
        self.Status = status
        self.airLine = name

#Setters
    def set_pId(self, id):
        self.flightId = id

    def setAirline(self, name):
        self.airLine = name

    def set_Star_Hour(self, st_hour):
        self.st_hour = st_hour

    def set_Arrive_Hour(self, arr_hour):
        self.arr_hour = arr_hour

    def set_Status(self, status):
        self.Status = status
#Getters

    def get_Start_Hour(self):
        return self.st_hour

    def get_Arrive_Hour(self):
        return self.arr_hour

    def get_Flight_Id(self):
        return self.flightId

    def getAirlineName(self):
        return self.airLine

    def getStatus(self):
        return self.Status

#PROCESS TO DEPLOY PLANES
    def deploy_planes(self, flight_id, destination, lock):
        lock.acquire()
        print("Deploying flight ", flight_id, " to: ", destination)
        time.sleep(5)
        lock.release()

#PROCESS TO DELAY FLIGHTS
    def delay_flight(self, flight_id, cause, destination, lock):
        lock.acquire()
        print("Flight ", flight_id, " to: ", destination, "Deleyed by: ", cause)
        time.sleep(20)
        lock.release()

#METHOD THAT RECEIVED PLANES
    def receivedPlanes(self, flightId, destiny, lock):
        lock.acquire()
        print("Flight ", flightId, " Arrived from ", destiny)
        time.sleep(5)
        lock.release()

#PARALEL METHOD TO DEPLOY, RECEIVED AND DELAY FLIGHTS
    def mainActions(self, flighList, destNameList, causeDelay, flig):
        for i in flighList:
            flighIt = multiprocessing.Value('i', flighList[i])
            destName = multiprocessing.Value('c', destNameList[i])
            lock = multiprocessing.Lock()
            if 3 >= i >= 6:
                dela = multiprocessing.Value('c', causeDelay[i])
                delay = multiprocessing.Process(target=flig.delay_flight, args=(flighIt, dela, destName, lock))
                delay.start()
                delay.join()
            deploy = multiprocessing.Process(target=flig.deploy_planes, args=(flighIt, destName, lock))
            deploy.start()
            deploy.join()

        for i in flighList:
            flighIt = multiprocessing.Value('i', flighList[i])
            destName = multiprocessing.Value('c', destNameList[i])
            lock = multiprocessing.Lock()
            received = multiprocessing.Process(target=flig.receivedPlanes, args=(flighIt, destName, lock))
            received.start()
            received.join()

#SET AIRLINE NAME
    def askFlight(self):
        self.setAirline(input("Insert the Name of the flight"))

    def concatenate(self):
        mycursor.execute("SELECT AirLine FROM flights")
        spc = mycursor.fetchall()
        for i in spc:
            flights.flighNames.append(i)

#QUERY TO SHOW THE FLIGHTS
    def showFlights(self):
        print("-----------------------------------------------------------------")
        mycursor.execute("SELECT FlightId, AirLine,pl.PlaneCode, StartDate, FinishDate,CountName,DestName, descrip FROM flights INNER JOIN plane as pl ON flights.PlaneCode = pl.PlaneCode INNER JOIN schedule ON flights.ScheduleCode = schedule.ScheduleCode INNER JOIN destinys ON flights.DestinyCode = destinys.DestinyCode INNER JOIN country ON destinys.CountryId = country.CountryId INNER JOIN status ON flights.StatusId = status.StatusId;")
        data = mycursor.fetchall()
        for i in data:
            print(i)
        print("-----------------------------------------------------------------")

#METHOD TO ASK SPACE IN A CERTAIN FLIGHT BY NAME
    def askSpace(self, name):
        mycursor.execute("SELECT SUM(Sits-Amount_Passengers) as spc FROM plane INNER JOIN flights ON flights.PlaneCode = plane.PlaneCode WHERE AirLine = '%s'" % name)
        spc = mycursor.fetchone()
        for i in spc:
            if i == 0:
                return False
            else:
                return True

#EXTRACT THE FLIGHT ID BY NAME
    def selectFlighId(self, Name):
        mycursor.execute("SELECT FlightId FROM flights WHERE AirLine = '%s'" % Name)
        spc = mycursor.fetchone()
        self.set_pId(int(spc[0]))

#METHOD TO UPDATE THE STATUS OF THE FLIGHT
    def updateStatusFlight(self, sta, FligId):
        select = "UPDATE flights SET StatusId= '%s' WHERE FlightId = '%s' "
        data = (sta, FligId)
        mycursor.execute(select, data)
        mydb.commit()
