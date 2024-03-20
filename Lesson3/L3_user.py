class User:
    def __init__(self, first_name, last_name):
        print("создано")
        self.first = first_name
        self.last = last_name

    def first_name(self):
        print(self.first)

    def last_name(self):
        print(self.last)

    def full_name(self):
        print(self.first, self.last )