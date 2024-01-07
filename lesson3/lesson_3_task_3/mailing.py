from lesson3.lesson_3_task_3.address import Address


class Mailing:
    cost = 250
    to_address: Address
    from_address: Address

    def __init__(self, from_address, to_address, track):
        self.to_address = to_address
        self.from_address = from_address
        self.track = track

    def set_cost(self, cost):
        self.cost = cost
