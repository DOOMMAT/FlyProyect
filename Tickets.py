import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8908',
    port='3306',
    database='flightsale'
)
mycursor = mydb.cursor()


#CLASS FOR TICKETS
class Ticket:

#CONSTRUCTOR FOR TICKETS
    def __init__(self, id, sale, Amount):
        self.TickId = id
        self.saleId = sale
        self.AmountTick = Amount

#SETTERS
    def set_TickId(self, id):
        self.TickId = id

    def set_SaleId(self, sale):
        self.saleId = sale

    def set_TickAmount(self, amount):
        self.AmountTick = amount

#GETTERS
    def get_TickId(self):
        return self.TickId

    def get_SaleId(self):
        return self.saleId

    def get_TickAmoun(self):
        return self.AmountTick

#SET THE AMOUNT OF TICKETS
    def askAmoun(self):
        self.set_TickAmount(int(input("How Many Tickets do you wish to buy?: ")))

#QUERY FOR THE TICKET
    def sendTickt(self, flightId, amount):
        ins = "INSERT INTO tickets(FlightId, Amount_Tickets) VALUES (%s, %s)"
        tick = (flightId, amount)
        mycursor.execute(ins, tick)
        mydb.commit()
        print("Ticket sold")
#QUERY FOR SELECT THE TICKET ID
    def selectTikId(self, flightId):
        mycursor.execute("SELECT TicketId FROM tickets WHERE FlightId = '%s'" % flightId)
        spc = mycursor.fetchone()
        self.set_TickId(int(spc[0]))
