import tkinter as tk
import tkinter.scrolledtext
import matplotlib
'''
the class of GUI ，run to test
'''
class GUI(tk.Frame,):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_button()
        self.create_scrollbar()
    
    def put_parameter(self):
        print("button pressed")
  
    def create_button(self):
        self.set_parameter = tk.Button(self)
        self.set_parameter["text"] = "change the parameter\n(click me)"
        self.set_parameter["command"] = self.put_parameter
        self.set_parameter.pack(side="top")
        
        #exit the window
        self.quit = tk.Button(self, text="QUIT", fg="green",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_scrollbar(self):
        self.set_value = tk.Scrollbar(self)
    
        self.set_value.pack(side = "right")
  
   

        

root = tk.Tk()
c = tkinter.Canvas(root, width=200, height=200)
c.pack()			
am = GUI(master=root)
am.mainloop()

