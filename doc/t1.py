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
            if action is not None and hasattr(action, "v67".split('[')[0].split('.')[0]):
                action.v67 = temp
            else:
                v67 = temp 


            temp = get_nested_attribute(action, 'v67', locals())
            if temp is None:
                temp = v67
            if action is not None and hasattr(action, "v68".split('[')[0].split('.')[0]):
                action.v68 = temp
            else:
                v68 = temp 


            temp = get_nested_attribute(action, 'v68', locals())
            if temp is None:
                temp = v68
            if action is not None and hasattr(action, "v69".split('[')[0].split('.')[0]):
                action.v69 = temp
            else:
                v69 = temp 


            temp = get_nested_attribute(action, 'v69', locals())
            if temp is None:
                temp = v69
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


            if self.active != self.last_active:

                temp = get_nested_attribute(action, 'active', locals())
                if temp is None:
                    temp = active
                if action is not None and hasattr(action, "v70".split('[')[0].split('.')[0]):
                    action.v70 = temp
                else:
                    v70 = temp 

                if v70:

                    temp = get_nested_attribute(action, '"green"', locals())
                    if temp is None:
                        temp = "green"
                    if action is not None and hasattr(action, "v71".split('[')[0].split('.')[0]):
                        action.v71 = temp
                    else:
                        v71 = temp 


                    temp = get_nested_attribute(action, 'v71', locals())
                    if temp is None:
                        temp = v71
                    if action is not None and hasattr(action, "v72".split('[')[0].split('.')[0]):
                        action.v72 = temp
                    else:
                        v72 = temp 


                    temp = get_nested_attribute(action, 'numberOfDisks', locals())
                    if temp is None:
                        temp = numberOfDisks
                    if action is not None and hasattr(action, "v74".split('[')[0].split('.')[0]):
                        action.v74 = temp
                    else:
                        v74 = temp 


                    temp = get_nested_attribute(action, '1', locals())
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v75".split('[')[0].split('.')[0]):
                        action.v75 = temp
                    else:
                        v75 = temp 

                    v73 = np.array(v74) - np.array(v75); v73 = tuple(v73) if isinstance(v73, np.ndarray) else v73

                    temp = get_nested_attribute(action, 'v72', locals())
                    if temp is None:
                        temp = v72
                    if action is not None and hasattr(action, "disks[v73].wood.fill".split('[')[0].split('.')[0]):
                        action.disks[v73].wood.fill = temp
                    else:
                        disks[v73].wood.fill = temp 
                    
                else:

                    temp = get_nested_attribute(action, '"brown"', locals())
                    if temp is None:
                        temp = "brown"
                    if action is not None and hasattr(action, "v76".split('[')[0].split('.')[0]):
                        action.v76 = temp
                    else:
                        v76 = temp 


                    temp = get_nested_attribute(action, 'v76', locals())
                    if temp is None:
                        temp = v76
                    if action is not None and hasattr(action, "v77".split('[')[0].split('.')[0]):
                        action.v77 = temp
                    else:
                        v77 = temp 


                    temp = get_nested_attribute(action, 'numberOfDisks', locals())
                    if temp is None:
                        temp = numberOfDisks
                    if action is not None and hasattr(action, "v79".split('[')[0].split('.')[0]):
                        action.v79 = temp
                    else:
                        v79 = temp 


                    temp = get_nested_attribute(action, '1', locals())
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v80".split('[')[0].split('.')[0]):
                        action.v80 = temp
                    else:
                        v80 = temp 

                    v78 = np.array(v79) - np.array(v80); v78 = tuple(v78) if isinstance(v78, np.ndarray) else v78

                    temp = get_nested_attribute(action, 'v77', locals())
                    if temp is None:
                        temp = v77
                    if action is not None and hasattr(action, "disks[v78].wood.fill".split('[')[0].split('.')[0]):
                        action.disks[v78].wood.fill = temp
                    else:
                        disks[v78].wood.fill = temp 

                    
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

            if model is not None:
                model_backup = model
                v81 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v81) # add object to model
            else:
                v81 = Disk(root = root, view = last_view)
              

            temp = get_nested_attribute(action, 'v81', locals())
            if temp is None:
                temp = v81
            if action is not None and hasattr(action, "v82".split('[')[0].split('.')[0]):
                action.v82 = temp
            else:
                v82 = temp 


            temp = get_nested_attribute(action, 'v82', locals())
            if temp is None:
                temp = v82
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
            if action is not None and hasattr(action, "v83".split('[')[0].split('.')[0]):
                action.v83 = temp
            else:
                v83 = temp 


            temp = get_nested_attribute(action, 'v83', locals())
            if temp is None:
                temp = v83
            if action is not None and hasattr(action, "v84".split('[')[0].split('.')[0]):
                action.v84 = temp
            else:
                v84 = temp 


            temp = get_nested_attribute(action, 'v84', locals())
            if temp is None:
                temp = v84
            if action is not None and hasattr(action, "diskL.size".split('[')[0].split('.')[0]):
                action.diskL.size = temp
            else:
                diskL.size = temp 


            if model is not None:
                model_backup = model
                v85 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v85) # add object to model
            else:
                v85 = Disk(root = root, view = last_view)
              

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
            if action is not None and hasattr(action, "v87".split('[')[0].split('.')[0]):
                action.v87 = temp
            else:
                v87 = temp 


            temp = get_nested_attribute(action, 'v87', locals())
            if temp is None:
                temp = v87
            if action is not None and hasattr(action, "v88".split('[')[0].split('.')[0]):
                action.v88 = temp
            else:
                v88 = temp 


            temp = get_nested_attribute(action, 'v88', locals())
            if temp is None:
                temp = v88
            if action is not None and hasattr(action, "diskM.size".split('[')[0].split('.')[0]):
                action.diskM.size = temp
            else:
                diskM.size = temp 


            if model is not None:
                model_backup = model
                v89 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v89) # add object to model
            else:
                v89 = Disk(root = root, view = last_view)
              

            temp = get_nested_attribute(action, 'v89', locals())
            if temp is None:
                temp = v89
            if action is not None and hasattr(action, "v90".split('[')[0].split('.')[0]):
                action.v90 = temp
            else:
                v90 = temp 


            temp = get_nested_attribute(action, 'v90', locals())
            if temp is None:
                temp = v90
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


            temp = get_nested_attribute(action, 'v92', locals())
            if temp is None:
                temp = v92
            if action is not None and hasattr(action, "diskS.size".split('[')[0].split('.')[0]):
                action.diskS.size = temp
            else:
                diskS.size = temp 


            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v95".split('[')[0].split('.')[0]):
                action.v95 = temp
            else:
                v95 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v96".split('[')[0].split('.')[0]):
                action.v96 = temp
            else:
                v96 = temp 

            v97 = - np.array(v96)
            v94 = (v95 , v97); v94 = tuple(v94) if isinstance(v94, np.ndarray) else v94

            if model is not None:
                model_backup = model
                v93 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v93) # add object to model
            else:
                v93 = Tower(root = root, view = last_view)
            v93.move_absolute(v94)  

            temp = get_nested_attribute(action, 'v93', locals())
            if temp is None:
                temp = v93
            if action is not None and hasattr(action, "v98".split('[')[0].split('.')[0]):
                action.v98 = temp
            else:
                v98 = temp 


            temp = get_nested_attribute(action, 'v98', locals())
            if temp is None:
                temp = v98
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
            if action is not None and hasattr(action, "v101".split('[')[0].split('.')[0]):
                action.v101 = temp
            else:
                v101 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v102".split('[')[0].split('.')[0]):
                action.v102 = temp
            else:
                v102 = temp 

            v103 = - np.array(v102)
            v100 = (v101 , v103); v100 = tuple(v100) if isinstance(v100, np.ndarray) else v100

            if model is not None:
                model_backup = model
                v99 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v99) # add object to model
            else:
                v99 = Tower(root = root, view = last_view)
            v99.move_absolute(v100)  

            temp = get_nested_attribute(action, 'v99', locals())
            if temp is None:
                temp = v99
            if action is not None and hasattr(action, "v104".split('[')[0].split('.')[0]):
                action.v104 = temp
            else:
                v104 = temp 


            temp = get_nested_attribute(action, 'v104', locals())
            if temp is None:
                temp = v104
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
            if action is not None and hasattr(action, "v107".split('[')[0].split('.')[0]):
                action.v107 = temp
            else:
                v107 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v108".split('[')[0].split('.')[0]):
                action.v108 = temp
            else:
                v108 = temp 

            v109 = - np.array(v108)
            v106 = (v107 , v109); v106 = tuple(v106) if isinstance(v106, np.ndarray) else v106

            if model is not None:
                model_backup = model
                v105 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v105) # add object to model
            else:
                v105 = Tower(root = root, view = last_view)
            v105.move_absolute(v106)  

            temp = get_nested_attribute(action, 'v105', locals())
            if temp is None:
                temp = v105
            if action is not None and hasattr(action, "v110".split('[')[0].split('.')[0]):
                action.v110 = temp
            else:
                v110 = temp 


            temp = get_nested_attribute(action, 'v110', locals())
            if temp is None:
                temp = v110
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
        v111 = View()
        model.add_object(v111) # add object to model
    else:
        v111 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v111
    root.last_view = last_view

    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v112".split('[')[0].split('.')[0]):
        action.v112 = temp
    else:
        v112 = temp 


    temp = get_nested_attribute(action, 'v112', locals())
    if temp is None:
        temp = v112
    if action is not None and hasattr(action, "v113".split('[')[0].split('.')[0]):
        action.v113 = temp
    else:
        v113 = temp 


    temp = get_nested_attribute(action, 'v113', locals())
    if temp is None:
        temp = v113
    if action is not None and hasattr(action, "v114".split('[')[0].split('.')[0]):
        action.v114 = temp
    else:
        v114 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v115".split('[')[0].split('.')[0]):
        action.v115 = temp
    else:
        v115 = temp 


    temp = get_nested_attribute(action, 'v115', locals())
    if temp is None:
        temp = v115
    if action is not None and hasattr(action, "v116".split('[')[0].split('.')[0]):
        action.v116 = temp
    else:
        v116 = temp 


    temp = get_nested_attribute(action, 'v116', locals())
    if temp is None:
        temp = v116
    if action is not None and hasattr(action, "v117".split('[')[0].split('.')[0]):
        action.v117 = temp
    else:
        v117 = temp 


    temp = get_nested_attribute(action, '"Tower 1"', locals())
    if temp is None:
        temp = "Tower 1"
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
    if action is not None and hasattr(action, "v120".split('[')[0].split('.')[0]):
        action.v120 = temp
    else:
        v120 = temp 


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
    if action is not None and hasattr(action, "v121".split('[')[0].split('.')[0]):
        action.v121 = temp
    else:
        v121 = temp 


    temp = get_nested_attribute(action, 'v121', locals())
    if temp is None:
        temp = v121
    if action is not None and hasattr(action, "v122".split('[')[0].split('.')[0]):
        action.v122 = temp
    else:
        v122 = temp 


    temp = get_nested_attribute(action, 'v122', locals())
    if temp is None:
        temp = v122
    if action is not None and hasattr(action, "v123".split('[')[0].split('.')[0]):
        action.v123 = temp
    else:
        v123 = temp 


    if action is not None:
        action.v111.width = v114
        action.v111.height = v117
        action.v111.title = v120
        action.v111.background = v123
    else:
        v111.width = v114
        v111.height = v117
        v111.title = v120
        v111.background = v123

    temp = get_nested_attribute(action, 'v111', locals())
    if temp is None:
        temp = v111
    if action is not None and hasattr(action, "view1".split('[')[0].split('.')[0]):
        action.view1 = temp
    else:
        view1 = temp 
    if model is not None: 
        model.view1 = view1
        model.last_view1 = copy.deepcopy(view1)

    if model is not None:
        v124 = View()
        model.add_object(v124) # add object to model
    else:
        v124 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v124
    root.last_view = last_view

    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
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
    if action is not None and hasattr(action, "v127".split('[')[0].split('.')[0]):
        action.v127 = temp
    else:
        v127 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v128".split('[')[0].split('.')[0]):
        action.v128 = temp
    else:
        v128 = temp 


    temp = get_nested_attribute(action, 'v128', locals())
    if temp is None:
        temp = v128
    if action is not None and hasattr(action, "v129".split('[')[0].split('.')[0]):
        action.v129 = temp
    else:
        v129 = temp 


    temp = get_nested_attribute(action, 'v129', locals())
    if temp is None:
        temp = v129
    if action is not None and hasattr(action, "v130".split('[')[0].split('.')[0]):
        action.v130 = temp
    else:
        v130 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v131".split('[')[0].split('.')[0]):
        action.v131 = temp
    else:
        v131 = temp 


    temp = get_nested_attribute(action, 'v131', locals())
    if temp is None:
        temp = v131
    if action is not None and hasattr(action, "v132".split('[')[0].split('.')[0]):
        action.v132 = temp
    else:
        v132 = temp 


    temp = get_nested_attribute(action, 'v132', locals())
    if temp is None:
        temp = v132
    if action is not None and hasattr(action, "v133".split('[')[0].split('.')[0]):
        action.v133 = temp
    else:
        v133 = temp 


    temp = get_nested_attribute(action, '"Tower 2"', locals())
    if temp is None:
        temp = "Tower 2"
    if action is not None and hasattr(action, "v134".split('[')[0].split('.')[0]):
        action.v134 = temp
    else:
        v134 = temp 


    temp = get_nested_attribute(action, 'v134', locals())
    if temp is None:
        temp = v134
    if action is not None and hasattr(action, "v135".split('[')[0].split('.')[0]):
        action.v135 = temp
    else:
        v135 = temp 


    temp = get_nested_attribute(action, 'v135', locals())
    if temp is None:
        temp = v135
    if action is not None and hasattr(action, "v136".split('[')[0].split('.')[0]):
        action.v136 = temp
    else:
        v136 = temp 


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
    if action is not None and hasattr(action, "v137".split('[')[0].split('.')[0]):
        action.v137 = temp
    else:
        v137 = temp 


    temp = get_nested_attribute(action, 'v137', locals())
    if temp is None:
        temp = v137
    if action is not None and hasattr(action, "v138".split('[')[0].split('.')[0]):
        action.v138 = temp
    else:
        v138 = temp 


    temp = get_nested_attribute(action, 'v138', locals())
    if temp is None:
        temp = v138
    if action is not None and hasattr(action, "v139".split('[')[0].split('.')[0]):
        action.v139 = temp
    else:
        v139 = temp 


    if action is not None:
        action.v124.Ox = v127
        action.v124.width = v130
        action.v124.height = v133
        action.v124.title = v136
        action.v124.background = v139
    else:
        v124.Ox = v127
        v124.width = v130
        v124.height = v133
        v124.title = v136
        v124.background = v139

    temp = get_nested_attribute(action, 'v124', locals())
    if temp is None:
        temp = v124
    if action is not None and hasattr(action, "view2".split('[')[0].split('.')[0]):
        action.view2 = temp
    else:
        view2 = temp 
    if model is not None: 
        model.view2 = view2
        model.last_view2 = copy.deepcopy(view2)

    if model is not None:
        v140 = View()
        model.add_object(v140) # add object to model
    else:
        v140 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v140
    root.last_view = last_view

    temp = get_nested_attribute(action, '1000', locals())
    if temp is None:
        temp = 1000
    if action is not None and hasattr(action, "v141".split('[')[0].split('.')[0]):
        action.v141 = temp
    else:
        v141 = temp 


    temp = get_nested_attribute(action, 'v141', locals())
    if temp is None:
        temp = v141
    if action is not None and hasattr(action, "v142".split('[')[0].split('.')[0]):
        action.v142 = temp
    else:
        v142 = temp 


    temp = get_nested_attribute(action, 'v142', locals())
    if temp is None:
        temp = v142
    if action is not None and hasattr(action, "v143".split('[')[0].split('.')[0]):
        action.v143 = temp
    else:
        v143 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v144".split('[')[0].split('.')[0]):
        action.v144 = temp
    else:
        v144 = temp 


    temp = get_nested_attribute(action, 'v144', locals())
    if temp is None:
        temp = v144
    if action is not None and hasattr(action, "v145".split('[')[0].split('.')[0]):
        action.v145 = temp
    else:
        v145 = temp 


    temp = get_nested_attribute(action, 'v145', locals())
    if temp is None:
        temp = v145
    if action is not None and hasattr(action, "v146".split('[')[0].split('.')[0]):
        action.v146 = temp
    else:
        v146 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
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


    temp = get_nested_attribute(action, 'v148', locals())
    if temp is None:
        temp = v148
    if action is not None and hasattr(action, "v149".split('[')[0].split('.')[0]):
        action.v149 = temp
    else:
        v149 = temp 


    temp = get_nested_attribute(action, '"Tower 3"', locals())
    if temp is None:
        temp = "Tower 3"
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


    temp = get_nested_attribute(action, 'v151', locals())
    if temp is None:
        temp = v151
    if action is not None and hasattr(action, "v152".split('[')[0].split('.')[0]):
        action.v152 = temp
    else:
        v152 = temp 


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
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


    temp = get_nested_attribute(action, 'v154', locals())
    if temp is None:
        temp = v154
    if action is not None and hasattr(action, "v155".split('[')[0].split('.')[0]):
        action.v155 = temp
    else:
        v155 = temp 


    if action is not None:
        action.v140.Ox = v143
        action.v140.width = v146
        action.v140.height = v149
        action.v140.title = v152
        action.v140.background = v155
    else:
        v140.Ox = v143
        v140.width = v146
        v140.height = v149
        v140.title = v152
        v140.background = v155

    temp = get_nested_attribute(action, 'v140', locals())
    if temp is None:
        temp = v140
    if action is not None and hasattr(action, "view3".split('[')[0].split('.')[0]):
        action.view3 = temp
    else:
        view3 = temp 
    if model is not None: 
        model.view3 = view3
        model.last_view3 = copy.deepcopy(view3)

    if model is not None:
        model_backup = model
        v156 = Game() # this makes model = None in the end!
        model = model_backup
        model.add_object(v156) # add object to model
    else:
        v156 = Game(root = root, view = last_view)
      

    temp = get_nested_attribute(action, 'v156', locals())
    if temp is None:
        temp = v156
    if action is not None and hasattr(action, "v157".split('[')[0].split('.')[0]):
        action.v157 = temp
    else:
        v157 = temp 


    temp = get_nested_attribute(action, 'v157', locals())
    if temp is None:
        temp = v157
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
    if action is not None and hasattr(action, "v158".split('[')[0].split('.')[0]):
        action.v158 = temp
    else:
        v158 = temp 


    temp = get_nested_attribute(action, 'v158', locals())
    if temp is None:
        temp = v158
    if action is not None and hasattr(action, "v159".split('[')[0].split('.')[0]):
        action.v159 = temp
    else:
        v159 = temp 


    temp = get_nested_attribute(action, 'v159', locals())
    if temp is None:
        temp = v159
    if action is not None and hasattr(action, "game.tower1.numberOfDisks".split('[')[0].split('.')[0]):
        action.game.tower1.numberOfDisks = temp
    else:
        game.tower1.numberOfDisks = temp 


    temp = get_nested_attribute(action, 'game.diskL', locals())
    if temp is None:
        temp = game.diskL
    if action is not None and hasattr(action, "v161".split('[')[0].split('.')[0]):
        action.v161 = temp
    else:
        v161 = temp 


    temp = get_nested_attribute(action, 'game.diskM', locals())
    if temp is None:
        temp = game.diskM
    if action is not None and hasattr(action, "v162".split('[')[0].split('.')[0]):
        action.v162 = temp
    else:
        v162 = temp 


    temp = get_nested_attribute(action, 'game.diskS', locals())
    if temp is None:
        temp = game.diskS
    if action is not None and hasattr(action, "v163".split('[')[0].split('.')[0]):
        action.v163 = temp
    else:
        v163 = temp 

    v160 = [v161,v162,v163]

    temp = get_nested_attribute(action, 'v160', locals())
    if temp is None:
        temp = v160
    if action is not None and hasattr(action, "v164".split('[')[0].split('.')[0]):
        action.v164 = temp
    else:
        v164 = temp 


    temp = get_nested_attribute(action, 'v164', locals())
    if temp is None:
        temp = v164
    if action is not None and hasattr(action, "game.tower1.disks".split('[')[0].split('.')[0]):
        action.game.tower1.disks = temp
    else:
        game.tower1.disks = temp 

    last_refresh = time.time()
    view1.update()

    last_refresh = time.time()
    view1.update()

    last_refresh = time.time()
    view2.update()

    last_refresh = time.time()
    view3.update()

    if action is not None:
        v165 = action.root.waitClick()
    else:
        v165 = root.waitClick()

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


    temp = get_nested_attribute(action, 'v167', locals())
    if temp is None:
        temp = v167
    if action is not None and hasattr(action, "p".split('[')[0].split('.')[0]):
        action.p = temp
    else:
        p = temp 
    if model is not None: 
        model.p = p
        model.last_p = copy.deepcopy(p)

    temp = get_nested_attribute(action, 'p', locals())
    if temp is None:
        temp = p
    if action is not None and hasattr(action, "v168".split('[')[0].split('.')[0]):
        action.v168 = temp
    else:
        v168 = temp 

    print(v168)

    last_refresh = time.time()
    view1.update()

    last_refresh = time.time()
    view2.update()

    last_refresh = time.time()
    view3.update()


    temp = get_nested_attribute(action, 'True', locals())
    if temp is None:
        temp = True
    if action is not None and hasattr(action, "v169".split('[')[0].split('.')[0]):
        action.v169 = temp
    else:
        v169 = temp 


    while v169:
        if action is not None:
            v170 = action.root.waitClick()
        else:
            v170 = root.waitClick()

        temp = get_nested_attribute(action, 'v170', locals())
        if temp is None:
            temp = v170
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
        if action is not None and hasattr(action, "p".split('[')[0].split('.')[0]):
            action.p = temp
        else:
            p = temp 
        if model is not None: 
            model.p = p
            model.last_p = copy.deepcopy(p)

        temp = get_nested_attribute(action, 'p', locals())
        if temp is None:
            temp = p
        if action is not None and hasattr(action, "v173".split('[')[0].split('.')[0]):
            action.v173 = temp
        else:
            v173 = temp 

        print(v173)

        temp = get_nested_attribute(action, '0', locals())
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v176".split('[')[0].split('.')[0]):
            action.v176 = temp
        else:
            v176 = temp 


        temp = get_nested_attribute(action, 'p[v176]', locals())
        if temp is None:
            temp = p[v176]
        if action is not None and hasattr(action, "v175".split('[')[0].split('.')[0]):
            action.v175 = temp
        else:
            v175 = temp 


        temp = get_nested_attribute(action, '250', locals())
        if temp is None:
            temp = 250
        if action is not None and hasattr(action, "v177".split('[')[0].split('.')[0]):
            action.v177 = temp
        else:
            v177 = temp 

        v174 = np.array(v175) < np.array(v177); v174 = tuple(v174) if isinstance(v174, np.ndarray) else v174
        if v174:

            temp = get_nested_attribute(action, '"Tower 1"', locals())
            if temp is None:
                temp = "Tower 1"
            if action is not None and hasattr(action, "v178".split('[')[0].split('.')[0]):
                action.v178 = temp
            else:
                v178 = temp 

            print(v178)    
        else:

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v181".split('[')[0].split('.')[0]):
                action.v181 = temp
            else:
                v181 = temp 


            temp = get_nested_attribute(action, 'p[v181]', locals())
            if temp is None:
                temp = p[v181]
            if action is not None and hasattr(action, "v180".split('[')[0].split('.')[0]):
                action.v180 = temp
            else:
                v180 = temp 


            temp = get_nested_attribute(action, '750', locals())
            if temp is None:
                temp = 750
            if action is not None and hasattr(action, "v182".split('[')[0].split('.')[0]):
                action.v182 = temp
            else:
                v182 = temp 

            v179 = np.array(v180) < np.array(v182); v179 = tuple(v179) if isinstance(v179, np.ndarray) else v179
            if v179:

                temp = get_nested_attribute(action, '"Tower 2"', locals())
                if temp is None:
                    temp = "Tower 2"
                if action is not None and hasattr(action, "v183".split('[')[0].split('.')[0]):
                    action.v183 = temp
                else:
                    v183 = temp 

                print(v183)    
            else:

                temp = get_nested_attribute(action, '"Tower 3"', locals())
                if temp is None:
                    temp = "Tower 3"
                if action is not None and hasattr(action, "v184".split('[')[0].split('.')[0]):
                    action.v184 = temp
                else:
                    v184 = temp 

                print(v184)
                
            
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
        if action is not None and hasattr(action, "v169".split('[')[0].split('.')[0]):
            action.v169 = temp
        else:
            v169 = temp 

        ##
