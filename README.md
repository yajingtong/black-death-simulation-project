# project2 summary
## GEOG5990 assignment2 -- black death
This project is based on the black death out break in 1665,simulating the epidemic situation caused by rats.The model displays 3 map represents for the average rats caught per week per 100x100m,average population density per 100x100m,and the average death estimated per week per 100x100m.
the first two map is based on data from two text files, the third map is calculated based on the equation d = (0.8 x r) x (1.3 x p),
After run the model,a GUI should appear,displaying 3 maps described above.

The model is tests and demonstrates several features:
- reads in  data contained in two txt files
- display the model as 3 maps 
- contained within a GUI
- allow the user to change the parameter 


## How to run
 Donwload the 2 data files"death.rats.txt"and "death.parishes.txt".Run the blackdeathmodel.py in spyder, after run the code, there will be hint to enter the paramenters in the python console, after the input of parameters,click "draw",there will be a GUI window appear on your computer screen, find the window and select the button "change the parameters" from menubar 
Click the "exit" button on the menu to exits the GUI window.

## files
- black death.py which defines the model itself,have the function of read in data and multiply two list and use matplotlib to draw 3 map.
- test.py
- death.rats.txt contains the data of rats caught per week per 100 x100m
- death.parishes.txt contains the data of average population density per 100 x 100m

