import random


class rpsPlayer:
    def __init__(self, id):
        self.id = id
        # rock, paper and scissors all start at 1/3
        self.prefs = [0.333, 0.333, 0.334]
        # number of games, total score, and average score which is totalScore/numGamesPlayed
        self.numGamesPlayed = 0
        self.totalScore = 0
        self.averageScore = 0.0
        self.history = []

    def getId(self):
        return self.id

    def getPrefs(self):
        return self.prefs

    def getStrategy(self):
        r = random.random()
        if r < self.prefs[0]:
            return 0  # rock
        elif r < self.prefs[0] + self.prefs[1]:
            return 1  # paper
        else:
            return 2  # scissors

    def updateScore(self, score):
        # updates score after preference
        self.totalScore += score
        self.numGamesPlayed += 1

    def updatePrefs(self, strategy_played, score):
        # Increase the played strategy, decrease others equally
        for i in range(3):
            if (self.prefs[i] != 1.0 or self.prefs[i] != 0.0):
                if i == strategy_played:
                    self.prefs[i] += (score - self.averageScore) / 100.0
                else:
                    self.prefs[i] -= (score - self.averageScore) / 200.0
                if self.prefs[i] > 1.0:
                    self.prefs[i] = 1.0
                elif self.prefs[i] < 0.0:
                    self.prefs[i] = 0.0
        # ensure sums up to 1.0
        total = self.prefs[0] + self.prefs[1] + self.prefs[2]
        self.prefs[0] = self.prefs[0] / total
        self.prefs[1] = self.prefs[1] / total
        self.prefs[2] = 1.0 - self.prefs[1] - self.prefs[0]
        new = []
        new.append(self.prefs[0])
        new.append(self.prefs[1])
        new.append(self.prefs[2])
        self.history.append(new)
#        print(new)

    def __str__(self):
        a = self.prefs[0]
        b = self.prefs[1]
        c = self.prefs[2]
        return f"{self.id}: R:{a:.2f} P:{b:.2f} S:{c:.2f}"