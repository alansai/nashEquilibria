import random


# Author alansai
'''
    Represents a Rock Paper Scissors Player for Mod/Sim Fall 2026 Final Project (MBHS)
    A Player has an id (like "P1"), as well as preferences for 3 strategies (which sum to 1.0).
    and keeps track of how many numGamesPlayed they've played, plus their tot score and avg score.

    Inspiration drawn from the work done by Dr. Andrew Davison (PSU)

    sample usage: p1 = Player("P1")
'''


class rpsPlayer:
    def __init__(self, id):
        """
        Args: id
        Sets initial values of player object
        """
        self.id = id
        # rock, paper and scissors all start at 1/3
        self.prefs = [0.333, 0.333, 0.334]
        # number of games, total score, and average score which is totalScore/numGamesPlayed
        self.numGamesPlayed = 0
        self.totalScore = 0
        self.averageScore = 0.0
        self.history = []

    def getId(self):
        """
        Args: None
        Returns: id
        """
        return self.id

    def getPrefs(self):
        """
        Args: None
        Returns: prefs
        """
        return self.prefs

    def getStrategy(self):
        """
        Args: None
        Returns: what strategy is played for
        """
        r = random.random()
        if r < self.prefs[0]:
            return 0  # rock
        elif r < self.prefs[0] + self.prefs[1]:
            return 1  # paper
        else:
            return 2  # scissors

    def updateScore(self, score):
        """
        Args: score
        Updates total score
        """
        # updates score after preference
        self.totalScore += score
        self.numGamesPlayed += 1
        self.averageScore = self.totalScore / self.numGamesPlayed

    def updatePrefs(self, strategy_played, score):
        """
        Args: strategy_played, score
        Updates preferences and adds to prefs history
        """
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
        """
        Args: None
        Returns: string of preferences
        """
        a = self.prefs[0]
        b = self.prefs[1]
        c = self.prefs[2]
        return f"{self.id}: R:{a:.2f} P:{b:.2f} S:{c:.2f}"