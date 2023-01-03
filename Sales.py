from Clients import *
from flights import *
from Country import *
from Status import *
from Tickets import *
from Cost import *
from HoldUp import *
from Destinys import *
import datetime
import mysql.connector
#CONNECTION WITH THE DATABASE
try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='8908 ',
        port='3306',
        database='flightsale'
    )
    mycursor = mydb.cursor()
except:
    print("Please Check the connection with the Database")

#CLASS FOR SALES
class Sales(Clients):

#CONSTRUCTOR FOR SALES
    def __init__(self, saleId, Destiny_Code, description, Ticket_Day):
        self.saleId = saleId
        self.Destiny_Code = Destiny_Code
        self.description = description
        self.ticket_Day = Ticket_Day

#Setters
    def setSale_Id(self, sale_Id):
        self.saleId = sale_Id

    def setDestiny_Code(self, destiny_Code):
        self.Destiny_Code = destiny_Code

    def setDescription(self, description):
        self.description = description

    def setTicket_Day(self, ticket_Day):
        self.ticket_Day = ticket_Day

#Getters
    def getSale_Id(self):
        return self.saleId

    def getDestinyCode(self):
        return self.Destiny_Code

    def getDescription(self):
        return self.description

    def getTicketDay(self):
        return self.ticket_Day

    def gotTime(self):
        todaysDate = datetime.date.today()
        self.setTicket_Day(todaysDate)

#INSERT SALE INTO DATABASE
    def insertSale(self, passport, destinyCode, descrip, TicketId, Cost):
        sale = " INSERT INTO sales(Passport, DestinyCode, Description, SaleDate, TicketId, idCost) VALUES (%s,%s,%s,%s,%s, %s)"
        inser = (passport, destinyCode, descrip, self.getTicketDay(), TicketId, Cost)
        mycursor.execute(sale, inser)
        mydb.commit()
#PRINT THE RECEIPT
    def printfReceipe(self, passport):
        mycursor.execute("SELECT * FROM sales WHERE Passport = '%s'" % passport)
        spc = mycursor.fetchall()
        for i in spc:
            print(i)


#MAIN PROCESS FOR THE SALE OF THE TICKET
def saleTicket():
    option = 0
    while option < 4:
        #MESAGGE FOR THE MAIN
        print("=================================WELCOME TO FLIGHTS S.A===================================================")
        option = int(input("1.Buy Ticket\n2.Show Flights\n3.Specific Info\n4.Exit\nChoose:"))
        if option == 1:
            #CREATION OF OBJECTS
            obj = Clients("", "", 0, 0, "", "", 0, 0, 0)
            flig = flights(0, 0, "", "", 0, "", "", "", 0, 0, 0, "")
            sale = Sales(0, 0, "", "")
            count = Country("", 0)
            tk = Ticket(0, 0, 0)
            co = cost(0, 0, "")
            dest = Destinys(0, "")
            deley = HoldUp(0, "", "", "")
            sale.gotTime()
            #ASK THE FLIGHT BY NAME
            flig.concatenate()
            for i in flig.flighNames:
                print(i)
            flig.askFlight()
            #STORAGE THE FLIGTH NAME
            na = flig.getAirlineName()
            o = flig.OnHold
            #VERIFY THE SPACE OF THE FLIGHT
            if o != 10:
                if flig.askSpace(na):
                    #SELECT AND STORAGE THE FLIGHT ID
                    flig.selectFlighId(na)
                    f = flig.get_Flight_Id()
                    #ASK THE AMOUNT OF TICKETS
                    tk.askAmoun()
                    #PERSONAL INFORMATION OF THE PERSON
                    obj.askPersonalInfo()
                    obj.askInfo()
                    #ASK THE COUNTRY ID
                    count.askCount_Id()
                    #STABLISH THE SIT NUMBER
                    obj.staNum()
                    #GET THE COUNTRY ID INTO A VARIABLE
                    k = count.getCountryId()
                    #SEND THE INFO TO THE DATABASE
                    obj.sendPerson()
                    obj.insertPassenger(k, f)
                    print("----------------------------------------------------------------")
                    #STORAGE THE AMOUNT OF TICKETS IN A VARIABLE
                    h = tk.get_TickAmoun()
                    #PROCESS TO SEND THE TICKET
                    tk.sendTickt(f, h)
                    #SEARCH FOR THE TICKET ID BY FLIGHT ID
                    tk.selectTikId(f)
                    #GET THE ID COST OF THE FLIGHT
                    co.getIdcost(f)
                    #GET THE COUNTRY ID
                    contId = count.getCountryId()
                    #SEARCH FOR DESTINATION ID
                    dest.getDestId(contId)
                    #STORAGE THE VALUE OF THE DEST ID
                    des = dest.getDestCode()
                    #SOME IMPORTAN INFO TO THE SALES TABLE
                    Passport = obj.getPassport()
                    costId = co.getIdCost()
                    tikId = tk.get_TickId()
                    descrip = "Ticket Sale"
                    #TAKE TODAY'S DATE
                    sale.gotTime()
                    #INSERT INTO THE SALES TABLE
                    sale.insertSale(Passport, des, descrip, tikId, costId)
                    #METHOD TO PRINTF THE RECEIPT
                    sale.printfReceipe(Passport)
                    #METHOD TO UPDATE THE AMOUNT OF PEOPLE IN THE PLANE OF THE PLANE
                    flig.updatePlane(h, f)
                else:
                    print("----------------------------------------------------------------")
                    print("No free sits left, please choose another flight")
                    # SELECT THE FLIGHT ID WHEN IT IS FULL
                    flig.selectFlighId(na)
                    # VARIBLE TO STORAGE THAT ID
                    g = flig.get_Flight_Id()
                    # VARIABLE WITH THE STATUS ID OF READY
                    o = flig.Ready
                    # METHOD TO UPDATE THE PLANE STATUS
                    flig.updateStatusPlane(o, g)
                    # METHOD TO UPDATE THE FLIGHT STATUS
                    flig.updateStatusFlight(o, g)
                    # CALL TO SEARCH FOR THE DESTINY NAME
                    dest.searchDestName(g)
                    # STORAGE THE DESTINY NAME
                    destName = dest.getDestName()
                    # INSERT INTO LISTS THE FLIGHT ID AND THE DESTINATION
                    flig.flighList.append(g)
                    flig.destNameList.append(destName)
                    # flig.mainActions(flig.flighList, flig.destNameList, deley.Cause, flig)
                    print("----------------------------------------------------------------")
            else:
                print("------------------------------------------------")
                print("Flight Already deployed")
                print("------------------------------------------------")

        else:
            if option == 2:
                #SHOW THE FLIGHTS TO THE CLIENT
                hg = flights(0, 0, "", "", 0, "", "", "", 0, 0, "", 0)
                hg.showFlights()
            else:
                if option == 3:
                    select = 0
                    while select < 5:
                        print("----------------------------------------------------------------")
                        select = int(input("1.Clients per Flight\n2. Planes Ready To  Flight\n3.Planes Arrived\n4.Planes Delayed\n5.Go back"))
                        if select == 1:
                            print("----------------------------------------------------------------")
                            cl = Clients("", "", 0, 0, "", "", 0, 0, 0)
                            cl.clientsPerFligh()
                            print("----------------------------------------------------------------")
                        else:
                            if select == 2 or select == 3:
                                print("----------------------------------------------------------------")
                                St = Status(0, "", '')
                                St.searchForId()
                                id = St.get_StatusId()
                                pl = Plane(0, 0, '', 0, "", "")
                                pl.planesBy(id)
                                print("----------------------------------------------------------------")
                            else:
                                if select == 4:
                                    print("----------------------------------------------------------------")
                                    pl = Plane(0, 0, '', 0, "", "")
                                    pl.planesDelayed()
                                    print("----------------------------------------------------------------")


saleTicket()



