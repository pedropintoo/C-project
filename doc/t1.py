from tkinter import *
from AGLClasses import *
import math
import time, os, sys
import copy
from enum import Enum, auto

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
    class Pacman(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self
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

            if model is not None:
                model.v3.length = v8
                v3.fill = v11
                v3.start = v14
                v3.extent = v17
            else:
                v3.length = v8
                v3.fill = v11
                v3.start = v14
                v3.extent = v17
            face = v3
            if model is not None: 
                model.face = face
                model.last_face = face

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

            if model is not None:
                model.v21.fill = v24
                v21.length = v29
            else:
                v21.fill = v24
                v21.length = v29
            class v30(Enum):
                Open = auto()
                Closed
            v31 = v30(1)  
            v32 = v31
            mouth = v32
            if model is not None: 
                model.mouth = mouth
                model.last_mouth = mouth


            if self.mouth != self.last_mouth:
                v34 = mouth
                v35 = Open
                v33 = v34 == v35
                if v33:
                    v36 = 30
                    v37 = v36
                    v38 = v37
                    v39 = 300
                    v40 = v39
                    v41 = v40

                    if model is not None:
                        model.face.start = v38
                        face.extent = v41
                    else:
                        face.start = v38
                        face.extent = v41
                else:
                    v42 = 1
                    v43 = v42
                    v44 = v43
                    v45 = 359
                    v46 = v45
                    v47 = v46

                    if model is not None:
                        model.face.start = v44
                        face.extent = v47
                    else:
                        face.start = v44
                        face.extent = v47
                self.last_mouth = self.mouth

            model = None
            self.fixCoords()

        def create_object(self, view):
        

            super().create_object(view)
    #################################################################
    v49 = 0
    v50 = 0
    v48 = (v49 , v50)

    if model is not None:
        v51 = Rectangle()
        model.add_object(v51) # add object to model
    else:
        v51 = Rectangle(root = root)
    v51.origin = v48
    v53 = 1000
    v54 = 70
    v52 = (v53 , v54)
    v55 = v52
    v56 = v55
    v57 = "blue"
    v58 = v57
    v59 = v58

    if model is not None:
        model.v51.length = v56
        v51.fill = v59
    else:
        v51.length = v56
        v51.fill = v59

    if model is not None:
        v60 = View()
        model.add_object(v60) # add object to model
    else:
        v60 = View(root = root)
    last_view = v60
    v61 = 450
    v62 = - v61
    v63 = v62
    v64 = v63
    v65 = 0
    v66 = v65
    v67 = v66
    v68 = 401
    v69 = v68
    v70 = v69
    v71 = 401
    v72 = v71
    v73 = v72
    v74 = "Illustrating a moving pacman"
    v75 = v74
    v76 = v75
    v77 = "alice blue"
    v78 = v77
    v79 = v78

    if model is not None:
        model.v60.Ox = v64
        v60.Oy = v67
        v60.width = v70
        v60.height = v73
        v60.title = v76
        v60.background = v79
    else:
        v60.Ox = v64
        v60.Oy = v67
        v60.width = v70
        v60.height = v73
        v60.title = v76
        v60.background = v79
    view = v60
    if model is not None: 
        model.view = view
        model.last_view = view

    v82 = 450
    v83 = - v82
    v84 = 0
    v81 = (v83 , v84)

    v80 = Pacman(root = root, view = last_view, origin = v81)

    v85 = v80
    pacman = v85
    if model is not None: 
        model.pacman = pacman
        model.last_pacman = pacman

    last_refresh = time.time()
    view.update()
    v86 = 1
    v87 = 10
    if model is not None:
        for model.i in range(v86, v87, 1):
            v88 = Close
            v89 = v88
            pacman.mouth = v89
             
            v90 = 20
            while (time.time() - last_refresh <= v90/1000):
                time.sleep(REFRESH_RATE)   

            last_refresh = time.time()
            view.update()
            v91 = Open
            v92 = v91
            pacman.mouth = v92
             
            v93 = 25
            while (time.time() - last_refresh <= v93/1000):
                time.sleep(REFRESH_RATE)   

            last_refresh = time.time()
            view.update()
            v95 = 10
            v96 = 0
            v94 = (v95 , v96)
            if model is not None:
                 model.pacman.move_relative(v94)
            else:
                pacman.move_relative(v94)
            v98 = 10
            v99 = 0
            v97 = (v98 , v99)
            if model is not None:
                 model.view.move_relative(v97)
            else:
                view.move_relative(v97)
            last_refresh = time.time()
            view.update()
    else:
        for i in range(v86, v87, 1):
            v88 = Close
            v89 = v88
            pacman.mouth = v89
             
            v90 = 20
            while (time.time() - last_refresh <= v90/1000):
                time.sleep(REFRESH_RATE)   

            last_refresh = time.time()
            view.update()
            v91 = Open
            v92 = v91
            pacman.mouth = v92
             
            v93 = 25
            while (time.time() - last_refresh <= v93/1000):
                time.sleep(REFRESH_RATE)   

            last_refresh = time.time()
            view.update()
            v95 = 10
            v96 = 0
            v94 = (v95 , v96)
            if model is not None:
                 model.pacman.move_relative(v94)
            else:
                pacman.move_relative(v94)
            v98 = 10
            v99 = 0
            v97 = (v98 , v99)
            if model is not None:
                 model.view.move_relative(v97)
            else:
                view.move_relative(v97)
            last_refresh = time.time()
            view.update()
    v100 = "Press any mouse button to quit"
    print(v100)
    if model is not None:
        model.v101 = model.view.waitClick()
    else:
        v101 = last_view.waitClick()
    v102 = v101
    v103 = v102
    pos = v103
    if model is not None: 
        model.pos = pos
        model.last_pos = pos

    view.close()
