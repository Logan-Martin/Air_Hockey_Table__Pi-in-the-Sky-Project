import board # type: ignore
import digitalio  # type: ignore
import time # type: ignore
import busio  # type: ignore
from digitalio import DigitalInOut # type: ignore

from CircuitPython_LCD.lcd.lcd import LCD, CursorMode  # type: ignore
from CircuitPython_LCD.lcd.i2c_pcf8574_interface import I2CPCF8574Interface  # type: ignore
# https://github.com/dhalbert/CircuitPython_LCD
# when downloading, the name of the folder was "CircuitPython_LCD-main", change that name of the folder and make sure it matches the above name.

# http://www.penguintutor.com/electronics/pico-lcd 
# Make sure to have at least 5v for LCD. Use battery pack or use VBUS. Note: VBUS has no volts when the pico's USB is unplugged.

i2c_address = 0x27 # check the i2c address of your specific device
cols = 16
rows = 2
i2c_bus_0 = busio.I2C(board.GP11, board.GP10) # make sure to check (SLC, SCA)
interface = I2CPCF8574Interface(i2c_bus_0, i2c_address)
lcd = LCD(interface, num_rows=rows, num_cols=cols)


lcd.print("abc ")
lcd.print("This is quite long and will wrap onto the next line automatically.")

lcd.clear()

# Start at the second line, fifth column (numbering from zero).
lcd.set_cursor_pos(1, 4)
lcd.print("Here I am")

# Make the cursor visible as a line.
lcd.set_cursor_mode(CursorMode.LINE)
