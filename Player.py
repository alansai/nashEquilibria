import random


# Author alansai
'''
    Represents a Player for Mod/Sim Fall 2026 Final Project (MBHS)
    A Player has an id (like "P1"), as well as preferences for 2 strategies (which sum to 1.0).
    and keeps track of how many numGamesPlayed they've played, plus their tot score and avg score.

    Inspiration drawn from the work done by Dr. Andrew Davison (PSU)

    sample usage: p1 = Player("P1")
'''


class Player:
    def __init__(self, id):
        """
        Args: id
        Sets initial values of player object
        """
        self.id = id
        # Create preferences as (0.5, 0.5 at beginning)
        self.prefs = [0.5, 0.5]
        self.currentGameScore = 0
        # number of games, total score, and average score which is totalScore/numGamesPlayed
        self.numGamesPlayed = 0
        self.totalScore = 0.0
        self.averageScore = 0.0
        # history of preferences as list to be plotted
        self.history = []
        self.history2 = []

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
        # randomly selects strategy through preference
        if random.random() < self.prefs[0]:
            return 0
        else:
            return 1

    def updateScore(self, score):
        """
        Args: score
        Updates total score
        """
        # updates score after preference
        self.totalScore += score
        self.numGamesPlayed += 1

    def updatePrefs(self, strategy, score):
        """
        Args: strategy_played, score
        Updates preferences and adds to prefs history
        """
        # utilizes formula to get new preference, makes sure it is within boundaries
        if (self.prefs[0] != 1.0 or self.prefs[1] != 1.0):
            if strategy == 0:
                self.prefs[0] = self.prefs[0] + (score - self.averageScore) / 100
                if self.prefs[0] > 1.0:
                    self.prefs[0] = 1.0
                elif self.prefs[0] < 0.0:
                    self.prefs[0] = 0.0
                self.prefs[1] = 1.0 - self.prefs[0]
            else:
                self.prefs[0] = self.prefs[0] - (score - self.averageScore) / 100
                if self.prefs[0] > 1.0:
                    self.prefs[0] = 1.0
                elif self.prefs[0] < 0.0:
                    self.prefs[0] = 0.0
                self.prefs[1] = 1.0 - self.prefs[0]
#        print(self.prefs[0])
        # updates average
        self.averageScore = self.totalScore / self.numGamesPlayed
        self.history.append(self.prefs[0])
        self.history2.append(self.prefs[1])

    # for final preferences
    def __str__(self):
        """
        Args: None
        Returns: string of preferences
        """
        a = self.prefs[0]
        b = 1.0 - a
        return f"{self.id}: <{a:.2f}, {b:.2f}>"
