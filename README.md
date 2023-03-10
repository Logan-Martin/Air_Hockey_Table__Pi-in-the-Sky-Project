# Air Hockey-Table Pi in the Sky Project
Our Pi in the Sky Project repo

&nbsp;


### Week of 1/2/2023
#### CAD:
This week I adjusted the pillars on the sides up 3mm in order to account for the socket heads of the screws. I also added some basic walls.

<img src="https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Images/Pillars.png" width="582" height="450"/>

#### Code:
- [Link to Code (1/4/2023)](https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/e0d8a948c9e20a26cdbd912a6f2891ffc34bfc92/Code/AirHockeyTableCode.py)
- Notes: Player scoring seemed to break at the begining of the week, but was later fixed. So, messing w/ player scoring and the reset button.



### Week of 1/9/2023
#### CAD:
This week I confirmed the model for the middle supports of the fans and also added a base for the air hockey table and receptacles for the pucks. Most things are getting 3-D printed over the weekend. Next week will be basic assembly of the pillars and fans in order to figure out how to apply the circuit board and other electronics.

#### Code:
- [Link to Code (1/12/2023)](https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/9c42973c04ebff49a86cc5cd290a6d5ad04bbca9/Code/AirHockeyTableCode.py)
- Notes: Trying to unlock/lock i2c devices. Well, first finding the address, and then going crazy because yes. The code could only would with one i2c for the LCD. Might be an issue later, cough cough it was, but that doesn't matter. Anyways, the LCD apparently worked at this point.



### Week of 1/16/2023
#### CAD
This week some of the pieces got put together in real life and work on puck receiver started. Next week will be fitting sensors and other parts inside the box.

#### Code:
- [Link to Code (1/12/2023)](https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/c005875d9523dc01ff9da4728bf7b6b127cd3f1b/Code/AirHockeyTableCode.py)
- Notes: Put code for searching i2c addresses into it's own file. Trying to now use distance sensor, one of them, and it wasn't working. Changing some names of variables around.


### Week of 1/23/2023
#### CAD
Finished puck receiver and made it consume less material for the print job.

#### Code:
- [Link to Code (1/26/2023)](https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/dbf2e9b68d2536f0424aa0f3236083821379db28/Code/SearchForI2CAddressCode.py)
- Notes: Getting one distance sensor to work. Then, with scoring. Changing pins. It work w/ one. cool.

### Week of 1/30/2023
#### CAD
Fixing all of the problems that cropped up with the test pieces and patching it. CHecking LCDs and distance sensor holes with the derived part feature on onshape.

#### Code:
- [Link to Code (2/2/2023)](https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/c37ed72708385dfef34a0d3229d6141b35cec875/Code/AirHockeyTableCode.py)
- Notes: This is when code was mostly done/working. Shutting down pins testing, didn't work, then I re-coded it, and it worked so yay! Print statements for checking to see what worked and what didn't. One of the errors was using `` sensor.range `` instead of ``` sensor.distance ```. Make sure to use distance if, ya know, you are looking for the distance. It was then just a matter of copy and pasting different files of code that I had made. Finally, I messed with some certain values that allow the player to score or not. I also noticed I had two debounce systems for stopping the player from scoring, so I got rid of one and changed more variable names.

### So What happened in February?
#### CAD
We have the upper box now. Waiting to get some of the pillars printed for supports. Got the circuitboards soldered and attached some solid core to them.

<img src="https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Images/AHT%20v2.png" width="582" height="450" />

#### Images:

<img src="https://user-images.githubusercontent.com/71342159/217565048-3209a2c7-22f0-437b-aaf2-e5d517898692.jpg" width="684" height="384" />

---

Progress Images:

2/22/2023:
<img src="https://user-images.githubusercontent.com/71342159/222756384-9a8b0a04-97da-4e19-ba1e-58af4e5d5f8f.jpg" width="591" height="443" />

2/24/2023:
<img src="https://user-images.githubusercontent.com/71342159/222756364-ebaa8fa5-493c-4486-9af9-a83a9e80f4aa.jpg" width="443" height="591" />

3/1/2023:
<img src="https://user-images.githubusercontent.com/71342159/222756422-b19d24ac-579c-4b44-aada-b9e5d6156cd3.jpg" width="443" height="591"/>

---


