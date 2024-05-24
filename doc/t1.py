from tkinter import *
from AGLClasses import *
import time, os, sys

#################################################################
## Auxiliar
#################################################################
REFRESH_RATE = 0.1
last_refresh = time.time()
last_view = None
mouseX = None
mouseY = None
#################################################################

if __name__ == "__main__":
    root = Tk()
    root.withdraw()

    top = Toplevel(root)

    v0 = 601
    v1 = v0
    v2 = v1
    v3 = 601
    v4 = v3
    v5 = v4
    v6 = "Illustrating the minimum level graphical models"
    v7 = v6
    v8 = v7
    v9 = "alice blue"
    v10 = v9
    v11 = v10

    v12 = View(
        top=top,
        width = v2,
        height = v5,
        title = v8,
        background = v11
        )
    last_view = v12
    view = v12
    v13 = 200
    v14 = v13
    v15 = v14
    cellSize = v15
    v17 = cellSize
    v18 = - v17
    v19 = cellSize
    v16 = (v18 , v19)
    v21 = 50
    v22 = 50
    v20 = (v21 , v22)
    v23 = v20
    v24 = v23
    v25 = "red"
    v26 = v25
    v27 = v26

    v28 = Line(
        view=last_view,
        origin=v16,
        length = v24,
        fill = v27
        )
    last_view.add_object(v28)
    line = v28
    last_refresh = time.time()
    view.update()
    v29 = 1
    v30 = 10
    for i in range(v29, v30, 1):
        v31 = "pedro "
        print(v31)
        v32 = i
        print(v32)
        v33 = "hidden"
        v34 = v33
        line.change(state = v34)
         
        v35 = 1
        while (time.time() - last_refresh <= v35):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
        v36 = "normal"
        v37 = v36
        line.change(state = v37)
         
        v38 = 1
        while (time.time() - last_refresh <= v38):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
    v39 = last_view.waitClick()
    v40 = v39
    v41 = v40
    p = v41
    v42 = p
    print(v42)
