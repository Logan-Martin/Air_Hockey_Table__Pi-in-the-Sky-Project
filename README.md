# Air Hockey-Table Pi in the Sky Project
Our Pi in the Sky Project repo

&nbsp;

## Final Product

### Materials

#### Purchased
|Type |Quantity |
|--- | --- |
|4-40 nuts |42|
|1-72 nuts| 46|
|4-40 3/8 screws| 8|
|4-40 1/2 screws|10|
|4-40 5/8 screws| 24|
|1-72 3/8 screws| 14|
|lcd with backpack| 1|
|vl53l0x distance sensor| 2|
|button| 1|
|switch| 1|
|wires| as needed|
|usb to micro usb wire| 1|
|24v power supply|1|

#### Made
|Part Type| Material|
|---|---|
|walls| birch wood(soft)(cut)|
|cages|PLA(3D printed)|
|pillars|PLA(3D printed)|
|puck|PLA(3D printed)|
|main table| acrylic(cut)|

### Wiring
Fans

<img src="https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Images/Fan%20wiring%20diagram.png" />

Arduino

<img src="https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Images/arduino%20wiring.png" />

### CAD Render

<img src="https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Images/Final%20render.png" />

### Final Product

<img src="https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Images/final%20table%20gif.gif">

### Code

https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/tree/main/Code

### Reflections
#### Logan
The code for this project was quite easym or so I thought. The main issue I faced was this needing to 'spoof' another address for one of the distance sensors because the distance sensor we were using only technically had one I2C address. At one point I wanted to let the player who won input their name with a highscore system, but I quickly dropped that idea as it would've added more complexity to the project. The reset button was a bit of an issue after wiring, but I only needed to switch the logic. A simple pull UP to a pull DOWN. Speaking of wiring, that was the most annoying thing for this project. Soldering a pin and realizing it was the wrong one, or that it's touching a pin it shouldn't- that's annoying. So, those who attempt this project, double check where you're soldering. 

#### Aidan
This project was fun. The pillar design was quite fun to do the first time, and although it ended in a slightly too precise way, I enjoyed the idea of the pillars in design, but it failed to be as productive as I hoped. The walls were an adventure. Originally, they only had one t-slot a piece, and each wall either had only ins or only outs. Although each edge of a wall having one of each would be nice, due to a lack of knowledge, I had to settle for one type per edge of the walls. The main table piece sucked. It slowed down the rest of the part studio, and was relevant enough that it could not be hidden well to reduce load (It also took 2 hours to cut, so be aware). When I went back to change the design of the walls, I had used the use/convert tool enough that I had to spend 2.5 hours fixing the entire project. Overall, I enjoyed the project through the hardship in CAD, and the assembly was more tedious than anything else. Good year-long project, but I just feel like I spent too long with simple mistakes now. *Iterative design certainly was a process.*
<img src="https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Images/iterations.jpg" />
## 5/24/2023 Update:

Completion!
We have finished it and it (mostly) works. The scoring can be a bit shifty, but overall it functions well.

<img src="https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Images/final%20table%20gif.gif" />

---

<details>
<summary><b> Update History on the Project</b></summary>
  
  <details>
  <summary><b>Week of 1/2/2023</b></summary>
    
    CAD:
    This week I adjusted the pillars on the sides up 3mm in order to account for the socket heads of the screws. I also added some basic walls.

      <img src="https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Images/Pillars.png" width="582" height="450"/>

     Code:
     - [Link to Code (1/4/2023)](https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/e0d8a948c9e20a26cdbd912a6f2891ffc34bfc92/Code/AirHockeyTableCode.py)
     - Notes: Player scoring seemed to break at the begining of the week, but was later fixed. So, messing w/ player scoring and the reset button.
  
  </details>
  
  <details>
  <summary><b>Week of 1/9/2023</b></summary>
    
   #### CAD:
This week I confirmed the model for the middle supports of the fans and also added a base for the air hockey table and receptacles for the pucks. Most things are getting 3-D printed over the weekend. Next week will be basic assembly of the pillars and fans in order to figure out how to apply the circuit board and other electronics.

#### Code:
- [Link to Code (1/12/2023)](https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/9c42973c04ebff49a86cc5cd290a6d5ad04bbca9/Code/AirHockeyTableCode.py)
- Notes: Trying to unlock/lock i2c devices. Well, first finding the address, and then going crazy because yes. The code could only would with one i2c for the LCD. Might be an issue later, cough cough it was, but that doesn't matter. Anyways, the LCD apparently worked at this point.
  
  </details>
  
  <details>
  <summary><b>Week of 1/16/2023</b></summary>
    
     CAD:
      This week some of the pieces got put together in real life and work on puck receiver started. Next week will be fitting sensors and other parts inside the box.

     Code:
        - [Link to Code (1/12/2023)](https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/c005875d9523dc01ff9da4728bf7b6b127cd3f1b/Code/AirHockeyTableCode.py)
        - Notes: Put code for searching i2c addresses into it's own file. Trying to now use distance sensor, one of them, and it wasn't working. Changing some names of variables around.

    
  </details>
  
  <details>
  <summary><b>Week of 1/23/2023</b></summary>
    
  #### CAD
    Finished puck receiver and made it consume less material for the print job.

  #### Code:
- [Link to Code (1/26/2023)](https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/dbf2e9b68d2536f0424aa0f3236083821379db28/Code/SearchForI2CAddressCode.py)
- Notes: Getting one distance sensor to work. Then, with scoring. Changing pins. It work w/ one. cool.
 
  </details>
  
  <details>
  <summary><b>Week of 1/30/2023</b></summary>
    
    #### CAD
Fixing all of the problems that cropped up with the test pieces and patching it. CHecking LCDs and distance sensor holes with the derived part feature on onshape.

#### Code:
- [Link to Code (2/2/2023)](https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/c37ed72708385dfef34a0d3229d6141b35cec875/Code/AirHockeyTableCode.py)
- Notes: This is when code was mostly done/working. Shutting down pins testing, didn't work, then I re-coded it, and it worked so yay! Print statements for checking to see what worked and what didn't. One of the errors was using `` sensor.range `` instead of ``` sensor.distance ```. Make sure to use distance if, ya know, you are looking for the distance. It was then just a matter of copy and pasting different files of code that I had made. Finally, I messed with some certain values that allow the player to score or not. I also noticed I had two debounce systems for stopping the player from scoring, so I got rid of one and changed more variable names.
  
  </details>
  
   <details>
  <summary><b>So What happened in February 2023?</b></summary>
    
    #### CAD
We have the upper box now. Waiting to get some of the pillars printed for supports. Got the circuitboards soldered and attached some solid core to them.

<img src="https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Images/AHT%20v2.png" width="582" height="450" />

#### Images:

<img src="https://user-images.githubusercontent.com/71342159/217565048-3209a2c7-22f0-437b-aaf2-e5d517898692.jpg" width="684" height="384" />

2/22/2023:
<img src="https://user-images.githubusercontent.com/71342159/222756384-9a8b0a04-97da-4e19-ba1e-58af4e5d5f8f.jpg" width="591" height="443" />

2/24/2023:
<img src="https://user-images.githubusercontent.com/71342159/222756364-ebaa8fa5-493c-4486-9af9-a83a9e80f4aa.jpg" width="443" height="591" />

  </details>
  
   <details>
  <summary><b>3/15/2023 Update</b></summary>
    
    <img src="https://user-images.githubusercontent.com/71342159/225336586-5cda7151-6b26-4450-a85b-127aecd334d1.jpg" width="300" height="400"/>

    The corner standoffs for the fans break easily, 3 total top plates were lost in the making of the image above. We can't make the corners 3D printed, for reasons I forget that Aidan said at least twice already, but       we're ok. Wiring might be a pain. And, 3D printing/laser cutting things takes a lot of time.
  
  </details>
  
   <details>
  <summary><b>5/3/2023 Update</b></summary>
    
    Lots of things have happened. The pillars are 3D printed now, and the walls have two t-slots each. THe process for doing this was to piece apart the part studio in order to fix every single error that pooped up from use(and hopefully prevent the reoccurance). The slight shift in the center of the walls from a shift to each wall having two ins and two out caused some centerlines to be off, and also shifted the main table. This required a bit of filing to fix, but there is a change in the part studio to avoid that. Right now it is just struggling through the soldering to the circuitboard and making sure all the code works before it all fits together. The cages at the ends have been revised in order to function better. It now ejects right outside of the table. A second puck has also been made, to try and take the wind better. Hopefully we are done within two weeks
We also found out about a minute after the previous writing, that most of our irritation came from a bad LCD, so that has now been replaced and it should work fine. We still need to solder the connections to the distance sensors.
  
  </details>
  
  <details>
  <summary><b>5/19/2023 Update</b></summary>
    
   Our project is almost done. We have a fullrender, and all of are parts are cut and printed. Currently it is just bugfixing in the code and wiring. Hopefully we are done today, but there is a high chance we finish in the next week. We have had lots of issues with the circuit board and are trying to prevent shorts or grounding.

<img src="https://github.com/Logan-Martin/Air-Hockey-Table---Pi-in-the-Sky-Project/blob/main/Images/Final%20render.png" width="582" height="450" />
   
  </details>

</details>
