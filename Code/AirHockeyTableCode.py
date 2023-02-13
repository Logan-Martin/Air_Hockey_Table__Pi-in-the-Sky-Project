import board # type: ignore
import digitalio  # type: ignore
import time # type: ignore
import busio  # type: ignore
import adafruit_vl53l0x # type: ignore
from digitalio import DigitalInOut # type: ignore
from adafruit_vl53l0x import VL53L0X # type: ignore
from CircuitPython_LCDFolder.lcd.lcd import LCD, CursorMode  # type: ignore
from CircuitPython_LCDFolder.lcd.i2c_pcf8574_interface import I2CPCF8574Interface  # type: ignore
# http://www.penguintutor.com/electronics/pico-lcd
# Make sure to have at least 5v. Pico only gives 3 volts. use battery back.
# address = 0x3f

i2c_address = 0x3f
cols = 16
rows = 2
i2c_bus_0 = busio.I2C(board.GP1, board.GP0) # 1 rn
interface = I2CPCF8574Interface(i2c_bus_0, i2c_address)
lcd = LCD(interface, num_rows=rows, num_cols=cols)

resetButton = digitalio.DigitalInOut(board.GP10) # Button stuff
resetButton.direction = digitalio.Direction.INPUT
resetButton.pull = digitalio.Pull.DOWN # power is connected to 3volts and ground pin is connected to the pin. 
resetButtonWasPressed = False

scoreNeededToWinGame = 7
someoneWonTheGame = False
player1_can_score = True
player2_can_score = True

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

# Distance Sensor Stuff:
distanceSensor_player1 = VL53L0X(i2c_bus_0)

i2c_bus_1 = busio.I2C(board.GP15,board.GP14) # declare the singleton variable for the default I2C bus
distanceSensor_player2 = VL53L0X(i2c_bus_1)

time_before_autoreset = 5
def playerWonFunction(whoScored):
    print(str(whoScored["name"]) + " won the game!")
    whoScored["winCount"] = whoScored["winCount"] + 1
    lcd.clear()
    lcd.print(str(whoScored["name"]) + " won the game!")

    time.sleep(time_before_autoreset)
    resetScoreFunction()
#hjrfg
def playerScoredFunction(whoScored):
    if player1["playerWonThisRound"] == False and player2["playerWonThisRound"] == False: ## if nobody won yet
        if whoScored["score"] + 1 != scoreNeededToWinGame:
            whoScored["score"] = whoScored["score"] + 1
            lcd.clear()
            lcd.print("Player1: " + str(player1["score"]) + "      " + "Player2: " + str(player2["score"]))
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
    player1["playerWonThisRound"] = False
    player2["playerWonThisRound"] = False
    lcd.clear()
    lcd.print("Player1: " + str(player1["score"]) + "      " + "Player2: " + str(player2["score"]))

lcd.clear()
lcd.print("Player1: " + str(player1["score"]) + "      " + "Player2: " + str(player2["score"]))

print("Done starting up!")

while True:
    
# Reset Button
    if resetButton.value == True and resetButtonWasPressed == False: # When player press button, and combined score does not equal 0, then reset score. (Maybe make something for protecting the score?)
       resetButtonWasPressed = True
       resetScoreFunction()
    if resetButton.value == False and resetButtonWasPressed == True:
       resetButtonWasPressed = False


# Scoring w/ Distance Sensors:
    # time.sleep(0.05)
    if distanceSensor_player1.distance < 8 and distanceSensor_player1.distance > 4 and player1["playerWonThisRound"] == False and player1_can_score == True:
        player1_can_score = False
        playerScoredFunction(player1)
    if distanceSensor_player1.distance > 10 and player1_can_score == False:
        player1_can_score = True

    if distanceSensor_player2.distance < 8 and distanceSensor_player2.distance > 4 and player2["playerWonThisRound"] == False and player2_can_score == True:
        player2_can_score = False
        playerScoredFunction(player2)
    if distanceSensor_player2.distance > 10 and player2_can_score == False:
        player2_can_score = True

