class Card:
    def __init__(self, suite, number, value):
        self.suite = suite
        self.number = number
        self.value = value

    def getValue(self):
        return int(self.value)

    def __str__(self):
        return f"{self.number} of {self.suite}"
    def copyCard(self):
        return Card(self.suite, self.number, self.value)
    def showNumber(self):
        return self.number

def buildDeck():
  buildSuites = ["Hearts", "Diamonds", "Clubs", "Spades"]
  buildNumbers = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
  buildValues = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  deck = []

  for tempSuite in buildSuites:
    for tempNumbers in range(13):
        deck.append(Card(tempSuite, buildNumbers[tempNumbers], buildValues[tempNumbers]))
  return deck

