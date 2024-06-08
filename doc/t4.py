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
def get_nested_attribute(obj, attr_path, local_dict=None):
    if obj is None:
        return None
    if local_dict is not None:
        return aaa(obj, attr_path, local_dict)

    attributes = attr_path.split('.')
    current_object = obj
    for attr in attributes:
        if hasattr(current_object, attr):
            current_object = getattr(current_object, attr)
        else:
            return None
    return current_object

def aaa(obj, attr_path, local_dict):
    if obj is None:
        return None
    if attr_path == '':
        return obj    

    # recursive approach
    attr = attr_path.split('.')[0]
    if '[' in attr:
        attr, index = attr.split('[')
        varIndex = index[:-1]
        # consider []...[]
        idx = None
        if varIndex in local_dict:
            idx = local_dict[varIndex]
        else:
            idx = int(varIndex)

        if hasattr(obj, attr):
            obj = getattr(obj, attr)
            obj = obj[idx]
        else:
            return None
    else:
        if hasattr(obj, attr):
            obj = getattr(obj, attr)
        else:
            return None
    
    if '.' in attr_path:
        attr_path = '.'.join(attr_path.split('.')[1:])
        return aaa(obj, attr_path, local_dict) 
    else:
        return obj
#################################################################

if __name__ == "__main__":
    root = Root()

    #################################################################
    ## Model
    #################################################################
    class Disk(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '1')
            if temp is None:
                temp = 1
            if action is not None and hasattr(action, "v0".split('[')[0].split('.')[0]):
                action.v0 = temp
            else:
                v0 = temp 


            temp = get_nested_attribute(action, 'v0')
            if temp is None:
                temp = v0
            if action is not None and hasattr(action, "v1".split('[')[0].split('.')[0]):
                action.v1 = temp
            else:
                v1 = temp 


            temp = get_nested_attribute(action, 'v1')
            if temp is None:
                temp = v1
            if action is not None and hasattr(action, "v2".split('[')[0].split('.')[0]):
                action.v2 = temp
            else:
                v2 = temp 


            temp = get_nested_attribute(action, 'v2')
            if temp is None:
                temp = v2
            if action is not None and hasattr(action, "size".split('[')[0].split('.')[0]):
                action.size = temp
            else:
                size = temp 
            if model is not None: 
                model.size = size
                model.last_size = copy.deepcopy(size)

            if model is not None:
                v11 = Rectangle()
                model.add_object(v11) # add object to model
            else:
                v11 = Rectangle(root = root)

            temp = get_nested_attribute(action, '75')
            if temp is None:
                temp = 75
            if action is not None and hasattr(action, "v13".split('[')[0].split('.')[0]):
                action.v13 = temp
            else:
                v13 = temp 


            temp = get_nested_attribute(action, '15')
            if temp is None:
                temp = 15
            if action is not None and hasattr(action, "v14".split('[')[0].split('.')[0]):
                action.v14 = temp
            else:
                v14 = temp 

            v12 = (v13 , v14); v12 = tuple(v12) if isinstance(v12, np.ndarray) else v12

            temp = get_nested_attribute(action, 'v12')
            if temp is None:
                temp = v12
            if action is not None and hasattr(action, "v15".split('[')[0].split('.')[0]):
                action.v15 = temp
            else:
                v15 = temp 


            temp = get_nested_attribute(action, 'v15')
            if temp is None:
                temp = v15
            if action is not None and hasattr(action, "v16".split('[')[0].split('.')[0]):
                action.v16 = temp
            else:
                v16 = temp 


            temp = get_nested_attribute(action, '"brown"')
            if temp is None:
                temp = "brown"
            if action is not None and hasattr(action, "v17".split('[')[0].split('.')[0]):
                action.v17 = temp
            else:
                v17 = temp 


            temp = get_nested_attribute(action, 'v17')
            if temp is None:
                temp = v17
            if action is not None and hasattr(action, "v18".split('[')[0].split('.')[0]):
                action.v18 = temp
            else:
                v18 = temp 


            temp = get_nested_attribute(action, 'v18')
            if temp is None:
                temp = v18
            if action is not None and hasattr(action, "v19".split('[')[0].split('.')[0]):
                action.v19 = temp
            else:
                v19 = temp 


            if action is not None:
                action.v11.length = v16
                action.v11.fill = v19
            else:
                v11.length = v16
                v11.fill = v19

            temp = get_nested_attribute(action, 'v11')
            if temp is None:
                temp = v11
            if action is not None and hasattr(action, "wood".split('[')[0].split('.')[0]):
                action.wood = temp
            else:
                wood = temp 
            if model is not None: 
                model.wood = wood
                model.last_wood = copy.deepcopy(wood)

            self.fixCoords()

        def create_object(self, view):
            action = self

            if self.size != self.last_size:

                temp = get_nested_attribute(action, '50')
                if temp is None:
                    temp = 50
                if action is not None and hasattr(action, "v5".split('[')[0].split('.')[0]):
                    action.v5 = temp
                else:
                    v5 = temp 


                temp = get_nested_attribute(action, '25')
                if temp is None:
                    temp = 25
                if action is not None and hasattr(action, "v7".split('[')[0].split('.')[0]):
                    action.v7 = temp
                else:
                    v7 = temp 


                temp = get_nested_attribute(action, 'size')
                if temp is None:
                    temp = size
                if action is not None and hasattr(action, "v8".split('[')[0].split('.')[0]):
                    action.v8 = temp
                else:
                    v8 = temp 

                v6 = np.dot(np.array(v7) , np.array(v8)); v6 = tuple(v6) if isinstance(v6, np.ndarray) else v6
                v4 = np.array(v5) + np.array(v6); v4 = tuple(v4) if isinstance(v4, np.ndarray) else v4

                temp = get_nested_attribute(action, '15')
                if temp is None:
                    temp = 15
                if action is not None and hasattr(action, "v9".split('[')[0].split('.')[0]):
                    action.v9 = temp
                else:
                    v9 = temp 

                v3 = (v4 , v9); v3 = tuple(v3) if isinstance(v3, np.ndarray) else v3

                temp = get_nested_attribute(action, 'v3')
                if temp is None:
                    temp = v3
                if action is not None and hasattr(action, "v10".split('[')[0].split('.')[0]):
                    action.v10 = temp
                else:
                    v10 = temp 


                temp = get_nested_attribute(action, 'v10')
                if temp is None:
                    temp = v10
                if action is not None and hasattr(action, "wood.length".split('[')[0].split('.')[0]):
                    action.wood.length = temp
                else:
                    wood.length = temp 

                self.last_size = copy.deepcopy(self.size)
        
            action = None
            super().create_object(view)
            model = None

        def __deepcopy__(self, memo=None):
            """Create a deep copy of the model."""
            if memo is None:
                memo = {} # this is required by the deepcopy protocol
            new_model = Disk()

            self.copyAttributesTo(new_model)
            return new_model       

    #################################################################
    #################################################################
    ## Model
    #################################################################
    class Base(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self

            if model is not None:
                v20 = Rectangle()
                model.add_object(v20) # add object to model
            else:
                v20 = Rectangle(root = root)

            temp = get_nested_attribute(action, '200')
            if temp is None:
                temp = 200
            if action is not None and hasattr(action, "v22".split('[')[0].split('.')[0]):
                action.v22 = temp
            else:
                v22 = temp 


            temp = get_nested_attribute(action, '20')
            if temp is None:
                temp = 20
            if action is not None and hasattr(action, "v23".split('[')[0].split('.')[0]):
                action.v23 = temp
            else:
                v23 = temp 

            v21 = (v22 , v23); v21 = tuple(v21) if isinstance(v21, np.ndarray) else v21

            temp = get_nested_attribute(action, 'v21')
            if temp is None:
                temp = v21
            if action is not None and hasattr(action, "v24".split('[')[0].split('.')[0]):
                action.v24 = temp
            else:
                v24 = temp 


            temp = get_nested_attribute(action, 'v24')
            if temp is None:
                temp = v24
            if action is not None and hasattr(action, "v25".split('[')[0].split('.')[0]):
                action.v25 = temp
            else:
                v25 = temp 


            temp = get_nested_attribute(action, '"brown"')
            if temp is None:
                temp = "brown"
            if action is not None and hasattr(action, "v26".split('[')[0].split('.')[0]):
                action.v26 = temp
            else:
                v26 = temp 


            temp = get_nested_attribute(action, 'v26')
            if temp is None:
                temp = v26
            if action is not None and hasattr(action, "v27".split('[')[0].split('.')[0]):
                action.v27 = temp
            else:
                v27 = temp 


            temp = get_nested_attribute(action, 'v27')
            if temp is None:
                temp = v27
            if action is not None and hasattr(action, "v28".split('[')[0].split('.')[0]):
                action.v28 = temp
            else:
                v28 = temp 


            if action is not None:
                action.v20.length = v25
                action.v20.fill = v28
            else:
                v20.length = v25
                v20.fill = v28

            temp = get_nested_attribute(action, 'v20')
            if temp is None:
                temp = v20
            if action is not None and hasattr(action, "rec".split('[')[0].split('.')[0]):
                action.rec = temp
            else:
                rec = temp 
            if model is not None: 
                model.rec = rec
                model.last_rec = copy.deepcopy(rec)

            if model is not None:
                v29 = Text()
                model.add_object(v29) # add object to model
            else:
                v29 = Text(root = root)

            temp = get_nested_attribute(action, '"Base"')
            if temp is None:
                temp = "Base"
            if action is not None and hasattr(action, "v30".split('[')[0].split('.')[0]):
                action.v30 = temp
            else:
                v30 = temp 


            temp = get_nested_attribute(action, 'v30', locals())
            if temp is None:
                temp = v30
            if action is not None and hasattr(action, "v31".split('[')[0].split('.')[0]):
                action.v31 = temp
            else:
                v31 = temp 


            temp = get_nested_attribute(action, 'v31')
            if temp is None:
                temp = v31
            if action is not None and hasattr(action, "v32".split('[')[0].split('.')[0]):
                action.v32 = temp
            else:
                v32 = temp 


            if action is not None:
                action.v29.text = v32
            else:
                v29.text = v32

            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v34".split('[')[0].split('.')[0]):
                action.v34 = temp
            else:
                v34 = temp 


            temp = get_nested_attribute(action, '120')
            if temp is None:
                temp = 120
            if action is not None and hasattr(action, "v35".split('[')[0].split('.')[0]):
                action.v35 = temp
            else:
                v35 = temp 

            v33 = (v34 , v35); v33 = tuple(v33) if isinstance(v33, np.ndarray) else v33

            if model is not None:
                v36 = Rectangle()
                model.add_object(v36) # add object to model
            else:
                v36 = Rectangle(root = root)
            v36.origin = v33

            temp = get_nested_attribute(action, '10')
            if temp is None:
                temp = 10
            if action is not None and hasattr(action, "v38".split('[')[0].split('.')[0]):
                action.v38 = temp
            else:
                v38 = temp 


            temp = get_nested_attribute(action, '100')
            if temp is None:
                temp = 100
            if action is not None and hasattr(action, "v39".split('[')[0].split('.')[0]):
                action.v39 = temp
            else:
                v39 = temp 

            v37 = (v38 , v39); v37 = tuple(v37) if isinstance(v37, np.ndarray) else v37

            temp = get_nested_attribute(action, 'v37')
            if temp is None:
                temp = v37
            if action is not None and hasattr(action, "v40".split('[')[0].split('.')[0]):
                action.v40 = temp
            else:
                v40 = temp 


            temp = get_nested_attribute(action, 'v40')
            if temp is None:
                temp = v40
            if action is not None and hasattr(action, "v41".split('[')[0].split('.')[0]):
                action.v41 = temp
            else:
                v41 = temp 


            temp = get_nested_attribute(action, '"brown"')
            if temp is None:
                temp = "brown"
            if action is not None and hasattr(action, "v42".split('[')[0].split('.')[0]):
                action.v42 = temp
            else:
                v42 = temp 


            temp = get_nested_attribute(action, 'v42')
            if temp is None:
                temp = v42
            if action is not None and hasattr(action, "v43".split('[')[0].split('.')[0]):
                action.v43 = temp
            else:
                v43 = temp 


            temp = get_nested_attribute(action, 'v43')
            if temp is None:
                temp = v43
            if action is not None and hasattr(action, "v44".split('[')[0].split('.')[0]):
                action.v44 = temp
            else:
                v44 = temp 


            if action is not None:
                action.v36.length = v41
                action.v36.fill = v44
            else:
                v36.length = v41
                v36.fill = v44

            temp = get_nested_attribute(action, 'v36')
            if temp is None:
                temp = v36
            if action is not None and hasattr(action, "stick".split('[')[0].split('.')[0]):
                action.stick = temp
            else:
                stick = temp 
            if model is not None: 
                model.stick = stick
                model.last_stick = copy.deepcopy(stick)

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
            new_model = Base()

            self.copyAttributesTo(new_model)
            return new_model       

    #################################################################
    #################################################################
    ## Model
    #################################################################
    class Tower(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self

            if model is not None:
                model_backup = model
                v45 = Base() # this makes model = None in the end!
                model = model_backup
                model.add_object(v45) # add object to model
            else:
                v45 = Base(root = root, view = last_view)
              

            temp = get_nested_attribute(action, 'v45')
            if temp is None:
                temp = v45
            if action is not None and hasattr(action, "v46".split('[')[0].split('.')[0]):
                action.v46 = temp
            else:
                v46 = temp 


            temp = get_nested_attribute(action, 'v46')
            if temp is None:
                temp = v46
            if action is not None and hasattr(action, "base".split('[')[0].split('.')[0]):
                action.base = temp
            else:
                base = temp 
            if model is not None: 
                model.base = base
                model.last_base = copy.deepcopy(base)

            temp = get_nested_attribute(action, '3')
            if temp is None:
                temp = 3
            if action is not None and hasattr(action, "v47".split('[')[0].split('.')[0]):
                action.v47 = temp
            else:
                v47 = temp 


            temp = get_nested_attribute(action, 'v47')
            if temp is None:
                temp = v47
            if action is not None and hasattr(action, "v48".split('[')[0].split('.')[0]):
                action.v48 = temp
            else:
                v48 = temp 


            temp = get_nested_attribute(action, 'v48')
            if temp is None:
                temp = v48
            if action is not None and hasattr(action, "v49".split('[')[0].split('.')[0]):
                action.v49 = temp
            else:
                v49 = temp 


            temp = get_nested_attribute(action, 'v49')
            if temp is None:
                temp = v49
            if action is not None and hasattr(action, "numberOfDisks".split('[')[0].split('.')[0]):
                action.numberOfDisks = temp
            else:
                numberOfDisks = temp 
            if model is not None: 
                model.numberOfDisks = numberOfDisks
                model.last_numberOfDisks = copy.deepcopy(numberOfDisks)

            if model is not None:
                model_backup = model
                v55 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v55) # add object to model
            else:
                v55 = Disk(root = root, view = last_view)
              

            temp = get_nested_attribute(action, 'v55')
            if temp is None:
                temp = v55
            if action is not None and hasattr(action, "v56".split('[')[0].split('.')[0]):
                action.v56 = temp
            else:
                v56 = temp 


            temp = get_nested_attribute(action, 'v56')
            if temp is None:
                temp = v56
            if action is not None and hasattr(action, "disk3".split('[')[0].split('.')[0]):
                action.disk3 = temp
            else:
                disk3 = temp 
            if model is not None: 
                model.disk3 = disk3
                model.last_disk3 = copy.deepcopy(disk3)

            temp = get_nested_attribute(action, '3')
            if temp is None:
                temp = 3
            if action is not None and hasattr(action, "v57".split('[')[0].split('.')[0]):
                action.v57 = temp
            else:
                v57 = temp 


            temp = get_nested_attribute(action, 'v57')
            if temp is None:
                temp = v57
            if action is not None and hasattr(action, "v58".split('[')[0].split('.')[0]):
                action.v58 = temp
            else:
                v58 = temp 


            temp = get_nested_attribute(action, 'v58')
            if temp is None:
                temp = v58
            if action is not None and hasattr(action, "disk3.size".split('[')[0].split('.')[0]):
                action.disk3.size = temp
            else:
                disk3.size = temp 


            if model is not None:
                model_backup = model
                v59 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v59) # add object to model
            else:
                v59 = Disk(root = root, view = last_view)
              

            temp = get_nested_attribute(action, 'v59')
            if temp is None:
                temp = v59
            if action is not None and hasattr(action, "v60".split('[')[0].split('.')[0]):
                action.v60 = temp
            else:
                v60 = temp 


            temp = get_nested_attribute(action, 'v60')
            if temp is None:
                temp = v60
            if action is not None and hasattr(action, "disk2".split('[')[0].split('.')[0]):
                action.disk2 = temp
            else:
                disk2 = temp 
            if model is not None: 
                model.disk2 = disk2
                model.last_disk2 = copy.deepcopy(disk2)

            temp = get_nested_attribute(action, '2')
            if temp is None:
                temp = 2
            if action is not None and hasattr(action, "v61".split('[')[0].split('.')[0]):
                action.v61 = temp
            else:
                v61 = temp 


            temp = get_nested_attribute(action, 'v61')
            if temp is None:
                temp = v61
            if action is not None and hasattr(action, "v62".split('[')[0].split('.')[0]):
                action.v62 = temp
            else:
                v62 = temp 


            temp = get_nested_attribute(action, 'v62')
            if temp is None:
                temp = v62
            if action is not None and hasattr(action, "disk2.size".split('[')[0].split('.')[0]):
                action.disk2.size = temp
            else:
                disk2.size = temp 


            if model is not None:
                model_backup = model
                v63 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v63) # add object to model
            else:
                v63 = Disk(root = root, view = last_view)
              

            temp = get_nested_attribute(action, 'v63')
            if temp is None:
                temp = v63
            if action is not None and hasattr(action, "v64".split('[')[0].split('.')[0]):
                action.v64 = temp
            else:
                v64 = temp 


            temp = get_nested_attribute(action, 'v64')
            if temp is None:
                temp = v64
            if action is not None and hasattr(action, "disk1".split('[')[0].split('.')[0]):
                action.disk1 = temp
            else:
                disk1 = temp 
            if model is not None: 
                model.disk1 = disk1
                model.last_disk1 = copy.deepcopy(disk1)

            temp = get_nested_attribute(action, 'disk3')
            if temp is None:
                temp = disk3
            if action is not None and hasattr(action, "v66".split('[')[0].split('.')[0]):
                action.v66 = temp
            else:
                v66 = temp 


            temp = get_nested_attribute(action, 'disk2')
            if temp is None:
                temp = disk2
            if action is not None and hasattr(action, "v67".split('[')[0].split('.')[0]):
                action.v67 = temp
            else:
                v67 = temp 


            temp = get_nested_attribute(action, 'disk1')
            if temp is None:
                temp = disk1
            if action is not None and hasattr(action, "v68".split('[')[0].split('.')[0]):
                action.v68 = temp
            else:
                v68 = temp 

            v65 = [v66,v67,v68]

            temp = get_nested_attribute(action, 'v65')
            if temp is None:
                temp = v65
            if action is not None and hasattr(action, "v69".split('[')[0].split('.')[0]):
                action.v69 = temp
            else:
                v69 = temp 


            temp = get_nested_attribute(action, 'v69')
            if temp is None:
                temp = v69
            if action is not None and hasattr(action, "v70".split('[')[0].split('.')[0]):
                action.v70 = temp
            else:
                v70 = temp 


            temp = get_nested_attribute(action, 'v70')
            if temp is None:
                temp = v70
            if action is not None and hasattr(action, "disks".split('[')[0].split('.')[0]):
                action.disks = temp
            else:
                disks = temp 
            if model is not None: 
                model.disks = disks
                model.last_disks = copy.deepcopy(disks)

            temp = get_nested_attribute(action, 'False')
            if temp is None:
                temp = False
            if action is not None and hasattr(action, "v85".split('[')[0].split('.')[0]):
                action.v85 = temp
            else:
                v85 = temp 


            temp = get_nested_attribute(action, 'v85')
            if temp is None:
                temp = v85
            if action is not None and hasattr(action, "v86".split('[')[0].split('.')[0]):
                action.v86 = temp
            else:
                v86 = temp 


            temp = get_nested_attribute(action, 'v86')
            if temp is None:
                temp = v86
            if action is not None and hasattr(action, "v87".split('[')[0].split('.')[0]):
                action.v87 = temp
            else:
                v87 = temp 


            temp = get_nested_attribute(action, 'v87')
            if temp is None:
                temp = v87
            if action is not None and hasattr(action, "active".split('[')[0].split('.')[0]):
                action.active = temp
            else:
                active = temp 
            if model is not None: 
                model.active = active
                model.last_active = copy.deepcopy(active)

            self.fixCoords()

        def create_object(self, view):
            action = self

            if self.numberOfDisks != self.last_numberOfDisks:

                temp = get_nested_attribute(action, 'numberOfDisks')
                if temp is None:
                    temp = numberOfDisks
                if action is not None and hasattr(action, "v50".split('[')[0].split('.')[0]):
                    action.v50 = temp
                else:
                    v50 = temp 


                temp = get_nested_attribute(action, '3')
                if temp is None:
                    temp = 3
                if action is not None and hasattr(action, "v51".split('[')[0].split('.')[0]):
                    action.v51 = temp
                else:
                    v51 = temp 

                for d in range(v50, v51, 1):

                    temp = get_nested_attribute(action, '"hidden"')
                    if temp is None:
                        temp = "hidden"
                    if action is not None and hasattr(action, "v52".split('[')[0].split('.')[0]):
                        action.v52 = temp
                    else:
                        v52 = temp 


                    temp = get_nested_attribute(action, 'v52')
                    if temp is None:
                        temp = v52
                    if action is not None and hasattr(action, "v53".split('[')[0].split('.')[0]):
                        action.v53 = temp
                    else:
                        v53 = temp 


                    temp = get_nested_attribute(action, 'd')
                    if temp is None:
                        temp = d
                    if action is not None and hasattr(action, "v54".split('[')[0].split('.')[0]):
                        action.v54 = temp
                    else:
                        v54 = temp 


                    temp = get_nested_attribute(action, 'v53')
                    if temp is None:
                        temp = v53
                    if action is not None and hasattr(action, "disks[v54].state".split('[')[0].split('.')[0]):
                        action.disks[v54].state = temp
                    else:
                        disks[v54].state = temp 

                self.last_numberOfDisks = copy.deepcopy(self.numberOfDisks)


            if self.disks != self.last_disks:

                temp = get_nested_attribute(action, '0')
                if temp is None:
                    temp = 0
                if action is not None and hasattr(action, "v71".split('[')[0].split('.')[0]):
                    action.v71 = temp
                else:
                    v71 = temp 


                temp = get_nested_attribute(action, 'numberOfDisks')
                if temp is None:
                    temp = numberOfDisks
                if action is not None and hasattr(action, "v72".split('[')[0].split('.')[0]):
                    action.v72 = temp
                else:
                    v72 = temp 

                for d in range(v71, v72, 1):

                    temp = get_nested_attribute(action, 'd')
                    if temp is None:
                        temp = d
                    if action is not None and hasattr(action, "v73".split('[')[0].split('.')[0]):
                        action.v73 = temp
                    else:
                        v73 = temp 


                    temp = get_nested_attribute(action, '0')
                    if temp is None:
                        temp = 0
                    if action is not None and hasattr(action, "v75".split('[')[0].split('.')[0]):
                        action.v75 = temp
                    else:
                        v75 = temp 


                    temp = get_nested_attribute(action, 'd')
                    if temp is None:
                        temp = d
                    if action is not None and hasattr(action, "v79".split('[')[0].split('.')[0]):
                        action.v79 = temp
                    else:
                        v79 = temp 


                    temp = get_nested_attribute(action, '1')
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v80".split('[')[0].split('.')[0]):
                        action.v80 = temp
                    else:
                        v80 = temp 

                    v78 = np.array(v79) + np.array(v80); v78 = tuple(v78) if isinstance(v78, np.ndarray) else v78

                    temp = get_nested_attribute(action, '30')
                    if temp is None:
                        temp = 30
                    if action is not None and hasattr(action, "v81".split('[')[0].split('.')[0]):
                        action.v81 = temp
                    else:
                        v81 = temp 

                    v77 = np.dot(np.array(v78) , np.array(v81)); v77 = tuple(v77) if isinstance(v77, np.ndarray) else v77

                    temp = get_nested_attribute(action, '45')
                    if temp is None:
                        temp = 45
                    if action is not None and hasattr(action, "v82".split('[')[0].split('.')[0]):
                        action.v82 = temp
                    else:
                        v82 = temp 

                    v76 = np.array(v77) - np.array(v82); v76 = tuple(v76) if isinstance(v76, np.ndarray) else v76
                    v74 = (v75 , v76); v74 = tuple(v74) if isinstance(v74, np.ndarray) else v74
                    if action is not None:
                        action.disks[v73].wood.move_absolute(v74)
                    else:
                        disks[v73].wood.move_absolute(v74)

                    temp = get_nested_attribute(action, '0', locals())
                    if temp is None:
                        temp = 0
                    if action is not None and hasattr(action, "v84".split('[')[0].split('.')[0]):
                        action.v84 = temp
                    else:
                        v84 = temp 


                    temp = get_nested_attribute(action, 'base.stick.origin[v84]', locals())
                    if temp is None:
                        temp = base.stick.origin[v84]
                    if action is not None and hasattr(action, "v83".split('[')[0].split('.')[0]):
                        action.v83 = temp
                    else:
                        v83 = temp 

                    print(v83)
                self.last_disks = copy.deepcopy(self.disks)


            if self.active != self.last_active:

                temp = get_nested_attribute(action, 'active')
                if temp is None:
                    temp = active
                if action is not None and hasattr(action, "v88".split('[')[0].split('.')[0]):
                    action.v88 = temp
                else:
                    v88 = temp 

                if v88:

                    temp = get_nested_attribute(action, '"green"')
                    if temp is None:
                        temp = "green"
                    if action is not None and hasattr(action, "v89".split('[')[0].split('.')[0]):
                        action.v89 = temp
                    else:
                        v89 = temp 


                    temp = get_nested_attribute(action, 'v89')
                    if temp is None:
                        temp = v89
                    if action is not None and hasattr(action, "v90".split('[')[0].split('.')[0]):
                        action.v90 = temp
                    else:
                        v90 = temp 


                    temp = get_nested_attribute(action, 'numberOfDisks')
                    if temp is None:
                        temp = numberOfDisks
                    if action is not None and hasattr(action, "v92".split('[')[0].split('.')[0]):
                        action.v92 = temp
                    else:
                        v92 = temp 


                    temp = get_nested_attribute(action, '1')
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v93".split('[')[0].split('.')[0]):
                        action.v93 = temp
                    else:
                        v93 = temp 

                    v91 = np.array(v92) - np.array(v93); v91 = tuple(v91) if isinstance(v91, np.ndarray) else v91

                    temp = get_nested_attribute(action, 'v90')
                    if temp is None:
                        temp = v90
                    if action is not None and hasattr(action, "disks[v91].wood.fill".split('[')[0].split('.')[0]):
                        action.disks[v91].wood.fill = temp
                    else:
                        disks[v91].wood.fill = temp 
                    
                else:

                    temp = get_nested_attribute(action, '"brown"')
                    if temp is None:
                        temp = "brown"
                    if action is not None and hasattr(action, "v94".split('[')[0].split('.')[0]):
                        action.v94 = temp
                    else:
                        v94 = temp 


                    temp = get_nested_attribute(action, 'v94')
                    if temp is None:
                        temp = v94
                    if action is not None and hasattr(action, "v95".split('[')[0].split('.')[0]):
                        action.v95 = temp
                    else:
                        v95 = temp 


                    temp = get_nested_attribute(action, 'numberOfDisks')
                    if temp is None:
                        temp = numberOfDisks
                    if action is not None and hasattr(action, "v97".split('[')[0].split('.')[0]):
                        action.v97 = temp
                    else:
                        v97 = temp 


                    temp = get_nested_attribute(action, '1')
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v98".split('[')[0].split('.')[0]):
                        action.v98 = temp
                    else:
                        v98 = temp 

                    v96 = np.array(v97) - np.array(v98); v96 = tuple(v96) if isinstance(v96, np.ndarray) else v96

                    temp = get_nested_attribute(action, 'v95')
                    if temp is None:
                        temp = v95
                    if action is not None and hasattr(action, "disks[v96].wood.fill".split('[')[0].split('.')[0]):
                        action.disks[v96].wood.fill = temp
                    else:
                        disks[v96].wood.fill = temp 

                    
                self.last_active = copy.deepcopy(self.active)
        
            action = None
            super().create_object(view)
            model = None

        def __deepcopy__(self, memo=None):
            """Create a deep copy of the model."""
            if memo is None:
                memo = {} # this is required by the deepcopy protocol
            new_model = Tower()

            self.copyAttributesTo(new_model)
            return new_model       

    #################################################################

    if model is not None:
        v99 = View()
        model.add_object(v99) # add object to model
    else:
        v99 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v99

    temp = get_nested_attribute(action, '500')
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v100".split('[')[0].split('.')[0]):
        action.v100 = temp
    else:
        v100 = temp 


    temp = get_nested_attribute(action, 'v100')
    if temp is None:
        temp = v100
    if action is not None and hasattr(action, "v101".split('[')[0].split('.')[0]):
        action.v101 = temp
    else:
        v101 = temp 


    temp = get_nested_attribute(action, 'v101')
    if temp is None:
        temp = v101
    if action is not None and hasattr(action, "v102".split('[')[0].split('.')[0]):
        action.v102 = temp
    else:
        v102 = temp 


    temp = get_nested_attribute(action, '500')
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v103".split('[')[0].split('.')[0]):
        action.v103 = temp
    else:
        v103 = temp 


    temp = get_nested_attribute(action, 'v103')
    if temp is None:
        temp = v103
    if action is not None and hasattr(action, "v104".split('[')[0].split('.')[0]):
        action.v104 = temp
    else:
        v104 = temp 


    temp = get_nested_attribute(action, 'v104')
    if temp is None:
        temp = v104
    if action is not None and hasattr(action, "v105".split('[')[0].split('.')[0]):
        action.v105 = temp
    else:
        v105 = temp 


    temp = get_nested_attribute(action, '"Tower 1"')
    if temp is None:
        temp = "Tower 1"
    if action is not None and hasattr(action, "v106".split('[')[0].split('.')[0]):
        action.v106 = temp
    else:
        v106 = temp 


    temp = get_nested_attribute(action, 'v106')
    if temp is None:
        temp = v106
    if action is not None and hasattr(action, "v107".split('[')[0].split('.')[0]):
        action.v107 = temp
    else:
        v107 = temp 


    temp = get_nested_attribute(action, 'v107')
    if temp is None:
        temp = v107
    if action is not None and hasattr(action, "v108".split('[')[0].split('.')[0]):
        action.v108 = temp
    else:
        v108 = temp 


    temp = get_nested_attribute(action, '"wheat"')
    if temp is None:
        temp = "wheat"
    if action is not None and hasattr(action, "v109".split('[')[0].split('.')[0]):
        action.v109 = temp
    else:
        v109 = temp 


    temp = get_nested_attribute(action, 'v109')
    if temp is None:
        temp = v109
    if action is not None and hasattr(action, "v110".split('[')[0].split('.')[0]):
        action.v110 = temp
    else:
        v110 = temp 


    temp = get_nested_attribute(action, 'v110')
    if temp is None:
        temp = v110
    if action is not None and hasattr(action, "v111".split('[')[0].split('.')[0]):
        action.v111 = temp
    else:
        v111 = temp 


    if action is not None:
        action.v99.width = v102
        action.v99.height = v105
        action.v99.title = v108
        action.v99.background = v111
    else:
        v99.width = v102
        v99.height = v105
        v99.title = v108
        v99.background = v111

    temp = get_nested_attribute(action, 'v99')
    if temp is None:
        temp = v99
    if action is not None and hasattr(action, "view1".split('[')[0].split('.')[0]):
        action.view1 = temp
    else:
        view1 = temp 
    if model is not None: 
        model.view1 = view1
        model.last_view1 = copy.deepcopy(view1)

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v114".split('[')[0].split('.')[0]):
        action.v114 = temp
    else:
        v114 = temp 


    temp = get_nested_attribute(action, '50')
    if temp is None:
        temp = 50
    if action is not None and hasattr(action, "v115".split('[')[0].split('.')[0]):
        action.v115 = temp
    else:
        v115 = temp 

    v116 = - np.array(v115)
    v113 = (v114 , v116); v113 = tuple(v113) if isinstance(v113, np.ndarray) else v113

    if model is not None:
        model_backup = model
        v112 = Tower() # this makes model = None in the end!
        model = model_backup
        model.add_object(v112) # add object to model
    else:
        v112 = Tower(root = root, view = last_view)
    v112.move_absolute(v113)  

    temp = get_nested_attribute(action, 'v112')
    if temp is None:
        temp = v112
    if action is not None and hasattr(action, "v117".split('[')[0].split('.')[0]):
        action.v117 = temp
    else:
        v117 = temp 


    temp = get_nested_attribute(action, 'v117')
    if temp is None:
        temp = v117
    if action is not None and hasattr(action, "tower1".split('[')[0].split('.')[0]):
        action.tower1 = temp
    else:
        tower1 = temp 
    if model is not None: 
        model.tower1 = tower1
        model.last_tower1 = copy.deepcopy(tower1)

    if model is not None:
        v118 = View()
        model.add_object(v118) # add object to model
    else:
        v118 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v118

    temp = get_nested_attribute(action, '501')
    if temp is None:
        temp = 501
    if action is not None and hasattr(action, "v119".split('[')[0].split('.')[0]):
        action.v119 = temp
    else:
        v119 = temp 


    temp = get_nested_attribute(action, 'v119')
    if temp is None:
        temp = v119
    if action is not None and hasattr(action, "v120".split('[')[0].split('.')[0]):
        action.v120 = temp
    else:
        v120 = temp 


    temp = get_nested_attribute(action, 'v120')
    if temp is None:
        temp = v120
    if action is not None and hasattr(action, "v121".split('[')[0].split('.')[0]):
        action.v121 = temp
    else:
        v121 = temp 


    temp = get_nested_attribute(action, '500')
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v122".split('[')[0].split('.')[0]):
        action.v122 = temp
    else:
        v122 = temp 


    temp = get_nested_attribute(action, 'v122')
    if temp is None:
        temp = v122
    if action is not None and hasattr(action, "v123".split('[')[0].split('.')[0]):
        action.v123 = temp
    else:
        v123 = temp 


    temp = get_nested_attribute(action, 'v123')
    if temp is None:
        temp = v123
    if action is not None and hasattr(action, "v124".split('[')[0].split('.')[0]):
        action.v124 = temp
    else:
        v124 = temp 


    temp = get_nested_attribute(action, '500')
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v125".split('[')[0].split('.')[0]):
        action.v125 = temp
    else:
        v125 = temp 


    temp = get_nested_attribute(action, 'v125')
    if temp is None:
        temp = v125
    if action is not None and hasattr(action, "v126".split('[')[0].split('.')[0]):
        action.v126 = temp
    else:
        v126 = temp 


    temp = get_nested_attribute(action, 'v126')
    if temp is None:
        temp = v126
    if action is not None and hasattr(action, "v127".split('[')[0].split('.')[0]):
        action.v127 = temp
    else:
        v127 = temp 


    temp = get_nested_attribute(action, '"Tower 2"')
    if temp is None:
        temp = "Tower 2"
    if action is not None and hasattr(action, "v128".split('[')[0].split('.')[0]):
        action.v128 = temp
    else:
        v128 = temp 


    temp = get_nested_attribute(action, 'v128')
    if temp is None:
        temp = v128
    if action is not None and hasattr(action, "v129".split('[')[0].split('.')[0]):
        action.v129 = temp
    else:
        v129 = temp 


    temp = get_nested_attribute(action, 'v129')
    if temp is None:
        temp = v129
    if action is not None and hasattr(action, "v130".split('[')[0].split('.')[0]):
        action.v130 = temp
    else:
        v130 = temp 


    temp = get_nested_attribute(action, '"wheat"')
    if temp is None:
        temp = "wheat"
    if action is not None and hasattr(action, "v131".split('[')[0].split('.')[0]):
        action.v131 = temp
    else:
        v131 = temp 


    temp = get_nested_attribute(action, 'v131')
    if temp is None:
        temp = v131
    if action is not None and hasattr(action, "v132".split('[')[0].split('.')[0]):
        action.v132 = temp
    else:
        v132 = temp 


    temp = get_nested_attribute(action, 'v132')
    if temp is None:
        temp = v132
    if action is not None and hasattr(action, "v133".split('[')[0].split('.')[0]):
        action.v133 = temp
    else:
        v133 = temp 


    if action is not None:
        action.v118.Ox = v121
        action.v118.width = v124
        action.v118.height = v127
        action.v118.title = v130
        action.v118.background = v133
    else:
        v118.Ox = v121
        v118.width = v124
        v118.height = v127
        v118.title = v130
        v118.background = v133

    temp = get_nested_attribute(action, 'v118')
    if temp is None:
        temp = v118
    if action is not None and hasattr(action, "view2".split('[')[0].split('.')[0]):
        action.view2 = temp
    else:
        view2 = temp 
    if model is not None: 
        model.view2 = view2
        model.last_view2 = copy.deepcopy(view2)

    temp = get_nested_attribute(action, '501')
    if temp is None:
        temp = 501
    if action is not None and hasattr(action, "v136".split('[')[0].split('.')[0]):
        action.v136 = temp
    else:
        v136 = temp 


    temp = get_nested_attribute(action, '50')
    if temp is None:
        temp = 50
    if action is not None and hasattr(action, "v137".split('[')[0].split('.')[0]):
        action.v137 = temp
    else:
        v137 = temp 

    v138 = - np.array(v137)
    v135 = (v136 , v138); v135 = tuple(v135) if isinstance(v135, np.ndarray) else v135

    if model is not None:
        model_backup = model
        v134 = Tower() # this makes model = None in the end!
        model = model_backup
        model.add_object(v134) # add object to model
    else:
        v134 = Tower(root = root, view = last_view)
    v134.move_absolute(v135)  

    temp = get_nested_attribute(action, 'v134')
    if temp is None:
        temp = v134
    if action is not None and hasattr(action, "v139".split('[')[0].split('.')[0]):
        action.v139 = temp
    else:
        v139 = temp 


    temp = get_nested_attribute(action, 'v139')
    if temp is None:
        temp = v139
    if action is not None and hasattr(action, "tower2".split('[')[0].split('.')[0]):
        action.tower2 = temp
    else:
        tower2 = temp 
    if model is not None: 
        model.tower2 = tower2
        model.last_tower2 = copy.deepcopy(tower2)

    last_refresh = time.time()
    view2.update()

    last_refresh = time.time()
    view1.update()

    if action is not None:
        v140 = action.view.waitClick()
    else:
        v140 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v140')
    if temp is None:
        temp = v140
    if action is not None and hasattr(action, "v141".split('[')[0].split('.')[0]):
        action.v141 = temp
    else:
        v141 = temp 


    temp = get_nested_attribute(action, 'v141')
    if temp is None:
        temp = v141
    if action is not None and hasattr(action, "v142".split('[')[0].split('.')[0]):
        action.v142 = temp
    else:
        v142 = temp 


    temp = get_nested_attribute(action, 'v142')
    if temp is None:
        temp = v142
    if action is not None and hasattr(action, "p".split('[')[0].split('.')[0]):
        action.p = temp
    else:
        p = temp 
    if model is not None: 
        model.p = p
        model.last_p = copy.deepcopy(p)

    temp = get_nested_attribute(action, 'p')
    if temp is None:
        temp = p
    if action is not None and hasattr(action, "v143".split('[')[0].split('.')[0]):
        action.v143 = temp
    else:
        v143 = temp 

    print(v143)

    temp = get_nested_attribute(action, 'True')
    if temp is None:
        temp = True
    if action is not None and hasattr(action, "v144".split('[')[0].split('.')[0]):
        action.v144 = temp
    else:
        v144 = temp 


    temp = get_nested_attribute(action, 'v144')
    if temp is None:
        temp = v144
    if action is not None and hasattr(action, "v145".split('[')[0].split('.')[0]):
        action.v145 = temp
    else:
        v145 = temp 


    temp = get_nested_attribute(action, 'v145')
    if temp is None:
        temp = v145
    if action is not None and hasattr(action, "tower1.active".split('[')[0].split('.')[0]):
        action.tower1.active = temp
    else:
        tower1.active = temp 

    last_refresh = time.time()
    view1.update()

    if action is not None:
        v146 = action.view.waitClick()
    else:
        v146 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v146')
    if temp is None:
        temp = v146
    if action is not None and hasattr(action, "v147".split('[')[0].split('.')[0]):
        action.v147 = temp
    else:
        v147 = temp 


    temp = get_nested_attribute(action, 'v147')
    if temp is None:
        temp = v147
    if action is not None and hasattr(action, "p".split('[')[0].split('.')[0]):
        action.p = temp
    else:
        p = temp 


    temp = get_nested_attribute(action, 'tower1.numberOfDisks')
    if temp is None:
        temp = tower1.numberOfDisks
    if action is not None and hasattr(action, "v149".split('[')[0].split('.')[0]):
        action.v149 = temp
    else:
        v149 = temp 


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v150".split('[')[0].split('.')[0]):
        action.v150 = temp
    else:
        v150 = temp 

    v148 = np.array(v149) - np.array(v150); v148 = tuple(v148) if isinstance(v148, np.ndarray) else v148

    temp = get_nested_attribute(action, 'v148')
    if temp is None:
        temp = v148
    if action is not None and hasattr(action, "v151".split('[')[0].split('.')[0]):
        action.v151 = temp
    else:
        v151 = temp 


    temp = get_nested_attribute(action, 'v151')
    if temp is None:
        temp = v151
    if action is not None and hasattr(action, "tower1.numberOfDisks".split('[')[0].split('.')[0]):
        action.tower1.numberOfDisks = temp
    else:
        tower1.numberOfDisks = temp 

    last_refresh = time.time()
    view1.update()

    if action is not None:
        v152 = action.view.waitClick()
    else:
        v152 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v152')
    if temp is None:
        temp = v152
    if action is not None and hasattr(action, "v153".split('[')[0].split('.')[0]):
        action.v153 = temp
    else:
        v153 = temp 


    temp = get_nested_attribute(action, 'v153')
    if temp is None:
        temp = v153
    if action is not None and hasattr(action, "p".split('[')[0].split('.')[0]):
        action.p = temp
    else:
        p = temp 


    temp = get_nested_attribute(action, 'tower1.numberOfDisks')
    if temp is None:
        temp = tower1.numberOfDisks
    if action is not None and hasattr(action, "v155".split('[')[0].split('.')[0]):
        action.v155 = temp
    else:
        v155 = temp 


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v156".split('[')[0].split('.')[0]):
        action.v156 = temp
    else:
        v156 = temp 

    v154 = np.array(v155) - np.array(v156); v154 = tuple(v154) if isinstance(v154, np.ndarray) else v154

    temp = get_nested_attribute(action, 'v154')
    if temp is None:
        temp = v154
    if action is not None and hasattr(action, "v157".split('[')[0].split('.')[0]):
        action.v157 = temp
    else:
        v157 = temp 


    temp = get_nested_attribute(action, 'v157')
    if temp is None:
        temp = v157
    if action is not None and hasattr(action, "tower1.numberOfDisks".split('[')[0].split('.')[0]):
        action.tower1.numberOfDisks = temp
    else:
        tower1.numberOfDisks = temp 

    last_refresh = time.time()
    view1.update()

    if action is not None:
        v158 = action.view.waitClick()
    else:
        v158 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v158')
    if temp is None:
        temp = v158
    if action is not None and hasattr(action, "v159".split('[')[0].split('.')[0]):
        action.v159 = temp
    else:
        v159 = temp 


    temp = get_nested_attribute(action, 'v159')
    if temp is None:
        temp = v159
    if action is not None and hasattr(action, "p".split('[')[0].split('.')[0]):
        action.p = temp
    else:
        p = temp 

    view1.close(); views.remove(view1) if last_view != view1 else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == view1 else last_view
