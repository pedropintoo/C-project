from tkinter import *
from AGLClasses import *
import math
import time, os, sys
import copy

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

    #################################################################
    ## Model
    #################################################################
    Pacman = Model()
    model = Pacman
    v1 = 0
    v2 = 0
    v0 = (v1 , v2)

    if model is not None:
        v3 = PieSlice()
        model.add_object(v3) # add object to model
    else:
        v3 = PieSlice(root = root)
    v3.origin = v0
    v5 = 50
    v6 = 50
    v4 = (v5 , v6)
    v7 = v4
    v8 = v7
    v9 = "pink"
    v10 = v9
    v11 = v10
    v12 = 30
    v13 = v12
    v14 = v13
    v15 = 300
    v16 = v15
    v17 = v16

    v3.length = v8
    v3.fill = v11
    v3.start = v14
    v3.extent = v17
    face = v3
    if model is not None: 
        model.face = face

    v19 = 20
    v20 = 35
    v18 = (v19 , v20)

    if model is not None:
        v21 = Ellipse()
        model.add_object(v21) # add object to model
    else:
        v21 = Ellipse(root = root)
    v21.origin = v18
    v22 = "black"
    v23 = v22
    v24 = v23
    v26 = 5
    v27 = 5
    v25 = (v26 , v27)
    v28 = v25
    v29 = v28

    v21.fill = v24
    v21.length = v29
    model = None
    #################################################################
    v31 = 0
    v32 = 0
    v30 = (v31 , v32)

    if model is not None:
        v33 = Rectangle()
        model.add_object(v33) # add object to model
    else:
        v33 = Rectangle(root = root)
    v33.origin = v30
    v35 = 1000
    v36 = 70
    v34 = (v35 , v36)
    v37 = v34
    v38 = v37
    v39 = "blue"
    v40 = v39
    v41 = v40

    v33.length = v38
    v33.fill = v41

    if model is not None:
        v42 = View()
        model.add_object(v42) # add object to model
    else:
        v42 = View(root = root)
    last_view = v42
    v43 = 450
    v44 = - v43
    v45 = v44
    v46 = v45
    v47 = 0
    v48 = v47
    v49 = v48
    v50 = 401
    v51 = v50
    v52 = v51
    v53 = 401
    v54 = v53
    v55 = v54
    v56 = "Illustrating a moving pacman"
    v57 = v56
    v58 = v57
    v59 = "alice blue"
    v60 = v59
    v61 = v60

    v42.Ox = v46
    v42.Oy = v49
    v42.width = v52
    v42.height = v55
    v42.title = v58
    v42.background = v61
    view = v42
    if model is not None: 
        model.view = view

    v64 = 450
    v65 = - v64
    v66 = 0
    v63 = (v65 , v66)

    Pacman.root = root
    Pacman.view = last_view
    Pacman.origin = v63
    v62 = copy.deepcopy(Pacman)

    v67 = v62
    pacman = v67
    if model is not None: 
        model.pacman = pacman

    last_refresh = time.time()
    view.update()
    v68 = 1
    v69 = 10
    for i in range(v68, v69, 1):
        v70 = 1
        v71 = v70
        v72 = v71
        v73 = 359
        v74 = v73
        v75 = v74

        pacman.face.start = v72
        pacman.face.extent = v75
         
        v76 = 20
        while (time.time() - last_refresh <= v76/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
        v77 = 30
        v78 = v77
        v79 = v78
        v80 = 300
        v81 = v80
        v82 = v81

        pacman.face.start = v79
        pacman.face.extent = v82
         
        v83 = 25
        while (time.time() - last_refresh <= v83/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
        v85 = 10
        v86 = 0
        v84 = (v85 , v86)
        pacman.move_relative(v84)
        v88 = 10
        v89 = 0
        v87 = (v88 , v89)
        view.move_relative(v87)
        last_refresh = time.time()
        view.update()
    v90 = "Press any mouse button to quit"
    print(v90)
    v91 = last_view.waitClick()
    v92 = v91
    v93 = v92
    pos = v93
    if model is not None: 
        model.pos = pos

    view.close()
