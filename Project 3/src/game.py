
from array import array
import imp
from itertools import count
import random
from re import A
import numpy as np
import matplotlib.pyplot as plt
import math





class Game:
    def __init__(self, levels):
        # Get a list of strings as levels
        # Store level length to determine if a sequence of action passes all the steps

        self.n = 200
        self.miu = int(self.n / 2)
        self.lamda = int(self.miu * 7)
        self.levels = levels
        self.current_level_index = 0
        self.current_level_len = len(self.levels[self.current_level_index])
        self.population = self.primary_population()
        self.parents = None
        self.children = None
        self.x_axis = []
        self.y_axis_best = []
        self.y_axis_mean = []
        self.y_axis_worst = []
        
    
    def load_next_level(self):
        self.current_level_index += 1
        self.current_level_len = len(self.levels[self.current_level_index])
        self.population = self.primary_population()
    
    def get_score(self, actions):
        # Get an action sequence and determine the steps taken/score
        # Return a tuple, the first one indicates if these actions result in victory
        # and the second one shows the steps taken

        current_level = self.levels[self.current_level_index]
        steps = 0
        for i in range(self.current_level_len - 1):
            current_step = current_level[i]
            if (current_step == '_'):
                steps += 1
            elif (current_step == 'G' and actions[i - 1] == '1'):
                steps += 1
            elif (current_step == 'L' and actions[i - 1] == '2'):
                steps += 1
            else:
                break
        return steps == self.current_level_len - 1, steps

    def get_score2(self, actions):

        sequance_len = []

        current_level = self.levels[self.current_level_index]
        steps = 0
        extra = 0
        for i in range(self.current_level_len - 1):
            current_step = current_level[i]
            if (current_step == '_'):
                steps += 1
                if (actions[i - 1] == '1'):
                    extra -= 0.5
            elif (current_step == 'G' and actions[i - 1] == '1'):
                steps += 1
            elif (current_step == 'L' and actions[i - 1] == '2'):
                steps += 1
            elif (current_step == 'M'):
                steps += 1
                if (actions[i - 1] != '1'):
                    extra += 2
            elif(current_step == 'G' and actions[i - 1] == '0' and actions[i - 2] == '1' and steps > 0):
                steps += 1
                extra += 2
            else:
                sequance_len.append(steps)
                steps = 0
            

        sequance_len.append(steps)

        bonus = max(sequance_len)
        isWin = bonus == self.current_level_len - 1
        if isWin:
            bonus += 5
        if (actions[self.current_level_len - 1] == '1'):
            bonus += 1
        bonus += extra

        return bonus

        
        


    
    def primary_population(self):
        n = self.n
        coroms = [[0 for i in range(self.current_level_len)] for j in range(n)]
        
        for i in range(n):
            for j in range(self.current_level_len):
                x = int(random.random() * 10) % 3
                coroms[i][j] = str(x)

        return coroms
    

    def selection(self):
        population = self.population
        scores = []
        n = self.n
        for i in range(n):
            scores.append(self.get_score2(population[i]))
        arr = np.sort(scores)
        sorted_scores = arr[::-1]

        parents = []
        for score in sorted_scores:
            for i in range(n):
                if self.get_score2(population[i]) == score :
                    parents.append(population[i])
                if len(parents) == (n / 2):
                    break
            if len(parents) == (n / 2):
                    break
        
        self.parents = parents
        return(parents)
            


    def crossover(self):
        children = []
        for i in range(self.lamda):
            x = random.randint(0, self.miu -1)
            y = random.randint(0, self.miu -1)
            firstParent = self.parents[x]
            secondParent = self.parents[y]
            child = []
            for j in range(self.current_level_len):
                z = random.random()
                if(z > 0.5):
                    child.append(firstParent[j])
                else:
                    child.append(secondParent[j])
            children.append(child)

        self.children = children


    def mutation(self):
        mutatedChildren = []
        for child in self.children:
            newChild = []
            for gen in child:
                c = random.random()
                if (c < 0.2):
                    if gen == '1' or gen == '2':
                        newChild.append('0')
                    else: newChild.append(gen)
                else: newChild.append(gen)
            mutatedChildren.append(newChild)
        
        self.children = mutatedChildren


    def mutation2(self):
        mutatedChildren = []
        for child in self.children:
            newChild = []
            for gen in child:
                c = random.random()
                if (c < 0.2):
                    p = int(random.random() * 3)
                    if p == 0:
                        newChild.append('0')
                    if p == 1:
                        newChild.append('1')
                    if p == 2:
                        newChild.append('2')

                else: newChild.append(gen)
            mutatedChildren.append(newChild)
        
        self.children = mutatedChildren



    def survivors(self):
        children = self.children
        scores = []
        for i in range(self.lamda):
            scores.append(self.get_score2(children[i]))
        arr = np.sort(scores)
        newarr = []
        for i in arr:
            if not(i in newarr):
                newarr.append(i)
        sorted_scores = newarr[::-1]

        sortedChildren = []
        for score in sorted_scores:
            for i in range(self.lamda):
                if self.get_score2(children[i]) == score :
                    sortedChildren.append(children[i])
        
        parents = []
        rw = []
        for i in range(len(sortedChildren)):
            j = int((1 / (i + 1)) * 1000)
            for k in range(j):
                rw.append(i + 1)
        l = len(rw)
        for i in range(self.miu):
            x = int(random.random() * l)
            y = rw[x] - 1
            parents.append(sortedChildren[y])
        

        for i in range(self.miu):
            scores.append(self.get_score2(parents[i]))
        arr = np.sort(scores)
        newarr = []
        for i in arr:
            if not(i in newarr):
                newarr.append(i)
        sorted_scores = newarr[::-1]
        
        sortedParents = []
        for score in sorted_scores:
            for i in range(self.miu):
                if self.get_score2(parents[i]) == score :
                    sortedParents.append(parents[i])
        
        currentScore = self.get_score2(sortedParents[0])
        count = 0
        for parent in sortedParents:
            if (self.get_score2(parent) == currentScore):
                count += 1
            else:
                count = 0
                currentScore = self.get_score2(parent)

        self.parents = sortedParents
        



    def childrenEval(self):
        meanValue = 0
        for child in self.children:
            meanValue += self.get_score2(child)
        meanValue /= self.lamda
        
        return meanValue
    
    def bestvalue(self):
        maxValue = 0
        for child in self.children:
            if (self.get_score2(child) > maxValue):
                maxValue = self.get_score2(child)
        
        return maxValue
    
    def worstvalue(self):
        minValue = math.inf
        for child in self.children:
            if (self.get_score2(child) < minValue):
                minValue = self.get_score2(child)
        
        return minValue

    
    
    
    
    def control(self):
        values = []
        self.selection()
        for i in range(20):
            self.x_axis.append(i)
            self.crossover()
            self.mutation2()
            maxValue = self.bestvalue()
            meanValue = self.childrenEval()
            minValue = self.worstvalue()
            self.y_axis_best.append(maxValue)
            self.y_axis_mean.append(meanValue)
            self.y_axis_worst.append(minValue)
            print("///////////////")
            print("maxValue: " + str(maxValue))
            self.survivors()
        print("solution: " + str(self.findBest()))
        

        
    def plot(self):
        plt.plot(self.x_axis, self.y_axis_best, label = "best value")
        plt.plot(self.x_axis, self.y_axis_mean, label = "mean value")
        plt.plot(self.x_axis, self.y_axis_worst, label = "worst value")
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('My graph!')
        plt.legend()
        plt.show()


    def findBest(self):
        value = 0
        bestChild = []
        for child in self.children:
            if (self.get_score2(child) > value):
                bestChild = child
                value = self.get_score2(child)
        return bestChild













g = Game(["__M_____", "____G_____", "__G___L_", "__G__G_L___", "____G_ML__G_", "____G_MLGL_G_", "_M_M_GM___LL__G__L__G_M__", "____G_G_MMM___L__L_G_____G___M_L__G__L_GM____L____", "___M____MGM________M_M______M____L___G____M____L__G__GM__L____ML__G___G___L___G__G___M__L___G____M__", "_G___M_____LL_____G__G______L_____G____MM___G_G____LML____G___L____LMG___G___GML______G____L___MG___"])
level = 5
for i in range(level - 1):
    g.load_next_level()


g.control()
g.plot()

