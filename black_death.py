"""

This model displays the population density,the  average rats caught per week and the total death per week.
When you run this code it is expected that a window will appear on your 
computer screen. To run the model,find this window and put in the parameter in the python console,and click "draw",3 map will
apear on your computer window.
"""




import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
from tkinter import Canvas
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter.scrolledtext

os.getcwd()
path="M:\GEOG5990"
os.chdir(path)


'''
Step 1: Initialise the data of population density and rats caught per week
'''

#read in the population density data from text file
pop = open ("death.parishes.txt")
p = []
for row in pop:
    pharsed_row= str.split(row,",")
    rowlist= []
    for data in pharsed_row:
        rowlist.append(float(data))
    p.append(rowlist)
pop.close

#print(p)  print to test the data pulled from text file  
#read in the average rats caught per week data from text file
rat = open ("death.rats.txt")
r = []
for line in rat:
    pharsed_line= str.split(line,",")
    linelist= []
    for value in pharsed_line:
        linelist.append(float(value))
    r.append(linelist)
rat.close    
print("Initialise the data")
#print(r) print to test the data pulled from text file   



"""
Step 2: multiply the two list
"""

print(" step2 :multiply two list")
print("Please enter the paramenter.")


#initialise the parameter of r and p
R = [[x0*0.8 for x0 in y0] for y0 in r]
P=  [[x1*1.3 for x1 in y1] for y1 in p]

# using list comprehension to multiply two list with a float number respectively,according to the equation d=(0.8*r)*(1.3*p)
def setting():
    global R
    global P
    N= float(input("Enter weight to population density:"))
    R= [[x0*N for x0 in y0] for y0 in r]
   
  
    M= float(input("Enter weight to rats caught:"))
    P=  [[x1*M for x1 in y1] for y1 in p]
   
    return R,P
#setting()



def multiply(R,P):
    global d
    d=[]
    for x,y in zip(R,P):
        m = []
        d.append(m)
        for e,f in zip(x,y):        
            m.append(e*f)
    return d
    #D=multiply(R,P)
    #print(D)#print to test the out come of two list multiply

#multiply(R,P)
#print(d)


"""
step 3:initialise GUI. Create 3 plot. Update the plot according to the parameter input. 
"""


print("Step3: Initialise GUI main window")
root = tkinter.Tk() # GUI Main window.
root.wm_title("blcak death Model")

fig,axs= plt.subplots(1,3,figsize=(9,3),sharey=True)
iteration=10

def update():
    setting()
    multiply(R,P)
    
def draw():
    for i in range(iteration):
       
        axs[0].imshow(r,cmap="BuPu_r")
        plt.title("rats caught per week")
        
       
        axs[1].imshow(p,cmap="BuPu_r")   
        plt.title("population density")
        
       
        axs[2].imshow(d,cmap="BuPu_r") 
        plt.title('average death')
        
        fig.suptitle("black death")
        canvas.draw()

update()

'''
 Step 4 :   Write output files and exits killing the GUI window.

'''
#save the desth map as a text file
def exit():
    """
    Write output files and exits  the GUI window.
    """
        print(" exiting")
        print("Step 4: Write out the total death data to the file 'total death.txt'")
        f= open("total death.txt","w+")
        f.write(str(d))
        f.close()
        print("End program")
        root.quit()
        root.destroy()



#create a GUI window
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="change parameter", command=update)
model_menu.add_command(label="Exit", command=exit)
model_menu.add_command(label="draw", command=draw)
tk.mainloop() 




























           
           
           
