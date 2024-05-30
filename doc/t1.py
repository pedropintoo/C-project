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
    class Fire(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '55')
            if temp is None:
                temp = 55
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
                v3 = Rectangle()
                model.add_object(v3) # add object to model
            else:
                v3 = Rectangle(root = root)
            v3.origin = v0

            temp = get_nested_attribute(action, '15')
            if temp is None:
                temp = 15
            if action is not None and hasattr(action, "v5".split('.')[0]):
                action.v5 = temp
            else:
                v5 = temp 


            temp = get_nested_attribute(action, '2')
            if temp is None:
                temp = 2
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


            temp = get_nested_attribute(action, '"red"')
            if temp is None:
                temp = "red"
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


            temp = get_nested_attribute(action, '"hidden"')
            if temp is None:
                temp = "hidden"
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


            if action is not None:
                action.v3.length = v8
                action.v3.fill = v11
                action.v3.state = v14
            else:
                v3.length = v8
                v3.fill = v11
                v3.state = v14

            temp = get_nested_attribute(action, 'v3')
            if temp is None:
                temp = v3
            if action is not None and hasattr(action, "flame".split('.')[0]):
                action.flame = temp
            else:
                flame = temp 
            if model is not None: 
                model.flame = flame
                model.last_flame = copy.deepcopy(flame)

            self.fixCoords()

        def create_object(self, view):
            action = self

            if self.flame.state != self.last_flame.state:

                temp = get_nested_attribute(action, '"The flame is "')
                if temp is None:
                    temp = "The flame is "
                if action is not None and hasattr(action, "v16".split('.')[0]):
                    action.v16 = temp
                else:
                    v16 = temp 


                temp = get_nested_attribute(action, 'flame.state')
                if temp is None:
                    temp = flame.state
                if action is not None and hasattr(action, "v17".split('.')[0]):
                    action.v17 = temp
                else:
                    v17 = temp 

                v15 = v16 + v17
                print(v15)
                self.last_flame.state = copy.deepcopy(self.flame.state)
        
            action = None
            super().create_object(view)
            model = None

    #################################################################
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
            if action is not None and hasattr(action, "v19".split('.')[0]):
                action.v19 = temp
            else:
                v19 = temp 


            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v20".split('.')[0]):
                action.v20 = temp
            else:
                v20 = temp 

            v18 = (v19 , v20)

            if model is not None:
                v21 = PieSlice()
                model.add_object(v21) # add object to model
            else:
                v21 = PieSlice(root = root)
            v21.origin = v18

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v23".split('.')[0]):
                action.v23 = temp
            else:
                v23 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v24".split('.')[0]):
                action.v24 = temp
            else:
                v24 = temp 

            v22 = (v23 , v24)

            temp = get_nested_attribute(action, 'v22')
            if temp is None:
                temp = v22
            if action is not None and hasattr(action, "v25".split('.')[0]):
                action.v25 = temp
            else:
                v25 = temp 


            temp = get_nested_attribute(action, 'v25')
            if temp is None:
                temp = v25
            if action is not None and hasattr(action, "v26".split('.')[0]):
                action.v26 = temp
            else:
                v26 = temp 


            temp = get_nested_attribute(action, '"pink"')
            if temp is None:
                temp = "pink"
            if action is not None and hasattr(action, "v27".split('.')[0]):
                action.v27 = temp
            else:
                v27 = temp 


            temp = get_nested_attribute(action, 'v27')
            if temp is None:
                temp = v27
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


            temp = get_nested_attribute(action, '30')
            if temp is None:
                temp = 30
            if action is not None and hasattr(action, "v30".split('.')[0]):
                action.v30 = temp
            else:
                v30 = temp 


            temp = get_nested_attribute(action, 'v30')
            if temp is None:
                temp = v30
            if action is not None and hasattr(action, "v31".split('.')[0]):
                action.v31 = temp
            else:
                v31 = temp 


            temp = get_nested_attribute(action, 'v31')
            if temp is None:
                temp = v31
            if action is not None and hasattr(action, "v32".split('.')[0]):
                action.v32 = temp
            else:
                v32 = temp 


            temp = get_nested_attribute(action, '300')
            if temp is None:
                temp = 300
            if action is not None and hasattr(action, "v33".split('.')[0]):
                action.v33 = temp
            else:
                v33 = temp 


            temp = get_nested_attribute(action, 'v33')
            if temp is None:
                temp = v33
            if action is not None and hasattr(action, "v34".split('.')[0]):
                action.v34 = temp
            else:
                v34 = temp 


            temp = get_nested_attribute(action, 'v34')
            if temp is None:
                temp = v34
            if action is not None and hasattr(action, "v35".split('.')[0]):
                action.v35 = temp
            else:
                v35 = temp 


            if action is not None:
                action.v21.length = v26
                action.v21.fill = v29
                action.v21.start = v32
                action.v21.extent = v35
            else:
                v21.length = v26
                v21.fill = v29
                v21.start = v32
                v21.extent = v35

            temp = get_nested_attribute(action, 'v21')
            if temp is None:
                temp = v21
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
            if action is not None and hasattr(action, "v37".split('.')[0]):
                action.v37 = temp
            else:
                v37 = temp 


            temp = get_nested_attribute(action, '35')
            if temp is None:
                temp = 35
            if action is not None and hasattr(action, "v38".split('.')[0]):
                action.v38 = temp
            else:
                v38 = temp 

            v36 = (v37 , v38)

            if model is not None:
                v39 = Ellipse()
                model.add_object(v39) # add object to model
            else:
                v39 = Ellipse(root = root)
            v39.origin = v36

            temp = get_nested_attribute(action, '"black"')
            if temp is None:
                temp = "black"
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


            temp = get_nested_attribute(action, 'v41')
            if temp is None:
                temp = v41
            if action is not None and hasattr(action, "v42".split('.')[0]):
                action.v42 = temp
            else:
                v42 = temp 


            temp = get_nested_attribute(action, '5')
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v44".split('.')[0]):
                action.v44 = temp
            else:
                v44 = temp 


            temp = get_nested_attribute(action, '5')
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v45".split('.')[0]):
                action.v45 = temp
            else:
                v45 = temp 

            v43 = (v44 , v45)

            temp = get_nested_attribute(action, 'v43')
            if temp is None:
                temp = v43
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
                action.v39.fill = v42
                action.v39.length = v47
            else:
                v39.fill = v42
                v39.length = v47

            temp = get_nested_attribute(action, 'v39')
            if temp is None:
                temp = v39
            if action is not None and hasattr(action, "eye".split('.')[0]):
                action.eye = temp
            else:
                eye = temp 
            if model is not None: 
                model.eye = eye
                model.last_eye = copy.deepcopy(eye)

            temp = get_nested_attribute(action, '55')
            if temp is None:
                temp = 55
            if action is not None and hasattr(action, "v50".split('.')[0]):
                action.v50 = temp
            else:
                v50 = temp 


            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v51".split('.')[0]):
                action.v51 = temp
            else:
                v51 = temp 

            v49 = (v50 , v51)

            if model is not None:
                model_backup = model
                v48 = Fire() # this makes model = None in the end!
                model = model_backup
                model.add_object(v48) # add object to model
            else:
                v48 = Fire(root = root, view = last_view, origin = v49)


            temp = get_nested_attribute(action, 'v48')
            if temp is None:
                temp = v48
            if action is not None and hasattr(action, "v52".split('.')[0]):
                action.v52 = temp
            else:
                v52 = temp 


            temp = get_nested_attribute(action, 'v52')
            if temp is None:
                temp = v52
            if action is not None and hasattr(action, "fire".split('.')[0]):
                action.fire = temp
            else:
                fire = temp 
            if model is not None: 
                model.fire = fire
                model.last_fire = copy.deepcopy(fire)

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v61".split('.')[0]):
                action.v61 = temp
            else:
                v61 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v62".split('.')[0]):
                action.v62 = temp
            else:
                v62 = temp 

            v60 = (v61 , v62)

            temp = get_nested_attribute(action, 'v60')
            if temp is None:
                temp = v60
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


            temp = get_nested_attribute(action, 'v64')
            if temp is None:
                temp = v64
            if action is not None and hasattr(action, "len_pac".split('.')[0]):
                action.len_pac = temp
            else:
                len_pac = temp 
            if model is not None: 
                model.len_pac = len_pac
                model.last_len_pac = copy.deepcopy(len_pac)
            class v68(Enum):
                Open = auto()
                Close = auto() 
            global Open; Open = v68.Open
            global Close; Close = v68.Close   
            v69 = v68(1) # first is default

            temp = get_nested_attribute(action, 'v69')
            if temp is None:
                temp = v69
            if action is not None and hasattr(action, "v70".split('.')[0]):
                action.v70 = temp
            else:
                v70 = temp 


            temp = get_nested_attribute(action, 'v70')
            if temp is None:
                temp = v70
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

            if self.eye.fill != self.last_eye.fill:

                temp = get_nested_attribute(action, 'eye.fill')
                if temp is None:
                    temp = eye.fill
                if action is not None and hasattr(action, "v54".split('.')[0]):
                    action.v54 = temp
                else:
                    v54 = temp 


                temp = get_nested_attribute(action, '"red"')
                if temp is None:
                    temp = "red"
                if action is not None and hasattr(action, "v55".split('.')[0]):
                    action.v55 = temp
                else:
                    v55 = temp 

                v53 = v54 == v55
                if v53:

                    temp = get_nested_attribute(action, '"normal"')
                    if temp is None:
                        temp = "normal"
                    if action is not None and hasattr(action, "v56".split('.')[0]):
                        action.v56 = temp
                    else:
                        v56 = temp 


                    temp = get_nested_attribute(action, 'v56')
                    if temp is None:
                        temp = v56
                    if action is not None and hasattr(action, "v57".split('.')[0]):
                        action.v57 = temp
                    else:
                        v57 = temp 


                    temp = get_nested_attribute(action, 'v57')
                    if temp is None:
                        temp = v57
                    if action is not None and hasattr(action, "fire.flame.state".split('.')[0]):
                        action.fire.flame.state = temp
                    else:
                        fire.flame.state = temp 

                else:

                    temp = get_nested_attribute(action, '"hidden"')
                    if temp is None:
                        temp = "hidden"
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


                    temp = get_nested_attribute(action, 'v59')
                    if temp is None:
                        temp = v59
                    if action is not None and hasattr(action, "fire.flame.state".split('.')[0]):
                        action.fire.flame.state = temp
                    else:
                        fire.flame.state = temp 

                self.last_eye.fill = copy.deepcopy(self.eye.fill)


            if self.len_pac != self.last_len_pac:

                temp = get_nested_attribute(action, 'len_pac')
                if temp is None:
                    temp = len_pac
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


                if action is not None:
                    action.face.length = v67
                else:
                    face.length = v67
                self.last_len_pac = copy.deepcopy(self.len_pac)


            if self.mouth != self.last_mouth:

                temp = get_nested_attribute(action, 'mouth')
                if temp is None:
                    temp = mouth
                if action is not None and hasattr(action, "v72".split('.')[0]):
                    action.v72 = temp
                else:
                    v72 = temp 


                temp = get_nested_attribute(action, 'Open')
                if temp is None:
                    temp = Open
                if action is not None and hasattr(action, "v73".split('.')[0]):
                    action.v73 = temp
                else:
                    v73 = temp 

                v71 = v72 == v73
                if v71:

                    temp = get_nested_attribute(action, '30')
                    if temp is None:
                        temp = 30
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


                    temp = get_nested_attribute(action, '300')
                    if temp is None:
                        temp = 300
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
                        action.face.start = v76
                        action.face.extent = v79
                    else:
                        face.start = v76
                        face.extent = v79

                    temp = get_nested_attribute(action, '50')
                    if temp is None:
                        temp = 50
                    if action is not None and hasattr(action, "v81".split('.')[0]):
                        action.v81 = temp
                    else:
                        v81 = temp 


                    temp = get_nested_attribute(action, '50')
                    if temp is None:
                        temp = 50
                    if action is not None and hasattr(action, "v82".split('.')[0]):
                        action.v82 = temp
                    else:
                        v82 = temp 

                    v80 = (v81 , v82)

                    temp = get_nested_attribute(action, 'v80')
                    if temp is None:
                        temp = v80
                    if action is not None and hasattr(action, "v83".split('.')[0]):
                        action.v83 = temp
                    else:
                        v83 = temp 


                    temp = get_nested_attribute(action, 'v83')
                    if temp is None:
                        temp = v83
                    if action is not None and hasattr(action, "len_pac".split('.')[0]):
                        action.len_pac = temp
                    else:
                        len_pac = temp 


                    temp = get_nested_attribute(action, 'face.fill')
                    if temp is None:
                        temp = face.fill
                    if action is not None and hasattr(action, "v84".split('.')[0]):
                        action.v84 = temp
                    else:
                        v84 = temp 


                    temp = get_nested_attribute(action, 'v84')
                    if temp is None:
                        temp = v84
                    if action is not None and hasattr(action, "v85".split('.')[0]):
                        action.v85 = temp
                    else:
                        v85 = temp 


                    temp = get_nested_attribute(action, 'v85')
                    if temp is None:
                        temp = v85
                    if action is not None and hasattr(action, "v86".split('.')[0]):
                        action.v86 = temp
                    else:
                        v86 = temp 


                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v88".split('.')[0]):
                        action.v88 = temp
                    else:
                        v88 = temp 


                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v89".split('.')[0]):
                        action.v89 = temp
                    else:
                        v89 = temp 

                    v87 = (v88 , v89)

                    temp = get_nested_attribute(action, 'v87')
                    if temp is None:
                        temp = v87
                    if action is not None and hasattr(action, "v90".split('.')[0]):
                        action.v90 = temp
                    else:
                        v90 = temp 


                    temp = get_nested_attribute(action, 'v90')
                    if temp is None:
                        temp = v90
                    if action is not None and hasattr(action, "v91".split('.')[0]):
                        action.v91 = temp
                    else:
                        v91 = temp 


                    if action is not None:
                        action.eye.fill = v86
                        action.eye.length = v91
                    else:
                        eye.fill = v86
                        eye.length = v91

                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v93".split('.')[0]):
                        action.v93 = temp
                    else:
                        v93 = temp 

                    v94 = - v93

                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v95".split('.')[0]):
                        action.v95 = temp
                    else:
                        v95 = temp 

                    v96 = - v95
                    v92 = (v94 , v96)
                    if action is not None:
                        action.eye.move_relative(v92)
                    else:
                        eye.move_relative(v92)
                else:

                    temp = get_nested_attribute(action, '1')
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v97".split('.')[0]):
                        action.v97 = temp
                    else:
                        v97 = temp 


                    temp = get_nested_attribute(action, 'v97')
                    if temp is None:
                        temp = v97
                    if action is not None and hasattr(action, "v98".split('.')[0]):
                        action.v98 = temp
                    else:
                        v98 = temp 


                    temp = get_nested_attribute(action, 'v98')
                    if temp is None:
                        temp = v98
                    if action is not None and hasattr(action, "v99".split('.')[0]):
                        action.v99 = temp
                    else:
                        v99 = temp 


                    temp = get_nested_attribute(action, '359')
                    if temp is None:
                        temp = 359
                    if action is not None and hasattr(action, "v100".split('.')[0]):
                        action.v100 = temp
                    else:
                        v100 = temp 


                    temp = get_nested_attribute(action, 'v100')
                    if temp is None:
                        temp = v100
                    if action is not None and hasattr(action, "v101".split('.')[0]):
                        action.v101 = temp
                    else:
                        v101 = temp 


                    temp = get_nested_attribute(action, 'v101')
                    if temp is None:
                        temp = v101
                    if action is not None and hasattr(action, "v102".split('.')[0]):
                        action.v102 = temp
                    else:
                        v102 = temp 


                    if action is not None:
                        action.face.start = v99
                        action.face.extent = v102
                    else:
                        face.start = v99
                        face.extent = v102

                    temp = get_nested_attribute(action, '60')
                    if temp is None:
                        temp = 60
                    if action is not None and hasattr(action, "v104".split('.')[0]):
                        action.v104 = temp
                    else:
                        v104 = temp 


                    temp = get_nested_attribute(action, '60')
                    if temp is None:
                        temp = 60
                    if action is not None and hasattr(action, "v105".split('.')[0]):
                        action.v105 = temp
                    else:
                        v105 = temp 

                    v103 = (v104 , v105)

                    temp = get_nested_attribute(action, 'v103')
                    if temp is None:
                        temp = v103
                    if action is not None and hasattr(action, "v106".split('.')[0]):
                        action.v106 = temp
                    else:
                        v106 = temp 


                    temp = get_nested_attribute(action, 'v106')
                    if temp is None:
                        temp = v106
                    if action is not None and hasattr(action, "len_pac".split('.')[0]):
                        action.len_pac = temp
                    else:
                        len_pac = temp 


                    temp = get_nested_attribute(action, '"red"')
                    if temp is None:
                        temp = "red"
                    if action is not None and hasattr(action, "v107".split('.')[0]):
                        action.v107 = temp
                    else:
                        v107 = temp 


                    temp = get_nested_attribute(action, 'v107')
                    if temp is None:
                        temp = v107
                    if action is not None and hasattr(action, "v108".split('.')[0]):
                        action.v108 = temp
                    else:
                        v108 = temp 


                    temp = get_nested_attribute(action, 'v108')
                    if temp is None:
                        temp = v108
                    if action is not None and hasattr(action, "v109".split('.')[0]):
                        action.v109 = temp
                    else:
                        v109 = temp 


                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v111".split('.')[0]):
                        action.v111 = temp
                    else:
                        v111 = temp 


                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v112".split('.')[0]):
                        action.v112 = temp
                    else:
                        v112 = temp 

                    v110 = (v111 , v112)

                    temp = get_nested_attribute(action, 'v110')
                    if temp is None:
                        temp = v110
                    if action is not None and hasattr(action, "v113".split('.')[0]):
                        action.v113 = temp
                    else:
                        v113 = temp 


                    temp = get_nested_attribute(action, 'v113')
                    if temp is None:
                        temp = v113
                    if action is not None and hasattr(action, "v114".split('.')[0]):
                        action.v114 = temp
                    else:
                        v114 = temp 


                    if action is not None:
                        action.eye.fill = v109
                        action.eye.length = v114
                    else:
                        eye.fill = v109
                        eye.length = v114

                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v116".split('.')[0]):
                        action.v116 = temp
                    else:
                        v116 = temp 


                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v117".split('.')[0]):
                        action.v117 = temp
                    else:
                        v117 = temp 

                    v115 = (v116 , v117)
                    if action is not None:
                        action.eye.move_relative(v115)
                    else:
                        eye.move_relative(v115)
                self.last_mouth = copy.deepcopy(self.mouth)
        
            action = None
            super().create_object(view)
            model = None

    #################################################################

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v119".split('.')[0]):
        action.v119 = temp
    else:
        v119 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v120".split('.')[0]):
        action.v120 = temp
    else:
        v120 = temp 

    v118 = (v119 , v120)

    if model is not None:
        v121 = Rectangle()
        model.add_object(v121) # add object to model
    else:
        v121 = Rectangle(root = root)
    v121.origin = v118

    temp = get_nested_attribute(action, '1000')
    if temp is None:
        temp = 1000
    if action is not None and hasattr(action, "v123".split('.')[0]):
        action.v123 = temp
    else:
        v123 = temp 


    temp = get_nested_attribute(action, '70')
    if temp is None:
        temp = 70
    if action is not None and hasattr(action, "v124".split('.')[0]):
        action.v124 = temp
    else:
        v124 = temp 

    v122 = (v123 , v124)

    temp = get_nested_attribute(action, 'v122')
    if temp is None:
        temp = v122
    if action is not None and hasattr(action, "v125".split('.')[0]):
        action.v125 = temp
    else:
        v125 = temp 


    temp = get_nested_attribute(action, 'v125')
    if temp is None:
        temp = v125
    if action is not None and hasattr(action, "v126".split('.')[0]):
        action.v126 = temp
    else:
        v126 = temp 


    temp = get_nested_attribute(action, '"blue"')
    if temp is None:
        temp = "blue"
    if action is not None and hasattr(action, "v127".split('.')[0]):
        action.v127 = temp
    else:
        v127 = temp 


    temp = get_nested_attribute(action, 'v127')
    if temp is None:
        temp = v127
    if action is not None and hasattr(action, "v128".split('.')[0]):
        action.v128 = temp
    else:
        v128 = temp 


    temp = get_nested_attribute(action, 'v128')
    if temp is None:
        temp = v128
    if action is not None and hasattr(action, "v129".split('.')[0]):
        action.v129 = temp
    else:
        v129 = temp 


    if action is not None:
        action.v121.length = v126
        action.v121.fill = v129
    else:
        v121.length = v126
        v121.fill = v129

    if model is not None:
        v130 = View()
        model.add_object(v130) # add object to model
    else:
        v130 = View(root = root)
    last_view = v130

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v131".split('.')[0]):
        action.v131 = temp
    else:
        v131 = temp 

    v132 = - v131

    temp = get_nested_attribute(action, 'v132')
    if temp is None:
        temp = v132
    if action is not None and hasattr(action, "v133".split('.')[0]):
        action.v133 = temp
    else:
        v133 = temp 


    temp = get_nested_attribute(action, 'v133')
    if temp is None:
        temp = v133
    if action is not None and hasattr(action, "v134".split('.')[0]):
        action.v134 = temp
    else:
        v134 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v135".split('.')[0]):
        action.v135 = temp
    else:
        v135 = temp 


    temp = get_nested_attribute(action, 'v135')
    if temp is None:
        temp = v135
    if action is not None and hasattr(action, "v136".split('.')[0]):
        action.v136 = temp
    else:
        v136 = temp 


    temp = get_nested_attribute(action, 'v136')
    if temp is None:
        temp = v136
    if action is not None and hasattr(action, "v137".split('.')[0]):
        action.v137 = temp
    else:
        v137 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
    if action is not None and hasattr(action, "v138".split('.')[0]):
        action.v138 = temp
    else:
        v138 = temp 


    temp = get_nested_attribute(action, 'v138')
    if temp is None:
        temp = v138
    if action is not None and hasattr(action, "v139".split('.')[0]):
        action.v139 = temp
    else:
        v139 = temp 


    temp = get_nested_attribute(action, 'v139')
    if temp is None:
        temp = v139
    if action is not None and hasattr(action, "v140".split('.')[0]):
        action.v140 = temp
    else:
        v140 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
    if action is not None and hasattr(action, "v141".split('.')[0]):
        action.v141 = temp
    else:
        v141 = temp 


    temp = get_nested_attribute(action, 'v141')
    if temp is None:
        temp = v141
    if action is not None and hasattr(action, "v142".split('.')[0]):
        action.v142 = temp
    else:
        v142 = temp 


    temp = get_nested_attribute(action, 'v142')
    if temp is None:
        temp = v142
    if action is not None and hasattr(action, "v143".split('.')[0]):
        action.v143 = temp
    else:
        v143 = temp 


    temp = get_nested_attribute(action, '"Illustrating a moving pacman"')
    if temp is None:
        temp = "Illustrating a moving pacman"
    if action is not None and hasattr(action, "v144".split('.')[0]):
        action.v144 = temp
    else:
        v144 = temp 


    temp = get_nested_attribute(action, 'v144')
    if temp is None:
        temp = v144
    if action is not None and hasattr(action, "v145".split('.')[0]):
        action.v145 = temp
    else:
        v145 = temp 


    temp = get_nested_attribute(action, 'v145')
    if temp is None:
        temp = v145
    if action is not None and hasattr(action, "v146".split('.')[0]):
        action.v146 = temp
    else:
        v146 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v147".split('.')[0]):
        action.v147 = temp
    else:
        v147 = temp 


    temp = get_nested_attribute(action, 'v147')
    if temp is None:
        temp = v147
    if action is not None and hasattr(action, "v148".split('.')[0]):
        action.v148 = temp
    else:
        v148 = temp 


    temp = get_nested_attribute(action, 'v148')
    if temp is None:
        temp = v148
    if action is not None and hasattr(action, "v149".split('.')[0]):
        action.v149 = temp
    else:
        v149 = temp 


    if action is not None:
        action.v130.Ox = v134
        action.v130.Oy = v137
        action.v130.width = v140
        action.v130.height = v143
        action.v130.title = v146
        action.v130.background = v149
    else:
        v130.Ox = v134
        v130.Oy = v137
        v130.width = v140
        v130.height = v143
        v130.title = v146
        v130.background = v149

    temp = get_nested_attribute(action, 'v130')
    if temp is None:
        temp = v130
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
    if action is not None and hasattr(action, "v152".split('.')[0]):
        action.v152 = temp
    else:
        v152 = temp 

    v153 = - v152

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v154".split('.')[0]):
        action.v154 = temp
    else:
        v154 = temp 

    v151 = (v153 , v154)

    if model is not None:
        model_backup = model
        v150 = Pacman() # this makes model = None in the end!
        model = model_backup
        model.add_object(v150) # add object to model
    else:
        v150 = Pacman(root = root, view = last_view, origin = v151)


    temp = get_nested_attribute(action, 'v150')
    if temp is None:
        temp = v150
    if action is not None and hasattr(action, "v155".split('.')[0]):
        action.v155 = temp
    else:
        v155 = temp 


    temp = get_nested_attribute(action, 'v155')
    if temp is None:
        temp = v155
    if action is not None and hasattr(action, "pacman".split('.')[0]):
        action.pacman = temp
    else:
        pacman = temp 
    if model is not None: 
        model.pacman = pacman
        model.last_pacman = copy.deepcopy(pacman)
    last_refresh = time.time()
    view.update()


    if model is not None:
        v156 = View()
        model.add_object(v156) # add object to model
    else:
        v156 = View(root = root)
    last_view = v156

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v157".split('.')[0]):
        action.v157 = temp
    else:
        v157 = temp 

    v158 = - v157

    temp = get_nested_attribute(action, 'v158')
    if temp is None:
        temp = v158
    if action is not None and hasattr(action, "v159".split('.')[0]):
        action.v159 = temp
    else:
        v159 = temp 


    temp = get_nested_attribute(action, 'v159')
    if temp is None:
        temp = v159
    if action is not None and hasattr(action, "v160".split('.')[0]):
        action.v160 = temp
    else:
        v160 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v161".split('.')[0]):
        action.v161 = temp
    else:
        v161 = temp 


    temp = get_nested_attribute(action, 'v161')
    if temp is None:
        temp = v161
    if action is not None and hasattr(action, "v162".split('.')[0]):
        action.v162 = temp
    else:
        v162 = temp 


    temp = get_nested_attribute(action, 'v162')
    if temp is None:
        temp = v162
    if action is not None and hasattr(action, "v163".split('.')[0]):
        action.v163 = temp
    else:
        v163 = temp 


    temp = get_nested_attribute(action, '400')
    if temp is None:
        temp = 400
    if action is not None and hasattr(action, "v164".split('.')[0]):
        action.v164 = temp
    else:
        v164 = temp 


    temp = get_nested_attribute(action, 'v164')
    if temp is None:
        temp = v164
    if action is not None and hasattr(action, "v165".split('.')[0]):
        action.v165 = temp
    else:
        v165 = temp 


    temp = get_nested_attribute(action, 'v165')
    if temp is None:
        temp = v165
    if action is not None and hasattr(action, "v166".split('.')[0]):
        action.v166 = temp
    else:
        v166 = temp 


    temp = get_nested_attribute(action, '400')
    if temp is None:
        temp = 400
    if action is not None and hasattr(action, "v167".split('.')[0]):
        action.v167 = temp
    else:
        v167 = temp 


    temp = get_nested_attribute(action, 'v167')
    if temp is None:
        temp = v167
    if action is not None and hasattr(action, "v168".split('.')[0]):
        action.v168 = temp
    else:
        v168 = temp 


    temp = get_nested_attribute(action, 'v168')
    if temp is None:
        temp = v168
    if action is not None and hasattr(action, "v169".split('.')[0]):
        action.v169 = temp
    else:
        v169 = temp 


    temp = get_nested_attribute(action, '"Illustrating a moving pacman"')
    if temp is None:
        temp = "Illustrating a moving pacman"
    if action is not None and hasattr(action, "v170".split('.')[0]):
        action.v170 = temp
    else:
        v170 = temp 


    temp = get_nested_attribute(action, 'v170')
    if temp is None:
        temp = v170
    if action is not None and hasattr(action, "v171".split('.')[0]):
        action.v171 = temp
    else:
        v171 = temp 


    temp = get_nested_attribute(action, 'v171')
    if temp is None:
        temp = v171
    if action is not None and hasattr(action, "v172".split('.')[0]):
        action.v172 = temp
    else:
        v172 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v173".split('.')[0]):
        action.v173 = temp
    else:
        v173 = temp 


    temp = get_nested_attribute(action, 'v173')
    if temp is None:
        temp = v173
    if action is not None and hasattr(action, "v174".split('.')[0]):
        action.v174 = temp
    else:
        v174 = temp 


    temp = get_nested_attribute(action, 'v174')
    if temp is None:
        temp = v174
    if action is not None and hasattr(action, "v175".split('.')[0]):
        action.v175 = temp
    else:
        v175 = temp 


    if action is not None:
        action.v156.Ox = v160
        action.v156.Oy = v163
        action.v156.width = v166
        action.v156.height = v169
        action.v156.title = v172
        action.v156.background = v175
    else:
        v156.Ox = v160
        v156.Oy = v163
        v156.width = v166
        v156.height = v169
        v156.title = v172
        v156.background = v175

    temp = get_nested_attribute(action, 'v156')
    if temp is None:
        temp = v156
    if action is not None and hasattr(action, "view2".split('.')[0]):
        action.view2 = temp
    else:
        view2 = temp 
    if model is not None: 
        model.view2 = view2
        model.last_view2 = copy.deepcopy(view2)
    last_refresh = time.time()
    view2.update()


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v176".split('.')[0]):
        action.v176 = temp
    else:
        v176 = temp 


    temp = get_nested_attribute(action, '10')
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v177".split('.')[0]):
        action.v177 = temp
    else:
        v177 = temp 

    for i in range(v176, v177, 1):

        temp = get_nested_attribute(action, 'Close')
        if temp is None:
            temp = Close
        if action is not None and hasattr(action, "v178".split('.')[0]):
            action.v178 = temp
        else:
            v178 = temp 


        temp = get_nested_attribute(action, 'v178')
        if temp is None:
            temp = v178
        if action is not None and hasattr(action, "v179".split('.')[0]):
            action.v179 = temp
        else:
            v179 = temp 


        temp = get_nested_attribute(action, 'v179')
        if temp is None:
            temp = v179
        if action is not None and hasattr(action, "pacman.mouth".split('.')[0]):
            action.pacman.mouth = temp
        else:
            pacman.mouth = temp 

        last_refresh = time.time()
        view2.update()

         

        temp = get_nested_attribute(action, '175')
        if temp is None:
            temp = 175
        if action is not None and hasattr(action, "v180".split('.')[0]):
            action.v180 = temp
        else:
            v180 = temp 

        while (time.time() - last_refresh <= v180/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, 'Open')
        if temp is None:
            temp = Open
        if action is not None and hasattr(action, "v181".split('.')[0]):
            action.v181 = temp
        else:
            v181 = temp 


        temp = get_nested_attribute(action, 'v181')
        if temp is None:
            temp = v181
        if action is not None and hasattr(action, "v182".split('.')[0]):
            action.v182 = temp
        else:
            v182 = temp 


        temp = get_nested_attribute(action, 'v182')
        if temp is None:
            temp = v182
        if action is not None and hasattr(action, "pacman.mouth".split('.')[0]):
            action.pacman.mouth = temp
        else:
            pacman.mouth = temp 

        last_refresh = time.time()
        view2.update()

         

        temp = get_nested_attribute(action, '175')
        if temp is None:
            temp = 175
        if action is not None and hasattr(action, "v183".split('.')[0]):
            action.v183 = temp
        else:
            v183 = temp 

        while (time.time() - last_refresh <= v183/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v185".split('.')[0]):
            action.v185 = temp
        else:
            v185 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v186".split('.')[0]):
            action.v186 = temp
        else:
            v186 = temp 

        v184 = (v185 , v186)
        if action is not None:
            action.pacman.move_relative(v184)
        else:
            pacman.move_relative(v184)

        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v188".split('.')[0]):
            action.v188 = temp
        else:
            v188 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v189".split('.')[0]):
            action.v189 = temp
        else:
            v189 = temp 

        v187 = (v188 , v189)
        if action is not None:
            action.view.move_relative(v187)
        else:
            view.move_relative(v187)

        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v191".split('.')[0]):
            action.v191 = temp
        else:
            v191 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v192".split('.')[0]):
            action.v192 = temp
        else:
            v192 = temp 

        v190 = (v191 , v192)
        if action is not None:
            action.view2.move_relative(v190)
        else:
            view2.move_relative(v190)
         

        temp = get_nested_attribute(action, '175')
        if temp is None:
            temp = 175
        if action is not None and hasattr(action, "v193".split('.')[0]):
            action.v193 = temp
        else:
            v193 = temp 

        while (time.time() - last_refresh <= v193/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()

         

        temp = get_nested_attribute(action, '175')
        if temp is None:
            temp = 175
        if action is not None and hasattr(action, "v194".split('.')[0]):
            action.v194 = temp
        else:
            v194 = temp 

        while (time.time() - last_refresh <= v194/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view2.update()


    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v195".split('.')[0]):
        action.v195 = temp
    else:
        v195 = temp 

    print(v195)
    if action is not None:
        v196 = action.view.waitClick()
    else:
        v196 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v196')
    if temp is None:
        temp = v196
    if action is not None and hasattr(action, "v197".split('.')[0]):
        action.v197 = temp
    else:
        v197 = temp 


    temp = get_nested_attribute(action, 'v197')
    if temp is None:
        temp = v197
    if action is not None and hasattr(action, "v198".split('.')[0]):
        action.v198 = temp
    else:
        v198 = temp 


    temp = get_nested_attribute(action, 'v198')
    if temp is None:
        temp = v198
    if action is not None and hasattr(action, "pos".split('.')[0]):
        action.pos = temp
    else:
        pos = temp 
    if model is not None: 
        model.pos = pos
        model.last_pos = copy.deepcopy(pos)
    view.close()
