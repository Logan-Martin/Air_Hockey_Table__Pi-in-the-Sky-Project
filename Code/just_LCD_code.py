
import time # type: ignore
import board # type: ignore
import busio  # type: ignore

i2c = busio.I2C(board.GP15,board.GP14) 

while not i2c.try_lock():
    pass

try:
    while True:
        print(
            "I2C addresses found:",
            [hex(device_address) for device_address in i2c.scan()],
        )
        time.sleep(2)

finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c.unlock()