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
def get_nested_attribute(obj, attr_path, local_dict):
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
        return get_nested_attribute(obj, attr_path, local_dict) 
    else:
        return obj
#################################################################

if __name__ == "__main__":
    root = Root(views, last_view)

    #################################################################
    ## Model
    #################################################################
    class Disk(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '1', locals())
            if temp is None:
                temp = 1
            if action is not None and hasattr(action, "v0".split('[')[0].split('.')[0]):
                action.v0 = temp
            else:
                v0 = temp 


            temp = get_nested_attribute(action, 'v0', locals())
            if temp is None:
                temp = v0
            if action is not None and hasattr(action, "v1".split('[')[0].split('.')[0]):
                action.v1 = temp
            else:
                v1 = temp 


            temp = get_nested_attribute(action, 'v1', locals())
            if temp is None:
                temp = v1
            if action is not None and hasattr(action, "v2".split('[')[0].split('.')[0]):
                action.v2 = temp
            else:
                v2 = temp 


            temp = get_nested_attribute(action, 'v2', locals())
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

            temp = get_nested_attribute(action, '75', locals())
            if temp is None:
                temp = 75
            if action is not None and hasattr(action, "v13".split('[')[0].split('.')[0]):
                action.v13 = temp
            else:
                v13 = temp 


            temp = get_nested_attribute(action, '15', locals())
            if temp is None:
                temp = 15
            if action is not None and hasattr(action, "v14".split('[')[0].split('.')[0]):
                action.v14 = temp
            else:
                v14 = temp 

            v12 = (v13 , v14); v12 = tuple(v12) if isinstance(v12, np.ndarray) else v12

            temp = get_nested_attribute(action, 'v12', locals())
            if temp is None:
                temp = v12
            if action is not None and hasattr(action, "v15".split('[')[0].split('.')[0]):
                action.v15 = temp
            else:
                v15 = temp 


            temp = get_nested_attribute(action, 'v15', locals())
            if temp is None:
                temp = v15
            if action is not None and hasattr(action, "v16".split('[')[0].split('.')[0]):
                action.v16 = temp
            else:
                v16 = temp 


            temp = get_nested_attribute(action, '"brown"', locals())
            if temp is None:
                temp = "brown"
            if action is not None and hasattr(action, "v17".split('[')[0].split('.')[0]):
                action.v17 = temp
            else:
                v17 = temp 


            temp = get_nested_attribute(action, 'v17', locals())
            if temp is None:
                temp = v17
            if action is not None and hasattr(action, "v18".split('[')[0].split('.')[0]):
                action.v18 = temp
            else:
                v18 = temp 


            temp = get_nested_attribute(action, 'v18', locals())
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

            temp = get_nested_attribute(action, 'v11', locals())
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

                temp = get_nested_attribute(action, '50', locals())
                if temp is None:
                    temp = 50
                if action is not None and hasattr(action, "v5".split('[')[0].split('.')[0]):
                    action.v5 = temp
                else:
                    v5 = temp 


                temp = get_nested_attribute(action, '25', locals())
                if temp is None:
                    temp = 25
                if action is not None and hasattr(action, "v7".split('[')[0].split('.')[0]):
                    action.v7 = temp
                else:
                    v7 = temp 


                temp = get_nested_attribute(action, 'size', locals())
                if temp is None:
                    temp = size
                if action is not None and hasattr(action, "v8".split('[')[0].split('.')[0]):
                    action.v8 = temp
                else:
                    v8 = temp 

                v6 = np.dot(np.array(v7) , np.array(v8)); v6 = tuple(v6) if isinstance(v6, np.ndarray) else v6
                v4 = np.array(v5) + np.array(v6); v4 = tuple(v4) if isinstance(v4, np.ndarray) else v4

                temp = get_nested_attribute(action, '15', locals())
                if temp is None:
                    temp = 15
                if action is not None and hasattr(action, "v9".split('[')[0].split('.')[0]):
                    action.v9 = temp
                else:
                    v9 = temp 

                v3 = (v4 , v9); v3 = tuple(v3) if isinstance(v3, np.ndarray) else v3

                temp = get_nested_attribute(action, 'v3', locals())
                if temp is None:
                    temp = v3
                if action is not None and hasattr(action, "v10".split('[')[0].split('.')[0]):
                    action.v10 = temp
                else:
                    v10 = temp 


                temp = get_nested_attribute(action, 'v10', locals())
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

            temp = get_nested_attribute(action, '200', locals())
            if temp is None:
                temp = 200
            if action is not None and hasattr(action, "v22".split('[')[0].split('.')[0]):
                action.v22 = temp
            else:
                v22 = temp 


            temp = get_nested_attribute(action, '20', locals())
            if temp is None:
                temp = 20
            if action is not None and hasattr(action, "v23".split('[')[0].split('.')[0]):
                action.v23 = temp
            else:
                v23 = temp 

            v21 = (v22 , v23); v21 = tuple(v21) if isinstance(v21, np.ndarray) else v21

            temp = get_nested_attribute(action, 'v21', locals())
            if temp is None:
                temp = v21
            if action is not None and hasattr(action, "v24".split('[')[0].split('.')[0]):
                action.v24 = temp
            else:
                v24 = temp 


            temp = get_nested_attribute(action, 'v24', locals())
            if temp is None:
                temp = v24
            if action is not None and hasattr(action, "v25".split('[')[0].split('.')[0]):
                action.v25 = temp
            else:
                v25 = temp 


            temp = get_nested_attribute(action, '"brown"', locals())
            if temp is None:
                temp = "brown"
            if action is not None and hasattr(action, "v26".split('[')[0].split('.')[0]):
                action.v26 = temp
            else:
                v26 = temp 


            temp = get_nested_attribute(action, 'v26', locals())
            if temp is None:
                temp = v26
            if action is not None and hasattr(action, "v27".split('[')[0].split('.')[0]):
                action.v27 = temp
            else:
                v27 = temp 


            temp = get_nested_attribute(action, 'v27', locals())
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

            temp = get_nested_attribute(action, 'v20', locals())
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

            temp = get_nested_attribute(action, '"Base"', locals())
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


            temp = get_nested_attribute(action, 'v31', locals())
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

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v34".split('[')[0].split('.')[0]):
                action.v34 = temp
            else:
                v34 = temp 


            temp = get_nested_attribute(action, '120', locals())
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

            temp = get_nested_attribute(action, '10', locals())
            if temp is None:
                temp = 10
            if action is not None and hasattr(action, "v38".split('[')[0].split('.')[0]):
                action.v38 = temp
            else:
                v38 = temp 


            temp = get_nested_attribute(action, '100', locals())
            if temp is None:
                temp = 100
            if action is not None and hasattr(action, "v39".split('[')[0].split('.')[0]):
                action.v39 = temp
            else:
                v39 = temp 

            v37 = (v38 , v39); v37 = tuple(v37) if isinstance(v37, np.ndarray) else v37

            temp = get_nested_attribute(action, 'v37', locals())
            if temp is None:
                temp = v37
            if action is not None and hasattr(action, "v40".split('[')[0].split('.')[0]):
                action.v40 = temp
            else:
                v40 = temp 


            temp = get_nested_attribute(action, 'v40', locals())
            if temp is None:
                temp = v40
            if action is not None and hasattr(action, "v41".split('[')[0].split('.')[0]):
                action.v41 = temp
            else:
                v41 = temp 


            temp = get_nested_attribute(action, '"brown"', locals())
            if temp is None:
                temp = "brown"
            if action is not None and hasattr(action, "v42".split('[')[0].split('.')[0]):
                action.v42 = temp
            else:
                v42 = temp 


            temp = get_nested_attribute(action, 'v42', locals())
            if temp is None:
                temp = v42
            if action is not None and hasattr(action, "v43".split('[')[0].split('.')[0]):
                action.v43 = temp
            else:
                v43 = temp 


            temp = get_nested_attribute(action, 'v43', locals())
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

            temp = get_nested_attribute(action, 'v36', locals())
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
              

            temp = get_nested_attribute(action, 'v45', locals())
            if temp is None:
                temp = v45
            if action is not None and hasattr(action, "v46".split('[')[0].split('.')[0]):
                action.v46 = temp
            else:
                v46 = temp 


            temp = get_nested_attribute(action, 'v46', locals())
            if temp is None:
                temp = v46
            if action is not None and hasattr(action, "base".split('[')[0].split('.')[0]):
                action.base = temp
            else:
                base = temp 
            if model is not None: 
                model.base = base
                model.last_base = copy.deepcopy(base)

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v47".split('[')[0].split('.')[0]):
                action.v47 = temp
            else:
                v47 = temp 


            temp = get_nested_attribute(action, 'v47', locals())
            if temp is None:
                temp = v47
            if action is not None and hasattr(action, "v48".split('[')[0].split('.')[0]):
                action.v48 = temp
            else:
                v48 = temp 


            temp = get_nested_attribute(action, 'v48', locals())
            if temp is None:
                temp = v48
            if action is not None and hasattr(action, "v49".split('[')[0].split('.')[0]):
                action.v49 = temp
            else:
                v49 = temp 


            temp = get_nested_attribute(action, 'v49', locals())
            if temp is None:
                temp = v49
            if action is not None and hasattr(action, "numberOfDisks".split('[')[0].split('.')[0]):
                action.numberOfDisks = temp
            else:
                numberOfDisks = temp 
            if model is not None: 
                model.numberOfDisks = numberOfDisks
                model.last_numberOfDisks = copy.deepcopy(numberOfDisks)

            temp = get_nested_attribute(action, 'None', locals())
            if temp is None:
                temp = None
            if action is not None and hasattr(action, "v51".split('[')[0].split('.')[0]):
                action.v51 = temp
            else:
                v51 = temp 

            v50 = [v51]

            temp = get_nested_attribute(action, 'v50', locals())
            if temp is None:
                temp = v50
            if action is not None and hasattr(action, "v52".split('[')[0].split('.')[0]):
                action.v52 = temp
            else:
                v52 = temp 


            temp = get_nested_attribute(action, 'v52', locals())
            if temp is None:
                temp = v52
            if action is not None and hasattr(action, "v53".split('[')[0].split('.')[0]):
                action.v53 = temp
            else:
                v53 = temp 


            temp = get_nested_attribute(action, 'v53', locals())
            if temp is None:
                temp = v53
            if action is not None and hasattr(action, "disks".split('[')[0].split('.')[0]):
                action.disks = temp
            else:
                disks = temp 
            if model is not None: 
                model.disks = disks
                model.last_disks = copy.deepcopy(disks)

            temp = get_nested_attribute(action, 'False', locals())
            if temp is None:
                temp = False
            if action is not None and hasattr(action, "v84".split('[')[0].split('.')[0]):
                action.v84 = temp
            else:
                v84 = temp 


            temp = get_nested_attribute(action, 'v84', locals())
            if temp is None:
                temp = v84
            if action is not None and hasattr(action, "v85".split('[')[0].split('.')[0]):
                action.v85 = temp
            else:
                v85 = temp 


            temp = get_nested_attribute(action, 'v85', locals())
            if temp is None:
                temp = v85
            if action is not None and hasattr(action, "v86".split('[')[0].split('.')[0]):
                action.v86 = temp
            else:
                v86 = temp 


            temp = get_nested_attribute(action, 'v86', locals())
            if temp is None:
                temp = v86
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

            if self.disks != self.last_disks:

                temp = get_nested_attribute(action, '0', locals())
                if temp is None:
                    temp = 0
                if action is not None and hasattr(action, "v54".split('[')[0].split('.')[0]):
                    action.v54 = temp
                else:
                    v54 = temp 


                temp = get_nested_attribute(action, 'numberOfDisks', locals())
                if temp is None:
                    temp = numberOfDisks
                if action is not None and hasattr(action, "v55".split('[')[0].split('.')[0]):
                    action.v55 = temp
                else:
                    v55 = temp 

                for d in range(v54, v55, 1):

                    temp = get_nested_attribute(action, 'd', locals())
                    if temp is None:
                        temp = d
                    if action is not None and hasattr(action, "v56".split('[')[0].split('.')[0]):
                        action.v56 = temp
                    else:
                        v56 = temp 


                    temp = get_nested_attribute(action, '0', locals())
                    if temp is None:
                        temp = 0
                    if action is not None and hasattr(action, "v59".split('[')[0].split('.')[0]):
                        action.v59 = temp
                    else:
                        v59 = temp 


                    temp = get_nested_attribute(action, 'base.origin[v59]', locals())
                    if temp is None:
                        temp = base.origin[v59]
                    if action is not None and hasattr(action, "v58".split('[')[0].split('.')[0]):
                        action.v58 = temp
                    else:
                        v58 = temp 


                    temp = get_nested_attribute(action, 'd', locals())
                    if temp is None:
                        temp = d
                    if action is not None and hasattr(action, "v63".split('[')[0].split('.')[0]):
                        action.v63 = temp
                    else:
                        v63 = temp 


                    temp = get_nested_attribute(action, '1', locals())
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v64".split('[')[0].split('.')[0]):
                        action.v64 = temp
                    else:
                        v64 = temp 

                    v62 = np.array(v63) + np.array(v64); v62 = tuple(v62) if isinstance(v62, np.ndarray) else v62

                    temp = get_nested_attribute(action, '30', locals())
                    if temp is None:
                        temp = 30
                    if action is not None and hasattr(action, "v65".split('[')[0].split('.')[0]):
                        action.v65 = temp
                    else:
                        v65 = temp 

                    v61 = np.dot(np.array(v62) , np.array(v65)); v61 = tuple(v61) if isinstance(v61, np.ndarray) else v61

                    temp = get_nested_attribute(action, '45', locals())
                    if temp is None:
                        temp = 45
                    if action is not None and hasattr(action, "v66".split('[')[0].split('.')[0]):
                        action.v66 = temp
                    else:
                        v66 = temp 

                    v60 = np.array(v61) - np.array(v66); v60 = tuple(v60) if isinstance(v60, np.ndarray) else v60
                    v57 = (v58 , v60); v57 = tuple(v57) if isinstance(v57, np.ndarray) else v57
                    if action is not None:
                        action.disks[v56].move_absolute(v57)
                    else:
                        disks[v56].move_absolute(v57)
                self.last_disks = copy.deepcopy(self.disks)


            if self.numberOfDisks != self.last_numberOfDisks:

                temp = get_nested_attribute(action, 'numberOfDisks', locals())
                if temp is None:
                    temp = numberOfDisks
                if action is not None and hasattr(action, "v68".split('[')[0].split('.')[0]):
                    action.v68 = temp
                else:
                    v68 = temp 


                temp = get_nested_attribute(action, '0', locals())
                if temp is None:
                    temp = 0
                if action is not None and hasattr(action, "v69".split('[')[0].split('.')[0]):
                    action.v69 = temp
                else:
                    v69 = temp 

                v67 = np.array(v68) < np.array(v69); v67 = tuple(v67) if isinstance(v67, np.ndarray) else v67
                if v67:

                    temp = get_nested_attribute(action, '0', locals())
                    if temp is None:
                        temp = 0
                    if action is not None and hasattr(action, "v70".split('[')[0].split('.')[0]):
                        action.v70 = temp
                    else:
                        v70 = temp 


                    temp = get_nested_attribute(action, 'v70', locals())
                    if temp is None:
                        temp = v70
                    if action is not None and hasattr(action, "v71".split('[')[0].split('.')[0]):
                        action.v71 = temp
                    else:
                        v71 = temp 


                    temp = get_nested_attribute(action, 'v71', locals())
                    if temp is None:
                        temp = v71
                    if action is not None and hasattr(action, "numberOfDisks".split('[')[0].split('.')[0]):
                        action.numberOfDisks = temp
                    else:
                        numberOfDisks = temp 
                    

                temp = get_nested_attribute(action, 'None', locals())
                if temp is None:
                    temp = None
                if action is not None and hasattr(action, "v73".split('[')[0].split('.')[0]):
                    action.v73 = temp
                else:
                    v73 = temp 

                v72 = [v73]

                temp = get_nested_attribute(action, 'v72', locals())
                if temp is None:
                    temp = v72
                if action is not None and hasattr(action, "v74".split('[')[0].split('.')[0]):
                    action.v74 = temp
                else:
                    v74 = temp 


                temp = get_nested_attribute(action, 'v74', locals())
                if temp is None:
                    temp = v74
                if action is not None and hasattr(action, "v75".split('[')[0].split('.')[0]):
                    action.v75 = temp
                else:
                    v75 = temp 


                temp = get_nested_attribute(action, 'v75', locals())
                if temp is None:
                    temp = v75
                if action is not None and hasattr(action, "temp".split('[')[0].split('.')[0]):
                    action.temp = temp
                else:
                    temp = temp 
                if model is not None: 
                    model.temp = temp
                    model.last_temp = copy.deepcopy(temp)

                temp = get_nested_attribute(action, '0', locals())
                if temp is None:
                    temp = 0
                if action is not None and hasattr(action, "v76".split('[')[0].split('.')[0]):
                    action.v76 = temp
                else:
                    v76 = temp 


                temp = get_nested_attribute(action, 'numberOfDisks', locals())
                if temp is None:
                    temp = numberOfDisks
                if action is not None and hasattr(action, "v77".split('[')[0].split('.')[0]):
                    action.v77 = temp
                else:
                    v77 = temp 

                for i in range(v76, v77, 1):

                    temp = get_nested_attribute(action, 'i', locals())
                    if temp is None:
                        temp = i
                    if action is not None and hasattr(action, "v79".split('[')[0].split('.')[0]):
                        action.v79 = temp
                    else:
                        v79 = temp 


                    temp = get_nested_attribute(action, 'disks[v79]', locals())
                    if temp is None:
                        temp = disks[v79]
                    if action is not None and hasattr(action, "v78".split('[')[0].split('.')[0]):
                        action.v78 = temp
                    else:
                        v78 = temp 


                    temp = get_nested_attribute(action, 'v78', locals())
                    if temp is None:
                        temp = v78
                    if action is not None and hasattr(action, "v80".split('[')[0].split('.')[0]):
                        action.v80 = temp
                    else:
                        v80 = temp 


                    temp = get_nested_attribute(action, 'i', locals())
                    if temp is None:
                        temp = i
                    if action is not None and hasattr(action, "v81".split('[')[0].split('.')[0]):
                        action.v81 = temp
                    else:
                        v81 = temp 


                    temp = get_nested_attribute(action, 'v80', locals())
                    if temp is None:
                        temp = v80
                    if action is not None and hasattr(action, "temp[v81]".split('[')[0].split('.')[0]):
                        action.temp[v81] = temp
                    else:
                        temp[v81] = temp 


                temp = get_nested_attribute(action, 'temp', locals())
                if temp is None:
                    temp = temp
                if action is not None and hasattr(action, "v82".split('[')[0].split('.')[0]):
                    action.v82 = temp
                else:
                    v82 = temp 


                temp = get_nested_attribute(action, 'v82', locals())
                if temp is None:
                    temp = v82
                if action is not None and hasattr(action, "v83".split('[')[0].split('.')[0]):
                    action.v83 = temp
                else:
                    v83 = temp 


                temp = get_nested_attribute(action, 'v83', locals())
                if temp is None:
                    temp = v83
                if action is not None and hasattr(action, "disks".split('[')[0].split('.')[0]):
                    action.disks = temp
                else:
                    disks = temp 

                self.last_numberOfDisks = copy.deepcopy(self.numberOfDisks)


            if self.active != self.last_active:

                temp = get_nested_attribute(action, 'active', locals())
                if temp is None:
                    temp = active
                if action is not None and hasattr(action, "v87".split('[')[0].split('.')[0]):
                    action.v87 = temp
                else:
                    v87 = temp 

                if v87:

                    temp = get_nested_attribute(action, 'numberOfDisks', locals())
                    if temp is None:
                        temp = numberOfDisks
                    if action is not None and hasattr(action, "v89".split('[')[0].split('.')[0]):
                        action.v89 = temp
                    else:
                        v89 = temp 


                    temp = get_nested_attribute(action, '0', locals())
                    if temp is None:
                        temp = 0
                    if action is not None and hasattr(action, "v90".split('[')[0].split('.')[0]):
                        action.v90 = temp
                    else:
                        v90 = temp 

                    v88 = np.array(v89) != np.array(v90); v88 = tuple(v88) if isinstance(v88, np.ndarray) else v88
                    if v88:

                        temp = get_nested_attribute(action, '"green"', locals())
                        if temp is None:
                            temp = "green"
                        if action is not None and hasattr(action, "v91".split('[')[0].split('.')[0]):
                            action.v91 = temp
                        else:
                            v91 = temp 


                        temp = get_nested_attribute(action, 'v91', locals())
                        if temp is None:
                            temp = v91
                        if action is not None and hasattr(action, "v92".split('[')[0].split('.')[0]):
                            action.v92 = temp
                        else:
                            v92 = temp 


                        temp = get_nested_attribute(action, 'numberOfDisks', locals())
                        if temp is None:
                            temp = numberOfDisks
                        if action is not None and hasattr(action, "v94".split('[')[0].split('.')[0]):
                            action.v94 = temp
                        else:
                            v94 = temp 


                        temp = get_nested_attribute(action, '1', locals())
                        if temp is None:
                            temp = 1
                        if action is not None and hasattr(action, "v95".split('[')[0].split('.')[0]):
                            action.v95 = temp
                        else:
                            v95 = temp 

                        v93 = np.array(v94) - np.array(v95); v93 = tuple(v93) if isinstance(v93, np.ndarray) else v93

                        temp = get_nested_attribute(action, 'v92', locals())
                        if temp is None:
                            temp = v92
                        if action is not None and hasattr(action, "disks[v93].wood.fill".split('[')[0].split('.')[0]):
                            action.disks[v93].wood.fill = temp
                        else:
                            disks[v93].wood.fill = temp 
                        
                    else:

                        temp = get_nested_attribute(action, 'False', locals())
                        if temp is None:
                            temp = False
                        if action is not None and hasattr(action, "v96".split('[')[0].split('.')[0]):
                            action.v96 = temp
                        else:
                            v96 = temp 


                        temp = get_nested_attribute(action, 'v96', locals())
                        if temp is None:
                            temp = v96
                        if action is not None and hasattr(action, "v97".split('[')[0].split('.')[0]):
                            action.v97 = temp
                        else:
                            v97 = temp 


                        temp = get_nested_attribute(action, 'v97', locals())
                        if temp is None:
                            temp = v97
                        if action is not None and hasattr(action, "active".split('[')[0].split('.')[0]):
                            action.active = temp
                        else:
                            active = temp 

                            
                else:

                    temp = get_nested_attribute(action, 'numberOfDisks', locals())
                    if temp is None:
                        temp = numberOfDisks
                    if action is not None and hasattr(action, "v99".split('[')[0].split('.')[0]):
                        action.v99 = temp
                    else:
                        v99 = temp 


                    temp = get_nested_attribute(action, '0', locals())
                    if temp is None:
                        temp = 0
                    if action is not None and hasattr(action, "v100".split('[')[0].split('.')[0]):
                        action.v100 = temp
                    else:
                        v100 = temp 

                    v98 = np.array(v99) != np.array(v100); v98 = tuple(v98) if isinstance(v98, np.ndarray) else v98
                    if v98:

                        temp = get_nested_attribute(action, '"brown"', locals())
                        if temp is None:
                            temp = "brown"
                        if action is not None and hasattr(action, "v101".split('[')[0].split('.')[0]):
                            action.v101 = temp
                        else:
                            v101 = temp 


                        temp = get_nested_attribute(action, 'v101', locals())
                        if temp is None:
                            temp = v101
                        if action is not None and hasattr(action, "v102".split('[')[0].split('.')[0]):
                            action.v102 = temp
                        else:
                            v102 = temp 


                        temp = get_nested_attribute(action, 'numberOfDisks', locals())
                        if temp is None:
                            temp = numberOfDisks
                        if action is not None and hasattr(action, "v104".split('[')[0].split('.')[0]):
                            action.v104 = temp
                        else:
                            v104 = temp 


                        temp = get_nested_attribute(action, '1', locals())
                        if temp is None:
                            temp = 1
                        if action is not None and hasattr(action, "v105".split('[')[0].split('.')[0]):
                            action.v105 = temp
                        else:
                            v105 = temp 

                        v103 = np.array(v104) - np.array(v105); v103 = tuple(v103) if isinstance(v103, np.ndarray) else v103

                        temp = get_nested_attribute(action, 'v102', locals())
                        if temp is None:
                            temp = v102
                        if action is not None and hasattr(action, "disks[v103].wood.fill".split('[')[0].split('.')[0]):
                            action.disks[v103].wood.fill = temp
                        else:
                            disks[v103].wood.fill = temp 
                        
                    
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
    #################################################################
    ## Model
    #################################################################
    class Game(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '100000', locals())
            if temp is None:
                temp = 100000
            if action is not None and hasattr(action, "v108".split('[')[0].split('.')[0]):
                action.v108 = temp
            else:
                v108 = temp 


            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v109".split('[')[0].split('.')[0]):
                action.v109 = temp
            else:
                v109 = temp 

            v107 = (v108 , v109); v107 = tuple(v107) if isinstance(v107, np.ndarray) else v107

            if model is not None:
                model_backup = model
                v106 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v106) # add object to model
            else:
                v106 = Disk(root = root, view = last_view)
            v106.move_absolute(v107)  

            temp = get_nested_attribute(action, 'v106', locals())
            if temp is None:
                temp = v106
            if action is not None and hasattr(action, "v110".split('[')[0].split('.')[0]):
                action.v110 = temp
            else:
                v110 = temp 


            temp = get_nested_attribute(action, 'v110', locals())
            if temp is None:
                temp = v110
            if action is not None and hasattr(action, "diskL".split('[')[0].split('.')[0]):
                action.diskL = temp
            else:
                diskL = temp 
            if model is not None: 
                model.diskL = diskL
                model.last_diskL = copy.deepcopy(diskL)

            temp = get_nested_attribute(action, '3', locals())
            if temp is None:
                temp = 3
            if action is not None and hasattr(action, "v111".split('[')[0].split('.')[0]):
                action.v111 = temp
            else:
                v111 = temp 


            temp = get_nested_attribute(action, 'v111', locals())
            if temp is None:
                temp = v111
            if action is not None and hasattr(action, "v112".split('[')[0].split('.')[0]):
                action.v112 = temp
            else:
                v112 = temp 


            temp = get_nested_attribute(action, 'v112', locals())
            if temp is None:
                temp = v112
            if action is not None and hasattr(action, "diskL.size".split('[')[0].split('.')[0]):
                action.diskL.size = temp
            else:
                diskL.size = temp 


            temp = get_nested_attribute(action, '100000', locals())
            if temp is None:
                temp = 100000
            if action is not None and hasattr(action, "v115".split('[')[0].split('.')[0]):
                action.v115 = temp
            else:
                v115 = temp 


            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v116".split('[')[0].split('.')[0]):
                action.v116 = temp
            else:
                v116 = temp 

            v114 = (v115 , v116); v114 = tuple(v114) if isinstance(v114, np.ndarray) else v114

            if model is not None:
                model_backup = model
                v113 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v113) # add object to model
            else:
                v113 = Disk(root = root, view = last_view)
            v113.move_absolute(v114)  

            temp = get_nested_attribute(action, 'v113', locals())
            if temp is None:
                temp = v113
            if action is not None and hasattr(action, "v117".split('[')[0].split('.')[0]):
                action.v117 = temp
            else:
                v117 = temp 


            temp = get_nested_attribute(action, 'v117', locals())
            if temp is None:
                temp = v117
            if action is not None and hasattr(action, "diskM".split('[')[0].split('.')[0]):
                action.diskM = temp
            else:
                diskM = temp 
            if model is not None: 
                model.diskM = diskM
                model.last_diskM = copy.deepcopy(diskM)

            temp = get_nested_attribute(action, '2', locals())
            if temp is None:
                temp = 2
            if action is not None and hasattr(action, "v118".split('[')[0].split('.')[0]):
                action.v118 = temp
            else:
                v118 = temp 


            temp = get_nested_attribute(action, 'v118', locals())
            if temp is None:
                temp = v118
            if action is not None and hasattr(action, "v119".split('[')[0].split('.')[0]):
                action.v119 = temp
            else:
                v119 = temp 


            temp = get_nested_attribute(action, 'v119', locals())
            if temp is None:
                temp = v119
            if action is not None and hasattr(action, "diskM.size".split('[')[0].split('.')[0]):
                action.diskM.size = temp
            else:
                diskM.size = temp 


            temp = get_nested_attribute(action, '100000', locals())
            if temp is None:
                temp = 100000
            if action is not None and hasattr(action, "v122".split('[')[0].split('.')[0]):
                action.v122 = temp
            else:
                v122 = temp 


            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v123".split('[')[0].split('.')[0]):
                action.v123 = temp
            else:
                v123 = temp 

            v121 = (v122 , v123); v121 = tuple(v121) if isinstance(v121, np.ndarray) else v121

            if model is not None:
                model_backup = model
                v120 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v120) # add object to model
            else:
                v120 = Disk(root = root, view = last_view)
            v120.move_absolute(v121)  

            temp = get_nested_attribute(action, 'v120', locals())
            if temp is None:
                temp = v120
            if action is not None and hasattr(action, "v124".split('[')[0].split('.')[0]):
                action.v124 = temp
            else:
                v124 = temp 


            temp = get_nested_attribute(action, 'v124', locals())
            if temp is None:
                temp = v124
            if action is not None and hasattr(action, "diskS".split('[')[0].split('.')[0]):
                action.diskS = temp
            else:
                diskS = temp 
            if model is not None: 
                model.diskS = diskS
                model.last_diskS = copy.deepcopy(diskS)

            temp = get_nested_attribute(action, '1', locals())
            if temp is None:
                temp = 1
            if action is not None and hasattr(action, "v125".split('[')[0].split('.')[0]):
                action.v125 = temp
            else:
                v125 = temp 


            temp = get_nested_attribute(action, 'v125', locals())
            if temp is None:
                temp = v125
            if action is not None and hasattr(action, "v126".split('[')[0].split('.')[0]):
                action.v126 = temp
            else:
                v126 = temp 


            temp = get_nested_attribute(action, 'v126', locals())
            if temp is None:
                temp = v126
            if action is not None and hasattr(action, "diskS.size".split('[')[0].split('.')[0]):
                action.diskS.size = temp
            else:
                diskS.size = temp 


            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v129".split('[')[0].split('.')[0]):
                action.v129 = temp
            else:
                v129 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v130".split('[')[0].split('.')[0]):
                action.v130 = temp
            else:
                v130 = temp 

            v131 = - np.array(v130)
            v128 = (v129 , v131); v128 = tuple(v128) if isinstance(v128, np.ndarray) else v128

            if model is not None:
                model_backup = model
                v127 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v127) # add object to model
            else:
                v127 = Tower(root = root, view = last_view)
            v127.move_absolute(v128)  

            temp = get_nested_attribute(action, 'v127', locals())
            if temp is None:
                temp = v127
            if action is not None and hasattr(action, "v132".split('[')[0].split('.')[0]):
                action.v132 = temp
            else:
                v132 = temp 


            temp = get_nested_attribute(action, 'v132', locals())
            if temp is None:
                temp = v132
            if action is not None and hasattr(action, "tower1".split('[')[0].split('.')[0]):
                action.tower1 = temp
            else:
                tower1 = temp 
            if model is not None: 
                model.tower1 = tower1
                model.last_tower1 = copy.deepcopy(tower1)

            temp = get_nested_attribute(action, '500', locals())
            if temp is None:
                temp = 500
            if action is not None and hasattr(action, "v135".split('[')[0].split('.')[0]):
                action.v135 = temp
            else:
                v135 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v136".split('[')[0].split('.')[0]):
                action.v136 = temp
            else:
                v136 = temp 

            v137 = - np.array(v136)
            v134 = (v135 , v137); v134 = tuple(v134) if isinstance(v134, np.ndarray) else v134

            if model is not None:
                model_backup = model
                v133 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v133) # add object to model
            else:
                v133 = Tower(root = root, view = last_view)
            v133.move_absolute(v134)  

            temp = get_nested_attribute(action, 'v133', locals())
            if temp is None:
                temp = v133
            if action is not None and hasattr(action, "v138".split('[')[0].split('.')[0]):
                action.v138 = temp
            else:
                v138 = temp 


            temp = get_nested_attribute(action, 'v138', locals())
            if temp is None:
                temp = v138
            if action is not None and hasattr(action, "tower2".split('[')[0].split('.')[0]):
                action.tower2 = temp
            else:
                tower2 = temp 
            if model is not None: 
                model.tower2 = tower2
                model.last_tower2 = copy.deepcopy(tower2)

            temp = get_nested_attribute(action, '1000', locals())
            if temp is None:
                temp = 1000
            if action is not None and hasattr(action, "v141".split('[')[0].split('.')[0]):
                action.v141 = temp
            else:
                v141 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v142".split('[')[0].split('.')[0]):
                action.v142 = temp
            else:
                v142 = temp 

            v143 = - np.array(v142)
            v140 = (v141 , v143); v140 = tuple(v140) if isinstance(v140, np.ndarray) else v140

            if model is not None:
                model_backup = model
                v139 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v139) # add object to model
            else:
                v139 = Tower(root = root, view = last_view)
            v139.move_absolute(v140)  

            temp = get_nested_attribute(action, 'v139', locals())
            if temp is None:
                temp = v139
            if action is not None and hasattr(action, "v144".split('[')[0].split('.')[0]):
                action.v144 = temp
            else:
                v144 = temp 


            temp = get_nested_attribute(action, 'v144', locals())
            if temp is None:
                temp = v144
            if action is not None and hasattr(action, "tower3".split('[')[0].split('.')[0]):
                action.tower3 = temp
            else:
                tower3 = temp 
            if model is not None: 
                model.tower3 = tower3
                model.last_tower3 = copy.deepcopy(tower3)

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
            new_model = Game()

            self.copyAttributesTo(new_model)
            return new_model       

    #################################################################

    if model is not None:
        v145 = View()
        model.add_object(v145) # add object to model
    else:
        v145 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v145
    root.last_view = last_view

    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v146".split('[')[0].split('.')[0]):
        action.v146 = temp
    else:
        v146 = temp 


    temp = get_nested_attribute(action, 'v146', locals())
    if temp is None:
        temp = v146
    if action is not None and hasattr(action, "v147".split('[')[0].split('.')[0]):
        action.v147 = temp
    else:
        v147 = temp 


    temp = get_nested_attribute(action, 'v147', locals())
    if temp is None:
        temp = v147
    if action is not None and hasattr(action, "v148".split('[')[0].split('.')[0]):
        action.v148 = temp
    else:
        v148 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v149".split('[')[0].split('.')[0]):
        action.v149 = temp
    else:
        v149 = temp 


    temp = get_nested_attribute(action, 'v149', locals())
    if temp is None:
        temp = v149
    if action is not None and hasattr(action, "v150".split('[')[0].split('.')[0]):
        action.v150 = temp
    else:
        v150 = temp 


    temp = get_nested_attribute(action, 'v150', locals())
    if temp is None:
        temp = v150
    if action is not None and hasattr(action, "v151".split('[')[0].split('.')[0]):
        action.v151 = temp
    else:
        v151 = temp 


    temp = get_nested_attribute(action, '"Tower 1"', locals())
    if temp is None:
        temp = "Tower 1"
    if action is not None and hasattr(action, "v152".split('[')[0].split('.')[0]):
        action.v152 = temp
    else:
        v152 = temp 


    temp = get_nested_attribute(action, 'v152', locals())
    if temp is None:
        temp = v152
    if action is not None and hasattr(action, "v153".split('[')[0].split('.')[0]):
        action.v153 = temp
    else:
        v153 = temp 


    temp = get_nested_attribute(action, 'v153', locals())
    if temp is None:
        temp = v153
    if action is not None and hasattr(action, "v154".split('[')[0].split('.')[0]):
        action.v154 = temp
    else:
        v154 = temp 


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
    if action is not None and hasattr(action, "v155".split('[')[0].split('.')[0]):
        action.v155 = temp
    else:
        v155 = temp 


    temp = get_nested_attribute(action, 'v155', locals())
    if temp is None:
        temp = v155
    if action is not None and hasattr(action, "v156".split('[')[0].split('.')[0]):
        action.v156 = temp
    else:
        v156 = temp 


    temp = get_nested_attribute(action, 'v156', locals())
    if temp is None:
        temp = v156
    if action is not None and hasattr(action, "v157".split('[')[0].split('.')[0]):
        action.v157 = temp
    else:
        v157 = temp 


    if action is not None:
        action.v145.width = v148
        action.v145.height = v151
        action.v145.title = v154
        action.v145.background = v157
    else:
        v145.width = v148
        v145.height = v151
        v145.title = v154
        v145.background = v157

    temp = get_nested_attribute(action, 'v145', locals())
    if temp is None:
        temp = v145
    if action is not None and hasattr(action, "view1".split('[')[0].split('.')[0]):
        action.view1 = temp
    else:
        view1 = temp 
    if model is not None: 
        model.view1 = view1
        model.last_view1 = copy.deepcopy(view1)

    if model is not None:
        v158 = View()
        model.add_object(v158) # add object to model
    else:
        v158 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v158
    root.last_view = last_view

    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v159".split('[')[0].split('.')[0]):
        action.v159 = temp
    else:
        v159 = temp 


    temp = get_nested_attribute(action, 'v159', locals())
    if temp is None:
        temp = v159
    if action is not None and hasattr(action, "v160".split('[')[0].split('.')[0]):
        action.v160 = temp
    else:
        v160 = temp 


    temp = get_nested_attribute(action, 'v160', locals())
    if temp is None:
        temp = v160
    if action is not None and hasattr(action, "v161".split('[')[0].split('.')[0]):
        action.v161 = temp
    else:
        v161 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v162".split('[')[0].split('.')[0]):
        action.v162 = temp
    else:
        v162 = temp 


    temp = get_nested_attribute(action, 'v162', locals())
    if temp is None:
        temp = v162
    if action is not None and hasattr(action, "v163".split('[')[0].split('.')[0]):
        action.v163 = temp
    else:
        v163 = temp 


    temp = get_nested_attribute(action, 'v163', locals())
    if temp is None:
        temp = v163
    if action is not None and hasattr(action, "v164".split('[')[0].split('.')[0]):
        action.v164 = temp
    else:
        v164 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v165".split('[')[0].split('.')[0]):
        action.v165 = temp
    else:
        v165 = temp 


    temp = get_nested_attribute(action, 'v165', locals())
    if temp is None:
        temp = v165
    if action is not None and hasattr(action, "v166".split('[')[0].split('.')[0]):
        action.v166 = temp
    else:
        v166 = temp 


    temp = get_nested_attribute(action, 'v166', locals())
    if temp is None:
        temp = v166
    if action is not None and hasattr(action, "v167".split('[')[0].split('.')[0]):
        action.v167 = temp
    else:
        v167 = temp 


    temp = get_nested_attribute(action, '"Tower 2"', locals())
    if temp is None:
        temp = "Tower 2"
    if action is not None and hasattr(action, "v168".split('[')[0].split('.')[0]):
        action.v168 = temp
    else:
        v168 = temp 


    temp = get_nested_attribute(action, 'v168', locals())
    if temp is None:
        temp = v168
    if action is not None and hasattr(action, "v169".split('[')[0].split('.')[0]):
        action.v169 = temp
    else:
        v169 = temp 


    temp = get_nested_attribute(action, 'v169', locals())
    if temp is None:
        temp = v169
    if action is not None and hasattr(action, "v170".split('[')[0].split('.')[0]):
        action.v170 = temp
    else:
        v170 = temp 


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
    if action is not None and hasattr(action, "v171".split('[')[0].split('.')[0]):
        action.v171 = temp
    else:
        v171 = temp 


    temp = get_nested_attribute(action, 'v171', locals())
    if temp is None:
        temp = v171
    if action is not None and hasattr(action, "v172".split('[')[0].split('.')[0]):
        action.v172 = temp
    else:
        v172 = temp 


    temp = get_nested_attribute(action, 'v172', locals())
    if temp is None:
        temp = v172
    if action is not None and hasattr(action, "v173".split('[')[0].split('.')[0]):
        action.v173 = temp
    else:
        v173 = temp 


    if action is not None:
        action.v158.Ox = v161
        action.v158.width = v164
        action.v158.height = v167
        action.v158.title = v170
        action.v158.background = v173
    else:
        v158.Ox = v161
        v158.width = v164
        v158.height = v167
        v158.title = v170
        v158.background = v173

    temp = get_nested_attribute(action, 'v158', locals())
    if temp is None:
        temp = v158
    if action is not None and hasattr(action, "view2".split('[')[0].split('.')[0]):
        action.view2 = temp
    else:
        view2 = temp 
    if model is not None: 
        model.view2 = view2
        model.last_view2 = copy.deepcopy(view2)

    if model is not None:
        v174 = View()
        model.add_object(v174) # add object to model
    else:
        v174 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v174
    root.last_view = last_view

    temp = get_nested_attribute(action, '1000', locals())
    if temp is None:
        temp = 1000
    if action is not None and hasattr(action, "v175".split('[')[0].split('.')[0]):
        action.v175 = temp
    else:
        v175 = temp 


    temp = get_nested_attribute(action, 'v175', locals())
    if temp is None:
        temp = v175
    if action is not None and hasattr(action, "v176".split('[')[0].split('.')[0]):
        action.v176 = temp
    else:
        v176 = temp 


    temp = get_nested_attribute(action, 'v176', locals())
    if temp is None:
        temp = v176
    if action is not None and hasattr(action, "v177".split('[')[0].split('.')[0]):
        action.v177 = temp
    else:
        v177 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v178".split('[')[0].split('.')[0]):
        action.v178 = temp
    else:
        v178 = temp 


    temp = get_nested_attribute(action, 'v178', locals())
    if temp is None:
        temp = v178
    if action is not None and hasattr(action, "v179".split('[')[0].split('.')[0]):
        action.v179 = temp
    else:
        v179 = temp 


    temp = get_nested_attribute(action, 'v179', locals())
    if temp is None:
        temp = v179
    if action is not None and hasattr(action, "v180".split('[')[0].split('.')[0]):
        action.v180 = temp
    else:
        v180 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v181".split('[')[0].split('.')[0]):
        action.v181 = temp
    else:
        v181 = temp 


    temp = get_nested_attribute(action, 'v181', locals())
    if temp is None:
        temp = v181
    if action is not None and hasattr(action, "v182".split('[')[0].split('.')[0]):
        action.v182 = temp
    else:
        v182 = temp 


    temp = get_nested_attribute(action, 'v182', locals())
    if temp is None:
        temp = v182
    if action is not None and hasattr(action, "v183".split('[')[0].split('.')[0]):
        action.v183 = temp
    else:
        v183 = temp 


    temp = get_nested_attribute(action, '"Tower 3"', locals())
    if temp is None:
        temp = "Tower 3"
    if action is not None and hasattr(action, "v184".split('[')[0].split('.')[0]):
        action.v184 = temp
    else:
        v184 = temp 


    temp = get_nested_attribute(action, 'v184', locals())
    if temp is None:
        temp = v184
    if action is not None and hasattr(action, "v185".split('[')[0].split('.')[0]):
        action.v185 = temp
    else:
        v185 = temp 


    temp = get_nested_attribute(action, 'v185', locals())
    if temp is None:
        temp = v185
    if action is not None and hasattr(action, "v186".split('[')[0].split('.')[0]):
        action.v186 = temp
    else:
        v186 = temp 


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
    if action is not None and hasattr(action, "v187".split('[')[0].split('.')[0]):
        action.v187 = temp
    else:
        v187 = temp 


    temp = get_nested_attribute(action, 'v187', locals())
    if temp is None:
        temp = v187
    if action is not None and hasattr(action, "v188".split('[')[0].split('.')[0]):
        action.v188 = temp
    else:
        v188 = temp 


    temp = get_nested_attribute(action, 'v188', locals())
    if temp is None:
        temp = v188
    if action is not None and hasattr(action, "v189".split('[')[0].split('.')[0]):
        action.v189 = temp
    else:
        v189 = temp 


    if action is not None:
        action.v174.Ox = v177
        action.v174.width = v180
        action.v174.height = v183
        action.v174.title = v186
        action.v174.background = v189
    else:
        v174.Ox = v177
        v174.width = v180
        v174.height = v183
        v174.title = v186
        v174.background = v189

    temp = get_nested_attribute(action, 'v174', locals())
    if temp is None:
        temp = v174
    if action is not None and hasattr(action, "view3".split('[')[0].split('.')[0]):
        action.view3 = temp
    else:
        view3 = temp 
    if model is not None: 
        model.view3 = view3
        model.last_view3 = copy.deepcopy(view3)

    if model is not None:
        model_backup = model
        v190 = Game() # this makes model = None in the end!
        model = model_backup
        model.add_object(v190) # add object to model
    else:
        v190 = Game(root = root, view = last_view)
      

    temp = get_nested_attribute(action, 'v190', locals())
    if temp is None:
        temp = v190
    if action is not None and hasattr(action, "v191".split('[')[0].split('.')[0]):
        action.v191 = temp
    else:
        v191 = temp 


    temp = get_nested_attribute(action, 'v191', locals())
    if temp is None:
        temp = v191
    if action is not None and hasattr(action, "game".split('[')[0].split('.')[0]):
        action.game = temp
    else:
        game = temp 
    if model is not None: 
        model.game = game
        model.last_game = copy.deepcopy(game)

    temp = get_nested_attribute(action, '3', locals())
    if temp is None:
        temp = 3
    if action is not None and hasattr(action, "v192".split('[')[0].split('.')[0]):
        action.v192 = temp
    else:
        v192 = temp 


    temp = get_nested_attribute(action, 'v192', locals())
    if temp is None:
        temp = v192
    if action is not None and hasattr(action, "v193".split('[')[0].split('.')[0]):
        action.v193 = temp
    else:
        v193 = temp 


    temp = get_nested_attribute(action, 'v193', locals())
    if temp is None:
        temp = v193
    if action is not None and hasattr(action, "game.tower1.numberOfDisks".split('[')[0].split('.')[0]):
        action.game.tower1.numberOfDisks = temp
    else:
        game.tower1.numberOfDisks = temp 


    temp = get_nested_attribute(action, 'game.diskL', locals())
    if temp is None:
        temp = game.diskL
    if action is not None and hasattr(action, "v195".split('[')[0].split('.')[0]):
        action.v195 = temp
    else:
        v195 = temp 


    temp = get_nested_attribute(action, 'game.diskM', locals())
    if temp is None:
        temp = game.diskM
    if action is not None and hasattr(action, "v196".split('[')[0].split('.')[0]):
        action.v196 = temp
    else:
        v196 = temp 


    temp = get_nested_attribute(action, 'game.diskS', locals())
    if temp is None:
        temp = game.diskS
    if action is not None and hasattr(action, "v197".split('[')[0].split('.')[0]):
        action.v197 = temp
    else:
        v197 = temp 

    v194 = [v195,v196,v197]

    temp = get_nested_attribute(action, 'v194', locals())
    if temp is None:
        temp = v194
    if action is not None and hasattr(action, "v198".split('[')[0].split('.')[0]):
        action.v198 = temp
    else:
        v198 = temp 


    temp = get_nested_attribute(action, 'v198', locals())
    if temp is None:
        temp = v198
    if action is not None and hasattr(action, "game.tower1.disks".split('[')[0].split('.')[0]):
        action.game.tower1.disks = temp
    else:
        game.tower1.disks = temp 

    last_refresh = time.time()
    view1.update()

    last_refresh = time.time()
    view2.update()

    last_refresh = time.time()
    view3.update()

    last_refresh = time.time()
    view1.update()

    last_refresh = time.time()
    view2.update()

    last_refresh = time.time()
    view3.update()


    temp = get_nested_attribute(action, 'True', locals())
    if temp is None:
        temp = True
    if action is not None and hasattr(action, "v199".split('[')[0].split('.')[0]):
        action.v199 = temp
    else:
        v199 = temp 


    while v199:
        if action is not None:
            v200 = action.root.waitClick()
        else:
            v200 = root.waitClick()

        temp = get_nested_attribute(action, 'v200', locals())
        if temp is None:
            temp = v200
        if action is not None and hasattr(action, "v201".split('[')[0].split('.')[0]):
            action.v201 = temp
        else:
            v201 = temp 


        temp = get_nested_attribute(action, 'v201', locals())
        if temp is None:
            temp = v201
        if action is not None and hasattr(action, "v202".split('[')[0].split('.')[0]):
            action.v202 = temp
        else:
            v202 = temp 


        temp = get_nested_attribute(action, 'v202', locals())
        if temp is None:
            temp = v202
        if action is not None and hasattr(action, "p1".split('[')[0].split('.')[0]):
            action.p1 = temp
        else:
            p1 = temp 
        if model is not None: 
            model.p1 = p1
            model.last_p1 = copy.deepcopy(p1)

        temp = get_nested_attribute(action, 'p1', locals())
        if temp is None:
            temp = p1
        if action is not None and hasattr(action, "v203".split('[')[0].split('.')[0]):
            action.v203 = temp
        else:
            v203 = temp 

        print(v203)

        temp = get_nested_attribute(action, '0', locals())
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v206".split('[')[0].split('.')[0]):
            action.v206 = temp
        else:
            v206 = temp 


        temp = get_nested_attribute(action, 'p1[v206]', locals())
        if temp is None:
            temp = p1[v206]
        if action is not None and hasattr(action, "v205".split('[')[0].split('.')[0]):
            action.v205 = temp
        else:
            v205 = temp 


        temp = get_nested_attribute(action, '250', locals())
        if temp is None:
            temp = 250
        if action is not None and hasattr(action, "v207".split('[')[0].split('.')[0]):
            action.v207 = temp
        else:
            v207 = temp 

        v204 = np.array(v205) < np.array(v207); v204 = tuple(v204) if isinstance(v204, np.ndarray) else v204
        if v204:

            temp = get_nested_attribute(action, '"Tower 1"', locals())
            if temp is None:
                temp = "Tower 1"
            if action is not None and hasattr(action, "v208".split('[')[0].split('.')[0]):
                action.v208 = temp
            else:
                v208 = temp 

            print(v208)

            temp = get_nested_attribute(action, 'True', locals())
            if temp is None:
                temp = True
            if action is not None and hasattr(action, "v209".split('[')[0].split('.')[0]):
                action.v209 = temp
            else:
                v209 = temp 


            temp = get_nested_attribute(action, 'v209', locals())
            if temp is None:
                temp = v209
            if action is not None and hasattr(action, "v210".split('[')[0].split('.')[0]):
                action.v210 = temp
            else:
                v210 = temp 


            temp = get_nested_attribute(action, 'v210', locals())
            if temp is None:
                temp = v210
            if action is not None and hasattr(action, "game.tower1.active".split('[')[0].split('.')[0]):
                action.game.tower1.active = temp
            else:
                game.tower1.active = temp 


            temp = get_nested_attribute(action, 'False', locals())
            if temp is None:
                temp = False
            if action is not None and hasattr(action, "v211".split('[')[0].split('.')[0]):
                action.v211 = temp
            else:
                v211 = temp 


            temp = get_nested_attribute(action, 'v211', locals())
            if temp is None:
                temp = v211
            if action is not None and hasattr(action, "v212".split('[')[0].split('.')[0]):
                action.v212 = temp
            else:
                v212 = temp 


            temp = get_nested_attribute(action, 'v212', locals())
            if temp is None:
                temp = v212
            if action is not None and hasattr(action, "game.tower2.active".split('[')[0].split('.')[0]):
                action.game.tower2.active = temp
            else:
                game.tower2.active = temp 


            temp = get_nested_attribute(action, 'False', locals())
            if temp is None:
                temp = False
            if action is not None and hasattr(action, "v213".split('[')[0].split('.')[0]):
                action.v213 = temp
            else:
                v213 = temp 


            temp = get_nested_attribute(action, 'v213', locals())
            if temp is None:
                temp = v213
            if action is not None and hasattr(action, "v214".split('[')[0].split('.')[0]):
                action.v214 = temp
            else:
                v214 = temp 


            temp = get_nested_attribute(action, 'v214', locals())
            if temp is None:
                temp = v214
            if action is not None and hasattr(action, "game.tower3.active".split('[')[0].split('.')[0]):
                action.game.tower3.active = temp
            else:
                game.tower3.active = temp 

            last_refresh = time.time()
            view1.update()
            
        else:

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v217".split('[')[0].split('.')[0]):
                action.v217 = temp
            else:
                v217 = temp 


            temp = get_nested_attribute(action, 'p1[v217]', locals())
            if temp is None:
                temp = p1[v217]
            if action is not None and hasattr(action, "v216".split('[')[0].split('.')[0]):
                action.v216 = temp
            else:
                v216 = temp 


            temp = get_nested_attribute(action, '750', locals())
            if temp is None:
                temp = 750
            if action is not None and hasattr(action, "v218".split('[')[0].split('.')[0]):
                action.v218 = temp
            else:
                v218 = temp 

            v215 = np.array(v216) < np.array(v218); v215 = tuple(v215) if isinstance(v215, np.ndarray) else v215
            if v215:

                temp = get_nested_attribute(action, '"Tower 2"', locals())
                if temp is None:
                    temp = "Tower 2"
                if action is not None and hasattr(action, "v219".split('[')[0].split('.')[0]):
                    action.v219 = temp
                else:
                    v219 = temp 

                print(v219)

                temp = get_nested_attribute(action, 'True', locals())
                if temp is None:
                    temp = True
                if action is not None and hasattr(action, "v220".split('[')[0].split('.')[0]):
                    action.v220 = temp
                else:
                    v220 = temp 


                temp = get_nested_attribute(action, 'v220', locals())
                if temp is None:
                    temp = v220
                if action is not None and hasattr(action, "v221".split('[')[0].split('.')[0]):
                    action.v221 = temp
                else:
                    v221 = temp 


                temp = get_nested_attribute(action, 'v221', locals())
                if temp is None:
                    temp = v221
                if action is not None and hasattr(action, "game.tower2.active".split('[')[0].split('.')[0]):
                    action.game.tower2.active = temp
                else:
                    game.tower2.active = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
                if action is not None and hasattr(action, "v222".split('[')[0].split('.')[0]):
                    action.v222 = temp
                else:
                    v222 = temp 


                temp = get_nested_attribute(action, 'v222', locals())
                if temp is None:
                    temp = v222
                if action is not None and hasattr(action, "v223".split('[')[0].split('.')[0]):
                    action.v223 = temp
                else:
                    v223 = temp 


                temp = get_nested_attribute(action, 'v223', locals())
                if temp is None:
                    temp = v223
                if action is not None and hasattr(action, "game.tower1.active".split('[')[0].split('.')[0]):
                    action.game.tower1.active = temp
                else:
                    game.tower1.active = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
                if action is not None and hasattr(action, "v224".split('[')[0].split('.')[0]):
                    action.v224 = temp
                else:
                    v224 = temp 


                temp = get_nested_attribute(action, 'v224', locals())
                if temp is None:
                    temp = v224
                if action is not None and hasattr(action, "v225".split('[')[0].split('.')[0]):
                    action.v225 = temp
                else:
                    v225 = temp 


                temp = get_nested_attribute(action, 'v225', locals())
                if temp is None:
                    temp = v225
                if action is not None and hasattr(action, "game.tower3.active".split('[')[0].split('.')[0]):
                    action.game.tower3.active = temp
                else:
                    game.tower3.active = temp 

                last_refresh = time.time()
                view2.update()
                
            else:

                temp = get_nested_attribute(action, '"Tower 3"', locals())
                if temp is None:
                    temp = "Tower 3"
                if action is not None and hasattr(action, "v226".split('[')[0].split('.')[0]):
                    action.v226 = temp
                else:
                    v226 = temp 

                print(v226)

                temp = get_nested_attribute(action, 'True', locals())
                if temp is None:
                    temp = True
                if action is not None and hasattr(action, "v227".split('[')[0].split('.')[0]):
                    action.v227 = temp
                else:
                    v227 = temp 


                temp = get_nested_attribute(action, 'v227', locals())
                if temp is None:
                    temp = v227
                if action is not None and hasattr(action, "v228".split('[')[0].split('.')[0]):
                    action.v228 = temp
                else:
                    v228 = temp 


                temp = get_nested_attribute(action, 'v228', locals())
                if temp is None:
                    temp = v228
                if action is not None and hasattr(action, "game.tower3.active".split('[')[0].split('.')[0]):
                    action.game.tower3.active = temp
                else:
                    game.tower3.active = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
                if action is not None and hasattr(action, "v229".split('[')[0].split('.')[0]):
                    action.v229 = temp
                else:
                    v229 = temp 


                temp = get_nested_attribute(action, 'v229', locals())
                if temp is None:
                    temp = v229
                if action is not None and hasattr(action, "v230".split('[')[0].split('.')[0]):
                    action.v230 = temp
                else:
                    v230 = temp 


                temp = get_nested_attribute(action, 'v230', locals())
                if temp is None:
                    temp = v230
                if action is not None and hasattr(action, "game.tower1.active".split('[')[0].split('.')[0]):
                    action.game.tower1.active = temp
                else:
                    game.tower1.active = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
                if action is not None and hasattr(action, "v231".split('[')[0].split('.')[0]):
                    action.v231 = temp
                else:
                    v231 = temp 


                temp = get_nested_attribute(action, 'v231', locals())
                if temp is None:
                    temp = v231
                if action is not None and hasattr(action, "v232".split('[')[0].split('.')[0]):
                    action.v232 = temp
                else:
                    v232 = temp 


                temp = get_nested_attribute(action, 'v232', locals())
                if temp is None:
                    temp = v232
                if action is not None and hasattr(action, "game.tower2.active".split('[')[0].split('.')[0]):
                    action.game.tower2.active = temp
                else:
                    game.tower2.active = temp 

                last_refresh = time.time()
                view3.update()

                
            
        last_refresh = time.time()
        view1.update()

        last_refresh = time.time()
        view2.update()

        last_refresh = time.time()
        view3.update()

        if action is not None:
            v233 = action.root.waitClick()
        else:
            v233 = root.waitClick()

        temp = get_nested_attribute(action, 'v233', locals())
        if temp is None:
            temp = v233
        if action is not None and hasattr(action, "v234".split('[')[0].split('.')[0]):
            action.v234 = temp
        else:
            v234 = temp 


        temp = get_nested_attribute(action, 'v234', locals())
        if temp is None:
            temp = v234
        if action is not None and hasattr(action, "v235".split('[')[0].split('.')[0]):
            action.v235 = temp
        else:
            v235 = temp 


        temp = get_nested_attribute(action, 'v235', locals())
        if temp is None:
            temp = v235
        if action is not None and hasattr(action, "p2".split('[')[0].split('.')[0]):
            action.p2 = temp
        else:
            p2 = temp 
        if model is not None: 
            model.p2 = p2
            model.last_p2 = copy.deepcopy(p2)

        temp = get_nested_attribute(action, '0', locals())
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v238".split('[')[0].split('.')[0]):
            action.v238 = temp
        else:
            v238 = temp 


        temp = get_nested_attribute(action, 'p2[v238]', locals())
        if temp is None:
            temp = p2[v238]
        if action is not None and hasattr(action, "v237".split('[')[0].split('.')[0]):
            action.v237 = temp
        else:
            v237 = temp 


        temp = get_nested_attribute(action, '250', locals())
        if temp is None:
            temp = 250
        if action is not None and hasattr(action, "v239".split('[')[0].split('.')[0]):
            action.v239 = temp
        else:
            v239 = temp 

        v236 = np.array(v237) < np.array(v239); v236 = tuple(v236) if isinstance(v236, np.ndarray) else v236
        if v236:

            temp = get_nested_attribute(action, '"Tower 1"', locals())
            if temp is None:
                temp = "Tower 1"
            if action is not None and hasattr(action, "v240".split('[')[0].split('.')[0]):
                action.v240 = temp
            else:
                v240 = temp 

            print(v240)    
        else:

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v243".split('[')[0].split('.')[0]):
                action.v243 = temp
            else:
                v243 = temp 


            temp = get_nested_attribute(action, 'p2[v243]', locals())
            if temp is None:
                temp = p2[v243]
            if action is not None and hasattr(action, "v242".split('[')[0].split('.')[0]):
                action.v242 = temp
            else:
                v242 = temp 


            temp = get_nested_attribute(action, '750', locals())
            if temp is None:
                temp = 750
            if action is not None and hasattr(action, "v244".split('[')[0].split('.')[0]):
                action.v244 = temp
            else:
                v244 = temp 

            v241 = np.array(v242) < np.array(v244); v241 = tuple(v241) if isinstance(v241, np.ndarray) else v241
            if v241:

                temp = get_nested_attribute(action, '"Tower 2"', locals())
                if temp is None:
                    temp = "Tower 2"
                if action is not None and hasattr(action, "v245".split('[')[0].split('.')[0]):
                    action.v245 = temp
                else:
                    v245 = temp 

                print(v245)

                temp = get_nested_attribute(action, '0', locals())
                if temp is None:
                    temp = 0
                if action is not None and hasattr(action, "v249".split('[')[0].split('.')[0]):
                    action.v249 = temp
                else:
                    v249 = temp 


                temp = get_nested_attribute(action, 'p1[v249]', locals())
                if temp is None:
                    temp = p1[v249]
                if action is not None and hasattr(action, "v248".split('[')[0].split('.')[0]):
                    action.v248 = temp
                else:
                    v248 = temp 


                temp = get_nested_attribute(action, '250', locals())
                if temp is None:
                    temp = 250
                if action is not None and hasattr(action, "v250".split('[')[0].split('.')[0]):
                    action.v250 = temp
                else:
                    v250 = temp 

                v247 = np.array(v248) < np.array(v250); v247 = tuple(v247) if isinstance(v247, np.ndarray) else v247

                temp = get_nested_attribute(action, '0', locals())
                if temp is None:
                    temp = 0
                if action is not None and hasattr(action, "v253".split('[')[0].split('.')[0]):
                    action.v253 = temp
                else:
                    v253 = temp 


                temp = get_nested_attribute(action, 'p1[v253]', locals())
                if temp is None:
                    temp = p1[v253]
                if action is not None and hasattr(action, "v252".split('[')[0].split('.')[0]):
                    action.v252 = temp
                else:
                    v252 = temp 


                temp = get_nested_attribute(action, '750', locals())
                if temp is None:
                    temp = 750
                if action is not None and hasattr(action, "v254".split('[')[0].split('.')[0]):
                    action.v254 = temp
                else:
                    v254 = temp 

                v251 = np.array(v252) >= np.array(v254); v251 = tuple(v251) if isinstance(v251, np.ndarray) else v251
                v246 = np.array(v247) or np.array(v251); v246 = tuple(v246) if isinstance(v246, np.ndarray) else v246
                if v246:

                    temp = get_nested_attribute(action, 'game.tower1.active', locals())
                    if temp is None:
                        temp = game.tower1.active
                    if action is not None and hasattr(action, "v255".split('[')[0].split('.')[0]):
                        action.v255 = temp
                    else:
                        v255 = temp 

                    if v255:

                        temp = get_nested_attribute(action, 'game.tower1.numberOfDisks', locals())
                        if temp is None:
                            temp = game.tower1.numberOfDisks
                        if action is not None and hasattr(action, "v256".split('[')[0].split('.')[0]):
                            action.v256 = temp
                        else:
                            v256 = temp 


                        temp = get_nested_attribute(action, 'v256', locals())
                        if temp is None:
                            temp = v256
                        if action is not None and hasattr(action, "v257".split('[')[0].split('.')[0]):
                            action.v257 = temp
                        else:
                            v257 = temp 


                        temp = get_nested_attribute(action, 'v257', locals())
                        if temp is None:
                            temp = v257
                        if action is not None and hasattr(action, "size_of_tower1".split('[')[0].split('.')[0]):
                            action.size_of_tower1 = temp
                        else:
                            size_of_tower1 = temp 


                        temp = get_nested_attribute(action, 'size_of_tower1', locals())
                        if temp is None:
                            temp = size_of_tower1
                        if action is not None and hasattr(action, "v260".split('[')[0].split('.')[0]):
                            action.v260 = temp
                        else:
                            v260 = temp 


                        temp = get_nested_attribute(action, '1', locals())
                        if temp is None:
                            temp = 1
                        if action is not None and hasattr(action, "v261".split('[')[0].split('.')[0]):
                            action.v261 = temp
                        else:
                            v261 = temp 

                        v259 = np.array(v260) - np.array(v261); v259 = tuple(v259) if isinstance(v259, np.ndarray) else v259

                        temp = get_nested_attribute(action, 'game.tower1.disks[v259]', locals())
                        if temp is None:
                            temp = game.tower1.disks[v259]
                        if action is not None and hasattr(action, "v258".split('[')[0].split('.')[0]):
                            action.v258 = temp
                        else:
                            v258 = temp 


                        temp = get_nested_attribute(action, 'v258', locals())
                        if temp is None:
                            temp = v258
                        if action is not None and hasattr(action, "v262".split('[')[0].split('.')[0]):
                            action.v262 = temp
                        else:
                            v262 = temp 


                        temp = get_nested_attribute(action, 'v262', locals())
                        if temp is None:
                            temp = v262
                        if action is not None and hasattr(action, "last_disk".split('[')[0].split('.')[0]):
                            action.last_disk = temp
                        else:
                            last_disk = temp 


                        temp = get_nested_attribute(action, 'game.tower1.numberOfDisks', locals())
                        if temp is None:
                            temp = game.tower1.numberOfDisks
                        if action is not None and hasattr(action, "v264".split('[')[0].split('.')[0]):
                            action.v264 = temp
                        else:
                            v264 = temp 


                        temp = get_nested_attribute(action, '1', locals())
                        if temp is None:
                            temp = 1
                        if action is not None and hasattr(action, "v265".split('[')[0].split('.')[0]):
                            action.v265 = temp
                        else:
                            v265 = temp 

                        v263 = np.array(v264) - np.array(v265); v263 = tuple(v263) if isinstance(v263, np.ndarray) else v263

                        temp = get_nested_attribute(action, 'v263', locals())
                        if temp is None:
                            temp = v263
                        if action is not None and hasattr(action, "v266".split('[')[0].split('.')[0]):
                            action.v266 = temp
                        else:
                            v266 = temp 


                        temp = get_nested_attribute(action, 'v266', locals())
                        if temp is None:
                            temp = v266
                        if action is not None and hasattr(action, "game.tower1.numberOfDisks".split('[')[0].split('.')[0]):
                            action.game.tower1.numberOfDisks = temp
                        else:
                            game.tower1.numberOfDisks = temp 


                        temp = get_nested_attribute(action, 'game.tower2.numberOfDisks', locals())
                        if temp is None:
                            temp = game.tower2.numberOfDisks
                        if action is not None and hasattr(action, "v268".split('[')[0].split('.')[0]):
                            action.v268 = temp
                        else:
                            v268 = temp 


                        temp = get_nested_attribute(action, '1', locals())
                        if temp is None:
                            temp = 1
                        if action is not None and hasattr(action, "v269".split('[')[0].split('.')[0]):
                            action.v269 = temp
                        else:
                            v269 = temp 

                        v267 = np.array(v268) + np.array(v269); v267 = tuple(v267) if isinstance(v267, np.ndarray) else v267

                        temp = get_nested_attribute(action, 'v267', locals())
                        if temp is None:
                            temp = v267
                        if action is not None and hasattr(action, "v270".split('[')[0].split('.')[0]):
                            action.v270 = temp
                        else:
                            v270 = temp 


                        temp = get_nested_attribute(action, 'v270', locals())
                        if temp is None:
                            temp = v270
                        if action is not None and hasattr(action, "game.tower2.numberOfDisks".split('[')[0].split('.')[0]):
                            action.game.tower2.numberOfDisks = temp
                        else:
                            game.tower2.numberOfDisks = temp 


                        temp = get_nested_attribute(action, 'game.tower2.disks', locals())
                        if temp is None:
                            temp = game.tower2.disks
                        if action is not None and hasattr(action, "v272".split('[')[0].split('.')[0]):
                            action.v272 = temp
                        else:
                            v272 = temp 


                        temp = get_nested_attribute(action, 'last_disk', locals())
                        if temp is None:
                            temp = last_disk
                        if action is not None and hasattr(action, "v273".split('[')[0].split('.')[0]):
                            action.v273 = temp
                        else:
                            v273 = temp 

                        v271 = np.array(v272) + np.array(v273); v271 = tuple(v271) if isinstance(v271, np.ndarray) else v271

                        temp = get_nested_attribute(action, 'v271', locals())
                        if temp is None:
                            temp = v271
                        if action is not None and hasattr(action, "v274".split('[')[0].split('.')[0]):
                            action.v274 = temp
                        else:
                            v274 = temp 


                        temp = get_nested_attribute(action, 'v274', locals())
                        if temp is None:
                            temp = v274
                        if action is not None and hasattr(action, "game.tower2.disks".split('[')[0].split('.')[0]):
                            action.game.tower2.disks = temp
                        else:
                            game.tower2.disks = temp 
                            

                last_refresh = time.time()
                view2.update()
                
            else:

                temp = get_nested_attribute(action, '"Tower 3"', locals())
                if temp is None:
                    temp = "Tower 3"
                if action is not None and hasattr(action, "v275".split('[')[0].split('.')[0]):
                    action.v275 = temp
                else:
                    v275 = temp 

                print(v275)

                temp = get_nested_attribute(action, 'True', locals())
                if temp is None:
                    temp = True
                if action is not None and hasattr(action, "v276".split('[')[0].split('.')[0]):
                    action.v276 = temp
                else:
                    v276 = temp 


                temp = get_nested_attribute(action, 'v276', locals())
                if temp is None:
                    temp = v276
                if action is not None and hasattr(action, "v277".split('[')[0].split('.')[0]):
                    action.v277 = temp
                else:
                    v277 = temp 


                temp = get_nested_attribute(action, 'v277', locals())
                if temp is None:
                    temp = v277
                if action is not None and hasattr(action, "game.tower3.active".split('[')[0].split('.')[0]):
                    action.game.tower3.active = temp
                else:
                    game.tower3.active = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
                if action is not None and hasattr(action, "v278".split('[')[0].split('.')[0]):
                    action.v278 = temp
                else:
                    v278 = temp 


                temp = get_nested_attribute(action, 'v278', locals())
                if temp is None:
                    temp = v278
                if action is not None and hasattr(action, "v279".split('[')[0].split('.')[0]):
                    action.v279 = temp
                else:
                    v279 = temp 


                temp = get_nested_attribute(action, 'v279', locals())
                if temp is None:
                    temp = v279
                if action is not None and hasattr(action, "game.tower1.active".split('[')[0].split('.')[0]):
                    action.game.tower1.active = temp
                else:
                    game.tower1.active = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
                if action is not None and hasattr(action, "v280".split('[')[0].split('.')[0]):
                    action.v280 = temp
                else:
                    v280 = temp 


                temp = get_nested_attribute(action, 'v280', locals())
                if temp is None:
                    temp = v280
                if action is not None and hasattr(action, "v281".split('[')[0].split('.')[0]):
                    action.v281 = temp
                else:
                    v281 = temp 


                temp = get_nested_attribute(action, 'v281', locals())
                if temp is None:
                    temp = v281
                if action is not None and hasattr(action, "game.tower2.active".split('[')[0].split('.')[0]):
                    action.game.tower2.active = temp
                else:
                    game.tower2.active = temp 

                last_refresh = time.time()
                view3.update()

                
            
        last_refresh = time.time()
        view1.update()

        last_refresh = time.time()
        view2.update()

        last_refresh = time.time()
        view3.update()

        last_refresh = time.time()
        view1.update()

        last_refresh = time.time()
        view2.update()

        last_refresh = time.time()
        view3.update()

        # refresh the condition

        temp = get_nested_attribute(action, 'True', locals())
        if temp is None:
            temp = True
        if action is not None and hasattr(action, "v199".split('[')[0].split('.')[0]):
            action.v199 = temp
        else:
            v199 = temp 

        ##
