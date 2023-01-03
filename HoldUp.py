import mysql.connector
import datetime
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8908',
    port='3306',
    database='flightsale'
)
mycursor = mydb.cursor()


class HoldUp:
    Cause = ["Wheater", "Mechanic Issues", "Runway Obstruction"]

    def __init__(self, delaycode, description, startdate, finisdate):
        self.delay_Code = delaycode
        self.description = description
        self.start_Date = startdate
        self.finish_Date = finisdate

#SETTERS
    def setDelay_Code(self, code):
        self.delay_Code = code

    def setDescription(self, descrip):
        self.delay_Code = descrip

    def set_start_Date(self, sDate):
        self.start_Date = sDate

    def set_finish_Date(self, fDate):
        self.finish_Date = fDate

#GETTERS
    def get_delay_code(self):
        return self.delay_Code

    def getDescription(self):
        return self.description

    def get_star_Date(self):
        return self.start_Date

    def get_Finish_Date(self):
        return self.finish_Date

    def Dates(self):
        startDate = datetime.date.today()
        finishDate = datetime.date.today()
        self.set_start_Date(str(startDate))
        self.set_finish_Date(str(finishDate))
#INSERTS IN CASE OF DELAYS

    def insertDelays(self, fligid):
        insert = "INSERT INTO delay(FlightId, description, startDate, finishDate) VALUES (%s,%s,%s,%s)"
        datos = (fligid, self.getDescription(), self.get_star_Date(), self.get_Finish_Date())
        mycursor.execute(insert, datos)
        mydb.commit()
        print("Data Inserted")
