

class Person:
    def __init__(self, id, wealth = 1000, give_moneygit = 1, crowd_num = 10000):
        self.id = id
        self.wealth = wealth
        self.give_money = give_money
        self.crowd_num = crowd_num


    def give(self):
        self.wealth -= self.give_money
        return self.give_money

    def receive(self, receive_money):
        self.wealth += receive_money
