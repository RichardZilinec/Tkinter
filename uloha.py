import tkinter as tk
win = tk.Tk()
win.title('Uloha')
#
# tvorba okna
#
canvas = tk.Canvas(win, width=400, height=400, bg='white')
canvas.pack()
#
#
#
for i in range (0, 11):
    canvas.create_line(i*20,0,200,200, fill='red')
    canvas.create_line(i*20, 0, 0, 200, fill='blue')
for x in range(0,7):
    canvas.create_oval(200+(x*20), 0+(x*20), 400-(x*20), 200-(x*20))

for y in range(0, 9, 2):
    for t in range(0, 9, 2):
        canvas.create_rectangle(y*20, 200+t*20, 20+(y*20), 220+t*20, fill='pink')
        canvas.create_rectangle(20+(y*20), 220+t*20, 40+(y*20), 240+t*20, fill='pink')
        canvas.create_rectangle(y*20, 220+t*20, 20+y*20, 240+t*20, fill='yellow')
        canvas.create_rectangle(20+y*20, 200+t*20, 40+y*20, 220+t*20, fill='yellow')
for u in range(0,11):
    canvas.create_rectangle(200+(u*20), 200+(u*20), 220+(u*20), 220+(u*20), fill='green')
    canvas.create_rectangle(380-u*20, 200+u*20, 400-u*20, 220+u*20, fill='yellow')

win.mainloop()