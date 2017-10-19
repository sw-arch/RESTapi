class ticket:

    price = 0.0
    seat = 0
    
    def __init__(price, seat, self):
        self.price = price
        self.seat = seat

    def getPrice(self):
        return self.price

    def getSeat(self):
        return self.seat

    def setPrice(self, price):
        self.price = price

    def setSeat(self, seat):
        self.seat = seat
