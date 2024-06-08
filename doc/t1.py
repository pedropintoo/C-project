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

            temp = get_nested_attribute(action, '100000', locals())
            if temp is None:
                temp = 100000
            if action is not None and hasattr(action, "v83".split('[')[0].split('.')[0]):
                action.v83 = temp
            else:
                v83 = temp 


            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v84".split('[')[0].split('.')[0]):
                action.v84 = temp
            else:
                v84 = temp 

            v82 = (v83 , v84); v82 = tuple(v82) if isinstance(v82, np.ndarray) else v82

            if model is not None:
                model_backup = model
                v81 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v81) # add object to model
            else:
                v81 = Disk(root = root, view = last_view)
            v81.move_absolute(v82)  

            temp = get_nested_attribute(action, 'v81', locals())
            if temp is None:
                temp = v81
            if action is not None and hasattr(action, "v85".split('[')[0].split('.')[0]):
                action.v85 = temp
            else:
                v85 = temp 


            temp = get_nested_attribute(action, 'v85', locals())
            if temp is None:
                temp = v85
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
            if action is not None and hasattr(action, "v86".split('[')[0].split('.')[0]):
                action.v86 = temp
            else:
                v86 = temp 


            temp = get_nested_attribute(action, 'v86', locals())
            if temp is None:
                temp = v86
            if action is not None and hasattr(action, "v87".split('[')[0].split('.')[0]):
                action.v87 = temp
            else:
                v87 = temp 


            temp = get_nested_attribute(action, 'v87', locals())
            if temp is None:
                temp = v87
            if action is not None and hasattr(action, "diskL.size".split('[')[0].split('.')[0]):
                action.diskL.size = temp
            else:
                diskL.size = temp 


            temp = get_nested_attribute(action, '100000', locals())
            if temp is None:
                temp = 100000
            if action is not None and hasattr(action, "v90".split('[')[0].split('.')[0]):
                action.v90 = temp
            else:
                v90 = temp 


            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v91".split('[')[0].split('.')[0]):
                action.v91 = temp
            else:
                v91 = temp 

            v89 = (v90 , v91); v89 = tuple(v89) if isinstance(v89, np.ndarray) else v89

            if model is not None:
                model_backup = model
                v88 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v88) # add object to model
            else:
                v88 = Disk(root = root, view = last_view)
            v88.move_absolute(v89)  

            temp = get_nested_attribute(action, 'v88', locals())
            if temp is None:
                temp = v88
            if action is not None and hasattr(action, "v92".split('[')[0].split('.')[0]):
                action.v92 = temp
            else:
                v92 = temp 


            temp = get_nested_attribute(action, 'v92', locals())
            if temp is None:
                temp = v92
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
            if action is not None and hasattr(action, "v93".split('[')[0].split('.')[0]):
                action.v93 = temp
            else:
                v93 = temp 


            temp = get_nested_attribute(action, 'v93', locals())
            if temp is None:
                temp = v93
            if action is not None and hasattr(action, "v94".split('[')[0].split('.')[0]):
                action.v94 = temp
            else:
                v94 = temp 


            temp = get_nested_attribute(action, 'v94', locals())
            if temp is None:
                temp = v94
            if action is not None and hasattr(action, "diskM.size".split('[')[0].split('.')[0]):
                action.diskM.size = temp
            else:
                diskM.size = temp 


            temp = get_nested_attribute(action, '100000', locals())
            if temp is None:
                temp = 100000
            if action is not None and hasattr(action, "v97".split('[')[0].split('.')[0]):
                action.v97 = temp
            else:
                v97 = temp 


            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v98".split('[')[0].split('.')[0]):
                action.v98 = temp
            else:
                v98 = temp 

            v96 = (v97 , v98); v96 = tuple(v96) if isinstance(v96, np.ndarray) else v96

            if model is not None:
                model_backup = model
                v95 = Disk() # this makes model = None in the end!
                model = model_backup
                model.add_object(v95) # add object to model
            else:
                v95 = Disk(root = root, view = last_view)
            v95.move_absolute(v96)  

            temp = get_nested_attribute(action, 'v95', locals())
            if temp is None:
                temp = v95
            if action is not None and hasattr(action, "v99".split('[')[0].split('.')[0]):
                action.v99 = temp
            else:
                v99 = temp 


            temp = get_nested_attribute(action, 'v99', locals())
            if temp is None:
                temp = v99
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
            if action is not None and hasattr(action, "v100".split('[')[0].split('.')[0]):
                action.v100 = temp
            else:
                v100 = temp 


            temp = get_nested_attribute(action, 'v100', locals())
            if temp is None:
                temp = v100
            if action is not None and hasattr(action, "v101".split('[')[0].split('.')[0]):
                action.v101 = temp
            else:
                v101 = temp 


            temp = get_nested_attribute(action, 'v101', locals())
            if temp is None:
                temp = v101
            if action is not None and hasattr(action, "diskS.size".split('[')[0].split('.')[0]):
                action.diskS.size = temp
            else:
                diskS.size = temp 


            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v104".split('[')[0].split('.')[0]):
                action.v104 = temp
            else:
                v104 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v105".split('[')[0].split('.')[0]):
                action.v105 = temp
            else:
                v105 = temp 

            v106 = - np.array(v105)
            v103 = (v104 , v106); v103 = tuple(v103) if isinstance(v103, np.ndarray) else v103

            if model is not None:
                model_backup = model
                v102 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v102) # add object to model
            else:
                v102 = Tower(root = root, view = last_view)
            v102.move_absolute(v103)  

            temp = get_nested_attribute(action, 'v102', locals())
            if temp is None:
                temp = v102
            if action is not None and hasattr(action, "v107".split('[')[0].split('.')[0]):
                action.v107 = temp
            else:
                v107 = temp 


            temp = get_nested_attribute(action, 'v107', locals())
            if temp is None:
                temp = v107
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
            if action is not None and hasattr(action, "v110".split('[')[0].split('.')[0]):
                action.v110 = temp
            else:
                v110 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v111".split('[')[0].split('.')[0]):
                action.v111 = temp
            else:
                v111 = temp 

            v112 = - np.array(v111)
            v109 = (v110 , v112); v109 = tuple(v109) if isinstance(v109, np.ndarray) else v109

            if model is not None:
                model_backup = model
                v108 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v108) # add object to model
            else:
                v108 = Tower(root = root, view = last_view)
            v108.move_absolute(v109)  

            temp = get_nested_attribute(action, 'v108', locals())
            if temp is None:
                temp = v108
            if action is not None and hasattr(action, "v113".split('[')[0].split('.')[0]):
                action.v113 = temp
            else:
                v113 = temp 


            temp = get_nested_attribute(action, 'v113', locals())
            if temp is None:
                temp = v113
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
            if action is not None and hasattr(action, "v116".split('[')[0].split('.')[0]):
                action.v116 = temp
            else:
                v116 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v117".split('[')[0].split('.')[0]):
                action.v117 = temp
            else:
                v117 = temp 

            v118 = - np.array(v117)
            v115 = (v116 , v118); v115 = tuple(v115) if isinstance(v115, np.ndarray) else v115

            if model is not None:
                model_backup = model
                v114 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v114) # add object to model
            else:
                v114 = Tower(root = root, view = last_view)
            v114.move_absolute(v115)  

            temp = get_nested_attribute(action, 'v114', locals())
            if temp is None:
                temp = v114
            if action is not None and hasattr(action, "v119".split('[')[0].split('.')[0]):
                action.v119 = temp
            else:
                v119 = temp 


            temp = get_nested_attribute(action, 'v119', locals())
            if temp is None:
                temp = v119
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
        v120 = View()
        model.add_object(v120) # add object to model
    else:
        v120 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v120
    root.last_view = last_view

    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
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


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v124".split('[')[0].split('.')[0]):
        action.v124 = temp
    else:
        v124 = temp 


    temp = get_nested_attribute(action, 'v124', locals())
    if temp is None:
        temp = v124
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


    temp = get_nested_attribute(action, '"Tower 1"', locals())
    if temp is None:
        temp = "Tower 1"
    if action is not None and hasattr(action, "v127".split('[')[0].split('.')[0]):
        action.v127 = temp
    else:
        v127 = temp 


    temp = get_nested_attribute(action, 'v127', locals())
    if temp is None:
        temp = v127
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


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
    if action is not None and hasattr(action, "v130".split('[')[0].split('.')[0]):
        action.v130 = temp
    else:
        v130 = temp 


    temp = get_nested_attribute(action, 'v130', locals())
    if temp is None:
        temp = v130
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


    if action is not None:
        action.v120.width = v123
        action.v120.height = v126
        action.v120.title = v129
        action.v120.background = v132
    else:
        v120.width = v123
        v120.height = v126
        v120.title = v129
        v120.background = v132

    temp = get_nested_attribute(action, 'v120', locals())
    if temp is None:
        temp = v120
    if action is not None and hasattr(action, "view1".split('[')[0].split('.')[0]):
        action.view1 = temp
    else:
        view1 = temp 
    if model is not None: 
        model.view1 = view1
        model.last_view1 = copy.deepcopy(view1)

    if model is not None:
        v133 = View()
        model.add_object(v133) # add object to model
    else:
        v133 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v133
    root.last_view = last_view

    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
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


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
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


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v140".split('[')[0].split('.')[0]):
        action.v140 = temp
    else:
        v140 = temp 


    temp = get_nested_attribute(action, 'v140', locals())
    if temp is None:
        temp = v140
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


    temp = get_nested_attribute(action, '"Tower 2"', locals())
    if temp is None:
        temp = "Tower 2"
    if action is not None and hasattr(action, "v143".split('[')[0].split('.')[0]):
        action.v143 = temp
    else:
        v143 = temp 


    temp = get_nested_attribute(action, 'v143', locals())
    if temp is None:
        temp = v143
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


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
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


    if action is not None:
        action.v133.Ox = v136
        action.v133.width = v139
        action.v133.height = v142
        action.v133.title = v145
        action.v133.background = v148
    else:
        v133.Ox = v136
        v133.width = v139
        v133.height = v142
        v133.title = v145
        v133.background = v148

    temp = get_nested_attribute(action, 'v133', locals())
    if temp is None:
        temp = v133
    if action is not None and hasattr(action, "view2".split('[')[0].split('.')[0]):
        action.view2 = temp
    else:
        view2 = temp 
    if model is not None: 
        model.view2 = view2
        model.last_view2 = copy.deepcopy(view2)

    if model is not None:
        v149 = View()
        model.add_object(v149) # add object to model
    else:
        v149 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v149
    root.last_view = last_view

    temp = get_nested_attribute(action, '1000', locals())
    if temp is None:
        temp = 1000
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


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
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


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
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


    temp = get_nested_attribute(action, 'v157', locals())
    if temp is None:
        temp = v157
    if action is not None and hasattr(action, "v158".split('[')[0].split('.')[0]):
        action.v158 = temp
    else:
        v158 = temp 


    temp = get_nested_attribute(action, '"Tower 3"', locals())
    if temp is None:
        temp = "Tower 3"
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


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
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


    if action is not None:
        action.v149.Ox = v152
        action.v149.width = v155
        action.v149.height = v158
        action.v149.title = v161
        action.v149.background = v164
    else:
        v149.Ox = v152
        v149.width = v155
        v149.height = v158
        v149.title = v161
        v149.background = v164

    temp = get_nested_attribute(action, 'v149', locals())
    if temp is None:
        temp = v149
    if action is not None and hasattr(action, "view3".split('[')[0].split('.')[0]):
        action.view3 = temp
    else:
        view3 = temp 
    if model is not None: 
        model.view3 = view3
        model.last_view3 = copy.deepcopy(view3)

    if model is not None:
        model_backup = model
        v165 = Game() # this makes model = None in the end!
        model = model_backup
        model.add_object(v165) # add object to model
    else:
        v165 = Game(root = root, view = last_view)
      

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
    if action is not None and hasattr(action, "game".split('[')[0].split('.')[0]):
        action.game = temp
    else:
        game = temp 
    if model is not None: 
        model.game = game
        model.last_game = copy.deepcopy(game)

    temp = get_nested_attribute(action, '2', locals())
    if temp is None:
        temp = 2
    if action is not None and hasattr(action, "v167".split('[')[0].split('.')[0]):
        action.v167 = temp
    else:
        v167 = temp 


    temp = get_nested_attribute(action, 'v167', locals())
    if temp is None:
        temp = v167
    if action is not None and hasattr(action, "v168".split('[')[0].split('.')[0]):
        action.v168 = temp
    else:
        v168 = temp 


    temp = get_nested_attribute(action, 'v168', locals())
    if temp is None:
        temp = v168
    if action is not None and hasattr(action, "game.tower1.numberOfDisks".split('[')[0].split('.')[0]):
        action.game.tower1.numberOfDisks = temp
    else:
        game.tower1.numberOfDisks = temp 


    temp = get_nested_attribute(action, 'game.diskL', locals())
    if temp is None:
        temp = game.diskL
    if action is not None and hasattr(action, "v170".split('[')[0].split('.')[0]):
        action.v170 = temp
    else:
        v170 = temp 


    temp = get_nested_attribute(action, 'game.diskS', locals())
    if temp is None:
        temp = game.diskS
    if action is not None and hasattr(action, "v171".split('[')[0].split('.')[0]):
        action.v171 = temp
    else:
        v171 = temp 

    v169 = [v170,v171]

    temp = get_nested_attribute(action, 'v169', locals())
    if temp is None:
        temp = v169
    if action is not None and hasattr(action, "v172".split('[')[0].split('.')[0]):
        action.v172 = temp
    else:
        v172 = temp 


    temp = get_nested_attribute(action, 'v172', locals())
    if temp is None:
        temp = v172
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
        v173 = action.root.waitClick()
    else:
        v173 = root.waitClick()

    temp = get_nested_attribute(action, 'v173', locals())
    if temp is None:
        temp = v173
    if action is not None and hasattr(action, "v174".split('[')[0].split('.')[0]):
        action.v174 = temp
    else:
        v174 = temp 


    temp = get_nested_attribute(action, 'v174', locals())
    if temp is None:
        temp = v174
    if action is not None and hasattr(action, "v175".split('[')[0].split('.')[0]):
        action.v175 = temp
    else:
        v175 = temp 


    temp = get_nested_attribute(action, 'v175', locals())
    if temp is None:
        temp = v175
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
    if action is not None and hasattr(action, "v176".split('[')[0].split('.')[0]):
        action.v176 = temp
    else:
        v176 = temp 

    print(v176)

    last_refresh = time.time()
    view1.update()

    last_refresh = time.time()
    view2.update()

    last_refresh = time.time()
    view3.update()


    temp = get_nested_attribute(action, 'True', locals())
    if temp is None:
        temp = True
    if action is not None and hasattr(action, "v177".split('[')[0].split('.')[0]):
        action.v177 = temp
    else:
        v177 = temp 


    while v177:
        if action is not None:
            v178 = action.root.waitClick()
        else:
            v178 = root.waitClick()

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


        temp = get_nested_attribute(action, 'v180', locals())
        if temp is None:
            temp = v180
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
        if action is not None and hasattr(action, "v181".split('[')[0].split('.')[0]):
            action.v181 = temp
        else:
            v181 = temp 

        print(v181)

        temp = get_nested_attribute(action, '0', locals())
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v184".split('[')[0].split('.')[0]):
            action.v184 = temp
        else:
            v184 = temp 


        temp = get_nested_attribute(action, 'p[v184]', locals())
        if temp is None:
            temp = p[v184]
        if action is not None and hasattr(action, "v183".split('[')[0].split('.')[0]):
            action.v183 = temp
        else:
            v183 = temp 


        temp = get_nested_attribute(action, '250', locals())
        if temp is None:
            temp = 250
        if action is not None and hasattr(action, "v185".split('[')[0].split('.')[0]):
            action.v185 = temp
        else:
            v185 = temp 

        v182 = np.array(v183) < np.array(v185); v182 = tuple(v182) if isinstance(v182, np.ndarray) else v182
        if v182:

            temp = get_nested_attribute(action, '"Tower 1"', locals())
            if temp is None:
                temp = "Tower 1"
            if action is not None and hasattr(action, "v186".split('[')[0].split('.')[0]):
                action.v186 = temp
            else:
                v186 = temp 

            print(v186)    
        else:

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v189".split('[')[0].split('.')[0]):
                action.v189 = temp
            else:
                v189 = temp 


            temp = get_nested_attribute(action, 'p[v189]', locals())
            if temp is None:
                temp = p[v189]
            if action is not None and hasattr(action, "v188".split('[')[0].split('.')[0]):
                action.v188 = temp
            else:
                v188 = temp 


            temp = get_nested_attribute(action, '750', locals())
            if temp is None:
                temp = 750
            if action is not None and hasattr(action, "v190".split('[')[0].split('.')[0]):
                action.v190 = temp
            else:
                v190 = temp 

            v187 = np.array(v188) < np.array(v190); v187 = tuple(v187) if isinstance(v187, np.ndarray) else v187
            if v187:

                temp = get_nested_attribute(action, '"Tower 2"', locals())
                if temp is None:
                    temp = "Tower 2"
                if action is not None and hasattr(action, "v191".split('[')[0].split('.')[0]):
                    action.v191 = temp
                else:
                    v191 = temp 

                print(v191)    
            else:

                temp = get_nested_attribute(action, '"Tower 3"', locals())
                if temp is None:
                    temp = "Tower 3"
                if action is not None and hasattr(action, "v192".split('[')[0].split('.')[0]):
                    action.v192 = temp
                else:
                    v192 = temp 

                print(v192)
                
            
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
        if action is not None and hasattr(action, "v177".split('[')[0].split('.')[0]):
            action.v177 = temp
        else:
            v177 = temp 

        ##
