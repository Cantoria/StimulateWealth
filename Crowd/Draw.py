import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np



class DrawCrowd:
    def __init__(self, personcrowd):
        self.personcrowd = personcrowd
    def sort_and_draw(self):
        crowd_array = self.personcrowd.crowd.copy()
        crowd_array.sort(key=lambda x:x.wealth,reverse=False)
        wealth = [x.wealth for x in crowd_array]
        n = np.arange(self.personcrowd.person_num)
        plt.bar(n, wealth,facecolor='#9999ff', edgecolor='white')
        for x, y in zip(n, wealth):
            # ha: horizontal alignment
            # va: vertical alignment
            plt.text(x + 0.4, y + 0.05, '%d' % y, ha='center', va='bottom')
        plt.show()
        plt.savefig("one.png")