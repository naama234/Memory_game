from tkinter import *
from tkinter.ttk import *
from functools import partial

from game import Game


root = Tk() # creates an instance of GUI
Game(root)
root.mainloop() # makes the graphics window stay up