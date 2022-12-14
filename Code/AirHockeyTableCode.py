import board # type: ignore
import digitalio  # type: ignore
import time

onOffSwitch = digitalio.DigitalInOut(board.GP17) # switch for turning on/off the air hockey table
onOffSwitch.direction = digitalio.Direction.INPUT
onOffSwitch.pull = digitalio.Pull.DOWN

resetButton = digitalio.DigitalInOut(board.GP16) # Button stuff
resetButton.direction = digitalio.Direction.INPUT
resetButton.pull = digitalio.Pull.DOWN

led1 = digitalio.DigitalInOut(board.GP18) # Button stuff

fan1 = digitalio.DigitalInOut(board.GP1)
fan2 = digitalio.DigitalInOut(board.GP2)
fan3 = digitalio.DigitalInOut(board.GP3)
fan4 = digitalio.DigitalInOut(board.GP4)
fan5 = digitalio.DigitalInOut(board.GP5)
fan6 = digitalio.DigitalInOut(board.GP6)

scoreNeededToWinGame = 7

player1 = dict(score = 0)
player2 = dict(score = 0)

def playerWonFunction(whoWon):
    print(str(whoWon) + " won the game!")


def playerScoredFunction(whoScored):
    if whoScored.score + 1 != scoreNeededToWinGame:
        whoScored.score = whoScored.score + 1
    else:
        print("Winning point scored.")
        playerWonFunction(whoScored)


def resetScoreFunction():
    print("Resetting Score.")
    player1Score = 0
    player2Score = 0



while True:
    time.sleep(0.01)
    led1.Value = True
    if resetButton.value == True and player1.score + player2.score != 0 : # When player press button, and combined score does not equal 0, then reset score. (Maybe make something for protecting the score?)
       resetScoreFunction()


     
