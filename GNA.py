from graphics import color_rgb
from random import randint
from Vec import Vec
from WindowSingleton import WindowSingleton

class GNA:

    def __init__(self, dt, numFamilies, totalPopulation, PopulateCLS, stdDev, reverseScoring=True):
        self.populates = []
        self.goalPopulation = totalPopulation
        self.totalTime = 0
        self.dt = 0
        self.numFamilies = numFamilies
        self.PopulateCLS = PopulateCLS
        self.populatesDead = 0
        self.reverseScoring = reverseScoring
        self.stdDev = stdDev
        self.gen = 0

        for i in range(self.numFamilies):
            color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
            p = self.PopulateCLS.createNew(dt, color)
            self.populates.append([p])
            for _ in range(self.goalPopulation // self.numFamilies):
                n = self.PopulateCLS.createFrom(p, self.stdDev)
                self.populates[i].append(n)
                
        self.populationSize = sum([len(i) for i in self.populates])

    def createNextGeneration(self):
        newPopulates = []
        # create list of average distance from hole per family
        avgDists = []
        indexes = []
        for i in range(self.numFamilies):
            avgDists.append(sum([x.getScore() for x in self.populates[i]]))
            
        avgDistsSorted = [i for i in avgDists]
        avgDistsSorted.sort(reverse=self.reverseScoring)
        for i in avgDistsSorted:
            indexes.append(avgDists.index(i))
            

        for i in range(self.numFamilies):
            self.populates[i].sort(
                key=lambda x: x.getScore(), reverse=self.reverseScoring)
            tempPopulates = []
            
            avgVel = Vec(0, 0, 0)
            
            top10p = (self.goalPopulation // self.numFamilies) // 10
            for j in range(top10p):
                avgVel += self.populates[i][j].veli
                
            avgVel /= top10p
            
            if self.numFamilies > 1:
                # get best ball and deviate family from that
                for _ in range(self.goalPopulation // (self.numFamilies - 1)):
                    tempPopulates.append(self.PopulateCLS.createFrom(self.populates[i][0], self.stdDev, avgVel))
            else:
                for _ in range(self.goalPopulation):
                    tempPopulates.append(self.PopulateCLS.createFrom(self.populates[i][0], self.stdDev, avgVel))
            
            newPopulates.append(tempPopulates)
            
        newPopulates = [newPopulates[i] for i in indexes]
        
        self.populationSize = sum([len(i) for i in newPopulates])
        
        print()
        print("Generation: " + str(self.gen))
        print("Best velocity: " + str(newPopulates[0][0].veli))
        print()
        
        self.populates = newPopulates
            
        self.gen += 1
        self.populatesDead = 0

    def __call__(self):
        for family in self.populates:
            for populate in family:
                died = populate()  # could replace with just "if i()"
                if died:
                    self.populatesDead += 1
                    # print(str(self.populatesDead) + "/" + str(self.populationSize))

        if self.populatesDead == self.populationSize:
            self.createNextGeneration()
            self.stdDev /= 1.1
            self.numFamilies -= 1
            if self.stdDev < 0.05:
                self.stdDev = 0.05
                
        # if WindowSingleton().instance().checkMouse():
        #     self.createNextGeneration()
        #     self.stdDev /= 1.25
        #     self.numFamilies -= 1
        #     if self.stdDev < 0.025:
        #         self.stdDev = 0.025
        self.totalTime += self.dt
