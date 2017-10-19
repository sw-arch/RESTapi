class Ticket:
    def __init__(self, price, seat):
        self.price = price
        self.seat = seat

    def get_price(self):
        return self.price

    def get_seat(self):
        return self.seat

    def set_price(self, price):
        if price > 0:
            self.price = price
            return True
        return False

    def set_seat(self, seat):
        if seat is not None:
            self.seat = seat
            return True
        return False
