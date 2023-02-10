class GNA:

    def __init__(self, dt, numFamilies, totalPopulation, PopulateCLS, stdDev, reverseScoring=True):
        self.populates = []
        self.populationSize = totalPopulation
        self.totalTime = 0
        self.dt = 0
        self.numFamilies = numFamilies
        self.PopulateCLS = PopulateCLS
        self.populatesDead = 0
        self.reverseScoring = reverseScoring
        self.stdDev = stdDev
        self.gen = 0

        for i in range(self.numFamilies):
            p = self.PopulateCLS.createNew(dt)
            self.populates.append([p])
            for _ in range(self.populationSize // self.numFamilies):
                n = self.PopulateCLS.createFrom(dt)
                self.populates[i].append(n)

    def createNextGeneration(self):
        new_populates = []
        # create list of average distance from hole per family
        avgDists = []
        for i in range(self.numFamilies):
            self.populates[i].sort(
                key=lambda x: x.getScore(), reverse=self.reverseScoring)
            avgDists.append(sum([x.getScore() for x in self.populates[i]]) / (self.populationSize // self.numFamilies))
            tempPopulates = []
            
            # get best ball and deviate family from that
            for _ in range(self.populationSize // self.numFamilies):
                tempPopulates.append(self.PopulateCLS.createFrom(self.populates[i][0], self.stdDev))
                
            new_populates.append(tempPopulates)

        print()
        print("Generation: " + str(self.gen))
        print("Best velocity: " + str(self.populates[0].veli))
        print("Loss: " + str(self.populates[0].getScore()))
        print()
        self.gen += 1

        self.populatesDead = 0

        self.populates = tempPopulates

    def __call__(self):
        for populate in self.populates:
            died = populate()  # could replace with just "if i()"
            if died:
                self.populatesDead += 1

        if self.populatesDead == self.populationSize:
            self.createNextGeneration()
            self.stdDev /= 2
        self.totalTime += self.dt
