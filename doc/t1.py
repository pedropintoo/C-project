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
action = None
def get_nested_attribute(obj, attr_path):
    if obj is None:
        return None  

    attributes = attr_path.split('.')
    current_object = obj
    for attr in attributes:
        if hasattr(current_object, attr):
            current_object = getattr(current_object, attr)
        else:
            return None 
    return current_object
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

            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v1".split('.')[0]):
                action.v1 = temp
            else:
                v1 = temp 


            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v2".split('.')[0]):
                action.v2 = temp
            else:
                v2 = temp 

            v0 = (v1 , v2)

            if model is not None:
                v3 = PieSlice()
                model.add_object(v3) # add object to model
            else:
                v3 = PieSlice(root = root)
            v3.origin = v0

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v5".split('.')[0]):
                action.v5 = temp
            else:
                v5 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v6".split('.')[0]):
                action.v6 = temp
            else:
                v6 = temp 

            v4 = (v5 , v6)

            temp = get_nested_attribute(action, 'v4')
            if temp is None:
                temp = v4
            if action is not None and hasattr(action, "v7".split('.')[0]):
                action.v7 = temp
            else:
                v7 = temp 


            temp = get_nested_attribute(action, 'v7')
            if temp is None:
                temp = v7
            if action is not None and hasattr(action, "v8".split('.')[0]):
                action.v8 = temp
            else:
                v8 = temp 


            temp = get_nested_attribute(action, '"pink"')
            if temp is None:
                temp = "pink"
            if action is not None and hasattr(action, "v9".split('.')[0]):
                action.v9 = temp
            else:
                v9 = temp 


            temp = get_nested_attribute(action, 'v9')
            if temp is None:
                temp = v9
            if action is not None and hasattr(action, "v10".split('.')[0]):
                action.v10 = temp
            else:
                v10 = temp 


            temp = get_nested_attribute(action, 'v10')
            if temp is None:
                temp = v10
            if action is not None and hasattr(action, "v11".split('.')[0]):
                action.v11 = temp
            else:
                v11 = temp 


            temp = get_nested_attribute(action, '30')
            if temp is None:
                temp = 30
            if action is not None and hasattr(action, "v12".split('.')[0]):
                action.v12 = temp
            else:
                v12 = temp 


            temp = get_nested_attribute(action, 'v12')
            if temp is None:
                temp = v12
            if action is not None and hasattr(action, "v13".split('.')[0]):
                action.v13 = temp
            else:
                v13 = temp 


            temp = get_nested_attribute(action, 'v13')
            if temp is None:
                temp = v13
            if action is not None and hasattr(action, "v14".split('.')[0]):
                action.v14 = temp
            else:
                v14 = temp 


            temp = get_nested_attribute(action, '300')
            if temp is None:
                temp = 300
            if action is not None and hasattr(action, "v15".split('.')[0]):
                action.v15 = temp
            else:
                v15 = temp 


            temp = get_nested_attribute(action, 'v15')
            if temp is None:
                temp = v15
            if action is not None and hasattr(action, "v16".split('.')[0]):
                action.v16 = temp
            else:
                v16 = temp 


            temp = get_nested_attribute(action, 'v16')
            if temp is None:
                temp = v16
            if action is not None and hasattr(action, "v17".split('.')[0]):
                action.v17 = temp
            else:
                v17 = temp 


            if action is not None:
                action.v3.length = v8
                action.v3.fill = v11
                action.v3.start = v14
                action.v3.extent = v17
            else:
                v3.length = v8
                v3.fill = v11
                v3.start = v14
                v3.extent = v17

            temp = get_nested_attribute(action, 'v3')
            if temp is None:
                temp = v3
            if action is not None and hasattr(action, "face".split('.')[0]):
                action.face = temp
            else:
                face = temp 
            if model is not None: 
                model.face = face
                model.last_face = copy.deepcopy(face)

            temp = get_nested_attribute(action, '20')
            if temp is None:
                temp = 20
            if action is not None and hasattr(action, "v19".split('.')[0]):
                action.v19 = temp
            else:
                v19 = temp 


            temp = get_nested_attribute(action, '35')
            if temp is None:
                temp = 35
            if action is not None and hasattr(action, "v20".split('.')[0]):
                action.v20 = temp
            else:
                v20 = temp 

            v18 = (v19 , v20)

            if model is not None:
                v21 = Ellipse()
                model.add_object(v21) # add object to model
            else:
                v21 = Ellipse(root = root)
            v21.origin = v18

            temp = get_nested_attribute(action, '"black"')
            if temp is None:
                temp = "black"
            if action is not None and hasattr(action, "v22".split('.')[0]):
                action.v22 = temp
            else:
                v22 = temp 


            temp = get_nested_attribute(action, 'v22')
            if temp is None:
                temp = v22
            if action is not None and hasattr(action, "v23".split('.')[0]):
                action.v23 = temp
            else:
                v23 = temp 


            temp = get_nested_attribute(action, 'v23')
            if temp is None:
                temp = v23
            if action is not None and hasattr(action, "v24".split('.')[0]):
                action.v24 = temp
            else:
                v24 = temp 


            temp = get_nested_attribute(action, '5')
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v26".split('.')[0]):
                action.v26 = temp
            else:
                v26 = temp 


            temp = get_nested_attribute(action, '5')
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v27".split('.')[0]):
                action.v27 = temp
            else:
                v27 = temp 

            v25 = (v26 , v27)

            temp = get_nested_attribute(action, 'v25')
            if temp is None:
                temp = v25
            if action is not None and hasattr(action, "v28".split('.')[0]):
                action.v28 = temp
            else:
                v28 = temp 


            temp = get_nested_attribute(action, 'v28')
            if temp is None:
                temp = v28
            if action is not None and hasattr(action, "v29".split('.')[0]):
                action.v29 = temp
            else:
                v29 = temp 


            if action is not None:
                action.v21.fill = v24
                action.v21.length = v29
            else:
                v21.fill = v24
                v21.length = v29
            class v30(Enum):
                Open = auto()
                Close = auto() 
            global Open; Open = v30.Open
            global Close; Close = v30.Close   
            v31 = v30(1) # first is default

            temp = get_nested_attribute(action, 'v31')
            if temp is None:
                temp = v31
            if action is not None and hasattr(action, "v32".split('.')[0]):
                action.v32 = temp
            else:
                v32 = temp 


            temp = get_nested_attribute(action, 'v32')
            if temp is None:
                temp = v32
            if action is not None and hasattr(action, "mouth".split('.')[0]):
                action.mouth = temp
            else:
                mouth = temp 
            if model is not None: 
                model.mouth = mouth
                model.last_mouth = copy.deepcopy(mouth)

            self.fixCoords()

        def create_object(self, view):
            action = self

            if self.mouth != self.last_mouth:

                temp = get_nested_attribute(action, 'mouth')
                if temp is None:
                    temp = mouth
                if action is not None and hasattr(action, "v34".split('.')[0]):
                    action.v34 = temp
                else:
                    v34 = temp 


                temp = get_nested_attribute(action, 'Open')
                if temp is None:
                    temp = Open
                if action is not None and hasattr(action, "v35".split('.')[0]):
                    action.v35 = temp
                else:
                    v35 = temp 

                v33 = v34 == v35
                if v33:

                    temp = get_nested_attribute(action, '30')
                    if temp is None:
                        temp = 30
                    if action is not None and hasattr(action, "v36".split('.')[0]):
                        action.v36 = temp
                    else:
                        v36 = temp 


                    temp = get_nested_attribute(action, 'v36')
                    if temp is None:
                        temp = v36
                    if action is not None and hasattr(action, "v37".split('.')[0]):
                        action.v37 = temp
                    else:
                        v37 = temp 


                    temp = get_nested_attribute(action, 'v37')
                    if temp is None:
                        temp = v37
                    if action is not None and hasattr(action, "v38".split('.')[0]):
                        action.v38 = temp
                    else:
                        v38 = temp 


                    temp = get_nested_attribute(action, '300')
                    if temp is None:
                        temp = 300
                    if action is not None and hasattr(action, "v39".split('.')[0]):
                        action.v39 = temp
                    else:
                        v39 = temp 


                    temp = get_nested_attribute(action, 'v39')
                    if temp is None:
                        temp = v39
                    if action is not None and hasattr(action, "v40".split('.')[0]):
                        action.v40 = temp
                    else:
                        v40 = temp 


                    temp = get_nested_attribute(action, 'v40')
                    if temp is None:
                        temp = v40
                    if action is not None and hasattr(action, "v41".split('.')[0]):
                        action.v41 = temp
                    else:
                        v41 = temp 


                    if action is not None:
                        action.face.start = v38
                        action.face.extent = v41
                    else:
                        face.start = v38
                        face.extent = v41
                else:

                    temp = get_nested_attribute(action, '1')
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v42".split('.')[0]):
                        action.v42 = temp
                    else:
                        v42 = temp 


                    temp = get_nested_attribute(action, 'v42')
                    if temp is None:
                        temp = v42
                    if action is not None and hasattr(action, "v43".split('.')[0]):
                        action.v43 = temp
                    else:
                        v43 = temp 


                    temp = get_nested_attribute(action, 'v43')
                    if temp is None:
                        temp = v43
                    if action is not None and hasattr(action, "v44".split('.')[0]):
                        action.v44 = temp
                    else:
                        v44 = temp 


                    temp = get_nested_attribute(action, '359')
                    if temp is None:
                        temp = 359
                    if action is not None and hasattr(action, "v45".split('.')[0]):
                        action.v45 = temp
                    else:
                        v45 = temp 


                    temp = get_nested_attribute(action, 'v45')
                    if temp is None:
                        temp = v45
                    if action is not None and hasattr(action, "v46".split('.')[0]):
                        action.v46 = temp
                    else:
                        v46 = temp 


                    temp = get_nested_attribute(action, 'v46')
                    if temp is None:
                        temp = v46
                    if action is not None and hasattr(action, "v47".split('.')[0]):
                        action.v47 = temp
                    else:
                        v47 = temp 


                    if action is not None:
                        action.face.start = v44
                        action.face.extent = v47
                    else:
                        face.start = v44
                        face.extent = v47
                self.last_mouth = copy.deepcopy(self.mouth)
        
            action = None
            super().create_object(view)
            model = None

    #################################################################

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v49".split('.')[0]):
        action.v49 = temp
    else:
        v49 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v50".split('.')[0]):
        action.v50 = temp
    else:
        v50 = temp 

    v48 = (v49 , v50)

    if model is not None:
        v51 = Rectangle()
        model.add_object(v51) # add object to model
    else:
        v51 = Rectangle(root = root)
    v51.origin = v48

    temp = get_nested_attribute(action, '1000')
    if temp is None:
        temp = 1000
    if action is not None and hasattr(action, "v53".split('.')[0]):
        action.v53 = temp
    else:
        v53 = temp 


    temp = get_nested_attribute(action, '70')
    if temp is None:
        temp = 70
    if action is not None and hasattr(action, "v54".split('.')[0]):
        action.v54 = temp
    else:
        v54 = temp 

    v52 = (v53 , v54)

    temp = get_nested_attribute(action, 'v52')
    if temp is None:
        temp = v52
    if action is not None and hasattr(action, "v55".split('.')[0]):
        action.v55 = temp
    else:
        v55 = temp 


    temp = get_nested_attribute(action, 'v55')
    if temp is None:
        temp = v55
    if action is not None and hasattr(action, "v56".split('.')[0]):
        action.v56 = temp
    else:
        v56 = temp 


    temp = get_nested_attribute(action, '"blue"')
    if temp is None:
        temp = "blue"
    if action is not None and hasattr(action, "v57".split('.')[0]):
        action.v57 = temp
    else:
        v57 = temp 


    temp = get_nested_attribute(action, 'v57')
    if temp is None:
        temp = v57
    if action is not None and hasattr(action, "v58".split('.')[0]):
        action.v58 = temp
    else:
        v58 = temp 


    temp = get_nested_attribute(action, 'v58')
    if temp is None:
        temp = v58
    if action is not None and hasattr(action, "v59".split('.')[0]):
        action.v59 = temp
    else:
        v59 = temp 


    if action is not None:
        action.v51.length = v56
        action.v51.fill = v59
    else:
        v51.length = v56
        v51.fill = v59

    if model is not None:
        v60 = View()
        model.add_object(v60) # add object to model
    else:
        v60 = View(root = root)
    last_view = v60

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v61".split('.')[0]):
        action.v61 = temp
    else:
        v61 = temp 

    v62 = - v61

    temp = get_nested_attribute(action, 'v62')
    if temp is None:
        temp = v62
    if action is not None and hasattr(action, "v63".split('.')[0]):
        action.v63 = temp
    else:
        v63 = temp 


    temp = get_nested_attribute(action, 'v63')
    if temp is None:
        temp = v63
    if action is not None and hasattr(action, "v64".split('.')[0]):
        action.v64 = temp
    else:
        v64 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v65".split('.')[0]):
        action.v65 = temp
    else:
        v65 = temp 


    temp = get_nested_attribute(action, 'v65')
    if temp is None:
        temp = v65
    if action is not None and hasattr(action, "v66".split('.')[0]):
        action.v66 = temp
    else:
        v66 = temp 


    temp = get_nested_attribute(action, 'v66')
    if temp is None:
        temp = v66
    if action is not None and hasattr(action, "v67".split('.')[0]):
        action.v67 = temp
    else:
        v67 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
    if action is not None and hasattr(action, "v68".split('.')[0]):
        action.v68 = temp
    else:
        v68 = temp 


    temp = get_nested_attribute(action, 'v68')
    if temp is None:
        temp = v68
    if action is not None and hasattr(action, "v69".split('.')[0]):
        action.v69 = temp
    else:
        v69 = temp 


    temp = get_nested_attribute(action, 'v69')
    if temp is None:
        temp = v69
    if action is not None and hasattr(action, "v70".split('.')[0]):
        action.v70 = temp
    else:
        v70 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
    if action is not None and hasattr(action, "v71".split('.')[0]):
        action.v71 = temp
    else:
        v71 = temp 


    temp = get_nested_attribute(action, 'v71')
    if temp is None:
        temp = v71
    if action is not None and hasattr(action, "v72".split('.')[0]):
        action.v72 = temp
    else:
        v72 = temp 


    temp = get_nested_attribute(action, 'v72')
    if temp is None:
        temp = v72
    if action is not None and hasattr(action, "v73".split('.')[0]):
        action.v73 = temp
    else:
        v73 = temp 


    temp = get_nested_attribute(action, '"Illustrating a moving pacman"')
    if temp is None:
        temp = "Illustrating a moving pacman"
    if action is not None and hasattr(action, "v74".split('.')[0]):
        action.v74 = temp
    else:
        v74 = temp 


    temp = get_nested_attribute(action, 'v74')
    if temp is None:
        temp = v74
    if action is not None and hasattr(action, "v75".split('.')[0]):
        action.v75 = temp
    else:
        v75 = temp 


    temp = get_nested_attribute(action, 'v75')
    if temp is None:
        temp = v75
    if action is not None and hasattr(action, "v76".split('.')[0]):
        action.v76 = temp
    else:
        v76 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v77".split('.')[0]):
        action.v77 = temp
    else:
        v77 = temp 


    temp = get_nested_attribute(action, 'v77')
    if temp is None:
        temp = v77
    if action is not None and hasattr(action, "v78".split('.')[0]):
        action.v78 = temp
    else:
        v78 = temp 


    temp = get_nested_attribute(action, 'v78')
    if temp is None:
        temp = v78
    if action is not None and hasattr(action, "v79".split('.')[0]):
        action.v79 = temp
    else:
        v79 = temp 


    if action is not None:
        action.v60.Ox = v64
        action.v60.Oy = v67
        action.v60.width = v70
        action.v60.height = v73
        action.v60.title = v76
        action.v60.background = v79
    else:
        v60.Ox = v64
        v60.Oy = v67
        v60.width = v70
        v60.height = v73
        v60.title = v76
        v60.background = v79

    temp = get_nested_attribute(action, 'v60')
    if temp is None:
        temp = v60
    if action is not None and hasattr(action, "view".split('.')[0]):
        action.view = temp
    else:
        view = temp 
    if model is not None: 
        model.view = view
        model.last_view = copy.deepcopy(view)

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v82".split('.')[0]):
        action.v82 = temp
    else:
        v82 = temp 

    v83 = - v82

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v84".split('.')[0]):
        action.v84 = temp
    else:
        v84 = temp 

    v81 = (v83 , v84)

    if model is not None:
        model_backup = model
        v80 = Pacman() # this makes model = None in the end!
        model = model_backup
        model.add_object(v80) # add object to model
    else:
        v80 = Pacman(root = root, view = last_view, origin = v81)


    temp = get_nested_attribute(action, 'v80')
    if temp is None:
        temp = v80
    if action is not None and hasattr(action, "v85".split('.')[0]):
        action.v85 = temp
    else:
        v85 = temp 


    temp = get_nested_attribute(action, 'v85')
    if temp is None:
        temp = v85
    if action is not None and hasattr(action, "pacman".split('.')[0]):
        action.pacman = temp
    else:
        pacman = temp 
    if model is not None: 
        model.pacman = pacman
        model.last_pacman = copy.deepcopy(pacman)
    last_refresh = time.time()
    view.update()


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v86".split('.')[0]):
        action.v86 = temp
    else:
        v86 = temp 


    temp = get_nested_attribute(action, '10')
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v87".split('.')[0]):
        action.v87 = temp
    else:
        v87 = temp 

    for i in range(v86, v87, 1):

        temp = get_nested_attribute(action, 'Close')
        if temp is None:
            temp = Close
        if action is not None and hasattr(action, "v88".split('.')[0]):
            action.v88 = temp
        else:
            v88 = temp 


        temp = get_nested_attribute(action, 'v88')
        if temp is None:
            temp = v88
        if action is not None and hasattr(action, "v89".split('.')[0]):
            action.v89 = temp
        else:
            v89 = temp 


        temp = get_nested_attribute(action, 'v89')
        if temp is None:
            temp = v89
        if action is not None and hasattr(action, "pacman.mouth".split('.')[0]):
            action.pacman.mouth = temp
        else:
            pacman.mouth = temp 

         

        temp = get_nested_attribute(action, '20')
        if temp is None:
            temp = 20
        if action is not None and hasattr(action, "v90".split('.')[0]):
            action.v90 = temp
        else:
            v90 = temp 

        while (time.time() - last_refresh <= v90/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, 'Open')
        if temp is None:
            temp = Open
        if action is not None and hasattr(action, "v91".split('.')[0]):
            action.v91 = temp
        else:
            v91 = temp 


        temp = get_nested_attribute(action, 'v91')
        if temp is None:
            temp = v91
        if action is not None and hasattr(action, "v92".split('.')[0]):
            action.v92 = temp
        else:
            v92 = temp 


        temp = get_nested_attribute(action, 'v92')
        if temp is None:
            temp = v92
        if action is not None and hasattr(action, "pacman.mouth".split('.')[0]):
            action.pacman.mouth = temp
        else:
            pacman.mouth = temp 

         

        temp = get_nested_attribute(action, '25')
        if temp is None:
            temp = 25
        if action is not None and hasattr(action, "v93".split('.')[0]):
            action.v93 = temp
        else:
            v93 = temp 

        while (time.time() - last_refresh <= v93/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v95".split('.')[0]):
            action.v95 = temp
        else:
            v95 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v96".split('.')[0]):
            action.v96 = temp
        else:
            v96 = temp 

        v94 = (v95 , v96)
        if action is not None:
            action.pacman.move_relative(v94)
        else:
            pacman.move_relative(v94)

        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v98".split('.')[0]):
            action.v98 = temp
        else:
            v98 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v99".split('.')[0]):
            action.v99 = temp
        else:
            v99 = temp 

        v97 = (v98 , v99)
        if action is not None:
            action.view.move_relative(v97)
        else:
            view.move_relative(v97)
        last_refresh = time.time()
        view.update()


    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v100".split('.')[0]):
        action.v100 = temp
    else:
        v100 = temp 

    print(v100)
    if action is not None:
        v101 = action.view.waitClick()
    else:
        v101 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v101')
    if temp is None:
        temp = v101
    if action is not None and hasattr(action, "v102".split('.')[0]):
        action.v102 = temp
    else:
        v102 = temp 


    temp = get_nested_attribute(action, 'v102')
    if temp is None:
        temp = v102
    if action is not None and hasattr(action, "v103".split('.')[0]):
        action.v103 = temp
    else:
        v103 = temp 


    temp = get_nested_attribute(action, 'v103')
    if temp is None:
        temp = v103
    if action is not None and hasattr(action, "pos".split('.')[0]):
        action.pos = temp
    else:
        pos = temp 
    if model is not None: 
        model.pos = pos
        model.last_pos = copy.deepcopy(pos)
    view.close()
