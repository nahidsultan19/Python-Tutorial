import sys
from tkinter import *
import time

app = Tk()
clock = Label(app,font= ('times',100,'bold'),fg='red',bg='green')
clock.grid()

def times():
	now_time = time.strftime('%H:%M:%S')
	clock.config(text = now_time)
	clock.after(200, times)

times()
app.title('Digital Clock')
app.mainloop()
