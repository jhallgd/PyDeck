import random
import Card

class black_jack():

    #When a game is initiated.
    def __init__(self, chips):
        self.unplayedDeck = []
        self.playedDeck = []
        self.dealerHand = []
        self.playerHand = []
        self.splitHand = []
        self.playerChips = chips
        self.playerBet = 0
        self.gameOver = True
        self.playerDone = False

    #Starts the game, and build and shuffle the decks.  
    def startGame(self, decksAmount):
        for x in range(int(decksAmount)):
            self.unplayedDeck.extend(Card.buildDeck())
    
    #Setups a new game
    def gameSetup(self, betAmount):
        self.gameOver = False
        self.playerBet = betAmount
        self.playerChips = self.playerChips - betAmount
        self.giveCard("player")
        self.giveCard("dealer")
        self.giveCard("player")
        self.giveCard("dealer")


#Get functions

    #Get Dealer Hand
    def getDealerHand(self):
        if(self.playerDone):
            return self.dealerHand
        else:
            showhand = [self.dealerHand[0], "????"]
            return showhand
    
    #Get Player Hand
    def getPlayerHand(self):
        return self.playerHand

    #Get Options
    def getOptions(self):
        options = ["Hit", "Stand"]
        if len(self.playerHand) == 2:
            options.append("Double")
            if self.playerHand[0].showNumber() == self.playerHand[1].showNumber():
                options.append("Split")
        return options
    
    def checkPlayerDone(self):
        return self.playerDone

    def getPlayerChips(self):
        return self.playerChips
    
    def getPlayerBet(self):
        return self.playerBet

    def checkPlayerBust(self):
        self.showPlayerHand()
        print("You Busted!")
        self.checkGameOver()

    def checkGameOver(self):
        if self.playerChips == 0:
            self.gameOver = True

    def countDealerHand(self):
        count = 0
        if(self.playerDone):
            for dh in self.dealerHand:
                count = count + dh.getValue()
        else:
            count = self.dealerHand[0].getValue()
        return count


    def countPlayerHand(self):
        count = 0
        for dh in self.playerHand:
            count = count + dh.getValue()
        if count > 21:
            count = 0
            for rdh in self.playerHand:
                if rdh.getValue() == 11:
                    count = count + 1
                else:
                    count = count + rdh.getValue()
        return count


    def cardCleanup(self):
        self.playerHand.clear()
        self.dealerHand.clear()
        self.gameSetup()

    def findWinner(self):
        self.playerChips
        self.playerBet
        print("  ")
        if self.countDealerHand() == self.countPlayerHand():
            self.playerChips = self.playerChips + self.playerBet
            print("Push")
        elif self.countDealerHand() > 21:
            print("Player Wins")
            self.playerChips = self.playerChips + (self.playerBet * 2)
        elif self.countDealerHand() > self.countPlayerHand():
            print("Dealer Wins")
        else:
            print("Player Wins")
            self.playerChips = self.playerChips + (self.playerBet * 2)
        print("  ")
        self.checkGameOver()


    # Dealer Decides what to do
    def dealerPlay(self):
        score = self.countDealerHand()
        if score <= 17:
            return "Hit"
        else:
            return "Stand"



    def showPlayerHand(self):
        self.showChips()
        print("Player Hand:")
        playerScore = 0
        for x in self.playerHand:
            playerScore = playerScore + x.getValue()
            print(x)
        print("Total: " + str(playerScore))
        print("  ")


    def checkBet(self, betAmount):
        if betAmount <= self.playerChips and betAmount > 0:
            return True
        return False

    
    
    #Player Actions
    
    #Hit
    def playerHit(self):
        self.giveCard("player")
    
    #Stand
    def playerStand(self):
        self.playerDone = True
    
    #Double
    def playerDouble(self):
        self.playerChips = self.playerChips - self.playerBet
        self.playerBet = self.playerBet * 2
        self.giveCard("player")
        self.playerDone = True

    

    
    def playGame(self):
        check = 0
        print("Dealer Hand:")
        print("????")
        print(self.dealerHand[0])
        print("  ")
        self.showPlayerHand()
        print("What would you like to do?")
        gameOptions = self.getOptions()
        for o in gameOptions:
            print(o)
        playerChoice = input("Choice:")
        for oTwo in gameOptions:
            if oTwo == playerChoice:
                check = check + 1
        if check == 0:
            print("Please try Again")
            self.playGame()
        if playerChoice == "Hit":
            self.giveCard("player")
            if self.countPlayerHand() <= 21:
                self.playGame()
            else:
                self.checkPlayerBust()
        elif playerChoice == "Stand":
            self.dealerPlay()
        elif playerChoice == "Double":
            if self.checkBet(self.playerBet):
                self.playerChips = self.playerChips - self.playerBet
                self.playerBet = self.playerBet * 2
                self.giveCard("player")
                self.showPlayerHand()
                self.dealerPlay()
            else:
                print("You don't have enough to double")
                self.playGame()

    def giveCard(self, target):
        card = random.randrange(0, len(self.unplayedDeck)-1, 1)
        tempCard = self.unplayedDeck[card]
        if target == "dealer":
            self.dealerHand.append(tempCard)
        else:
            self.playerHand.append(tempCard)
        del self.unplayedDeck[card]