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

            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
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


            temp = get_nested_attribute(action, 'v17')
            if temp is None:
                temp = v17
            if action is not None and hasattr(action, "color_count".split('.')[0]):
                action.color_count = temp
            else:
                color_count = temp 
            if model is not None: 
                model.color_count = color_count
                model.last_color_count = copy.deepcopy(color_count)

            self.fixCoords()

        def create_object(self, view):
            action = self

            if self.flame.state != self.last_flame.state:

                temp = get_nested_attribute(action, '"The flame is "')
                if temp is None:
                    temp = "The flame is "
                if action is not None and hasattr(action, "v19".split('.')[0]):
                    action.v19 = temp
                else:
                    v19 = temp 


                temp = get_nested_attribute(action, 'flame.state')
                if temp is None:
                    temp = flame.state
                if action is not None and hasattr(action, "v20".split('.')[0]):
                    action.v20 = temp
                else:
                    v20 = temp 

                v18 = v19 + v20
                print(v18)

                temp = get_nested_attribute(action, 'flame.state')
                if temp is None:
                    temp = flame.state
                if action is not None and hasattr(action, "v22".split('.')[0]):
                    action.v22 = temp
                else:
                    v22 = temp 


                temp = get_nested_attribute(action, '"normal"')
                if temp is None:
                    temp = "normal"
                if action is not None and hasattr(action, "v23".split('.')[0]):
                    action.v23 = temp
                else:
                    v23 = temp 

                v21 = v22 == v23
                if v21:

                    temp = get_nested_attribute(action, 'color_count')
                    if temp is None:
                        temp = color_count
                    if action is not None and hasattr(action, "v25".split('.')[0]):
                        action.v25 = temp
                    else:
                        v25 = temp 


                    temp = get_nested_attribute(action, '0')
                    if temp is None:
                        temp = 0
                    if action is not None and hasattr(action, "v26".split('.')[0]):
                        action.v26 = temp
                    else:
                        v26 = temp 

                    v24 = v25 == v26
                    if v24:

                        temp = get_nested_attribute(action, '"red"')
                        if temp is None:
                            temp = "red"
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
                        if action is not None and hasattr(action, "flame.fill".split('.')[0]):
                            action.flame.fill = temp
                        else:
                            flame.fill = temp 


                        temp = get_nested_attribute(action, '1')
                        if temp is None:
                            temp = 1
                        if action is not None and hasattr(action, "v29".split('.')[0]):
                            action.v29 = temp
                        else:
                            v29 = temp 


                        temp = get_nested_attribute(action, 'v29')
                        if temp is None:
                            temp = v29
                        if action is not None and hasattr(action, "v30".split('.')[0]):
                            action.v30 = temp
                        else:
                            v30 = temp 


                        temp = get_nested_attribute(action, 'v30')
                        if temp is None:
                            temp = v30
                        if action is not None and hasattr(action, "color_count".split('.')[0]):
                            action.color_count = temp
                        else:
                            color_count = temp 
                        
                    else:

                        temp = get_nested_attribute(action, '"blue"')
                        if temp is None:
                            temp = "blue"
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


                        temp = get_nested_attribute(action, 'v32')
                        if temp is None:
                            temp = v32
                        if action is not None and hasattr(action, "flame.fill".split('.')[0]):
                            action.flame.fill = temp
                        else:
                            flame.fill = temp 


                        temp = get_nested_attribute(action, '0')
                        if temp is None:
                            temp = 0
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
                        if action is not None and hasattr(action, "color_count".split('.')[0]):
                            action.color_count = temp
                        else:
                            color_count = temp 

                            
                self.last_flame.state = copy.deepcopy(self.flame.state)
        
            action = None
            super().create_object(view)
            model = None

        def __deepcopy__(self, memo=None):
            """Create a deep copy of the model."""
            if memo is None:
                memo = {} # this is required by the deepcopy protocol
            new_model = Fire()

            self.copyAttributesTo(new_model)
            return new_model       

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
            if action is not None and hasattr(action, "v36".split('.')[0]):
                action.v36 = temp
            else:
                v36 = temp 


            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v37".split('.')[0]):
                action.v37 = temp
            else:
                v37 = temp 

            v35 = (v36 , v37)

            if model is not None:
                v38 = PieSlice()
                model.add_object(v38) # add object to model
            else:
                v38 = PieSlice(root = root)
            v38.origin = v35

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v40".split('.')[0]):
                action.v40 = temp
            else:
                v40 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v41".split('.')[0]):
                action.v41 = temp
            else:
                v41 = temp 

            v39 = (v40 , v41)

            temp = get_nested_attribute(action, 'v39')
            if temp is None:
                temp = v39
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


            temp = get_nested_attribute(action, '"pink"')
            if temp is None:
                temp = "pink"
            if action is not None and hasattr(action, "v44".split('.')[0]):
                action.v44 = temp
            else:
                v44 = temp 


            temp = get_nested_attribute(action, 'v44')
            if temp is None:
                temp = v44
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


            temp = get_nested_attribute(action, '30')
            if temp is None:
                temp = 30
            if action is not None and hasattr(action, "v47".split('.')[0]):
                action.v47 = temp
            else:
                v47 = temp 


            temp = get_nested_attribute(action, 'v47')
            if temp is None:
                temp = v47
            if action is not None and hasattr(action, "v48".split('.')[0]):
                action.v48 = temp
            else:
                v48 = temp 


            temp = get_nested_attribute(action, 'v48')
            if temp is None:
                temp = v48
            if action is not None and hasattr(action, "v49".split('.')[0]):
                action.v49 = temp
            else:
                v49 = temp 


            temp = get_nested_attribute(action, '300')
            if temp is None:
                temp = 300
            if action is not None and hasattr(action, "v50".split('.')[0]):
                action.v50 = temp
            else:
                v50 = temp 


            temp = get_nested_attribute(action, 'v50')
            if temp is None:
                temp = v50
            if action is not None and hasattr(action, "v51".split('.')[0]):
                action.v51 = temp
            else:
                v51 = temp 


            temp = get_nested_attribute(action, 'v51')
            if temp is None:
                temp = v51
            if action is not None and hasattr(action, "v52".split('.')[0]):
                action.v52 = temp
            else:
                v52 = temp 


            if action is not None:
                action.v38.length = v43
                action.v38.fill = v46
                action.v38.start = v49
                action.v38.extent = v52
            else:
                v38.length = v43
                v38.fill = v46
                v38.start = v49
                v38.extent = v52

            temp = get_nested_attribute(action, 'v38')
            if temp is None:
                temp = v38
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
            if action is not None and hasattr(action, "v54".split('.')[0]):
                action.v54 = temp
            else:
                v54 = temp 


            temp = get_nested_attribute(action, '35')
            if temp is None:
                temp = 35
            if action is not None and hasattr(action, "v55".split('.')[0]):
                action.v55 = temp
            else:
                v55 = temp 

            v53 = (v54 , v55)

            if model is not None:
                v56 = Ellipse()
                model.add_object(v56) # add object to model
            else:
                v56 = Ellipse(root = root)
            v56.origin = v53

            temp = get_nested_attribute(action, '"black"')
            if temp is None:
                temp = "black"
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


            temp = get_nested_attribute(action, '5')
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v61".split('.')[0]):
                action.v61 = temp
            else:
                v61 = temp 


            temp = get_nested_attribute(action, '5')
            if temp is None:
                temp = 5
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


            if action is not None:
                action.v56.fill = v59
                action.v56.length = v64
            else:
                v56.fill = v59
                v56.length = v64

            temp = get_nested_attribute(action, 'v56')
            if temp is None:
                temp = v56
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
            if action is not None and hasattr(action, "v67".split('.')[0]):
                action.v67 = temp
            else:
                v67 = temp 


            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v68".split('.')[0]):
                action.v68 = temp
            else:
                v68 = temp 

            v66 = (v67 , v68)

            if model is not None:
                model_backup = model
                v65 = Fire() # this makes model = None in the end!
                model = model_backup
                model.add_object(v65) # add object to model
            else:
                v65 = Fire(root = root, view = last_view, origin = v66)


            temp = get_nested_attribute(action, 'v65')
            if temp is None:
                temp = v65
            if action is not None and hasattr(action, "v69".split('.')[0]):
                action.v69 = temp
            else:
                v69 = temp 


            temp = get_nested_attribute(action, 'v69')
            if temp is None:
                temp = v69
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
            if action is not None and hasattr(action, "v78".split('.')[0]):
                action.v78 = temp
            else:
                v78 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v79".split('.')[0]):
                action.v79 = temp
            else:
                v79 = temp 

            v77 = (v78 , v79)

            temp = get_nested_attribute(action, 'v77')
            if temp is None:
                temp = v77
            if action is not None and hasattr(action, "v80".split('.')[0]):
                action.v80 = temp
            else:
                v80 = temp 


            temp = get_nested_attribute(action, 'v80')
            if temp is None:
                temp = v80
            if action is not None and hasattr(action, "v81".split('.')[0]):
                action.v81 = temp
            else:
                v81 = temp 


            temp = get_nested_attribute(action, 'v81')
            if temp is None:
                temp = v81
            if action is not None and hasattr(action, "len_pac".split('.')[0]):
                action.len_pac = temp
            else:
                len_pac = temp 
            if model is not None: 
                model.len_pac = len_pac
                model.last_len_pac = copy.deepcopy(len_pac)
            class v85(Enum):
                Open = auto()
                Close = auto() 
            global Open; Open = v85.Open
            global Close; Close = v85.Close   
            v86 = v85(1) # first is default

            temp = get_nested_attribute(action, 'v86')
            if temp is None:
                temp = v86
            if action is not None and hasattr(action, "v87".split('.')[0]):
                action.v87 = temp
            else:
                v87 = temp 


            temp = get_nested_attribute(action, 'v87')
            if temp is None:
                temp = v87
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
                if action is not None and hasattr(action, "v71".split('.')[0]):
                    action.v71 = temp
                else:
                    v71 = temp 


                temp = get_nested_attribute(action, '"red"')
                if temp is None:
                    temp = "red"
                if action is not None and hasattr(action, "v72".split('.')[0]):
                    action.v72 = temp
                else:
                    v72 = temp 

                v70 = v71 == v72
                if v70:

                    temp = get_nested_attribute(action, '"normal"')
                    if temp is None:
                        temp = "normal"
                    if action is not None and hasattr(action, "v73".split('.')[0]):
                        action.v73 = temp
                    else:
                        v73 = temp 


                    temp = get_nested_attribute(action, 'v73')
                    if temp is None:
                        temp = v73
                    if action is not None and hasattr(action, "v74".split('.')[0]):
                        action.v74 = temp
                    else:
                        v74 = temp 


                    temp = get_nested_attribute(action, 'v74')
                    if temp is None:
                        temp = v74
                    if action is not None and hasattr(action, "fire.flame.state".split('.')[0]):
                        action.fire.flame.state = temp
                    else:
                        fire.flame.state = temp 
                    
                else:

                    temp = get_nested_attribute(action, '"hidden"')
                    if temp is None:
                        temp = "hidden"
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


                    temp = get_nested_attribute(action, 'v76')
                    if temp is None:
                        temp = v76
                    if action is not None and hasattr(action, "fire.flame.state".split('.')[0]):
                        action.fire.flame.state = temp
                    else:
                        fire.flame.state = temp 

                    
                self.last_eye.fill = copy.deepcopy(self.eye.fill)


            if self.len_pac != self.last_len_pac:

                temp = get_nested_attribute(action, 'len_pac')
                if temp is None:
                    temp = len_pac
                if action is not None and hasattr(action, "v82".split('.')[0]):
                    action.v82 = temp
                else:
                    v82 = temp 


                temp = get_nested_attribute(action, 'v82')
                if temp is None:
                    temp = v82
                if action is not None and hasattr(action, "v83".split('.')[0]):
                    action.v83 = temp
                else:
                    v83 = temp 


                temp = get_nested_attribute(action, 'v83')
                if temp is None:
                    temp = v83
                if action is not None and hasattr(action, "v84".split('.')[0]):
                    action.v84 = temp
                else:
                    v84 = temp 


                if action is not None:
                    action.face.length = v84
                else:
                    face.length = v84
                self.last_len_pac = copy.deepcopy(self.len_pac)


            if self.mouth != self.last_mouth:

                temp = get_nested_attribute(action, 'mouth')
                if temp is None:
                    temp = mouth
                if action is not None and hasattr(action, "v89".split('.')[0]):
                    action.v89 = temp
                else:
                    v89 = temp 


                temp = get_nested_attribute(action, 'Open')
                if temp is None:
                    temp = Open
                if action is not None and hasattr(action, "v90".split('.')[0]):
                    action.v90 = temp
                else:
                    v90 = temp 

                v88 = v89 == v90
                if v88:

                    temp = get_nested_attribute(action, '30')
                    if temp is None:
                        temp = 30
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
                    if action is not None and hasattr(action, "v93".split('.')[0]):
                        action.v93 = temp
                    else:
                        v93 = temp 


                    temp = get_nested_attribute(action, '300')
                    if temp is None:
                        temp = 300
                    if action is not None and hasattr(action, "v94".split('.')[0]):
                        action.v94 = temp
                    else:
                        v94 = temp 


                    temp = get_nested_attribute(action, 'v94')
                    if temp is None:
                        temp = v94
                    if action is not None and hasattr(action, "v95".split('.')[0]):
                        action.v95 = temp
                    else:
                        v95 = temp 


                    temp = get_nested_attribute(action, 'v95')
                    if temp is None:
                        temp = v95
                    if action is not None and hasattr(action, "v96".split('.')[0]):
                        action.v96 = temp
                    else:
                        v96 = temp 


                    if action is not None:
                        action.face.start = v93
                        action.face.extent = v96
                    else:
                        face.start = v93
                        face.extent = v96

                    temp = get_nested_attribute(action, '50')
                    if temp is None:
                        temp = 50
                    if action is not None and hasattr(action, "v98".split('.')[0]):
                        action.v98 = temp
                    else:
                        v98 = temp 


                    temp = get_nested_attribute(action, '50')
                    if temp is None:
                        temp = 50
                    if action is not None and hasattr(action, "v99".split('.')[0]):
                        action.v99 = temp
                    else:
                        v99 = temp 

                    v97 = (v98 , v99)

                    temp = get_nested_attribute(action, 'v97')
                    if temp is None:
                        temp = v97
                    if action is not None and hasattr(action, "v100".split('.')[0]):
                        action.v100 = temp
                    else:
                        v100 = temp 


                    temp = get_nested_attribute(action, 'v100')
                    if temp is None:
                        temp = v100
                    if action is not None and hasattr(action, "len_pac".split('.')[0]):
                        action.len_pac = temp
                    else:
                        len_pac = temp 


                    temp = get_nested_attribute(action, 'face.fill')
                    if temp is None:
                        temp = face.fill
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


                    temp = get_nested_attribute(action, 'v102')
                    if temp is None:
                        temp = v102
                    if action is not None and hasattr(action, "v103".split('.')[0]):
                        action.v103 = temp
                    else:
                        v103 = temp 


                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v105".split('.')[0]):
                        action.v105 = temp
                    else:
                        v105 = temp 


                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v106".split('.')[0]):
                        action.v106 = temp
                    else:
                        v106 = temp 

                    v104 = (v105 , v106)

                    temp = get_nested_attribute(action, 'v104')
                    if temp is None:
                        temp = v104
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


                    if action is not None:
                        action.eye.fill = v103
                        action.eye.length = v108
                    else:
                        eye.fill = v103
                        eye.length = v108

                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v110".split('.')[0]):
                        action.v110 = temp
                    else:
                        v110 = temp 

                    v111 = - v110

                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v112".split('.')[0]):
                        action.v112 = temp
                    else:
                        v112 = temp 

                    v113 = - v112
                    v109 = (v111 , v113)
                    if action is not None:
                        action.eye.move_relative(v109)
                    else:
                        eye.move_relative(v109)    
                else:

                    temp = get_nested_attribute(action, '1')
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v114".split('.')[0]):
                        action.v114 = temp
                    else:
                        v114 = temp 


                    temp = get_nested_attribute(action, 'v114')
                    if temp is None:
                        temp = v114
                    if action is not None and hasattr(action, "v115".split('.')[0]):
                        action.v115 = temp
                    else:
                        v115 = temp 


                    temp = get_nested_attribute(action, 'v115')
                    if temp is None:
                        temp = v115
                    if action is not None and hasattr(action, "v116".split('.')[0]):
                        action.v116 = temp
                    else:
                        v116 = temp 


                    temp = get_nested_attribute(action, '359')
                    if temp is None:
                        temp = 359
                    if action is not None and hasattr(action, "v117".split('.')[0]):
                        action.v117 = temp
                    else:
                        v117 = temp 


                    temp = get_nested_attribute(action, 'v117')
                    if temp is None:
                        temp = v117
                    if action is not None and hasattr(action, "v118".split('.')[0]):
                        action.v118 = temp
                    else:
                        v118 = temp 


                    temp = get_nested_attribute(action, 'v118')
                    if temp is None:
                        temp = v118
                    if action is not None and hasattr(action, "v119".split('.')[0]):
                        action.v119 = temp
                    else:
                        v119 = temp 


                    if action is not None:
                        action.face.start = v116
                        action.face.extent = v119
                    else:
                        face.start = v116
                        face.extent = v119

                    temp = get_nested_attribute(action, '60')
                    if temp is None:
                        temp = 60
                    if action is not None and hasattr(action, "v121".split('.')[0]):
                        action.v121 = temp
                    else:
                        v121 = temp 


                    temp = get_nested_attribute(action, '60')
                    if temp is None:
                        temp = 60
                    if action is not None and hasattr(action, "v122".split('.')[0]):
                        action.v122 = temp
                    else:
                        v122 = temp 

                    v120 = (v121 , v122)

                    temp = get_nested_attribute(action, 'v120')
                    if temp is None:
                        temp = v120
                    if action is not None and hasattr(action, "v123".split('.')[0]):
                        action.v123 = temp
                    else:
                        v123 = temp 


                    temp = get_nested_attribute(action, 'v123')
                    if temp is None:
                        temp = v123
                    if action is not None and hasattr(action, "len_pac".split('.')[0]):
                        action.len_pac = temp
                    else:
                        len_pac = temp 


                    temp = get_nested_attribute(action, '"red"')
                    if temp is None:
                        temp = "red"
                    if action is not None and hasattr(action, "v124".split('.')[0]):
                        action.v124 = temp
                    else:
                        v124 = temp 


                    temp = get_nested_attribute(action, 'v124')
                    if temp is None:
                        temp = v124
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


                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v128".split('.')[0]):
                        action.v128 = temp
                    else:
                        v128 = temp 


                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v129".split('.')[0]):
                        action.v129 = temp
                    else:
                        v129 = temp 

                    v127 = (v128 , v129)

                    temp = get_nested_attribute(action, 'v127')
                    if temp is None:
                        temp = v127
                    if action is not None and hasattr(action, "v130".split('.')[0]):
                        action.v130 = temp
                    else:
                        v130 = temp 


                    temp = get_nested_attribute(action, 'v130')
                    if temp is None:
                        temp = v130
                    if action is not None and hasattr(action, "v131".split('.')[0]):
                        action.v131 = temp
                    else:
                        v131 = temp 


                    if action is not None:
                        action.eye.fill = v126
                        action.eye.length = v131
                    else:
                        eye.fill = v126
                        eye.length = v131

                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v133".split('.')[0]):
                        action.v133 = temp
                    else:
                        v133 = temp 


                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v134".split('.')[0]):
                        action.v134 = temp
                    else:
                        v134 = temp 

                    v132 = (v133 , v134)
                    if action is not None:
                        action.eye.move_relative(v132)
                    else:
                        eye.move_relative(v132)
                    
                self.last_mouth = copy.deepcopy(self.mouth)
        
            action = None
            super().create_object(view)
            model = None

        def __deepcopy__(self, memo=None):
            """Create a deep copy of the model."""
            if memo is None:
                memo = {} # this is required by the deepcopy protocol
            new_model = Pacman()

            self.copyAttributesTo(new_model)
            return new_model       

    #################################################################

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v136".split('.')[0]):
        action.v136 = temp
    else:
        v136 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v137".split('.')[0]):
        action.v137 = temp
    else:
        v137 = temp 

    v135 = (v136 , v137)

    if model is not None:
        v138 = Rectangle()
        model.add_object(v138) # add object to model
    else:
        v138 = Rectangle(root = root)
    v138.origin = v135

    temp = get_nested_attribute(action, '1000')
    if temp is None:
        temp = 1000
    if action is not None and hasattr(action, "v140".split('.')[0]):
        action.v140 = temp
    else:
        v140 = temp 


    temp = get_nested_attribute(action, '70')
    if temp is None:
        temp = 70
    if action is not None and hasattr(action, "v141".split('.')[0]):
        action.v141 = temp
    else:
        v141 = temp 

    v139 = (v140 , v141)

    temp = get_nested_attribute(action, 'v139')
    if temp is None:
        temp = v139
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


    temp = get_nested_attribute(action, '"blue"')
    if temp is None:
        temp = "blue"
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


    if action is not None:
        action.v138.length = v143
        action.v138.fill = v146
    else:
        v138.length = v143
        v138.fill = v146

    if model is not None:
        v147 = View()
        model.add_object(v147) # add object to model
    else:
        v147 = View(root = root)
    last_view = v147

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v148".split('.')[0]):
        action.v148 = temp
    else:
        v148 = temp 

    v149 = - v148

    temp = get_nested_attribute(action, 'v149')
    if temp is None:
        temp = v149
    if action is not None and hasattr(action, "v150".split('.')[0]):
        action.v150 = temp
    else:
        v150 = temp 


    temp = get_nested_attribute(action, 'v150')
    if temp is None:
        temp = v150
    if action is not None and hasattr(action, "v151".split('.')[0]):
        action.v151 = temp
    else:
        v151 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v152".split('.')[0]):
        action.v152 = temp
    else:
        v152 = temp 


    temp = get_nested_attribute(action, 'v152')
    if temp is None:
        temp = v152
    if action is not None and hasattr(action, "v153".split('.')[0]):
        action.v153 = temp
    else:
        v153 = temp 


    temp = get_nested_attribute(action, 'v153')
    if temp is None:
        temp = v153
    if action is not None and hasattr(action, "v154".split('.')[0]):
        action.v154 = temp
    else:
        v154 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
    if action is not None and hasattr(action, "v155".split('.')[0]):
        action.v155 = temp
    else:
        v155 = temp 


    temp = get_nested_attribute(action, 'v155')
    if temp is None:
        temp = v155
    if action is not None and hasattr(action, "v156".split('.')[0]):
        action.v156 = temp
    else:
        v156 = temp 


    temp = get_nested_attribute(action, 'v156')
    if temp is None:
        temp = v156
    if action is not None and hasattr(action, "v157".split('.')[0]):
        action.v157 = temp
    else:
        v157 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
    if action is not None and hasattr(action, "v158".split('.')[0]):
        action.v158 = temp
    else:
        v158 = temp 


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


    temp = get_nested_attribute(action, '"Illustrating a moving pacman"')
    if temp is None:
        temp = "Illustrating a moving pacman"
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


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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


    if action is not None:
        action.v147.Ox = v151
        action.v147.Oy = v154
        action.v147.width = v157
        action.v147.height = v160
        action.v147.title = v163
        action.v147.background = v166
    else:
        v147.Ox = v151
        v147.Oy = v154
        v147.width = v157
        v147.height = v160
        v147.title = v163
        v147.background = v166

    temp = get_nested_attribute(action, 'v147')
    if temp is None:
        temp = v147
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
    if action is not None and hasattr(action, "v169".split('.')[0]):
        action.v169 = temp
    else:
        v169 = temp 

    v170 = - v169

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v171".split('.')[0]):
        action.v171 = temp
    else:
        v171 = temp 

    v168 = (v170 , v171)

    if model is not None:
        model_backup = model
        v167 = Pacman() # this makes model = None in the end!
        model = model_backup
        model.add_object(v167) # add object to model
    else:
        v167 = Pacman(root = root, view = last_view, origin = v168)


    temp = get_nested_attribute(action, 'v167')
    if temp is None:
        temp = v167
    if action is not None and hasattr(action, "v172".split('.')[0]):
        action.v172 = temp
    else:
        v172 = temp 


    temp = get_nested_attribute(action, 'v172')
    if temp is None:
        temp = v172
    if action is not None and hasattr(action, "pacman".split('.')[0]):
        action.pacman = temp
    else:
        pacman = temp 
    if model is not None: 
        model.pacman = pacman
        model.last_pacman = copy.deepcopy(pacman)

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v174".split('.')[0]):
        action.v174 = temp
    else:
        v174 = temp 


    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v175".split('.')[0]):
        action.v175 = temp
    else:
        v175 = temp 

    v173 = (v174 , v175)
    if action is not None:
        action.pacman.move_relative(v173)
    else:
        pacman.move_relative(v173)

    if model is not None:
        v176 = View()
        model.add_object(v176) # add object to model
    else:
        v176 = View(root = root)
    last_view = v176

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v177".split('.')[0]):
        action.v177 = temp
    else:
        v177 = temp 

    v178 = - v177

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
    if action is not None and hasattr(action, "v180".split('.')[0]):
        action.v180 = temp
    else:
        v180 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
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
    if action is not None and hasattr(action, "v183".split('.')[0]):
        action.v183 = temp
    else:
        v183 = temp 


    temp = get_nested_attribute(action, '1000')
    if temp is None:
        temp = 1000
    if action is not None and hasattr(action, "v184".split('.')[0]):
        action.v184 = temp
    else:
        v184 = temp 


    temp = get_nested_attribute(action, 'v184')
    if temp is None:
        temp = v184
    if action is not None and hasattr(action, "v185".split('.')[0]):
        action.v185 = temp
    else:
        v185 = temp 


    temp = get_nested_attribute(action, 'v185')
    if temp is None:
        temp = v185
    if action is not None and hasattr(action, "v186".split('.')[0]):
        action.v186 = temp
    else:
        v186 = temp 


    temp = get_nested_attribute(action, '600')
    if temp is None:
        temp = 600
    if action is not None and hasattr(action, "v187".split('.')[0]):
        action.v187 = temp
    else:
        v187 = temp 


    temp = get_nested_attribute(action, 'v187')
    if temp is None:
        temp = v187
    if action is not None and hasattr(action, "v188".split('.')[0]):
        action.v188 = temp
    else:
        v188 = temp 


    temp = get_nested_attribute(action, 'v188')
    if temp is None:
        temp = v188
    if action is not None and hasattr(action, "v189".split('.')[0]):
        action.v189 = temp
    else:
        v189 = temp 


    temp = get_nested_attribute(action, '"Illustrating a moving pacman"')
    if temp is None:
        temp = "Illustrating a moving pacman"
    if action is not None and hasattr(action, "v190".split('.')[0]):
        action.v190 = temp
    else:
        v190 = temp 


    temp = get_nested_attribute(action, 'v190')
    if temp is None:
        temp = v190
    if action is not None and hasattr(action, "v191".split('.')[0]):
        action.v191 = temp
    else:
        v191 = temp 


    temp = get_nested_attribute(action, 'v191')
    if temp is None:
        temp = v191
    if action is not None and hasattr(action, "v192".split('.')[0]):
        action.v192 = temp
    else:
        v192 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v193".split('.')[0]):
        action.v193 = temp
    else:
        v193 = temp 


    temp = get_nested_attribute(action, 'v193')
    if temp is None:
        temp = v193
    if action is not None and hasattr(action, "v194".split('.')[0]):
        action.v194 = temp
    else:
        v194 = temp 


    temp = get_nested_attribute(action, 'v194')
    if temp is None:
        temp = v194
    if action is not None and hasattr(action, "v195".split('.')[0]):
        action.v195 = temp
    else:
        v195 = temp 


    if action is not None:
        action.v176.Ox = v180
        action.v176.Oy = v183
        action.v176.width = v186
        action.v176.height = v189
        action.v176.title = v192
        action.v176.background = v195
    else:
        v176.Ox = v180
        v176.Oy = v183
        v176.width = v186
        v176.height = v189
        v176.title = v192
        v176.background = v195

    temp = get_nested_attribute(action, 'v176')
    if temp is None:
        temp = v176
    if action is not None and hasattr(action, "view2".split('.')[0]):
        action.view2 = temp
    else:
        view2 = temp 
    if model is not None: 
        model.view2 = view2
        model.last_view2 = copy.deepcopy(view2)

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v197".split('.')[0]):
        action.v197 = temp
    else:
        v197 = temp 

    v198 = - v197

    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v199".split('.')[0]):
        action.v199 = temp
    else:
        v199 = temp 

    v200 = - v199
    v196 = (v198 , v200)

    if action is not None:
        new_model = Pacman() ### TODO: !!!
        action.pacman.copyAttributesTo(new_model, draw=True)
        v201 = new_model
        v201.move_absolute(v196)
        model.add_object(v201) # add object to model
    else:
        new_model = Pacman() ### TODO: !!!
        pacman.copyAttributesTo(new_model, draw=True)
        v201 = new_model
        v201.move_absolute(v196)


    temp = get_nested_attribute(action, 'v201')
    if temp is None:
        temp = v201
    if action is not None and hasattr(action, "v202".split('.')[0]):
        action.v202 = temp
    else:
        v202 = temp 


    temp = get_nested_attribute(action, 'v202')
    if temp is None:
        temp = v202
    if action is not None and hasattr(action, "v203".split('.')[0]):
        action.v203 = temp
    else:
        v203 = temp 


    temp = get_nested_attribute(action, 'v203')
    if temp is None:
        temp = v203
    if action is not None and hasattr(action, "pacman2".split('.')[0]):
        action.pacman2 = temp
    else:
        pacman2 = temp 
    if model is not None: 
        model.pacman2 = pacman2
        model.last_pacman2 = copy.deepcopy(pacman2)
    last_refresh = time.time()
    view.update()

    last_refresh = time.time()
    view2.update()


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v204".split('.')[0]):
        action.v204 = temp
    else:
        v204 = temp 


    temp = get_nested_attribute(action, '10')
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v205".split('.')[0]):
        action.v205 = temp
    else:
        v205 = temp 

    for i in range(v204, v205, 1):

        temp = get_nested_attribute(action, 'Close')
        if temp is None:
            temp = Close
        if action is not None and hasattr(action, "v206".split('.')[0]):
            action.v206 = temp
        else:
            v206 = temp 


        temp = get_nested_attribute(action, 'v206')
        if temp is None:
            temp = v206
        if action is not None and hasattr(action, "v207".split('.')[0]):
            action.v207 = temp
        else:
            v207 = temp 


        temp = get_nested_attribute(action, 'v207')
        if temp is None:
            temp = v207
        if action is not None and hasattr(action, "pacman.mouth".split('.')[0]):
            action.pacman.mouth = temp
        else:
            pacman.mouth = temp 

         

        temp = get_nested_attribute(action, '175')
        if temp is None:
            temp = 175
        if action is not None and hasattr(action, "v208".split('.')[0]):
            action.v208 = temp
        else:
            v208 = temp 

        while (time.time() - last_refresh <= v208/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, 'Open')
        if temp is None:
            temp = Open
        if action is not None and hasattr(action, "v209".split('.')[0]):
            action.v209 = temp
        else:
            v209 = temp 


        temp = get_nested_attribute(action, 'v209')
        if temp is None:
            temp = v209
        if action is not None and hasattr(action, "v210".split('.')[0]):
            action.v210 = temp
        else:
            v210 = temp 


        temp = get_nested_attribute(action, 'v210')
        if temp is None:
            temp = v210
        if action is not None and hasattr(action, "pacman.mouth".split('.')[0]):
            action.pacman.mouth = temp
        else:
            pacman.mouth = temp 

         

        temp = get_nested_attribute(action, '175')
        if temp is None:
            temp = 175
        if action is not None and hasattr(action, "v211".split('.')[0]):
            action.v211 = temp
        else:
            v211 = temp 

        while (time.time() - last_refresh <= v211/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v213".split('.')[0]):
            action.v213 = temp
        else:
            v213 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v214".split('.')[0]):
            action.v214 = temp
        else:
            v214 = temp 

        v212 = (v213 , v214)
        if action is not None:
            action.pacman.move_relative(v212)
        else:
            pacman.move_relative(v212)

        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v216".split('.')[0]):
            action.v216 = temp
        else:
            v216 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v217".split('.')[0]):
            action.v217 = temp
        else:
            v217 = temp 

        v215 = (v216 , v217)
        if action is not None:
            action.view.move_relative(v215)
        else:
            view.move_relative(v215)
         

        temp = get_nested_attribute(action, '175')
        if temp is None:
            temp = 175
        if action is not None and hasattr(action, "v218".split('.')[0]):
            action.v218 = temp
        else:
            v218 = temp 

        while (time.time() - last_refresh <= v218/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v219".split('.')[0]):
        action.v219 = temp
    else:
        v219 = temp 


    temp = get_nested_attribute(action, '10')
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v220".split('.')[0]):
        action.v220 = temp
    else:
        v220 = temp 

    for i in range(v219, v220, 1):

        temp = get_nested_attribute(action, 'Close')
        if temp is None:
            temp = Close
        if action is not None and hasattr(action, "v221".split('.')[0]):
            action.v221 = temp
        else:
            v221 = temp 


        temp = get_nested_attribute(action, 'v221')
        if temp is None:
            temp = v221
        if action is not None and hasattr(action, "v222".split('.')[0]):
            action.v222 = temp
        else:
            v222 = temp 


        temp = get_nested_attribute(action, 'v222')
        if temp is None:
            temp = v222
        if action is not None and hasattr(action, "pacman2.mouth".split('.')[0]):
            action.pacman2.mouth = temp
        else:
            pacman2.mouth = temp 

         

        temp = get_nested_attribute(action, '175')
        if temp is None:
            temp = 175
        if action is not None and hasattr(action, "v223".split('.')[0]):
            action.v223 = temp
        else:
            v223 = temp 

        while (time.time() - last_refresh <= v223/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, 'Open')
        if temp is None:
            temp = Open
        if action is not None and hasattr(action, "v224".split('.')[0]):
            action.v224 = temp
        else:
            v224 = temp 


        temp = get_nested_attribute(action, 'v224')
        if temp is None:
            temp = v224
        if action is not None and hasattr(action, "v225".split('.')[0]):
            action.v225 = temp
        else:
            v225 = temp 


        temp = get_nested_attribute(action, 'v225')
        if temp is None:
            temp = v225
        if action is not None and hasattr(action, "pacman2.mouth".split('.')[0]):
            action.pacman2.mouth = temp
        else:
            pacman2.mouth = temp 

         

        temp = get_nested_attribute(action, '175')
        if temp is None:
            temp = 175
        if action is not None and hasattr(action, "v226".split('.')[0]):
            action.v226 = temp
        else:
            v226 = temp 

        while (time.time() - last_refresh <= v226/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v228".split('.')[0]):
            action.v228 = temp
        else:
            v228 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v229".split('.')[0]):
            action.v229 = temp
        else:
            v229 = temp 

        v227 = (v228 , v229)
        if action is not None:
            action.pacman2.move_relative(v227)
        else:
            pacman2.move_relative(v227)

        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v231".split('.')[0]):
            action.v231 = temp
        else:
            v231 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v232".split('.')[0]):
            action.v232 = temp
        else:
            v232 = temp 

        v230 = (v231 , v232)
        if action is not None:
            action.view.move_relative(v230)
        else:
            view.move_relative(v230)
         

        temp = get_nested_attribute(action, '175')
        if temp is None:
            temp = 175
        if action is not None and hasattr(action, "v233".split('.')[0]):
            action.v233 = temp
        else:
            v233 = temp 

        while (time.time() - last_refresh <= v233/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()

    last_refresh = time.time()
    view2.update()


    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v234".split('.')[0]):
        action.v234 = temp
    else:
        v234 = temp 

    print(v234)
    if action is not None:
        v235 = action.view.waitClick()
    else:
        v235 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v235')
    if temp is None:
        temp = v235
    if action is not None and hasattr(action, "v236".split('.')[0]):
        action.v236 = temp
    else:
        v236 = temp 


    temp = get_nested_attribute(action, 'v236')
    if temp is None:
        temp = v236
    if action is not None and hasattr(action, "v237".split('.')[0]):
        action.v237 = temp
    else:
        v237 = temp 


    temp = get_nested_attribute(action, 'v237')
    if temp is None:
        temp = v237
    if action is not None and hasattr(action, "pos".split('.')[0]):
        action.pos = temp
    else:
        pos = temp 
    if model is not None: 
        model.pos = pos
        model.last_pos = copy.deepcopy(pos)
    view.close()
