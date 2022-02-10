import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.hatDict = kwargs
        self.contents = list()

        for i in self.hatDict.keys():
            for j in range(self.hatDict[i]):
                self.contents.append(i)
        print(self.contents)

    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            return self.contents

        drawnList = list()
        temp_contents = self.contents.copy()
        for i in range(num_balls_drawn):
            luckyNum = int(random.uniform(0,len(temp_contents)))
            drawnList.append(temp_contents[luckyNum])
            temp_contents.remove(temp_contents[luckyNum])
        return drawnList


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0

