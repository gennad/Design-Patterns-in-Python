class AbstractGame:
     """An abstract class that is common to several games in which
     players play against the others, but only one is playing at a
     given time.
     """
     def __init__(self, *args, **kwargs):
         if self.__class__ is AbstractGame:
             raise TypeError('abstract class cannot be instantiated')

     def playOneGame(self, playersCount):
         self.playersCount = playersCount
         self.initializeGame()
         j = 0
         while not self.endOfGame():
             self.makePlay(j)
             j = (j + 1) % self.playersCount
         self.printWinner()

     def initializeGame(self):
         raise TypeError('abstract method must be overridden')

     def endOfGame(self):
         raise TypeError('abstract method must be overridden')

     def makePlay(self, player_num):
         raise TypeError('abstract method must be overridden')

     def printWinner(self):
         raise TypeError('abstract method must be overridden')


# Now to create concrete (non-abstract) games, you subclass AbstractGame
# and override the abstract methods.

class Chess(AbstractGame):
     def initializeGame(self):
         # Put the pieces on the board.
         pass

     def makePlay(player):
         # Process a turn for the player
         pass

# --------- Alex's Martelli example ---------

class AbstractBase(object):
    def orgMethod(self):
        self.doThis()
        self.doThat()

class Concrete(AbstractBase):
    def doThis(self):
        pass
    def doThat(self):
        pass
