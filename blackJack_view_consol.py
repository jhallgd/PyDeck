import blackJack_model as blm

game = blm.black_jack(200)

#Starts the game.
def startGame():
    decksAmount = input("How Many Decks? (1-5)")
    if int(decksAmount) > 0 and int(decksAmount) < 6:
        game.startGame(decksAmount)
        gameSetup()
    else:
        print("Please enter a valid number (1-5)")
        startGame()

#Setups the game
def gameSetup():
    showChips()
    betAmount = int(input("Place your bet."))
    if not game.checkBet(betAmount):
        print("You can not bet that.")
        gameSetup()
    else:
        game.gameSetup(betAmount)
        playGame()

#Plays the game
def playGame():
    if game.checkGameOver():
        print("Game Over")
        startGame()
    elif game.checkPlayerDone():
        dealerAction()
    else:
        showTable()
        playerChoice = input("Choice:")
        check = False
        for option in game.getOptions():
            if option == playerChoice:
                check = True
        if check == False:
            print("Please try Again")
            playGame()
        if playerChoice == "Hit":
            game.playerHit()
        elif playerChoice == "Stand":
            game.playerStand()
        elif playerChoice == "Double":
            if game.checkBet(game.getPlayerBet()):
                game.playerDouble
            else:
                print("You don't have enough to double")
        playGame()

        



def showTable():
    print("Dealer Hand-----------------------------")
    showHand(game.getDealerHand())
    print("Dealer Total: " + str(game.countDealerHand()))
    print("----------------------------------------")
    print("Player Hand-----------------------------")
    showHand(game.getPlayerHand())
    print("Player Total: " + str(game.countPlayerHand()))
    print("----------------------------------------")
    print("Player Options--------------------------")
    for option in game.getOptions():
        print(option)

def showHand(hand):
    for card in hand:
        print(card)
        

#Prints the player chips
def showChips():
    chips = game.getPlayerChips()
    print("Player Chips: " + str(chips))

#Dealer Actions
def dealerAction():
    action = game.dealerPlay()
    print("Dealer Action: " + action)


startGame()