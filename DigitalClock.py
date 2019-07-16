import sys
from tkinter import *
import time

def times():
	now_time = time.strftime('%H:%M:%S')
	clock.config(text = now_time)
	clock.after(200, times)


root = Tk()
clock = Label(root,font= ('times',100,'bold'),fg='red',bg='green')
clock.grid()
times()
root.mainloop()
