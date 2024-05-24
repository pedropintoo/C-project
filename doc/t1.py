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

    v0 = 401
    v1 = v0
    v2 = v1
    v3 = 401
    v4 = v3
    v5 = v4
    v6 = "Illustrating the rectangle shape"
    v7 = v6
    v8 = v7
    v9 = "wheat"
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
    v14 = 10
    v15 = 0
    v13 = (v14 , v15)
    v17 = 200
    v18 = 60
    v16 = (v17 , v18)
    v19 = v16
    v20 = v19
    v21 = "blue"
    v22 = v21
    v23 = v22

    v24 = Rectangle(
        view=last_view
        ,origin=v13
        ,length=v20
        ,fill=v23
        )
    last_view.add_object(v24)    
    v26 = 0
    v27 = 0
    v25 = (v26 , v27)
    v29 = 50
    v30 = 50
    v28 = (v29 , v30)
    v31 = v28
    v32 = v31
    v33 = "pink"
    v34 = v33
    v35 = v34
    v36 = 30
    v37 = v36
    v38 = v37
    v39 = 300
    v40 = v39
    v41 = v40

    v42 = PieSlice(
        view=last_view
        ,origin=v25
        ,length=v32
        ,start=v38
        ,extent=v41
        ,fill=v35
        )
    last_view.add_object(v42) 
    pacman = v42
    last_refresh = time.time()
    view.update()
    v43 = 1
    v44 = 10
    for i in range(v43, v44, 1):
         
        v45 = 20
        while (time.time() - last_refresh <= v45/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
         
        v46 = 25
        while (time.time() - last_refresh <= v46/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
        last_refresh = time.time()
        view.update()
    v47 = "Press any mouse button to quit"
    print(v47)
    v48 = last_view.waitClick()
    v49 = v48
    v50 = v49
    pos = v50
