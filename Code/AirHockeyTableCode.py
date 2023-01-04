import board # type: ignore
import digitalio  # type: ignore
import time

resetButton = digitalio.DigitalInOut(board.GP18) # Button stuff
resetButton.direction = digitalio.Direction.INPUT
resetButton.pull = digitalio.Pull.DOWN
resetButtonWasPressed = False

led1 = digitalio.DigitalInOut(board.GP19)
led1.direction = digitalio.Direction.OUTPUT

scoreNeededToWinGame = 7
someoneWonTheGame = False
scoringDebounceForPlayer1 = False
scoringDebounceForPlayer2 = False

player1 = {
    "name" : "player1", ## maybe let people enter their own names?
    "score": 0,
    "winCount" : 0,
    "playerWonThisRound" : False
}
player2 = {
    "name" : "player2",
    "score": 0,
    "winCount" : 0,
    "playerWonThisRound" : False
}

player1Button = digitalio.DigitalInOut(board.GP2) # Button stuff
player1Button.direction = digitalio.Direction.INPUT
player1Button.pull = digitalio.Pull.DOWN

player2Button = digitalio.DigitalInOut(board.GP3) # Button stuff
player2Button.direction = digitalio.Direction.INPUT
player2Button.pull = digitalio.Pull.DOWN

def playerWonFunction(whoScored):
    print(str(whoScored["name"]) + " won the game!")
    whoScored["winCount"] = whoScored["winCount"] + 1

def playerScoredFunction(whoScored):
    if player1["playerWonThisRound"] == False and player2["playerWonThisRound"] == False: ## if nobody won yet
        if whoScored["score"] + 1 != scoreNeededToWinGame:
            whoScored["score"] = whoScored["score"] + 1
        else:
            whoScored["playerWonThisRound"] = True
            whoScored["score"] = whoScored["score"] + 1
            playerWonFunction(whoScored)
    else:
        print("Reset score to play again.")
            
def resetScoreFunction():
    print("Score Reset.")
    player1["score"] = 0
    player2["score"] = 0

def setScoreToWinFunction():
    ## scoreNeededToWinGame = scoreNeededToWinGame - 1
    ## scoreNeededToWinGame = scoreNeededToWinGame + 1
    ## scoreNeededToWinGame = 999999 ## This is the inf setting

    ## print("Score needed to win: " + str(scoreNeededToWinGame))
    ## print("Score needed to win: inf (999999)")
    print("Haha no.")

while True:
    time.sleep(0.01)
    led1.value = True
    if resetButton.value == True and player1["score"] + player2["score"] != 0 and resetButtonWasPressed == False: # When player press button, and combined score does not equal 0, then reset score. (Maybe make something for protecting the score?)
       resetButtonWasPressed = True
       player1["playerWonThisRound"] = False
       resetScoreFunction()
    if resetButton.value == False and resetButtonWasPressed == True:
       resetButtonWasPressed = False

    if player1Button.value == True and scoringDebounceForPlayer1 == False and player1["playerWonThisRound"] == False:
        scoringDebounceForPlayer1 = True
        print("Player1 scored!")
        playerScoredFunction(player1)
        print("Score: " + "P1 - " + str(player1["score"]) + ", " + "P2 - " + str(player2["score"]))
    if player1Button.value == False and scoringDebounceForPlayer1 == True:
        scoringDebounceForPlayer1 = False

    if player2Button.value == True and scoringDebounceForPlayer2 == False and player2["playerWonThisRound"] == False:
        scoringDebounceForPlayer2 = True
        print("Player2 scored!")
        playerScoredFunction(player2)
        print("Score: " + "P1 - " + str(player1["score"]) + ", " + "P2 - " + str(player2["score"]))
    if player2Button.value == False and scoringDebounceForPlayer2 == True:
        scoringDebounceForPlayer2 = False