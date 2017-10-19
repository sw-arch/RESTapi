from .Ticket import Ticket


class Event:
    def __init__(self, eventName, description, seats, ticketPrice):
        self.eventName = eventName
        self.description = description
        self.tickets = list(self.generate_tickets(seats))
        self.ticketPrice = ticketPrice
        self.seatsReserved = 0

    def reserve_ticket(self):
        if self.seatsReserved < len(self.tickets):
            self.seatsReserved += 1
            return self.tickets[self.seatsReserved - 1]
        return None

    def generate_tickets(self, seats):
        for ticketNumber in range(seats):
            yield Ticket(self.ticketPrice, ticketNumber)
