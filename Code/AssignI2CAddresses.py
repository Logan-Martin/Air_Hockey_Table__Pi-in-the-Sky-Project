
import time  # type: ignore
import board  # type: ignore
import busio  # type: ignore

from digitalio import DigitalInOut
from adafruit_vl53l0x import VL53L0X

i2c = busio.I2C(board.GP15,board.GP14) # declare the singleton variable for the default I2C bus

# declare the digital output pins connected to the "SHDN" pin on each VL53L0X sensor
xshut = [
    DigitalInOut(board.GP11), # 2
    DigitalInOut(board.GP10), # 1
    # add more VL53L0X sensors by defining their SHDN pins here
]

for power_pin in xshut:
    # make sure these pins are a digital output, not a digital input
    power_pin.switch_to_output(value=False)
    # These pins are active when Low, meaning:
    #   if the output signal is LOW, then the VL53L0X sensor is off.
    #   if the output signal is HIGH, then the VL53L0X sensor is on.
# all VL53L0X sensors are now off

# initialize a list to be used for the array of VL53L0X sensors
vl53 = []

for i, power_pin in enumerate(xshut): # now change the addresses of the VL53L0X sensors
    power_pin.value = True # turn on the VL53L0X to allow hardware check
    # instantiate the VL53L0X sensor on the I2C bus & insert it into the "vl53" list
    vl53.insert(i, VL53L0X(i2c))  # also performs VL53L0X hardware check
    if i < len(xshut) - 1:
        vl53[i].set_address(i + 0x30)  # address assigned should NOT be already in use

def detect_range(count=5):
    """take count=5 samples"""
    while count:
        for index, sensor in enumerate(vl53):
            print("Sensor {} Range: {}mm".format(index + 1, sensor.range))
        time.sleep(1.0)
        count -= 1


print(
    "Multiple VL53L0X sensors' addresses are assigned properly\n"
    "execute detect_range() to read each sensors range readings"
)

detect_range()