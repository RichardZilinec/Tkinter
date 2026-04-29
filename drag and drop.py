import tkinter as tk, math, datetime as dt
win = tk.Tk()
win.title('drag and drop')
#
# konstanty
#
velkost = 800
pos_x = -1
pos_y = -1
#
#
#
canvas = tk.Canvas(win, width=velkost, height=velkost, bg='white')
canvas.pack()
obj = canvas.create_rectangle(0, 0, 100, 100, fill='limegreen', outline='black')
#
#
#
def click (event):
    #print('klikol si')
    global pos_x, pos_y
    objekty = canvas.find_overlapping(event.x, event.y, event.x+1, event.y+1)
    #print('objekty', objekty)
    if obj in objekty:
        pos_x = event.x
        pos_y = event.y


def move_it (event):
    #print('som stlaceny a taham')
    global pos_x, pos_y
    if pos_x != -1:
        vector_x = event.x - pos_x
        vector_y = event.y - pos_y
        pos_x, pos_y = event.x, event.y
        canvas.move(obj, vector_x, vector_y)

def end_it(event):
    #print('koniec')
    global pos_x, pos_y
    pos_x = -1
    pos_y = -1
#
#
#
canvas.bind('<Button-1>', click)
canvas.bind('<B1-Motion>', move_it)
canvas.bind('<ButtonRelease>', end_it)
win.mainloop()