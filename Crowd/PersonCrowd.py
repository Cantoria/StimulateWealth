import numpy as np
import random as rand
from Person import Person
from Draw import DrawCrowd


class PersonCrowd:
    def __init__(self, person_num=10000):
        self.person_num = person_num
        self.crowd = []
        for i in range(person_num):
            self.crowd.append(Person(id = i))

    def iteration(self):
        for i in range(self.person_num):
            while True:
                give_id = rand.randint(0, self.person_num - 1)
                if give_id != self.crowd[i].id:
                    break
            self.crowd[give_id].receive(self.crowd[i].give())

    def summary(self):
        d = DrawCrowd(self)
        d.sort_and_draw()





