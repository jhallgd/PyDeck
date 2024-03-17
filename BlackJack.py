import random
import Card

unplayedDeck = []
playedDeck = []
dealerHand = []
playerHand = []
splitHand = []
playerChips = 0
playerBet = 0


def getOptions():
    options = ["Hit", "Stand"]
    if len(playerHand) == 2:
        options.append("Double")
        if playerHand[0].showNumber() == playerHand[1].showNumber():
            options.append("Split")
    return options

def showChips():
    global playerChips
    print("Player Chips: " + str(playerChips))

def checkPlayerBust():
    showPlayerHand()
    print("You Busted!")
    checkGameOver()

def checkGameOver():
    global playerChips
    if playerChips == 0:
        print("Game Over you Lost")
    else:
        cardCleanup()

def showDealerHand():
    for dh in dealerHand:
        print(dh)


def countDealerHand():
    count = 0
    for dh in dealerHand:
        count = count + dh.getValue()
    return count


def countPlayerHand():
    count = 0
    for dh in playerHand:
        count = count + dh.getValue()
    if count > 21:
        count = 0
        for rdh in playerHand:
          if rdh.getValue() == 11:
              count = count + 1
          else:
              count = count + rdh.getValue()
    return count


def cardCleanup():
    playerHand.clear()
    dealerHand.clear()
    gameSetup()


def findWinner():
    global playerChips
    global playerBet
    print("  ")
    if countDealerHand() == countPlayerHand():
        playerChips = playerChips + playerBet
        print("Push")
    elif countDealerHand() > 21:
        print("Player Wins")
        playerChips = playerChips + (playerBet * 2)
    elif countDealerHand() > countPlayerHand():
        print("Dealer Wins")
    else:
        print("Player Wins")
        playerChips = playerChips + (playerBet * 2)
    print("  ")
    checkGameOver()



def dealerPlay():
    showDealerHand()
    score = countDealerHand()
    if score <= 17:
        print("Dealer has " + str(score))
        print("  ")
        print("Dealer takes a hit.")
        print("  ")
        giveCard("dealer")
        dealerPlay()
    else:
        print("Dealer has " + str(score))
        print("  ")
        findWinner()


def showPlayerHand():
    showChips()
    print("Player Hand:")
    playerScore = 0
    for x in playerHand:
        playerScore = playerScore + x.getValue()
        print(x)
    print("Total: " + str(playerScore))
    print("  ")


def checkBet(betAmount):
    global playerChips
    if betAmount <= playerChips and betAmount > 0:
        return True
    return False

def playGame():
    check = 0
    print("Dealer Hand:")
    print("????")
    print(dealerHand[0])
    print("  ")
    showPlayerHand()
    print("What would you like to do?")
    gameOptions = getOptions()
    for o in gameOptions:
        print(o)
    playerChoice = input("Choice:")
    for oTwo in gameOptions:
        if oTwo == playerChoice:
            check = check + 1
    if check == 0:
        print("Please try Again")
        playGame()
    if playerChoice == "Hit":
        giveCard("player")
        if countPlayerHand() <= 21:
            playGame()
        else:
            checkPlayerBust()
    elif playerChoice == "Stand":
        dealerPlay()
    elif playerChoice == "Double":
        global playerBet
        global playerChips
        if checkBet(playerBet):
            playerChips = playerChips - playerBet
            playerBet = playerBet * 2
            giveCard("player")
            showPlayerHand()
            dealerPlay()
        else:
            print("You don't have enough to double")
            playGame()


def gameSetup():
    showChips()
    betAmount = int(input("Place your bet."))
    if not checkBet(betAmount):
        print("You can not bet that.")
        gameSetup()
    global playerChips
    global playerBet
    playerChips = playerChips - betAmount
    playerBet = betAmount
    giveCard("player")
    giveCard("dealer")
    giveCard("player")
    giveCard("dealer")
    playGame()


def startGame():
    decksAmount = input("How Many Decks? (1-5)")
    if int(decksAmount) > 0 and int(decksAmount) < 6:
        for x in range(int(decksAmount)):
            unplayedDeck.extend(Card.buildDeck())
        global playerChips
        playerChips = 200
        gameSetup()

    else:
        print("Please enter a valid number (1-5")
        startGame()

def giveCard(target):
    card = random.randrange(0, len(unplayedDeck)-1, 1)
    tempCard = unplayedDeck[card]
    if target == "dealer":
        dealerHand.append(tempCard)
    else:
        playerHand.append(tempCard)
    del unplayedDeck[card]

startGame()