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

            temp = get_nested_attribute(action, '75')
            if temp is None:
                temp = 75
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
            class v15(Enum):
                red = auto()
                blue = auto() 
            global red; red = v15.red
            global blue; blue = v15.blue   
            v16 = v15(1) # first is default

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
            if action is not None and hasattr(action, "color".split('.')[0]):
                action.color = temp
            else:
                color = temp 
            if model is not None: 
                model.color = color
                model.last_color = copy.deepcopy(color)

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

                    temp = get_nested_attribute(action, 'color')
                    if temp is None:
                        temp = color
                    if action is not None and hasattr(action, "v25".split('.')[0]):
                        action.v25 = temp
                    else:
                        v25 = temp 


                    temp = get_nested_attribute(action, 'blue')
                    if temp is None:
                        temp = blue
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


                        temp = get_nested_attribute(action, 'red')
                        if temp is None:
                            temp = red
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
                        if action is not None and hasattr(action, "color".split('.')[0]):
                            action.color = temp
                        else:
                            color = temp 
                        
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


                        temp = get_nested_attribute(action, 'blue')
                        if temp is None:
                            temp = blue
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
                        if action is not None and hasattr(action, "color".split('.')[0]):
                            action.color = temp
                        else:
                            color = temp 

                            
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

            if model is not None:
                v35 = PieSlice()
                model.add_object(v35) # add object to model
            else:
                v35 = PieSlice(root = root)

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v37".split('.')[0]):
                action.v37 = temp
            else:
                v37 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v38".split('.')[0]):
                action.v38 = temp
            else:
                v38 = temp 

            v36 = (v37 , v38)

            temp = get_nested_attribute(action, 'v36')
            if temp is None:
                temp = v36
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


            temp = get_nested_attribute(action, '"pink"')
            if temp is None:
                temp = "pink"
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


            temp = get_nested_attribute(action, 'v42')
            if temp is None:
                temp = v42
            if action is not None and hasattr(action, "v43".split('.')[0]):
                action.v43 = temp
            else:
                v43 = temp 


            temp = get_nested_attribute(action, '30')
            if temp is None:
                temp = 30
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


            temp = get_nested_attribute(action, '300')
            if temp is None:
                temp = 300
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


            if action is not None:
                action.v35.length = v40
                action.v35.fill = v43
                action.v35.start = v46
                action.v35.extent = v49
            else:
                v35.length = v40
                v35.fill = v43
                v35.start = v46
                v35.extent = v49

            temp = get_nested_attribute(action, 'v35')
            if temp is None:
                temp = v35
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
            if action is not None and hasattr(action, "v51".split('.')[0]):
                action.v51 = temp
            else:
                v51 = temp 


            temp = get_nested_attribute(action, '35')
            if temp is None:
                temp = 35
            if action is not None and hasattr(action, "v52".split('.')[0]):
                action.v52 = temp
            else:
                v52 = temp 

            v50 = (v51 , v52)

            if model is not None:
                v53 = Ellipse()
                model.add_object(v53) # add object to model
            else:
                v53 = Ellipse(root = root)
            v53.origin = v50

            temp = get_nested_attribute(action, '"black"')
            if temp is None:
                temp = "black"
            if action is not None and hasattr(action, "v54".split('.')[0]):
                action.v54 = temp
            else:
                v54 = temp 


            temp = get_nested_attribute(action, 'v54')
            if temp is None:
                temp = v54
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


            temp = get_nested_attribute(action, '5')
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v58".split('.')[0]):
                action.v58 = temp
            else:
                v58 = temp 


            temp = get_nested_attribute(action, '5')
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v59".split('.')[0]):
                action.v59 = temp
            else:
                v59 = temp 

            v57 = (v58 , v59)

            temp = get_nested_attribute(action, 'v57')
            if temp is None:
                temp = v57
            if action is not None and hasattr(action, "v60".split('.')[0]):
                action.v60 = temp
            else:
                v60 = temp 


            temp = get_nested_attribute(action, 'v60')
            if temp is None:
                temp = v60
            if action is not None and hasattr(action, "v61".split('.')[0]):
                action.v61 = temp
            else:
                v61 = temp 


            if action is not None:
                action.v53.fill = v56
                action.v53.length = v61
            else:
                v53.fill = v56
                v53.length = v61

            temp = get_nested_attribute(action, 'v53')
            if temp is None:
                temp = v53
            if action is not None and hasattr(action, "eye".split('.')[0]):
                action.eye = temp
            else:
                eye = temp 
            if model is not None: 
                model.eye = eye
                model.last_eye = copy.deepcopy(eye)

            if model is not None:
                model_backup = model
                v62 = Fire() # this makes model = None in the end!
                model = model_backup
                model.add_object(v62) # add object to model
            else:
                v62 = Fire(root = root, view = last_view)
              

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
            if action is not None and hasattr(action, "fire".split('.')[0]):
                action.fire = temp
            else:
                fire = temp 
            if model is not None: 
                model.fire = fire
                model.last_fire = copy.deepcopy(fire)
            class v83(Enum):
                Open = auto()
                Close = auto() 
            global Open; Open = v83.Open
            global Close; Close = v83.Close   
            v84 = v83(1) # first is default

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

            if self.fire.flame.state != self.last_fire.flame.state:

                temp = get_nested_attribute(action, 'fire.flame.state')
                if temp is None:
                    temp = fire.flame.state
                if action is not None and hasattr(action, "v65".split('.')[0]):
                    action.v65 = temp
                else:
                    v65 = temp 


                temp = get_nested_attribute(action, '"normal"')
                if temp is None:
                    temp = "normal"
                if action is not None and hasattr(action, "v66".split('.')[0]):
                    action.v66 = temp
                else:
                    v66 = temp 

                v64 = v65 == v66
                if v64:

                    temp = get_nested_attribute(action, '"red"')
                    if temp is None:
                        temp = "red"
                    if action is not None and hasattr(action, "v67".split('.')[0]):
                        action.v67 = temp
                    else:
                        v67 = temp 


                    temp = get_nested_attribute(action, 'v67')
                    if temp is None:
                        temp = v67
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


                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v71".split('.')[0]):
                        action.v71 = temp
                    else:
                        v71 = temp 


                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v72".split('.')[0]):
                        action.v72 = temp
                    else:
                        v72 = temp 

                    v70 = (v71 , v72)

                    temp = get_nested_attribute(action, 'v70')
                    if temp is None:
                        temp = v70
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


                    if action is not None:
                        action.eye.fill = v69
                        action.eye.length = v74
                    else:
                        eye.fill = v69
                        eye.length = v74    
                else:

                    temp = get_nested_attribute(action, 'face.fill')
                    if temp is None:
                        temp = face.fill
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
                    if action is not None and hasattr(action, "v77".split('.')[0]):
                        action.v77 = temp
                    else:
                        v77 = temp 


                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v79".split('.')[0]):
                        action.v79 = temp
                    else:
                        v79 = temp 


                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v80".split('.')[0]):
                        action.v80 = temp
                    else:
                        v80 = temp 

                    v78 = (v79 , v80)

                    temp = get_nested_attribute(action, 'v78')
                    if temp is None:
                        temp = v78
                    if action is not None and hasattr(action, "v81".split('.')[0]):
                        action.v81 = temp
                    else:
                        v81 = temp 


                    temp = get_nested_attribute(action, 'v81')
                    if temp is None:
                        temp = v81
                    if action is not None and hasattr(action, "v82".split('.')[0]):
                        action.v82 = temp
                    else:
                        v82 = temp 


                    if action is not None:
                        action.eye.fill = v77
                        action.eye.length = v82
                    else:
                        eye.fill = v77
                        eye.length = v82
                    
                self.last_fire.flame.state = copy.deepcopy(self.fire.flame.state)


            if self.mouth != self.last_mouth:

                temp = get_nested_attribute(action, 'mouth')
                if temp is None:
                    temp = mouth
                if action is not None and hasattr(action, "v87".split('.')[0]):
                    action.v87 = temp
                else:
                    v87 = temp 


                temp = get_nested_attribute(action, 'Open')
                if temp is None:
                    temp = Open
                if action is not None and hasattr(action, "v88".split('.')[0]):
                    action.v88 = temp
                else:
                    v88 = temp 

                v86 = v87 == v88
                if v86:

                    temp = get_nested_attribute(action, '30')
                    if temp is None:
                        temp = 30
                    if action is not None and hasattr(action, "v89".split('.')[0]):
                        action.v89 = temp
                    else:
                        v89 = temp 


                    temp = get_nested_attribute(action, 'v89')
                    if temp is None:
                        temp = v89
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


                    temp = get_nested_attribute(action, '300')
                    if temp is None:
                        temp = 300
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


                    temp = get_nested_attribute(action, 'v93')
                    if temp is None:
                        temp = v93
                    if action is not None and hasattr(action, "v94".split('.')[0]):
                        action.v94 = temp
                    else:
                        v94 = temp 


                    if action is not None:
                        action.face.start = v91
                        action.face.extent = v94
                    else:
                        face.start = v91
                        face.extent = v94

                    temp = get_nested_attribute(action, '"normal"')
                    if temp is None:
                        temp = "normal"
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


                    temp = get_nested_attribute(action, 'v96')
                    if temp is None:
                        temp = v96
                    if action is not None and hasattr(action, "fire.flame.state".split('.')[0]):
                        action.fire.flame.state = temp
                    else:
                        fire.flame.state = temp 
                    
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

                    temp = get_nested_attribute(action, '"hidden"')
                    if temp is None:
                        temp = "hidden"
                    if action is not None and hasattr(action, "v103".split('.')[0]):
                        action.v103 = temp
                    else:
                        v103 = temp 


                    temp = get_nested_attribute(action, 'v103')
                    if temp is None:
                        temp = v103
                    if action is not None and hasattr(action, "v104".split('.')[0]):
                        action.v104 = temp
                    else:
                        v104 = temp 


                    temp = get_nested_attribute(action, 'v104')
                    if temp is None:
                        temp = v104
                    if action is not None and hasattr(action, "fire.flame.state".split('.')[0]):
                        action.fire.flame.state = temp
                    else:
                        fire.flame.state = temp 

                    
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


    if model is not None:
        v105 = Rectangle()
        model.add_object(v105) # add object to model
    else:
        v105 = Rectangle(root = root)

    temp = get_nested_attribute(action, '1000')
    if temp is None:
        temp = 1000
    if action is not None and hasattr(action, "v107".split('.')[0]):
        action.v107 = temp
    else:
        v107 = temp 


    temp = get_nested_attribute(action, '70')
    if temp is None:
        temp = 70
    if action is not None and hasattr(action, "v108".split('.')[0]):
        action.v108 = temp
    else:
        v108 = temp 

    v106 = (v107 , v108)

    temp = get_nested_attribute(action, 'v106')
    if temp is None:
        temp = v106
    if action is not None and hasattr(action, "v109".split('.')[0]):
        action.v109 = temp
    else:
        v109 = temp 


    temp = get_nested_attribute(action, 'v109')
    if temp is None:
        temp = v109
    if action is not None and hasattr(action, "v110".split('.')[0]):
        action.v110 = temp
    else:
        v110 = temp 


    temp = get_nested_attribute(action, '"blue"')
    if temp is None:
        temp = "blue"
    if action is not None and hasattr(action, "v111".split('.')[0]):
        action.v111 = temp
    else:
        v111 = temp 


    temp = get_nested_attribute(action, 'v111')
    if temp is None:
        temp = v111
    if action is not None and hasattr(action, "v112".split('.')[0]):
        action.v112 = temp
    else:
        v112 = temp 


    temp = get_nested_attribute(action, 'v112')
    if temp is None:
        temp = v112
    if action is not None and hasattr(action, "v113".split('.')[0]):
        action.v113 = temp
    else:
        v113 = temp 


    if action is not None:
        action.v105.length = v110
        action.v105.fill = v113
    else:
        v105.length = v110
        v105.fill = v113

    if model is not None:
        v114 = View()
        model.add_object(v114) # add object to model
    else:
        v114 = View(root = root)
    last_view = v114

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v115".split('.')[0]):
        action.v115 = temp
    else:
        v115 = temp 

    v116 = - v115

    temp = get_nested_attribute(action, 'v116')
    if temp is None:
        temp = v116
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


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v119".split('.')[0]):
        action.v119 = temp
    else:
        v119 = temp 


    temp = get_nested_attribute(action, 'v119')
    if temp is None:
        temp = v119
    if action is not None and hasattr(action, "v120".split('.')[0]):
        action.v120 = temp
    else:
        v120 = temp 


    temp = get_nested_attribute(action, 'v120')
    if temp is None:
        temp = v120
    if action is not None and hasattr(action, "v121".split('.')[0]):
        action.v121 = temp
    else:
        v121 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
    if action is not None and hasattr(action, "v122".split('.')[0]):
        action.v122 = temp
    else:
        v122 = temp 


    temp = get_nested_attribute(action, 'v122')
    if temp is None:
        temp = v122
    if action is not None and hasattr(action, "v123".split('.')[0]):
        action.v123 = temp
    else:
        v123 = temp 


    temp = get_nested_attribute(action, 'v123')
    if temp is None:
        temp = v123
    if action is not None and hasattr(action, "v124".split('.')[0]):
        action.v124 = temp
    else:
        v124 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
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


    temp = get_nested_attribute(action, 'v126')
    if temp is None:
        temp = v126
    if action is not None and hasattr(action, "v127".split('.')[0]):
        action.v127 = temp
    else:
        v127 = temp 


    temp = get_nested_attribute(action, '"1"')
    if temp is None:
        temp = "1"
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


    temp = get_nested_attribute(action, 'v129')
    if temp is None:
        temp = v129
    if action is not None and hasattr(action, "v130".split('.')[0]):
        action.v130 = temp
    else:
        v130 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v131".split('.')[0]):
        action.v131 = temp
    else:
        v131 = temp 


    temp = get_nested_attribute(action, 'v131')
    if temp is None:
        temp = v131
    if action is not None and hasattr(action, "v132".split('.')[0]):
        action.v132 = temp
    else:
        v132 = temp 


    temp = get_nested_attribute(action, 'v132')
    if temp is None:
        temp = v132
    if action is not None and hasattr(action, "v133".split('.')[0]):
        action.v133 = temp
    else:
        v133 = temp 


    if action is not None:
        action.v114.Ox = v118
        action.v114.Oy = v121
        action.v114.width = v124
        action.v114.height = v127
        action.v114.title = v130
        action.v114.background = v133
    else:
        v114.Ox = v118
        v114.Oy = v121
        v114.width = v124
        v114.height = v127
        v114.title = v130
        v114.background = v133

    temp = get_nested_attribute(action, 'v114')
    if temp is None:
        temp = v114
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
    if action is not None and hasattr(action, "v136".split('.')[0]):
        action.v136 = temp
    else:
        v136 = temp 

    v137 = - v136

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v138".split('.')[0]):
        action.v138 = temp
    else:
        v138 = temp 

    v135 = (v137 , v138)

    if model is not None:
        model_backup = model
        v134 = Pacman() # this makes model = None in the end!
        model = model_backup
        model.add_object(v134) # add object to model
    else:
        v134 = Pacman(root = root, view = last_view)
    v134.move_absolute(v135)  

    temp = get_nested_attribute(action, 'v134')
    if temp is None:
        temp = v134
    if action is not None and hasattr(action, "v139".split('.')[0]):
        action.v139 = temp
    else:
        v139 = temp 


    temp = get_nested_attribute(action, 'v139')
    if temp is None:
        temp = v139
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
    if action is not None and hasattr(action, "v141".split('.')[0]):
        action.v141 = temp
    else:
        v141 = temp 


    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v142".split('.')[0]):
        action.v142 = temp
    else:
        v142 = temp 

    v140 = (v141 , v142)
    if action is not None:
        action.pacman.move_relative(v140)
    else:
        pacman.move_relative(v140)

    if model is not None:
        v143 = View()
        model.add_object(v143) # add object to model
    else:
        v143 = View(root = root)
    last_view = v143

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v144".split('.')[0]):
        action.v144 = temp
    else:
        v144 = temp 

    v145 = - v144

    temp = get_nested_attribute(action, 'v145')
    if temp is None:
        temp = v145
    if action is not None and hasattr(action, "v146".split('.')[0]):
        action.v146 = temp
    else:
        v146 = temp 


    temp = get_nested_attribute(action, 'v146')
    if temp is None:
        temp = v146
    if action is not None and hasattr(action, "v147".split('.')[0]):
        action.v147 = temp
    else:
        v147 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
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


    temp = get_nested_attribute(action, 'v149')
    if temp is None:
        temp = v149
    if action is not None and hasattr(action, "v150".split('.')[0]):
        action.v150 = temp
    else:
        v150 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
    if action is not None and hasattr(action, "v151".split('.')[0]):
        action.v151 = temp
    else:
        v151 = temp 


    temp = get_nested_attribute(action, 'v151')
    if temp is None:
        temp = v151
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


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
    if action is not None and hasattr(action, "v154".split('.')[0]):
        action.v154 = temp
    else:
        v154 = temp 


    temp = get_nested_attribute(action, 'v154')
    if temp is None:
        temp = v154
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


    temp = get_nested_attribute(action, '"2"')
    if temp is None:
        temp = "2"
    if action is not None and hasattr(action, "v157".split('.')[0]):
        action.v157 = temp
    else:
        v157 = temp 


    temp = get_nested_attribute(action, 'v157')
    if temp is None:
        temp = v157
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


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v160".split('.')[0]):
        action.v160 = temp
    else:
        v160 = temp 


    temp = get_nested_attribute(action, 'v160')
    if temp is None:
        temp = v160
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


    if action is not None:
        action.v143.Ox = v147
        action.v143.Oy = v150
        action.v143.width = v153
        action.v143.height = v156
        action.v143.title = v159
        action.v143.background = v162
    else:
        v143.Ox = v147
        v143.Oy = v150
        v143.width = v153
        v143.height = v156
        v143.title = v159
        v143.background = v162

    temp = get_nested_attribute(action, 'v143')
    if temp is None:
        temp = v143
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
    if action is not None and hasattr(action, "v164".split('.')[0]):
        action.v164 = temp
    else:
        v164 = temp 

    v165 = - v164

    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v166".split('.')[0]):
        action.v166 = temp
    else:
        v166 = temp 

    v167 = - v166
    v163 = (v165 , v167)

    if action is not None:
        new_model = Pacman() ### TODO: !!!
        action.pacman.copyAttributesTo(new_model, draw=True)
        v168 = new_model
        v168.move_absolute(v163)
        model.add_object(v168) # add object to model
    else:
        new_model = Pacman() ### TODO: !!!
        pacman.copyAttributesTo(new_model, draw=True)
        v168 = new_model
        v168.move_absolute(v163)


    temp = get_nested_attribute(action, 'v168')
    if temp is None:
        temp = v168
    if action is not None and hasattr(action, "v169".split('.')[0]):
        action.v169 = temp
    else:
        v169 = temp 


    temp = get_nested_attribute(action, 'v169')
    if temp is None:
        temp = v169
    if action is not None and hasattr(action, "v170".split('.')[0]):
        action.v170 = temp
    else:
        v170 = temp 


    temp = get_nested_attribute(action, 'v170')
    if temp is None:
        temp = v170
    if action is not None and hasattr(action, "pacman2".split('.')[0]):
        action.pacman2 = temp
    else:
        pacman2 = temp 
    if model is not None: 
        model.pacman2 = pacman2
        model.last_pacman2 = copy.deepcopy(pacman2)

    temp = get_nested_attribute(action, '"wheat"')
    if temp is None:
        temp = "wheat"
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


    temp = get_nested_attribute(action, 'v172')
    if temp is None:
        temp = v172
    if action is not None and hasattr(action, "pacman2.face.fill".split('.')[0]):
        action.pacman2.face.fill = temp
    else:
        pacman2.face.fill = temp 

    last_refresh = time.time()
    view2.update()


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v173".split('.')[0]):
        action.v173 = temp
    else:
        v173 = temp 


    temp = get_nested_attribute(action, '10')
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v174".split('.')[0]):
        action.v174 = temp
    else:
        v174 = temp 

    for i in range(v173, v174, 1):

        temp = get_nested_attribute(action, 'Close')
        if temp is None:
            temp = Close
        if action is not None and hasattr(action, "v175".split('.')[0]):
            action.v175 = temp
        else:
            v175 = temp 


        temp = get_nested_attribute(action, 'v175')
        if temp is None:
            temp = v175
        if action is not None and hasattr(action, "v176".split('.')[0]):
            action.v176 = temp
        else:
            v176 = temp 


        temp = get_nested_attribute(action, 'v176')
        if temp is None:
            temp = v176
        if action is not None and hasattr(action, "pacman.mouth".split('.')[0]):
            action.pacman.mouth = temp
        else:
            pacman.mouth = temp 

         
         

        temp = get_nested_attribute(action, '25')
        if temp is None:
            temp = 25
        if action is not None and hasattr(action, "v177".split('.')[0]):
            action.v177 = temp
        else:
            v177 = temp 

        while (time.time() - last_refresh <= v177/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '25')
        if temp is None:
            temp = 25
        if action is not None and hasattr(action, "v178".split('.')[0]):
            action.v178 = temp
        else:
            v178 = temp 

        while (time.time() - last_refresh <= v178/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view2.update()


        temp = get_nested_attribute(action, 'Open')
        if temp is None:
            temp = Open
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


        temp = get_nested_attribute(action, 'v180')
        if temp is None:
            temp = v180
        if action is not None and hasattr(action, "pacman.mouth".split('.')[0]):
            action.pacman.mouth = temp
        else:
            pacman.mouth = temp 

         
         

        temp = get_nested_attribute(action, '25')
        if temp is None:
            temp = 25
        if action is not None and hasattr(action, "v181".split('.')[0]):
            action.v181 = temp
        else:
            v181 = temp 

        while (time.time() - last_refresh <= v181/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '25')
        if temp is None:
            temp = 25
        if action is not None and hasattr(action, "v182".split('.')[0]):
            action.v182 = temp
        else:
            v182 = temp 

        while (time.time() - last_refresh <= v182/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view2.update()


        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v184".split('.')[0]):
            action.v184 = temp
        else:
            v184 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v185".split('.')[0]):
            action.v185 = temp
        else:
            v185 = temp 

        v183 = (v184 , v185)
        if action is not None:
            action.pacman.move_relative(v183)
        else:
            pacman.move_relative(v183)

        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v187".split('.')[0]):
            action.v187 = temp
        else:
            v187 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v188".split('.')[0]):
            action.v188 = temp
        else:
            v188 = temp 

        v186 = (v187 , v188)
        if action is not None:
            action.view.move_relative(v186)
        else:
            view.move_relative(v186)

        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v190".split('.')[0]):
            action.v190 = temp
        else:
            v190 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v191".split('.')[0]):
            action.v191 = temp
        else:
            v191 = temp 

        v189 = (v190 , v191)
        if action is not None:
            action.view2.move_relative(v189)
        else:
            view2.move_relative(v189)
         
         

        temp = get_nested_attribute(action, '25')
        if temp is None:
            temp = 25
        if action is not None and hasattr(action, "v192".split('.')[0]):
            action.v192 = temp
        else:
            v192 = temp 

        while (time.time() - last_refresh <= v192/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '25')
        if temp is None:
            temp = 25
        if action is not None and hasattr(action, "v193".split('.')[0]):
            action.v193 = temp
        else:
            v193 = temp 

        while (time.time() - last_refresh <= v193/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view2.update()


    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v194".split('.')[0]):
        action.v194 = temp
    else:
        v194 = temp 

    print(v194)
    if action is not None:
        v195 = action.view.waitClick()
    else:
        v195 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v195')
    if temp is None:
        temp = v195
    if action is not None and hasattr(action, "v196".split('.')[0]):
        action.v196 = temp
    else:
        v196 = temp 


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
    if action is not None and hasattr(action, "pos".split('.')[0]):
        action.pos = temp
    else:
        pos = temp 
    if model is not None: 
        model.pos = pos
        model.last_pos = copy.deepcopy(pos)
    view.close()
