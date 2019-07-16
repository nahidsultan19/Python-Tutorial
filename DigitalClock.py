import sys
from tkinter import *
import time

def tick():
	time_string = time.strftime('%H:%M:%S')
	clock.config(text = time_string)
	clock.after(200, tick)


root = Tk()
clock = Label(root,font= ('times',100,'bold'),fg='red',bg='green')
clock.grid()
tick()
root.mainloop()