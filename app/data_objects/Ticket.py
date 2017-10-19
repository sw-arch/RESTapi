class Ticket:
    def __init__(self, price, seat):
        self.ticketNumber = seat
        self.price = price

    def to_json(self):
        return {
            'ticket_number': self.ticketNumber,
            'price': self.price,
        }
