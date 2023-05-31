# How to build the Mini Air Hockey Table, step by step.


### Step 1.) Understand & Gather Materials:

##### Screws & Nuts Needed:
- 4-40 nuts	42
- 1-72 nuts	46
- 4-40 3/8 screws	8
- 4-40 1/2 screws	10
- 4-40 5/8 screws	24
- 1-72 3/8 screws	14

##### Mechanical things you'll need:
- 1 push button
- 1 LCD with a backpack
- 6 Computer fans
- 1 Rasberry Pi Pico w/ cord to connect to a computer via USB
- 2 Distance sensors (vl53l0x)
- 24 volt Power Supply
- 1 Switch
- Wires	as needed

##### You will need to 3D print the following:
- Puck
- Standoff pillars:
  - 4 corner pillars
  - 2 center/mid pillars
  - 6 side/edge pillars
- 2 Goal catcher/cage
- Cap for power supply to get plugged into

##### You will need to laser cut the following:
- The 4 walls
  - 2 walls that have the distance sensor hole
  - 1 wall with the LCD extention on it
  - 1 wall with the power cord hole
- The playing field (WARNING: This took 2 hours for us to laser cut.)

##### Code:
- General Tree: https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/tree/main/Code
- Code for the Mini Air Hockey Table: https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Code/AirHockeyTableCode.py

### Step 2.) Assembly 1 and Wiring 1
- Put the walls together with screws
- Srew the goal catchers into the 2 walls that need them
- Screw in push button and wire that end
- Screw in LCD and wire that end
- Screw in Distance Sensors and wire that end

### Step 4.) Fans

1. Screw in standoffs/pillars onto the underside of the fans:

2. Connect all ground wires from the fans to a hub
3. Connect all power wires from the fans to a hub
4. Connect the hubs to their respective entry point where you insert the 24volt power supply:

**WARNING: Make sure the power supply is not giving any power, make sure it's not plugged in. You could hurt yourself if the fans are on while assembling. We learned this the hard way.**

### Step 5.) Wiring 2
Wire everything to the Pico

image of wiring here

### Step 6.) Assembly 2

1. Put the assembled walls into the pillar holes that are are attached to the fans.

2. put playing field into the holes of the walls
**WARNING: This is annoying to do and will probably take you a while.**

### Step 7.) Code
Run the code to the Pico, hopefully everything works perfectly fine.

---

### Errors section:
Run into any errors while running, check out this part of the 'wikihow'.

coming soon, hopefully


