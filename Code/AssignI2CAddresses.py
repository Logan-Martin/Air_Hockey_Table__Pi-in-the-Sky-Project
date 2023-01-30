import time
import board # type: ignore
import busio # type: ignore
from digitalio import DigitalInOut # type: ignore
import adafruit_vl53l0x # type: ignore

print("Check 0!")

i2c = busio.I2C(board.GP15,board.GP14) 

print("Check 1!")

shutdownPin_Table = [
    DigitalInOut(board.GP11), # 2
    DigitalInOut(board.GP10), # 1
    # add more VL53L0X sensors by defining their SHDN pins here
]

table_of_distance_sensors = [

]

for shutdown_pin in shutdownPin_Table:
    # make sure these pins are a digital output, not a digital input
    shutdown_pin.switch_to_output(value=False)
    print("Check 2!")

for i, v in enumerate(shutdownPin_Table):
    print(str(i) + " From shutdownPin_Table.")
    shutdown_pin.value = True # turn on the VL53L0X to allow hardware check
    if i == 1:
        # default address is 0x29. Change that to something else
        distance_sensor_B = adafruit_vl53l0x.VL53L0X(i2c)
        distance_sensor_B.set_address(0x30)  # address assigned should NOT be already in use
        table_of_distance_sensors.insert(1,distance_sensor_B)
        print("Check 4!")
    else:
        distance_sensor_A = adafruit_vl53l0x.VL53L0X(i2c)
        # distance_sensor_A.set_address(0x30)  # address assigned should NOT be already in use
        table_of_distance_sensors.insert(0,distance_sensor_A)
        print("Check 4!")



def detect_range(count=5):
    """take count=5 samples"""
    while count:
        for index, sensor in enumerate(table_of_distance_sensors):
            print("Check 5!")
            print("Sensor {} Range: {}mm".format(index + 1, sensor.range))
        time.sleep(1.0)
        count -= 1

print(
    "Multiple VL53L0X sensors' addresses are assigned properly\n"
    "execute detect_range() to read each sensors range readings"
)