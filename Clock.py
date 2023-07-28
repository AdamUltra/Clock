import time
from tkinter import *
win = Tk()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))

win.title(" Clock by AdamUltra ")


def close():
    quit()


def struct():
    global STime
    STime = time.localtime()


def refresh():
    struct()
    clock = time.strftime("%H:%M:%S", STime)
    # Labels
    Clock = Label(win, text=f"Clock: {clock}", font='bold')
    Clock.place(x=600, y=350)
    Clock.update()
    time.sleep(1)
    refresh()


refresh()
win.mainloop()
