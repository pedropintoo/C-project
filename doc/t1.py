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


            temp = get_nested_attribute(action, '25')
            if temp is None:
                temp = 25
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


            temp = get_nested_attribute(action, '30')
            if temp is None:
                temp = 30
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


            temp = get_nested_attribute(action, '100')
            if temp is None:
                temp = 100
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


            temp = get_nested_attribute(action, '"tomato"')
            if temp is None:
                temp = "tomato"
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
                action.v3.start = v11
                action.v3.extent = v14
                action.v3.outline = v17
            else:
                v3.length = v8
                v3.start = v11
                v3.extent = v14
                v3.outline = v17

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
    class Pacman(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self

            if model is not None:
                v18 = PieSlice()
                model.add_object(v18) # add object to model
            else:
                v18 = PieSlice(root = root)

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v20".split('.')[0]):
                action.v20 = temp
            else:
                v20 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v21".split('.')[0]):
                action.v21 = temp
            else:
                v21 = temp 

            v19 = (v20 , v21)

            temp = get_nested_attribute(action, 'v19')
            if temp is None:
                temp = v19
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


            temp = get_nested_attribute(action, '"pink"')
            if temp is None:
                temp = "pink"
            if action is not None and hasattr(action, "v24".split('.')[0]):
                action.v24 = temp
            else:
                v24 = temp 


            temp = get_nested_attribute(action, 'v24')
            if temp is None:
                temp = v24
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


            temp = get_nested_attribute(action, '30')
            if temp is None:
                temp = 30
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


            temp = get_nested_attribute(action, '300')
            if temp is None:
                temp = 300
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


            if action is not None:
                action.v18.length = v23
                action.v18.fill = v26
                action.v18.start = v29
                action.v18.extent = v32
            else:
                v18.length = v23
                v18.fill = v26
                v18.start = v29
                v18.extent = v32

            temp = get_nested_attribute(action, 'v18')
            if temp is None:
                temp = v18
            if action is not None and hasattr(action, "face".split('.')[0]):
                action.face = temp
            else:
                face = temp 
            if model is not None: 
                model.face = face
                model.last_face = copy.deepcopy(face)

            if model is not None:
                model_backup = model
                v33 = Fire() # this makes model = None in the end!
                model = model_backup
                model.add_object(v33) # add object to model
            else:
                v33 = Fire(root = root, view = last_view)
              

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
            if action is not None and hasattr(action, "fire".split('.')[0]):
                action.fire = temp
            else:
                fire = temp 
            if model is not None: 
                model.fire = fire
                model.last_fire = copy.deepcopy(fire)

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
    if action is not None and hasattr(action, "v37".split('.')[0]):
        action.v37 = temp
    else:
        v37 = temp 

    v38 = - v37

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v39".split('.')[0]):
        action.v39 = temp
    else:
        v39 = temp 

    v36 = (v38 , v39)

    if model is not None:
        model_backup = model
        v35 = Pacman() # this makes model = None in the end!
        model = model_backup
        model.add_object(v35) # add object to model
    else:
        v35 = Pacman(root = root, view = last_view)
    v35.move_absolute(v36)  

    temp = get_nested_attribute(action, 'v35')
    if temp is None:
        temp = v35
    if action is not None and hasattr(action, "v40".split('.')[0]):
        action.v40 = temp
    else:
        v40 = temp 


    temp = get_nested_attribute(action, 'v40')
    if temp is None:
        temp = v40
    if action is not None and hasattr(action, "pacman".split('.')[0]):
        action.pacman = temp
    else:
        pacman = temp 
    if model is not None: 
        model.pacman = pacman
        model.last_pacman = copy.deepcopy(pacman)

    if model is not None:
        v41 = View()
        model.add_object(v41) # add object to model
    else:
        v41 = View(root = root)
    last_view = v41

    temp = get_nested_attribute(action, '450')
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v42".split('.')[0]):
        action.v42 = temp
    else:
        v42 = temp 

    v43 = - v42

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


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
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


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
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


    temp = get_nested_attribute(action, 'v50')
    if temp is None:
        temp = v50
    if action is not None and hasattr(action, "v51".split('.')[0]):
        action.v51 = temp
    else:
        v51 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
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


    temp = get_nested_attribute(action, 'v53')
    if temp is None:
        temp = v53
    if action is not None and hasattr(action, "v54".split('.')[0]):
        action.v54 = temp
    else:
        v54 = temp 


    temp = get_nested_attribute(action, '"1"')
    if temp is None:
        temp = "1"
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


    temp = get_nested_attribute(action, 'v56')
    if temp is None:
        temp = v56
    if action is not None and hasattr(action, "v57".split('.')[0]):
        action.v57 = temp
    else:
        v57 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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
    if action is not None and hasattr(action, "v60".split('.')[0]):
        action.v60 = temp
    else:
        v60 = temp 


    if action is not None:
        action.v41.Ox = v45
        action.v41.Oy = v48
        action.v41.width = v51
        action.v41.height = v54
        action.v41.title = v57
        action.v41.background = v60
    else:
        v41.Ox = v45
        v41.Oy = v48
        v41.width = v51
        v41.height = v54
        v41.title = v57
        v41.background = v60

    temp = get_nested_attribute(action, 'v41')
    if temp is None:
        temp = v41
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

    for i in range(v61, v62, 1):

        temp = get_nested_attribute(action, '45')
        if temp is None:
            temp = 45
        if action is not None and hasattr(action, "v64".split('.')[0]):
            action.v64 = temp
        else:
            v64 = temp 


        temp = get_nested_attribute(action, '45')
        if temp is None:
            temp = 45
        if action is not None and hasattr(action, "v65".split('.')[0]):
            action.v65 = temp
        else:
            v65 = temp 

        v63 = (v64 , v65)
        if action is not None:
            action.pacman.move_relative(v63)
        else:
            pacman.rotate(90)
         

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v66".split('.')[0]):
            action.v66 = temp
        else:
            v66 = temp 

        while (time.time() - last_refresh <= v66):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()

