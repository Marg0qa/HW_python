from L3_address import Address
class Mailing:
    def __init__(self, to_address, from_address, track, cost):
        self.address = to_address
        self.f_address = from_address
        self.track = track
        self.cost = cost
        