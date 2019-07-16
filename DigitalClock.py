import sys
from tkinter import *
import time

def tick():
	now_time = time.strftime('%H:%M:%S')
	clock.config(text = now_time)
	clock.after(200, tick)


root = Tk()
clock = Label(root,font= ('times',100,'bold'),fg='red',bg='green')
clock.grid()
tick()
root.mainloop()