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
    root = Root()

    v1 = 401
    v2 = v1
    v3 = v2
    v4 = 401
    v5 = v4
    v6 = v5
    v7 = "Illustrating the rectangle shape"
    v8 = v7
    v9 = v8
    v10 = "black"
    v11 = v10
    v12 = v11

    v0 = View(root = root)
    last_view = v0
    v0.width = v3
    v0.height = v6
    v0.title = v9
    v0.background = v12
    view = v0
    v14 = 0
    v15 = 0
    v13 = (v14 , v15)
    v16 = v13
    v17 = v16
    p = v17
    v18 = p
    v21 = 100
    v22 = 100
    v20 = (v21 , v22)
    v23 = v20
    v24 = v23
    v25 = "pink"
    v26 = v25
    v27 = v26

    v19 = Rectangle(root = root)
    v19.origin = v18
    v19.length = v24
    v19.fill = v27
    v28 = p
    v31 = 50
    v32 = 50
    v30 = (v31 , v32)
    v33 = v30
    v34 = v33
    v35 = "wheat"
    v36 = v35
    v37 = v36

    v29 = Rectangle(root = root)
    v29.origin = v28
    v29.length = v34
    v29.fill = v37
    r = v29
    last_refresh = time.time()
    last_view = view
    view.update()
    v38 = 1
    v39 = 10
    for i in range(v38, v39, 1):
        v40 = "hidden"
        v41 = v40
        r.state = v41
         
        v42 = 100
        while (time.time() - last_refresh <= v42/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        last_view = view
        view.update()
        v43 = "normal"
        v44 = v43
        r.state = v44
         
        v45 = 100
        while (time.time() - last_refresh <= v45/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        last_view = view
        view.update()
    v46 = "Press any mouse button to quit"
    print(v46)
    v47 = last_view.waitClick()
    v48 = v47
    p = v48
