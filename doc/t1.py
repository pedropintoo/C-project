from tkinter import *
from AGLClasses import *
import math
import time, os, sys
import copy
from enum import Enum, auto
import numpy as np

#################################################################
## Auxiliar
#################################################################
REFRESH_RATE = 0.001
last_refresh = time.time()
views = []
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

            v0 = (v1 , v2); v0 = tuple(v0) if isinstance(v0, np.ndarray) else v0

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

            v4 = (v5 , v6); v4 = tuple(v4) if isinstance(v4, np.ndarray) else v4

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
                if action is not None and hasattr(action, "v18".split('.')[0]):
                    action.v18 = temp
                else:
                    v18 = temp 

                print(v18)

                temp = get_nested_attribute(action, 'flame.state')
                if temp is None:
                    temp = flame.state
                if action is not None and hasattr(action, "v19".split('.')[0]):
                    action.v19 = temp
                else:
                    v19 = temp 

                print(v19)

                temp = get_nested_attribute(action, 'flame.state')
                if temp is None:
                    temp = flame.state
                if action is not None and hasattr(action, "v21".split('.')[0]):
                    action.v21 = temp
                else:
                    v21 = temp 


                temp = get_nested_attribute(action, '"normal"')
                if temp is None:
                    temp = "normal"
                if action is not None and hasattr(action, "v22".split('.')[0]):
                    action.v22 = temp
                else:
                    v22 = temp 

                v20 = np.array(v21) == np.array(v22); v20 = tuple(v20) if isinstance(v20, np.ndarray) else v20
                if v20:

                    temp = get_nested_attribute(action, 'color')
                    if temp is None:
                        temp = color
                    if action is not None and hasattr(action, "v24".split('.')[0]):
                        action.v24 = temp
                    else:
                        v24 = temp 


                    temp = get_nested_attribute(action, 'blue')
                    if temp is None:
                        temp = blue
                    if action is not None and hasattr(action, "v25".split('.')[0]):
                        action.v25 = temp
                    else:
                        v25 = temp 

                    v23 = np.array(v24) == np.array(v25); v23 = tuple(v23) if isinstance(v23, np.ndarray) else v23
                    if v23:

                        temp = get_nested_attribute(action, '"red"')
                        if temp is None:
                            temp = "red"
                        if action is not None and hasattr(action, "v26".split('.')[0]):
                            action.v26 = temp
                        else:
                            v26 = temp 


                        temp = get_nested_attribute(action, 'v26')
                        if temp is None:
                            temp = v26
                        if action is not None and hasattr(action, "v27".split('.')[0]):
                            action.v27 = temp
                        else:
                            v27 = temp 


                        temp = get_nested_attribute(action, 'v27')
                        if temp is None:
                            temp = v27
                        if action is not None and hasattr(action, "flame.fill".split('.')[0]):
                            action.flame.fill = temp
                        else:
                            flame.fill = temp 


                        temp = get_nested_attribute(action, 'red')
                        if temp is None:
                            temp = red
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


                        temp = get_nested_attribute(action, 'v29')
                        if temp is None:
                            temp = v29
                        if action is not None and hasattr(action, "color".split('.')[0]):
                            action.color = temp
                        else:
                            color = temp 
                        
                    else:

                        temp = get_nested_attribute(action, '"blue"')
                        if temp is None:
                            temp = "blue"
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
                        if action is not None and hasattr(action, "flame.fill".split('.')[0]):
                            action.flame.fill = temp
                        else:
                            flame.fill = temp 


                        temp = get_nested_attribute(action, 'blue')
                        if temp is None:
                            temp = blue
                        if action is not None and hasattr(action, "v32".split('.')[0]):
                            action.v32 = temp
                        else:
                            v32 = temp 


                        temp = get_nested_attribute(action, 'v32')
                        if temp is None:
                            temp = v32
                        if action is not None and hasattr(action, "v33".split('.')[0]):
                            action.v33 = temp
                        else:
                            v33 = temp 


                        temp = get_nested_attribute(action, 'v33')
                        if temp is None:
                            temp = v33
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
                v34 = PieSlice()
                model.add_object(v34) # add object to model
            else:
                v34 = PieSlice(root = root)

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v36".split('.')[0]):
                action.v36 = temp
            else:
                v36 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v37".split('.')[0]):
                action.v37 = temp
            else:
                v37 = temp 

            v35 = (v36 , v37); v35 = tuple(v35) if isinstance(v35, np.ndarray) else v35

            temp = get_nested_attribute(action, 'v35')
            if temp is None:
                temp = v35
            if action is not None and hasattr(action, "v38".split('.')[0]):
                action.v38 = temp
            else:
                v38 = temp 


            temp = get_nested_attribute(action, 'v38')
            if temp is None:
                temp = v38
            if action is not None and hasattr(action, "v39".split('.')[0]):
                action.v39 = temp
            else:
                v39 = temp 


            temp = get_nested_attribute(action, '"pink"')
            if temp is None:
                temp = "pink"
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


            temp = get_nested_attribute(action, '30')
            if temp is None:
                temp = 30
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


            temp = get_nested_attribute(action, 'v44')
            if temp is None:
                temp = v44
            if action is not None and hasattr(action, "v45".split('.')[0]):
                action.v45 = temp
            else:
                v45 = temp 


            temp = get_nested_attribute(action, '300')
            if temp is None:
                temp = 300
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


            temp = get_nested_attribute(action, 'v47')
            if temp is None:
                temp = v47
            if action is not None and hasattr(action, "v48".split('.')[0]):
                action.v48 = temp
            else:
                v48 = temp 


            if action is not None:
                action.v34.length = v39
                action.v34.fill = v42
                action.v34.start = v45
                action.v34.extent = v48
            else:
                v34.length = v39
                v34.fill = v42
                v34.start = v45
                v34.extent = v48

            temp = get_nested_attribute(action, 'v34')
            if temp is None:
                temp = v34
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
            if action is not None and hasattr(action, "v50".split('.')[0]):
                action.v50 = temp
            else:
                v50 = temp 


            temp = get_nested_attribute(action, '35')
            if temp is None:
                temp = 35
            if action is not None and hasattr(action, "v51".split('.')[0]):
                action.v51 = temp
            else:
                v51 = temp 

            v49 = (v50 , v51); v49 = tuple(v49) if isinstance(v49, np.ndarray) else v49

            if model is not None:
                v52 = Ellipse()
                model.add_object(v52) # add object to model
            else:
                v52 = Ellipse(root = root)
            v52.origin = v49

            temp = get_nested_attribute(action, '"black"')
            if temp is None:
                temp = "black"
            if action is not None and hasattr(action, "v53".split('.')[0]):
                action.v53 = temp
            else:
                v53 = temp 


            temp = get_nested_attribute(action, 'v53')
            if temp is None:
                temp = v53
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


            temp = get_nested_attribute(action, '5')
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v57".split('.')[0]):
                action.v57 = temp
            else:
                v57 = temp 


            temp = get_nested_attribute(action, '5')
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v58".split('.')[0]):
                action.v58 = temp
            else:
                v58 = temp 

            v56 = (v57 , v58); v56 = tuple(v56) if isinstance(v56, np.ndarray) else v56

            temp = get_nested_attribute(action, 'v56')
            if temp is None:
                temp = v56
            if action is not None and hasattr(action, "v59".split('.')[0]):
                action.v59 = temp
            else:
                v59 = temp 


            temp = get_nested_attribute(action, 'v59')
            if temp is None:
                temp = v59
            if action is not None and hasattr(action, "v60".split('.')[0]):
                action.v60 = temp
            else:
                v60 = temp 


            if action is not None:
                action.v52.fill = v55
                action.v52.length = v60
            else:
                v52.fill = v55
                v52.length = v60

            temp = get_nested_attribute(action, 'v52')
            if temp is None:
                temp = v52
            if action is not None and hasattr(action, "eye".split('.')[0]):
                action.eye = temp
            else:
                eye = temp 
            if model is not None: 
                model.eye = eye
                model.last_eye = copy.deepcopy(eye)

            if model is not None:
                model_backup = model
                v61 = Fire() # this makes model = None in the end!
                model = model_backup
                model.add_object(v61) # add object to model
            else:
                v61 = Fire(root = root, view = last_view)
              

            temp = get_nested_attribute(action, 'v61')
            if temp is None:
                temp = v61
            if action is not None and hasattr(action, "v62".split('.')[0]):
                action.v62 = temp
            else:
                v62 = temp 


            temp = get_nested_attribute(action, 'v62')
            if temp is None:
                temp = v62
            if action is not None and hasattr(action, "fire".split('.')[0]):
                action.fire = temp
            else:
                fire = temp 
            if model is not None: 
                model.fire = fire
                model.last_fire = copy.deepcopy(fire)
            class v82(Enum):
                Open = auto()
                Close = auto() 
            global Open; Open = v82.Open
            global Close; Close = v82.Close   
            v83 = v82(1) # first is default

            temp = get_nested_attribute(action, 'v83')
            if temp is None:
                temp = v83
            if action is not None and hasattr(action, "v84".split('.')[0]):
                action.v84 = temp
            else:
                v84 = temp 


            temp = get_nested_attribute(action, 'v84')
            if temp is None:
                temp = v84
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
                if action is not None and hasattr(action, "v64".split('.')[0]):
                    action.v64 = temp
                else:
                    v64 = temp 


                temp = get_nested_attribute(action, '"normal"')
                if temp is None:
                    temp = "normal"
                if action is not None and hasattr(action, "v65".split('.')[0]):
                    action.v65 = temp
                else:
                    v65 = temp 

                v63 = np.array(v64) == np.array(v65); v63 = tuple(v63) if isinstance(v63, np.ndarray) else v63
                if v63:

                    temp = get_nested_attribute(action, '"red"')
                    if temp is None:
                        temp = "red"
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


                    temp = get_nested_attribute(action, 'v67')
                    if temp is None:
                        temp = v67
                    if action is not None and hasattr(action, "v68".split('.')[0]):
                        action.v68 = temp
                    else:
                        v68 = temp 


                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v70".split('.')[0]):
                        action.v70 = temp
                    else:
                        v70 = temp 


                    temp = get_nested_attribute(action, '10')
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v71".split('.')[0]):
                        action.v71 = temp
                    else:
                        v71 = temp 

                    v69 = (v70 , v71); v69 = tuple(v69) if isinstance(v69, np.ndarray) else v69

                    temp = get_nested_attribute(action, 'v69')
                    if temp is None:
                        temp = v69
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


                    if action is not None:
                        action.eye.fill = v68
                        action.eye.length = v73
                    else:
                        eye.fill = v68
                        eye.length = v73    
                else:

                    temp = get_nested_attribute(action, 'face.fill')
                    if temp is None:
                        temp = face.fill
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


                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v78".split('.')[0]):
                        action.v78 = temp
                    else:
                        v78 = temp 


                    temp = get_nested_attribute(action, '5')
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v79".split('.')[0]):
                        action.v79 = temp
                    else:
                        v79 = temp 

                    v77 = (v78 , v79); v77 = tuple(v77) if isinstance(v77, np.ndarray) else v77

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


                    if action is not None:
                        action.eye.fill = v76
                        action.eye.length = v81
                    else:
                        eye.fill = v76
                        eye.length = v81
                    
                self.last_fire.flame.state = copy.deepcopy(self.fire.flame.state)


            if self.mouth != self.last_mouth:

                temp = get_nested_attribute(action, 'mouth')
                if temp is None:
                    temp = mouth
                if action is not None and hasattr(action, "v86".split('.')[0]):
                    action.v86 = temp
                else:
                    v86 = temp 


                temp = get_nested_attribute(action, 'Open')
                if temp is None:
                    temp = Open
                if action is not None and hasattr(action, "v87".split('.')[0]):
                    action.v87 = temp
                else:
                    v87 = temp 

                v85 = np.array(v86) == np.array(v87); v85 = tuple(v85) if isinstance(v85, np.ndarray) else v85
                if v85:

                    temp = get_nested_attribute(action, '30')
                    if temp is None:
                        temp = 30
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
                    if action is not None and hasattr(action, "v90".split('.')[0]):
                        action.v90 = temp
                    else:
                        v90 = temp 


                    temp = get_nested_attribute(action, '300')
                    if temp is None:
                        temp = 300
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


                    if action is not None:
                        action.face.start = v90
                        action.face.extent = v93
                    else:
                        face.start = v90
                        face.extent = v93

                    temp = get_nested_attribute(action, '"normal"')
                    if temp is None:
                        temp = "normal"
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
                    if action is not None and hasattr(action, "fire.flame.state".split('.')[0]):
                        action.fire.flame.state = temp
                    else:
                        fire.flame.state = temp 
                    
                else:

                    temp = get_nested_attribute(action, '1')
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v96".split('.')[0]):
                        action.v96 = temp
                    else:
                        v96 = temp 


                    temp = get_nested_attribute(action, 'v96')
                    if temp is None:
                        temp = v96
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


                    temp = get_nested_attribute(action, '359')
                    if temp is None:
                        temp = 359
                    if action is not None and hasattr(action, "v99".split('.')[0]):
                        action.v99 = temp
                    else:
                        v99 = temp 


                    temp = get_nested_attribute(action, 'v99')
                    if temp is None:
                        temp = v99
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


                    if action is not None:
                        action.face.start = v98
                        action.face.extent = v101
                    else:
                        face.start = v98
                        face.extent = v101

                    temp = get_nested_attribute(action, '"hidden"')
                    if temp is None:
                        temp = "hidden"
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
        v104 = Rectangle()
        model.add_object(v104) # add object to model
    else:
        v104 = Rectangle(root = root)

    temp = get_nested_attribute(action, '650')
    if temp is None:
        temp = 650
    if action is not None and hasattr(action, "v106".split('.')[0]):
        action.v106 = temp
    else:
        v106 = temp 


    temp = get_nested_attribute(action, '70')
    if temp is None:
        temp = 70
    if action is not None and hasattr(action, "v107".split('.')[0]):
        action.v107 = temp
    else:
        v107 = temp 

    v105 = (v106 , v107); v105 = tuple(v105) if isinstance(v105, np.ndarray) else v105

    temp = get_nested_attribute(action, 'v105')
    if temp is None:
        temp = v105
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


    temp = get_nested_attribute(action, '"blue"')
    if temp is None:
        temp = "blue"
    if action is not None and hasattr(action, "v110".split('.')[0]):
        action.v110 = temp
    else:
        v110 = temp 


    temp = get_nested_attribute(action, 'v110')
    if temp is None:
        temp = v110
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


    if action is not None:
        action.v104.length = v109
        action.v104.fill = v112
    else:
        v104.length = v109
        v104.fill = v112

    if model is not None:
        v113 = View()
        model.add_object(v113) # add object to model
    else:
        v113 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v113

    temp = get_nested_attribute(action, '30')
    if temp is None:
        temp = 30
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


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
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


    temp = get_nested_attribute(action, '1800')
    if temp is None:
        temp = 1800
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


    temp = get_nested_attribute(action, 'v121')
    if temp is None:
        temp = v121
    if action is not None and hasattr(action, "v122".split('.')[0]):
        action.v122 = temp
    else:
        v122 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
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


    temp = get_nested_attribute(action, 'v124')
    if temp is None:
        temp = v124
    if action is not None and hasattr(action, "v125".split('.')[0]):
        action.v125 = temp
    else:
        v125 = temp 


    temp = get_nested_attribute(action, '"1"')
    if temp is None:
        temp = "1"
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


    temp = get_nested_attribute(action, 'v127')
    if temp is None:
        temp = v127
    if action is not None and hasattr(action, "v128".split('.')[0]):
        action.v128 = temp
    else:
        v128 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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


    temp = get_nested_attribute(action, 'v130')
    if temp is None:
        temp = v130
    if action is not None and hasattr(action, "v131".split('.')[0]):
        action.v131 = temp
    else:
        v131 = temp 


    if action is not None:
        action.v113.Ox = v116
        action.v113.Oy = v119
        action.v113.width = v122
        action.v113.height = v125
        action.v113.title = v128
        action.v113.background = v131
    else:
        v113.Ox = v116
        v113.Oy = v119
        v113.width = v122
        v113.height = v125
        v113.title = v128
        v113.background = v131

    temp = get_nested_attribute(action, 'v113')
    if temp is None:
        temp = v113
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
    if action is not None and hasattr(action, "v134".split('.')[0]):
        action.v134 = temp
    else:
        v134 = temp 

    v135 = - v134

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v136".split('.')[0]):
        action.v136 = temp
    else:
        v136 = temp 

    v133 = (v135 , v136); v133 = tuple(v133) if isinstance(v133, np.ndarray) else v133

    if model is not None:
        model_backup = model
        v132 = Pacman() # this makes model = None in the end!
        model = model_backup
        model.add_object(v132) # add object to model
    else:
        v132 = Pacman(root = root, view = last_view)
    v132.move_absolute(v133)  

    temp = get_nested_attribute(action, 'v132')
    if temp is None:
        temp = v132
    if action is not None and hasattr(action, "v137".split('.')[0]):
        action.v137 = temp
    else:
        v137 = temp 


    temp = get_nested_attribute(action, 'v137')
    if temp is None:
        temp = v137
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
    if action is not None and hasattr(action, "v139".split('.')[0]):
        action.v139 = temp
    else:
        v139 = temp 


    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v140".split('.')[0]):
        action.v140 = temp
    else:
        v140 = temp 

    v138 = (v139 , v140); v138 = tuple(v138) if isinstance(v138, np.ndarray) else v138
    if action is not None:
        action.pacman.move_relative(v138)
    else:
        pacman.move_relative(v138)

    if model is not None:
        v141 = View()
        model.add_object(v141) # add object to model
    else:
        v141 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v141

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v142".split('.')[0]):
        action.v142 = temp
    else:
        v142 = temp 

    v143 = - v142

    temp = get_nested_attribute(action, 'v143')
    if temp is None:
        temp = v143
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


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
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


    temp = get_nested_attribute(action, 'v147')
    if temp is None:
        temp = v147
    if action is not None and hasattr(action, "v148".split('.')[0]):
        action.v148 = temp
    else:
        v148 = temp 


    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
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


    temp = get_nested_attribute(action, 'v150')
    if temp is None:
        temp = v150
    if action is not None and hasattr(action, "v151".split('.')[0]):
        action.v151 = temp
    else:
        v151 = temp 


    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
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


    temp = get_nested_attribute(action, '"2"')
    if temp is None:
        temp = "2"
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


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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


    if action is not None:
        action.v141.Ox = v145
        action.v141.Oy = v148
        action.v141.width = v151
        action.v141.height = v154
        action.v141.title = v157
        action.v141.background = v160
    else:
        v141.Ox = v145
        v141.Oy = v148
        v141.width = v151
        v141.height = v154
        v141.title = v157
        v141.background = v160

    temp = get_nested_attribute(action, 'v141')
    if temp is None:
        temp = v141
    if action is not None and hasattr(action, "view2".split('.')[0]):
        action.view2 = temp
    else:
        view2 = temp 
    if model is not None: 
        model.view2 = view2
        model.last_view2 = copy.deepcopy(view2)

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v162".split('.')[0]):
        action.v162 = temp
    else:
        v162 = temp 


    temp = get_nested_attribute(action, 'pacman.origin[v162]')
    if temp is None:
        temp = pacman.origin[v162]
    if action is not None and hasattr(action, "v161".split('.')[0]):
        action.v161 = temp
    else:
        v161 = temp 


    temp = get_nested_attribute(action, 'v161')
    if temp is None:
        temp = v161
    if action is not None and hasattr(action, "v163".split('.')[0]):
        action.v163 = temp
    else:
        v163 = temp 


    temp = get_nested_attribute(action, 'v163')
    if temp is None:
        temp = v163
    if action is not None and hasattr(action, "view2.Ox".split('.')[0]):
        action.view2.Ox = temp
    else:
        view2.Ox = temp 


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v165".split('.')[0]):
        action.v165 = temp
    else:
        v165 = temp 


    temp = get_nested_attribute(action, 'pacman.origin[v165]')
    if temp is None:
        temp = pacman.origin[v165]
    if action is not None and hasattr(action, "v164".split('.')[0]):
        action.v164 = temp
    else:
        v164 = temp 


    temp = get_nested_attribute(action, 'v164')
    if temp is None:
        temp = v164
    if action is not None and hasattr(action, "v166".split('.')[0]):
        action.v166 = temp
    else:
        v166 = temp 


    temp = get_nested_attribute(action, 'v166')
    if temp is None:
        temp = v166
    if action is not None and hasattr(action, "view2.Oy".split('.')[0]):
        action.view2.Oy = temp
    else:
        view2.Oy = temp 


    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v168".split('.')[0]):
        action.v168 = temp
    else:
        v168 = temp 

    v169 = - v168

    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v170".split('.')[0]):
        action.v170 = temp
    else:
        v170 = temp 

    v171 = - v170
    v167 = (v169 , v171); v167 = tuple(v167) if isinstance(v167, np.ndarray) else v167

    if action is not None:
        new_model = Pacman() ### TODO: !!!
        action.pacman.copyAttributesTo(new_model, draw=True)
        v172 = new_model
        v172.move_absolute(v167)
        model.add_object(v172) # add object to model
    else:
        new_model = Pacman() ### TODO: !!!
        pacman.copyAttributesTo(new_model, draw=True)
        v172 = new_model
        v172.move_absolute(v167)


    temp = get_nested_attribute(action, 'v172')
    if temp is None:
        temp = v172
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
    if action is not None and hasattr(action, "pacman2.face.fill".split('.')[0]):
        action.pacman2.face.fill = temp
    else:
        pacman2.face.fill = temp 

    last_refresh = time.time()
    view.update()

    last_refresh = time.time()
    view2.update()


    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v177".split('.')[0]):
        action.v177 = temp
    else:
        v177 = temp 

    print(v177)
    if action is not None:
        v178 = action.view.waitClick()
    else:
        v178 = last_view.waitClick()

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


    temp = get_nested_attribute(action, 'v180')
    if temp is None:
        temp = v180
    if action is not None and hasattr(action, "pos".split('.')[0]):
        action.pos = temp
    else:
        pos = temp 
    if model is not None: 
        model.pos = pos
        model.last_pos = copy.deepcopy(pos)

    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v181".split('.')[0]):
        action.v181 = temp
    else:
        v181 = temp 


    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v182".split('.')[0]):
        action.v182 = temp
    else:
        v182 = temp 

    for i in range(v181, v182, 1):

        temp = get_nested_attribute(action, 'Close')
        if temp is None:
            temp = Close
        if action is not None and hasattr(action, "v183".split('.')[0]):
            action.v183 = temp
        else:
            v183 = temp 


        temp = get_nested_attribute(action, 'v183')
        if temp is None:
            temp = v183
        if action is not None and hasattr(action, "v184".split('.')[0]):
            action.v184 = temp
        else:
            v184 = temp 


        temp = get_nested_attribute(action, 'v184')
        if temp is None:
            temp = v184
        if action is not None and hasattr(action, "pacman.mouth".split('.')[0]):
            action.pacman.mouth = temp
        else:
            pacman.mouth = temp 


        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v185".split('.')[0]):
            action.v185 = temp
        else:
            v185 = temp 

         
        while (time.time() - last_refresh <= v185/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v186".split('.')[0]):
            action.v186 = temp
        else:
            v186 = temp 

         
        while (time.time() - last_refresh <= v186/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view2.update()


        temp = get_nested_attribute(action, 'Open')
        if temp is None:
            temp = Open
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
        if action is not None and hasattr(action, "pacman.mouth".split('.')[0]):
            action.pacman.mouth = temp
        else:
            pacman.mouth = temp 


        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v189".split('.')[0]):
            action.v189 = temp
        else:
            v189 = temp 

         
        while (time.time() - last_refresh <= v189/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v190".split('.')[0]):
            action.v190 = temp
        else:
            v190 = temp 

         
        while (time.time() - last_refresh <= v190/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view2.update()


        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v192".split('.')[0]):
            action.v192 = temp
        else:
            v192 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v193".split('.')[0]):
            action.v193 = temp
        else:
            v193 = temp 

        v191 = (v192 , v193); v191 = tuple(v191) if isinstance(v191, np.ndarray) else v191
        if action is not None:
            action.pacman.move_relative(v191)
        else:
            pacman.move_relative(v191)

        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v195".split('.')[0]):
            action.v195 = temp
        else:
            v195 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v196".split('.')[0]):
            action.v196 = temp
        else:
            v196 = temp 

        v194 = (v195 , v196); v194 = tuple(v194) if isinstance(v194, np.ndarray) else v194
        if action is not None:
            action.view2.move_relative(v194)
        else:
            view2.move_relative(v194)

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v197".split('.')[0]):
            action.v197 = temp
        else:
            v197 = temp 

         
        while (time.time() - last_refresh <= v197/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view2.update()


    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v198".split('.')[0]):
        action.v198 = temp
    else:
        v198 = temp 

    print(v198)
    if action is not None:
        v199 = action.view.waitClick()
    else:
        v199 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v199')
    if temp is None:
        temp = v199
    if action is not None and hasattr(action, "v200".split('.')[0]):
        action.v200 = temp
    else:
        v200 = temp 


    temp = get_nested_attribute(action, 'v200')
    if temp is None:
        temp = v200
    if action is not None and hasattr(action, "v201".split('.')[0]):
        action.v201 = temp
    else:
        v201 = temp 


    temp = get_nested_attribute(action, 'v201')
    if temp is None:
        temp = v201
    if action is not None and hasattr(action, "pos".split('.')[0]):
        action.pos = temp
    else:
        pos = temp 
    if model is not None: 
        model.pos = pos
        model.last_pos = copy.deepcopy(pos)

    temp = get_nested_attribute(action, 'pacman2.origin')
    if temp is None:
        temp = pacman2.origin
    if action is not None and hasattr(action, "v202".split('.')[0]):
        action.v202 = temp
    else:
        v202 = temp 

    if action is not None:
        action.view2.move_absolute(v202)
    else:
        view2.move_absolute(v202)
    last_refresh = time.time()
    view.update()

    last_refresh = time.time()
    view2.update()


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v203".split('.')[0]):
        action.v203 = temp
    else:
        v203 = temp 


    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v204".split('.')[0]):
        action.v204 = temp
    else:
        v204 = temp 

    for i in range(v203, v204, 1):

        temp = get_nested_attribute(action, 'Close')
        if temp is None:
            temp = Close
        if action is not None and hasattr(action, "v205".split('.')[0]):
            action.v205 = temp
        else:
            v205 = temp 


        temp = get_nested_attribute(action, 'v205')
        if temp is None:
            temp = v205
        if action is not None and hasattr(action, "v206".split('.')[0]):
            action.v206 = temp
        else:
            v206 = temp 


        temp = get_nested_attribute(action, 'v206')
        if temp is None:
            temp = v206
        if action is not None and hasattr(action, "pacman2.mouth".split('.')[0]):
            action.pacman2.mouth = temp
        else:
            pacman2.mouth = temp 


        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v207".split('.')[0]):
            action.v207 = temp
        else:
            v207 = temp 

         
        while (time.time() - last_refresh <= v207/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v208".split('.')[0]):
            action.v208 = temp
        else:
            v208 = temp 

         
        while (time.time() - last_refresh <= v208/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view2.update()


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
        if action is not None and hasattr(action, "pacman2.mouth".split('.')[0]):
            action.pacman2.mouth = temp
        else:
            pacman2.mouth = temp 


        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v211".split('.')[0]):
            action.v211 = temp
        else:
            v211 = temp 

         
        while (time.time() - last_refresh <= v211/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v212".split('.')[0]):
            action.v212 = temp
        else:
            v212 = temp 

         
        while (time.time() - last_refresh <= v212/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view2.update()


        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v214".split('.')[0]):
            action.v214 = temp
        else:
            v214 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v215".split('.')[0]):
            action.v215 = temp
        else:
            v215 = temp 

        v213 = (v214 , v215); v213 = tuple(v213) if isinstance(v213, np.ndarray) else v213
        if action is not None:
            action.pacman2.move_relative(v213)
        else:
            pacman2.move_relative(v213)

        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v217".split('.')[0]):
            action.v217 = temp
        else:
            v217 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v218".split('.')[0]):
            action.v218 = temp
        else:
            v218 = temp 

        v216 = (v217 , v218); v216 = tuple(v216) if isinstance(v216, np.ndarray) else v216
        if action is not None:
            action.view2.move_relative(v216)
        else:
            view2.move_relative(v216)

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v219".split('.')[0]):
            action.v219 = temp
        else:
            v219 = temp 

         
        while (time.time() - last_refresh <= v219/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v220".split('.')[0]):
            action.v220 = temp
        else:
            v220 = temp 

         
        while (time.time() - last_refresh <= v220/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view2.update()


    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v221".split('.')[0]):
        action.v221 = temp
    else:
        v221 = temp 

    print(v221)
    if action is not None:
        v222 = action.view.waitClick()
    else:
        v222 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v222')
    if temp is None:
        temp = v222
    if action is not None and hasattr(action, "v223".split('.')[0]):
        action.v223 = temp
    else:
        v223 = temp 


    temp = get_nested_attribute(action, 'v223')
    if temp is None:
        temp = v223
    if action is not None and hasattr(action, "v224".split('.')[0]):
        action.v224 = temp
    else:
        v224 = temp 


    temp = get_nested_attribute(action, 'v224')
    if temp is None:
        temp = v224
    if action is not None and hasattr(action, "pos".split('.')[0]):
        action.pos = temp
    else:
        pos = temp 
    if model is not None: 
        model.pos = pos
        model.last_pos = copy.deepcopy(pos)
    view2.close(); views.remove(view2) if last_view != view2 else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == view2 else last_view

    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v225".split('.')[0]):
        action.v225 = temp
    else:
        v225 = temp 

    print(v225)
    if action is not None:
        v226 = action.view.waitClick()
    else:
        v226 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v226')
    if temp is None:
        temp = v226
    if action is not None and hasattr(action, "v227".split('.')[0]):
        action.v227 = temp
    else:
        v227 = temp 


    temp = get_nested_attribute(action, 'v227')
    if temp is None:
        temp = v227
    if action is not None and hasattr(action, "pos".split('.')[0]):
        action.pos = temp
    else:
        pos = temp 

    view.close(); views.remove(view) if last_view != view else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == view else last_view
