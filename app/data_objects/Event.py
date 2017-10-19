from .Ticket import Ticket


class Event:
    def __init__(self, name, description, numberOfSeats, ticketPrice):
        self.eventName = name
        self.description = description
        self.ticketsAvailable = set(self._generate_tickets(numberOfSeats))
        self.ticketsReserved = dict()
        self.ticketPrice = ticketPrice

    def reserve_ticket(self):
        if self.ticketsAvailable:
            ticket = self.ticketsAvailable.pop()
            self.ticketsReserved[ticket.ticketNumber] = ticket
            return ticket
        return None

    def refund_ticket(self, ticketNumber):
        if ticketNumber in self.ticketsReserved:
            ticket = self.ticketsReserved.pop(ticketNumber)
            self.ticketsAvailable.add(ticket)
            return True
        return False

    def _generate_tickets(self, seats):
        for ticketNumber in range(seats):
            yield Ticket(self.ticketPrice, ticketNumber)
