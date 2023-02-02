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
i2c_scl = board.GP1
i2c_sda = board.GP0
i2c_address = 0x3f
cols = 16
rows = 2
LCDi2c = busio.I2C(scl=i2c_scl, sda=i2c_sda)
interface = I2CPCF8574Interface(LCDi2c, i2c_address)
lcd = LCD(interface, num_rows=rows, num_cols=cols)

resetButton = digitalio.DigitalInOut(board.GP18) # Button stuff
resetButton.direction = digitalio.Direction.INPUT
resetButton.pull = digitalio.Pull.DOWN
resetButtonWasPressed = False

led1 = digitalio.DigitalInOut(board.GP19)
led1.direction = digitalio.Direction.OUTPUT

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
i2c = busio.I2C(board.GP15,board.GP14) # declare the singleton variable for the default I2C bus
xshut = [ # declare the digital output pins connected to the "SHDN" pin on each VL53L0X sensor
    DigitalInOut(board.GP11), # 2
    DigitalInOut(board.GP10), # 1
    # add more VL53L0X sensors by defining their SHDN pins here
]

for power_pin in xshut:
    # make sure these pins are a digital output, not a digital input
    power_pin.switch_to_output(value=False)
# all VL53L0X sensors are now off

vl53 = [] # initialize a list to be used for the array of VL53L0X sensors
for i, power_pin in enumerate(xshut): # now change the addresses of the VL53L0X sensors
    power_pin.value = True # turn on the VL53L0X to allow hardware check
    # instantiate the VL53L0X sensor on the I2C bus & insert it into the "vl53" list
    vl53.insert(i, VL53L0X(i2c))  # also performs VL53L0X hardware check
    if i < len(xshut) - 1:
        vl53[i].set_address(i + 0x30)  # address assigned should NOT be already in use


def playerWonFunction(whoScored):
    print(str(whoScored["name"]) + " won the game!")
    whoScored["winCount"] = whoScored["winCount"] + 1
    lcd.clear()
    lcd.print(str(whoScored["name"]) + " won the game!")

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
    # time.sleep(0.01)
    led1.value = True

# Reset Button
    if resetButton.value == True and resetButtonWasPressed == False: # When player press button, and combined score does not equal 0, then reset score. (Maybe make something for protecting the score?)
       resetButtonWasPressed = True
       player1["playerWonThisRound"] = False
       resetScoreFunction()
    if resetButton.value == False and resetButtonWasPressed == True:
       resetButtonWasPressed = False


# Scoring w/ Distance Sensors:
    for index, sensor in enumerate(vl53):
        time.sleep(0.05)
        if index == 0:
            if sensor.distance < 12 and sensor.distance > 8 and player1["playerWonThisRound"] == False and player1_can_score == True:
                player1_can_score = False
                # print("Player 1 OMG SCORING YAAAAH!")
                playerScoredFunction(player1)
            if sensor.distance > 30 and player1_can_score == True:
                player1_can_score = False

        if index == 1:
            # print("Sensor {} Range: {}mm".format(index + 1, sensor.distance))
            if sensor.distance < 14 and sensor.distance > 10 and player2["playerWonThisRound"] == False and player2_can_score == True:
                player2_can_score = False
                playerScoredFunction(player2)
            if sensor.distance > 30 and player2_can_score == True:
               player2_can_score = False
        # print("Sensor {} Range: {}mm".format(index + 1, sensor.distance))

