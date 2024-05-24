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
        top=top,
        width = v2,
        height = v5,
        title = v8,
        background = v11
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
        view=last_view,
        origin=v13,
        length = v20,
        fill = v23
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
        view=last_view,
        origin=v25,
        length = v32,
        fill = v35,
        start = v38,
        extent = v41
        )
    last_view.add_object(v42) 
    pacman = v42
    last_refresh = time.time()
    view.update()
    v43 = 1
    v44 = 10
    for i in range(v43, v44, 1):
        v45 = 1
        v46 = v45
        v47 = v46
        v48 = 359
        v49 = v48
        v50 = v49
        pacman.change(start = v47,
        extent = v50)
         
        v51 = 20
        while (time.time() - last_refresh <= v51/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
        v52 = 30
        v53 = v52
        v54 = v53
        v55 = 300
        v56 = v55
        v57 = v56
        pacman.change(start = v54,
        extent = v57)
         
        v58 = 25
        while (time.time() - last_refresh <= v58/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
        v60 = 10
        v61 = 0
        v59 = (v60 , v61)
        pacman.move(v59)
        v63 = 10
        v64 = 0
        v62 = (v63 , v64)
        view.move(v62)
        last_refresh = time.time()
        view.update()
    v65 = "Press any mouse button to quit"
    print(v65)
    v66 = last_view.waitClick()
    v67 = v66
    v68 = v67
    pos = v68
