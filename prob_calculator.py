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

    # def draw(self, num_balls_drawn):
    #     if num_balls_drawn > len(self.contents):
    #         return self.contents
    #
    #     drawnList = list()
    #     for i in range(num_balls_drawn):
    #         luckyNum = int(random.uniform(0,len(self.contents)))
    #         drawnList.append(self.contents[luckyNum])
    #         self.contents.remove(self.contents[luckyNum])
    #     return drawnList

    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            return self.contents
        drawnList = list()
        temp_contents = self.contents.copy()
        for i in range(num_balls_drawn):
            luckyNum = random.randint(0,len(temp_contents)-1)
            drawnList.append(temp_contents[luckyNum])
            temp_contents.remove(temp_contents[luckyNum])
            # print(len(temp_contents))
        return drawnList


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0

    for i in range(num_experiments):
        expected_balls_temp = expected_balls.copy()
        drawList = hat.draw(num_balls_drawn)
        drawDict = dict()
        for j in drawList:
            drawDict[j] = drawDict.get(j,0) + 1

        for k in expected_balls.keys():
            if expected_balls_temp[k] - drawDict.get(k,0) <=0:
                expected_balls_temp[k] = 0

        if sum(expected_balls_temp.values()) == 0:
            probability += 1

    return probability/num_experiments




