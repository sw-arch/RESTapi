from .Ticket import Ticket

class Event:
    def __init__(self, eventName, description, seats):
        self.eventName = eventName
        self.description = description
        self.seats = seats
        self.seatsLeft = seats

    def reserve_ticket(self):
        if self.seatsLeft > 0:
            self.seatsLeft -= 1
            return True
        else:
            return False
