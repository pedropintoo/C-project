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
        top=top
        ,height=v5
        ,width=v2
        ,title=v8
        ,background=v11
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
        view=last_view
        ,origin=v16
        ,length=v24
        ,fill=v27
        )
    last_view.add_object(v28)    
     
    v29 = 0.5
    while (time.time() - last_refresh <= v29):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    view.update()
    v31 = 0
    v32 = cellSize
    v30 = (v31 , v32)
    v34 = 50
    v35 = 50
    v33 = (v34 , v35)
    v36 = v33
    v37 = v36
    v38 = "orange"
    v39 = v38
    v40 = v39

    v41 = Rectangle(
        view=last_view
        ,origin=v30
        ,length=v37
        ,fill=v40
        )
    last_view.add_object(v41)    
     
    v42 = 0.5
    while (time.time() - last_refresh <= v42):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    view.update()
    v43 = 1
    v44 = 10
    for i in range(v43, v44, 1):
        v45 = "pedro "
        print(v45)
        v46 = i
        print(v46)
    v47 = last_view.waitClick()
    v48 = v47
    v49 = v48
    p = v49
    v50 = p
    print(v50)
