from tkinter import *
import time, os, sys

## Auxiliar vars
REFRESH_RATE = 0.1
last_refresh = time.time()
##

root = Tk()
root.withdraw()
root.title("C-Project Compiler")  

v0 = 601
v1 = v0
v2 = v1
v3 = 601
v4 = v3
v5 = v4
v6 = "Illustrating the minimum level graphical models"
v7 = v6
v8 = v7
v9 = "white"
v10 = v9
v11 = v10

root.title(v8)
top = Toplevel(root)
v12 = Canvas(top, width=v2,height=v5,background=v11)
v12.pack()

# binding onClick and getMouse
mouseX = None
mouseY = None
def onClick(event):
    global mouseX, mouseY
    mouseX, mouseY = event.x, event.y

def getMouse():
    global mouseX, mouseY
    v12.update()
    mouseX = None; mouseY = None
    while mouseX == None:
        time.sleep(REFRESH_RATE)
        v12.update() 

top.bind("<Button-1>", onClick)

view = v12
v13 = 1
v14 = 10
for i in range(v13, v14, 1):

    v15 = "pedro "
    print(v15)

    v16 = i
    print(v16)

arcPoints = [ (10,500), (240,210) ]
arc = view.create_arc(arcPoints, start=0, extent=180, fill="cyan", outline='', style="chord")
view.update()

getMouse()
v17 = (mouseX, mouseY)
v18 = v17
v19 = v18
p = v19

v20 = p
print(v20)
