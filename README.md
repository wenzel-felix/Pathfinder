# Pathfinder
This is a small tool to visualize a algorithm that that searches a certain area(size: x=80, y=60) from its start point 
and after finding the end point, goes back the shortest path between the two and marks it pink.

The User is able to set the location of the two points and also can build walls and/or hills between them.
## How to use?
After starting to run the code you have to assign the x- and y-coordinates for the end and the start point.
By pushing the "Submit"-button you close the active Tkinter-window and open a pygame-window.
In the pygame-window you can see your start and endpoint marked in red and purple.

Now you can manipulate every node in the area. You can...

...create walls the algorithm can't jump over. (press the middle mouse button)

...create hills the algorithm needs more steps to surpass the higher you make them. (press the left mouse button)

...delete walls and lower/delete hills. (press the right mouse button)

When you have finished customizing the terrain, just press "Space" to start the algorithm.

To restart or exit the program close the pygame-window and a small menu-window will pop-up.

