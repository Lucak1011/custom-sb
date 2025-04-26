# Custom SweatBox

A custom sweatbox written by Alice Ford (@AliceFord)

Please note, this software is in rapid development, so may have bugs!

### Installation Instructions

1. Download / Clone repository
2. Install python dependencies with `pip install -r requirements.txt`

### Starting and running the sweatbox

1. Open a terminal in your chosen IDE and run ```py sb.py```
2. **This only applies if you AND other people are using the sweatbox**: Open NGROK and run `ngrok tcp 6809`
3. run `py main.py`, this starts the script that generates the aircraft.

### Controlling the planes
You can control what the planes do by assigning a speed, heading or level in the aircraft tag as you would do if you were controlling on the network. To clear an aircraft on the ILS, in the dropdown, select "CL/APP".


### Adjusting what happens in the sweatbox

I'd assume you will want to change what aircraft you get and from where when using this tool. This section explains how to do this!

In `main.py` after line 675, there is a considerable amount of commented code. These are all different "profiles" that have been over time by myself or Alice. These all work, but there is now a much easier way of doing this, so you can ignore this section. HOWEVER, you will still need to look around line 1590 to choose which profile you wish to use. 

Profiles are located in the "profiles" directory. The way that these work is quite self-explanitory based on what the json file looks like. The interval specified in these profiles is measured in seconds. 

In the afformention section of code in main that involves the selection of these profiles, you need to change the file name to match the one that you want to use. 

**YOU NEED TO FIND THE ROUTES YOURSELF**

The constants file defines what positions users control, the master controller (the one that the position that the file uses to transfer aircraft) and, active aerodromes and their respective runways. Most of the profiles are configured for westerly runway operations. 
