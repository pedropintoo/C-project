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

            temp = get_nested_attribute(action, '100')
            if temp is None:
                temp = 100
            if action is not None and hasattr(action, "v1".split('.')[0]):
                action.v1 = temp
            else:
                v1 = temp 


            temp = get_nested_attribute(action, '56')
            if temp is None:
                temp = 56
            if action is not None and hasattr(action, "v2".split('.')[0]):
                action.v2 = temp
            else:
                v2 = temp 

            v0 = (v1 , v2)

            if model is not None:
                v3 = Polygon()
                model.add_object(v3) # add object to model
            else:
                v3 = Polygon(root = root)
            v3.origin = v0

            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v6".split('.')[0]):
                action.v6 = temp
            else:
                v6 = temp 


            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v7".split('.')[0]):
                action.v7 = temp
            else:
                v7 = temp 

            v5 = (v6 , v7)

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v9".split('.')[0]):
                action.v9 = temp
            else:
                v9 = temp 


            temp = get_nested_attribute(action, '25')
            if temp is None:
                temp = 25
            if action is not None and hasattr(action, "v10".split('.')[0]):
                action.v10 = temp
            else:
                v10 = temp 

            v8 = (v9 , v10)

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v12".split('.')[0]):
                action.v12 = temp
            else:
                v12 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v13".split('.')[0]):
                action.v13 = temp
            else:
                v13 = temp 

            v11 = (v12 , v13)

            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v15".split('.')[0]):
                action.v15 = temp
            else:
                v15 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v16".split('.')[0]):
                action.v16 = temp
            else:
                v16 = temp 

            v14 = (v15 , v16)

            temp = get_nested_attribute(action, '25')
            if temp is None:
                temp = 25
            if action is not None and hasattr(action, "v18".split('.')[0]):
                action.v18 = temp
            else:
                v18 = temp 


            temp = get_nested_attribute(action, '41')
            if temp is None:
                temp = 41
            if action is not None and hasattr(action, "v19".split('.')[0]):
                action.v19 = temp
            else:
                v19 = temp 

            v17 = (v18 , v19)
            v4 = [v5,v8,v11,v14,v17]

            temp = get_nested_attribute(action, 'v4')
            if temp is None:
                temp = v4
            if action is not None and hasattr(action, "v20".split('.')[0]):
                action.v20 = temp
            else:
                v20 = temp 


            temp = get_nested_attribute(action, 'v20')
            if temp is None:
                temp = v20
            if action is not None and hasattr(action, "v21".split('.')[0]):
                action.v21 = temp
            else:
                v21 = temp 


            temp = get_nested_attribute(action, '"tomato"')
            if temp is None:
                temp = "tomato"
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


            if action is not None:
                action.v3.points = v21
                action.v3.fill = v24
            else:
                v3.points = v21
                v3.fill = v24

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
    class Jorge(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v26".split('.')[0]):
                action.v26 = temp
            else:
                v26 = temp 


            temp = get_nested_attribute(action, '80')
            if temp is None:
                temp = 80
            if action is not None and hasattr(action, "v27".split('.')[0]):
                action.v27 = temp
            else:
                v27 = temp 

            v28 = - v27
            v25 = (v26 , v28)

            if model is not None:
                v29 = Rectangle()
                model.add_object(v29) # add object to model
            else:
                v29 = Rectangle(root = root)
            v29.origin = v25

            temp = get_nested_attribute(action, '21')
            if temp is None:
                temp = 21
            if action is not None and hasattr(action, "v31".split('.')[0]):
                action.v31 = temp
            else:
                v31 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v32".split('.')[0]):
                action.v32 = temp
            else:
                v32 = temp 

            v30 = (v31 , v32)

            temp = get_nested_attribute(action, 'v30')
            if temp is None:
                temp = v30
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


            temp = get_nested_attribute(action, '"orange"')
            if temp is None:
                temp = "orange"
            if action is not None and hasattr(action, "v35".split('.')[0]):
                action.v35 = temp
            else:
                v35 = temp 


            temp = get_nested_attribute(action, 'v35')
            if temp is None:
                temp = v35
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


            if action is not None:
                action.v29.length = v34
                action.v29.fill = v37
            else:
                v29.length = v34
                v29.fill = v37

            temp = get_nested_attribute(action, 'v29')
            if temp is None:
                temp = v29
            if action is not None and hasattr(action, "jorge".split('.')[0]):
                action.jorge = temp
            else:
                jorge = temp 
            if model is not None: 
                model.jorge = jorge
                model.last_jorge = copy.deepcopy(jorge)

            temp = get_nested_attribute(action, '60')
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v39".split('.')[0]):
                action.v39 = temp
            else:
                v39 = temp 

            v40 = - v39

            temp = get_nested_attribute(action, '26')
            if temp is None:
                temp = 26
            if action is not None and hasattr(action, "v41".split('.')[0]):
                action.v41 = temp
            else:
                v41 = temp 

            v38 = (v40 , v41)

            if model is not None:
                v42 = ArcChord()
                model.add_object(v42) # add object to model
            else:
                v42 = ArcChord(root = root)
            v42.origin = v38

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v44".split('.')[0]):
                action.v44 = temp
            else:
                v44 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
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


            temp = get_nested_attribute(action, '90')
            if temp is None:
                temp = 90
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


            temp = get_nested_attribute(action, 'v49')
            if temp is None:
                temp = v49
            if action is not None and hasattr(action, "v50".split('.')[0]):
                action.v50 = temp
            else:
                v50 = temp 


            temp = get_nested_attribute(action, '100')
            if temp is None:
                temp = 100
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


            temp = get_nested_attribute(action, 'v52')
            if temp is None:
                temp = v52
            if action is not None and hasattr(action, "v53".split('.')[0]):
                action.v53 = temp
            else:
                v53 = temp 


            temp = get_nested_attribute(action, '"tomato"')
            if temp is None:
                temp = "tomato"
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


            if action is not None:
                action.v42.length = v47
                action.v42.start = v50
                action.v42.extent = v53
                action.v42.outline = v56
            else:
                v42.length = v47
                v42.start = v50
                v42.extent = v53
                v42.outline = v56

            temp = get_nested_attribute(action, 'v42')
            if temp is None:
                temp = v42
            if action is not None and hasattr(action, "jorjão".split('.')[0]):
                action.jorjão = temp
            else:
                jorjão = temp 
            if model is not None: 
                model.jorjão = jorjão
                model.last_jorjão = copy.deepcopy(jorjão)

            self.fixCoords()

        def create_object(self, view):
            action = self
        
            action = None
            super().create_object(view)
            model = None

        def __deepcopy__(self, memo=None):
            """Create a deep copy of the model."""
            if memo is None:
                memo = {} # this is required by the deepcopy protocol
            new_model = Jorge()

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
                v57 = PieSlice()
                model.add_object(v57) # add object to model
            else:
                v57 = PieSlice(root = root)

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v59".split('.')[0]):
                action.v59 = temp
            else:
                v59 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v60".split('.')[0]):
                action.v60 = temp
            else:
                v60 = temp 

            v58 = (v59 , v60)

            temp = get_nested_attribute(action, 'v58')
            if temp is None:
                temp = v58
            if action is not None and hasattr(action, "v61".split('.')[0]):
                action.v61 = temp
            else:
                v61 = temp 


            temp = get_nested_attribute(action, 'v61')
            if temp is None:
                temp = v61
            if action is not None and hasattr(action, "v62".split('.')[0]):
                action.v62 = temp
            else:
                v62 = temp 


            temp = get_nested_attribute(action, '"pink"')
            if temp is None:
                temp = "pink"
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
            if action is not None and hasattr(action, "v65".split('.')[0]):
                action.v65 = temp
            else:
                v65 = temp 


            temp = get_nested_attribute(action, '30')
            if temp is None:
                temp = 30
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


            temp = get_nested_attribute(action, '300')
            if temp is None:
                temp = 300
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


            temp = get_nested_attribute(action, 'v70')
            if temp is None:
                temp = v70
            if action is not None and hasattr(action, "v71".split('.')[0]):
                action.v71 = temp
            else:
                v71 = temp 


            if action is not None:
                action.v57.length = v62
                action.v57.fill = v65
                action.v57.start = v68
                action.v57.extent = v71
            else:
                v57.length = v62
                v57.fill = v65
                v57.start = v68
                v57.extent = v71

            temp = get_nested_attribute(action, 'v57')
            if temp is None:
                temp = v57
            if action is not None and hasattr(action, "face".split('.')[0]):
                action.face = temp
            else:
                face = temp 
            if model is not None: 
                model.face = face
                model.last_face = copy.deepcopy(face)

            if model is not None:
                model_backup = model
                v72 = Fire() # this makes model = None in the end!
                model = model_backup
                model.add_object(v72) # add object to model
            else:
                v72 = Fire(root = root, view = last_view)
              

            temp = get_nested_attribute(action, 'v72')
            if temp is None:
                temp = v72
            if action is not None and hasattr(action, "v73".split('.')[0]):
                action.v73 = temp
            else:
                v73 = temp 


            temp = get_nested_attribute(action, 'v73')
            if temp is None:
                temp = v73
            if action is not None and hasattr(action, "fire".split('.')[0]):
                action.fire = temp
            else:
                fire = temp 
            if model is not None: 
                model.fire = fire
                model.last_fire = copy.deepcopy(fire)

            if model is not None:
                model_backup = model
                v74 = Jorge() # this makes model = None in the end!
                model = model_backup
                model.add_object(v74) # add object to model
            else:
                v74 = Jorge(root = root, view = last_view)
              

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
            if action is not None and hasattr(action, "jorgin".split('.')[0]):
                action.jorgin = temp
            else:
                jorgin = temp 
            if model is not None: 
                model.jorgin = jorgin
                model.last_jorgin = copy.deepcopy(jorgin)

            self.fixCoords()

        def create_object(self, view):
            action = self
        
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

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v78".split('.')[0]):
        action.v78 = temp
    else:
        v78 = temp 

    v79 = - v78

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v80".split('.')[0]):
        action.v80 = temp
    else:
        v80 = temp 

    v77 = (v79 , v80)

    if model is not None:
        model_backup = model
        v76 = Pacman() # this makes model = None in the end!
        model = model_backup
        model.add_object(v76) # add object to model
    else:
        v76 = Pacman(root = root, view = last_view)
    v76.move_absolute(v77)  

    temp = get_nested_attribute(action, 'v76')
    if temp is None:
        temp = v76
    if action is not None and hasattr(action, "v81".split('.')[0]):
        action.v81 = temp
    else:
        v81 = temp 


    temp = get_nested_attribute(action, 'v81')
    if temp is None:
        temp = v81
    if action is not None and hasattr(action, "pacman".split('.')[0]):
        action.pacman = temp
    else:
        pacman = temp 
    if model is not None: 
        model.pacman = pacman
        model.last_pacman = copy.deepcopy(pacman)

    if model is not None:
        v82 = View()
        model.add_object(v82) # add object to model
    else:
        v82 = View(root = root)
    last_view = v82

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v83".split('.')[0]):
        action.v83 = temp
    else:
        v83 = temp 

    v84 = - v83

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


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v87".split('.')[0]):
        action.v87 = temp
    else:
        v87 = temp 


    temp = get_nested_attribute(action, 'v87')
    if temp is None:
        temp = v87
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


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
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


    temp = get_nested_attribute(action, 'v91')
    if temp is None:
        temp = v91
    if action is not None and hasattr(action, "v92".split('.')[0]):
        action.v92 = temp
    else:
        v92 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
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


    temp = get_nested_attribute(action, 'v94')
    if temp is None:
        temp = v94
    if action is not None and hasattr(action, "v95".split('.')[0]):
        action.v95 = temp
    else:
        v95 = temp 


    temp = get_nested_attribute(action, '"1"')
    if temp is None:
        temp = "1"
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


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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
        action.v82.Ox = v86
        action.v82.Oy = v89
        action.v82.width = v92
        action.v82.height = v95
        action.v82.title = v98
        action.v82.background = v101
    else:
        v82.Ox = v86
        v82.Oy = v89
        v82.width = v92
        v82.height = v95
        v82.title = v98
        v82.background = v101

    temp = get_nested_attribute(action, 'v82')
    if temp is None:
        temp = v82
    if action is not None and hasattr(action, "view".split('.')[0]):
        action.view = temp
    else:
        view = temp 
    if model is not None: 
        model.view = view
        model.last_view = copy.deepcopy(view)
    last_refresh = time.time()
    view.update()
    view.update()


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v102".split('.')[0]):
        action.v102 = temp
    else:
        v102 = temp 


    temp = get_nested_attribute(action, '5')
    if temp is None:
        temp = 5
    if action is not None and hasattr(action, "v103".split('.')[0]):
        action.v103 = temp
    else:
        v103 = temp 

    for i in range(v102, v103, 1):

        temp = get_nested_attribute(action, '45')
        if temp is None:
            temp = 45
        if action is not None and hasattr(action, "v105".split('.')[0]):
            action.v105 = temp
        else:
            v105 = temp 


        temp = get_nested_attribute(action, '45')
        if temp is None:
            temp = 45
        if action is not None and hasattr(action, "v106".split('.')[0]):
            action.v106 = temp
        else:
            v106 = temp 

        v104 = (v105 , v106)
        if action is not None:
            action.pacman.move_relative(v104)
        else:
            pacman.rotate(90)
         

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v107".split('.')[0]):
            action.v107 = temp
        else:
            v107 = temp 

        while (time.time() - last_refresh <= v107):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()

