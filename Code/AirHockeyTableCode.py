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

scoringDebounceForPlayer1 = False
scoringDebounceForPlayer2 = False

player1 = {
    "score": 1
}
player2 = {
    "score": 0
}

player1Button = digitalio.DigitalInOut(board.GP2) # Button stuff
player1Button.direction = digitalio.Direction.INPUT
player1Button.pull = digitalio.Pull.DOWN

player2Button = digitalio.DigitalInOut(board.GP3) # Button stuff
player2Button.direction = digitalio.Direction.INPUT
player2Button.pull = digitalio.Pull.DOWN

def playerWonFunction(whoWon):
    print(str(whoWon) + " won the game!")


def playerScoredFunction(whoScored):
    if whoScored["score"] + 1 != scoreNeededToWinGame:
        whoScored["score"] = whoScored["score"] + 1
    else:
        print("Winning point scored.")
        playerWonFunction(whoScored)


def resetScoreFunction():
    print("Resetting Score.")
    player1["score"] = 0
    player2["score"] = 0

while True:
    time.sleep(0.01)
    led1.value = True
    if resetButton.value == True and player1["score"] + player2["score"] != 0 and resetButtonWasPressed == False: # When player press button, and combined score does not equal 0, then reset score. (Maybe make something for protecting the score?)
       resetButtonWasPressed = True
       resetScoreFunction()
    if resetButton.value == False and resetButtonWasPressed == True:
       resetButtonWasPressed = False

    if player1Button.value == True and scoringDebounceForPlayer1 == False:
        scoringDebounceForPlayer1 = True
        print("Player1 scored!")
        playerScoredFunction(player1)
        print("Score: " + "P1 - " + str(player1["score"]) + ", " + "P2 - " + str(player2["score"]))
    if player1Button.value == False and scoringDebounceForPlayer1 == True:
        scoringDebounceForPlayer1 = False

    if player2Button.value == True and scoringDebounceForPlayer2 == False:
        scoringDebounceForPlayer2 = True
        print("Player2 scored!")
        playerScoredFunction(player2)
        print("Score: " + "P1 - " + str(player1["score"]) + ", " + "P2 - " + str(player2["score"]))
    if player2Button.value == False and scoringDebounceForPlayer2 == True:
        scoringDebounceForPlayer2 = False