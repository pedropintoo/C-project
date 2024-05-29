from tkinter import *
from AGLClasses import *
import math
import time, os, sys

#################################################################
## Auxiliar
#################################################################
REFRESH_RATE = 0.1
last_refresh = time.time()
last_view = None
mouseX = None
mouseY = None
model = None
#################################################################

if __name__ == "__main__":
    root = Root()


    v0 = View(root = root)
    last_view = v0
    v1 = 601
    v2 = v1
    v3 = v2
    v4 = 601
    v5 = v4
    v6 = v5
    v7 = "Illustrating the minimum level graphical models"
    v8 = v7
    v9 = v8
    v10 = "alice blue"
    v11 = v10
    v12 = v11

    v0.width = v3
    v0.height = v6
    v0.title = v9
    v0.background = v12
    view = v0
    v13 = 200
    v14 = v13
    v15 = v14
    cellSize = v15
    v17 = cellSize
    v18 = - v17
    v19 = cellSize
    v16 = (v18 , v19)

    v20 = Line(root = root)
    v20.origin = v16
    if model is not None:
        model.add_object(v20)
    v22 = 50
    v23 = 50
    v21 = (v22 , v23)
    v24 = v21
    v25 = v24
    v26 = "red"
    v27 = v26
    v28 = v27

    v20.length = v25
    v20.fill = v28
    v30 = 0
    v31 = cellSize
    v29 = (v30 , v31)

    v32 = Rectangle(root = root)
    v32.origin = v29
    if model is not None:
        model.add_object(v32)
    v34 = 50
    v35 = 50
    v33 = (v34 , v35)
    v36 = v33
    v37 = v36
    v38 = "orange"
    v39 = v38
    v40 = v39

    v32.length = v37
    v32.fill = v40
    rec = v32
     
    v41 = 1
    while (time.time() - last_refresh <= v41):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    view.update()
    v43 = 10
    v44 = 0
    v42 = (v43 , v44)
    rec.move_relative(v42)
     
    v45 = 1
    while (time.time() - last_refresh <= v45):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    view.update()
    v47 = 10
    v48 = 0
    v46 = (v47 , v48)
    rec.move_relative(v46)
     
    v49 = 1
    while (time.time() - last_refresh <= v49):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    view.update()
    v51 = 10
    v52 = 0
    v50 = (v51 , v52)
    rec.move_relative(v50)
     
    v53 = 1
    while (time.time() - last_refresh <= v53):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    view.update()
    v55 = 10
    v56 = 0
    v54 = (v55 , v56)
    rec.move_relative(v54)
     
    v57 = 1
    while (time.time() - last_refresh <= v57):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    view.update()
    v59 = 0
    v60 = cellSize
    v58 = (v59 , v60)
    rec.move_absolute(v58)
     
    v61 = 1
    while (time.time() - last_refresh <= v61):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    view.update()
    v62 = "Press any mouse button to quit"
    print(v62)
    v63 = last_view.waitClick()
    v64 = v63
    p = v64
    view.close()
