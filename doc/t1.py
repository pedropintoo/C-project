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
    v14 = 0
    v15 = 0
    v13 = (v14 , v15)
    v16 = v13
    v17 = v16
    p = v17
    v18 = p
    v20 = 100
    v21 = 100
    v19 = (v20 , v21)
    v22 = v19
    v23 = v22
    v24 = "pink"
    v25 = v24
    v26 = v25

    v27 = Rectangle(
        view=last_view
        ,origin=v18
        ,length=v23
        ,fill=v26
        )
    last_view.add_object(v27)    
    v28 = p
    v30 = 50
    v31 = 50
    v29 = (v30 , v31)
    v32 = v29
    v33 = v32
    v34 = "wheat"
    v35 = v34
    v36 = v35

    v37 = Rectangle(
        view=last_view
        ,origin=v28
        ,length=v33
        ,fill=v36
        )
    last_view.add_object(v37)    
    r = v37
    last_refresh = time.time()
    view.update()
    v38 = 1
    v39 = 10
    for i in range(v38, v39, 1):
        v40 = "hidden"
        v41 = v40
        r.change(state = v41)
         
        v42 = 100
        while (time.time() - last_refresh <= v42/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
        v43 = "normal"
        v44 = v43
        r.change(state = v44)
         
        v45 = 100
        while (time.time() - last_refresh <= v45/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
    v46 = "Press any mouse button to quit"
    print(v46)
    v47 = last_view.waitClick()
    v48 = v47
    p = v48
