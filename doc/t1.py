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
    class Base(Model):
        def __init__(self, root_local: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root_local, view=view, origin=origin)
            model = self

            if model is not None:
                v0 = Rectangle()
                model.add_object(v0) # add object to model
            else:
                v0 = Rectangle(root = root)

            temp = get_nested_attribute(action, '200', locals())
            if temp is None:
                temp = 200
            if action is not None and hasattr(action, "v2".split('[')[0].split('.')[0]):
                action.v2 = temp
            else:
                v2 = temp 


            temp = get_nested_attribute(action, '20', locals())
            if temp is None:
                temp = 20
            if action is not None and hasattr(action, "v3".split('[')[0].split('.')[0]):
                action.v3 = temp
            else:
                v3 = temp 

            v1 = (v2 , v3); v1 = tuple(v1) if isinstance(v1, np.ndarray) else v1

            temp = get_nested_attribute(action, 'v1', locals())
            if temp is None:
                temp = v1
            if action is not None and hasattr(action, "v4".split('[')[0].split('.')[0]):
                action.v4 = temp
            else:
                v4 = temp 


            temp = get_nested_attribute(action, 'v4', locals())
            if temp is None:
                temp = v4
            if action is not None and hasattr(action, "v5".split('[')[0].split('.')[0]):
                action.v5 = temp
            else:
                v5 = temp 


            temp = get_nested_attribute(action, '"brown"', locals())
            if temp is None:
                temp = "brown"
            if action is not None and hasattr(action, "v6".split('[')[0].split('.')[0]):
                action.v6 = temp
            else:
                v6 = temp 


            temp = get_nested_attribute(action, 'v6', locals())
            if temp is None:
                temp = v6
            if action is not None and hasattr(action, "v7".split('[')[0].split('.')[0]):
                action.v7 = temp
            else:
                v7 = temp 


            temp = get_nested_attribute(action, 'v7', locals())
            if temp is None:
                temp = v7
            if action is not None and hasattr(action, "v8".split('[')[0].split('.')[0]):
                action.v8 = temp
            else:
                v8 = temp 


            if action is not None:
                action.v0.length = v5
                action.v0.fill = v8
            else:
                v0.length = v5
                v0.fill = v8

            temp = get_nested_attribute(action, 'v0', locals())
            if temp is None:
                temp = v0
            if action is not None and hasattr(action, "var__agl__rec".split('[')[0].split('.')[0]):
                action.var__agl__rec = temp
            else:
                var__agl__rec = temp 
            if model is not None: 
                model.var__agl__rec = var__agl__rec
                model.last_var__agl__rec = copy.deepcopy(var__agl__rec)

            if model is not None:
                v9 = Text()
                model.add_object(v9) # add object to model
            else:
                v9 = Text(root = root)

            temp = get_nested_attribute(action, '"Base"', locals())
            if temp is None:
                temp = "Base"
            if action is not None and hasattr(action, "v10".split('[')[0].split('.')[0]):
                action.v10 = temp
            else:
                v10 = temp 


            temp = get_nested_attribute(action, 'v10', locals())
            if temp is None:
                temp = v10
            if action is not None and hasattr(action, "v11".split('[')[0].split('.')[0]):
                action.v11 = temp
            else:
                v11 = temp 


            temp = get_nested_attribute(action, 'v11', locals())
            if temp is None:
                temp = v11
            if action is not None and hasattr(action, "v12".split('[')[0].split('.')[0]):
                action.v12 = temp
            else:
                v12 = temp 


            if action is not None:
                action.v9.text = v12
            else:
                v9.text = v12

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v14".split('[')[0].split('.')[0]):
                action.v14 = temp
            else:
                v14 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v15".split('[')[0].split('.')[0]):
                action.v15 = temp
            else:
                v15 = temp 

            v16 = - np.array(v15)
            v13 = (v14 , v16); v13 = tuple(v13) if isinstance(v13, np.ndarray) else v13

            if model is not None:
                v17 = Text()
                model.add_object(v17) # add object to model
            else:
                v17 = Text(root = root)
            v17.origin = v13

            temp = get_nested_attribute(action, '"Solved!!!"', locals())
            if temp is None:
                temp = "Solved!!!"
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


            temp = get_nested_attribute(action, 'v19', locals())
            if temp is None:
                temp = v19
            if action is not None and hasattr(action, "v20".split('[')[0].split('.')[0]):
                action.v20 = temp
            else:
                v20 = temp 


            temp = get_nested_attribute(action, '"hidden"', locals())
            if temp is None:
                temp = "hidden"
            if action is not None and hasattr(action, "v21".split('[')[0].split('.')[0]):
                action.v21 = temp
            else:
                v21 = temp 


            temp = get_nested_attribute(action, 'v21', locals())
            if temp is None:
                temp = v21
            if action is not None and hasattr(action, "v22".split('[')[0].split('.')[0]):
                action.v22 = temp
            else:
                v22 = temp 


            temp = get_nested_attribute(action, 'v22', locals())
            if temp is None:
                temp = v22
            if action is not None and hasattr(action, "v23".split('[')[0].split('.')[0]):
                action.v23 = temp
            else:
                v23 = temp 


            if action is not None:
                action.v17.text = v20
                action.v17.state = v23
            else:
                v17.text = v20
                v17.state = v23

            temp = get_nested_attribute(action, 'v17', locals())
            if temp is None:
                temp = v17
            if action is not None and hasattr(action, "var__agl__solved".split('[')[0].split('.')[0]):
                action.var__agl__solved = temp
            else:
                var__agl__solved = temp 
            if model is not None: 
                model.var__agl__solved = var__agl__solved
                model.last_var__agl__solved = copy.deepcopy(var__agl__solved)

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v25".split('[')[0].split('.')[0]):
                action.v25 = temp
            else:
                v25 = temp 


            temp = get_nested_attribute(action, '120', locals())
            if temp is None:
                temp = 120
            if action is not None and hasattr(action, "v26".split('[')[0].split('.')[0]):
                action.v26 = temp
            else:
                v26 = temp 

            v24 = (v25 , v26); v24 = tuple(v24) if isinstance(v24, np.ndarray) else v24

            if model is not None:
                v27 = Rectangle()
                model.add_object(v27) # add object to model
            else:
                v27 = Rectangle(root = root)
            v27.origin = v24

            temp = get_nested_attribute(action, '10', locals())
            if temp is None:
                temp = 10
            if action is not None and hasattr(action, "v29".split('[')[0].split('.')[0]):
                action.v29 = temp
            else:
                v29 = temp 


            temp = get_nested_attribute(action, '100', locals())
            if temp is None:
                temp = 100
            if action is not None and hasattr(action, "v30".split('[')[0].split('.')[0]):
                action.v30 = temp
            else:
                v30 = temp 

            v28 = (v29 , v30); v28 = tuple(v28) if isinstance(v28, np.ndarray) else v28

            temp = get_nested_attribute(action, 'v28', locals())
            if temp is None:
                temp = v28
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


            temp = get_nested_attribute(action, '"brown"', locals())
            if temp is None:
                temp = "brown"
            if action is not None and hasattr(action, "v33".split('[')[0].split('.')[0]):
                action.v33 = temp
            else:
                v33 = temp 


            temp = get_nested_attribute(action, 'v33', locals())
            if temp is None:
                temp = v33
            if action is not None and hasattr(action, "v34".split('[')[0].split('.')[0]):
                action.v34 = temp
            else:
                v34 = temp 


            temp = get_nested_attribute(action, 'v34', locals())
            if temp is None:
                temp = v34
            if action is not None and hasattr(action, "v35".split('[')[0].split('.')[0]):
                action.v35 = temp
            else:
                v35 = temp 


            if action is not None:
                action.v27.length = v32
                action.v27.fill = v35
            else:
                v27.length = v32
                v27.fill = v35

            temp = get_nested_attribute(action, 'v27', locals())
            if temp is None:
                temp = v27
            if action is not None and hasattr(action, "var__agl__stick".split('[')[0].split('.')[0]):
                action.var__agl__stick = temp
            else:
                var__agl__stick = temp 
            if model is not None: 
                model.var__agl__stick = var__agl__stick
                model.last_var__agl__stick = copy.deepcopy(var__agl__stick)

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
            new_model.view = self.view
            new_model.root = self.root
            return new_model       

    #################################################################
    #################################################################
    ## Model
    #################################################################
    class Tower(Model):
        def __init__(self, root_local: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root_local, view=view, origin=origin)
            model = self

            if model is not None:
                model_backup = model
                v36 = Base() # this makes model = None in the end!
                model = model_backup
                model.add_object(v36) # add object to model
            else:
                v36 = Base(root_local = root, view = last_view)
              

            temp = get_nested_attribute(action, 'v36', locals())
            if temp is None:
                temp = v36
            if action is not None and hasattr(action, "v37".split('[')[0].split('.')[0]):
                action.v37 = temp
            else:
                v37 = temp 


            temp = get_nested_attribute(action, 'v37', locals())
            if temp is None:
                temp = v37
            if action is not None and hasattr(action, "var__agl__base".split('[')[0].split('.')[0]):
                action.var__agl__base = temp
            else:
                var__agl__base = temp 
            if model is not None: 
                model.var__agl__base = var__agl__base
                model.last_var__agl__base = copy.deepcopy(var__agl__base)

            if model is not None:
                v38 = Rectangle()
                model.add_object(v38) # add object to model
            else:
                v38 = Rectangle(root = root)

            temp = get_nested_attribute(action, '75', locals())
            if temp is None:
                temp = 75
            if action is not None and hasattr(action, "v40".split('[')[0].split('.')[0]):
                action.v40 = temp
            else:
                v40 = temp 


            temp = get_nested_attribute(action, '15', locals())
            if temp is None:
                temp = 15
            if action is not None and hasattr(action, "v41".split('[')[0].split('.')[0]):
                action.v41 = temp
            else:
                v41 = temp 

            v39 = (v40 , v41); v39 = tuple(v39) if isinstance(v39, np.ndarray) else v39

            temp = get_nested_attribute(action, 'v39', locals())
            if temp is None:
                temp = v39
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


            temp = get_nested_attribute(action, '"brown"', locals())
            if temp is None:
                temp = "brown"
            if action is not None and hasattr(action, "v44".split('[')[0].split('.')[0]):
                action.v44 = temp
            else:
                v44 = temp 


            temp = get_nested_attribute(action, 'v44', locals())
            if temp is None:
                temp = v44
            if action is not None and hasattr(action, "v45".split('[')[0].split('.')[0]):
                action.v45 = temp
            else:
                v45 = temp 


            temp = get_nested_attribute(action, 'v45', locals())
            if temp is None:
                temp = v45
            if action is not None and hasattr(action, "v46".split('[')[0].split('.')[0]):
                action.v46 = temp
            else:
                v46 = temp 


            if action is not None:
                action.v38.length = v43
                action.v38.fill = v46
            else:
                v38.length = v43
                v38.fill = v46

            temp = get_nested_attribute(action, 'v38', locals())
            if temp is None:
                temp = v38
            if action is not None and hasattr(action, "var__agl__diskS".split('[')[0].split('.')[0]):
                action.var__agl__diskS = temp
            else:
                var__agl__diskS = temp 
            if model is not None: 
                model.var__agl__diskS = var__agl__diskS
                model.last_var__agl__diskS = copy.deepcopy(var__agl__diskS)

            if model is not None:
                v47 = Rectangle()
                model.add_object(v47) # add object to model
            else:
                v47 = Rectangle(root = root)

            temp = get_nested_attribute(action, '100', locals())
            if temp is None:
                temp = 100
            if action is not None and hasattr(action, "v49".split('[')[0].split('.')[0]):
                action.v49 = temp
            else:
                v49 = temp 


            temp = get_nested_attribute(action, '15', locals())
            if temp is None:
                temp = 15
            if action is not None and hasattr(action, "v50".split('[')[0].split('.')[0]):
                action.v50 = temp
            else:
                v50 = temp 

            v48 = (v49 , v50); v48 = tuple(v48) if isinstance(v48, np.ndarray) else v48

            temp = get_nested_attribute(action, 'v48', locals())
            if temp is None:
                temp = v48
            if action is not None and hasattr(action, "v51".split('[')[0].split('.')[0]):
                action.v51 = temp
            else:
                v51 = temp 


            temp = get_nested_attribute(action, 'v51', locals())
            if temp is None:
                temp = v51
            if action is not None and hasattr(action, "v52".split('[')[0].split('.')[0]):
                action.v52 = temp
            else:
                v52 = temp 


            temp = get_nested_attribute(action, '"brown"', locals())
            if temp is None:
                temp = "brown"
            if action is not None and hasattr(action, "v53".split('[')[0].split('.')[0]):
                action.v53 = temp
            else:
                v53 = temp 


            temp = get_nested_attribute(action, 'v53', locals())
            if temp is None:
                temp = v53
            if action is not None and hasattr(action, "v54".split('[')[0].split('.')[0]):
                action.v54 = temp
            else:
                v54 = temp 


            temp = get_nested_attribute(action, 'v54', locals())
            if temp is None:
                temp = v54
            if action is not None and hasattr(action, "v55".split('[')[0].split('.')[0]):
                action.v55 = temp
            else:
                v55 = temp 


            if action is not None:
                action.v47.length = v52
                action.v47.fill = v55
            else:
                v47.length = v52
                v47.fill = v55

            temp = get_nested_attribute(action, 'v47', locals())
            if temp is None:
                temp = v47
            if action is not None and hasattr(action, "var__agl__diskM".split('[')[0].split('.')[0]):
                action.var__agl__diskM = temp
            else:
                var__agl__diskM = temp 
            if model is not None: 
                model.var__agl__diskM = var__agl__diskM
                model.last_var__agl__diskM = copy.deepcopy(var__agl__diskM)

            if model is not None:
                v56 = Rectangle()
                model.add_object(v56) # add object to model
            else:
                v56 = Rectangle(root = root)

            temp = get_nested_attribute(action, '125', locals())
            if temp is None:
                temp = 125
            if action is not None and hasattr(action, "v58".split('[')[0].split('.')[0]):
                action.v58 = temp
            else:
                v58 = temp 


            temp = get_nested_attribute(action, '15', locals())
            if temp is None:
                temp = 15
            if action is not None and hasattr(action, "v59".split('[')[0].split('.')[0]):
                action.v59 = temp
            else:
                v59 = temp 

            v57 = (v58 , v59); v57 = tuple(v57) if isinstance(v57, np.ndarray) else v57

            temp = get_nested_attribute(action, 'v57', locals())
            if temp is None:
                temp = v57
            if action is not None and hasattr(action, "v60".split('[')[0].split('.')[0]):
                action.v60 = temp
            else:
                v60 = temp 


            temp = get_nested_attribute(action, 'v60', locals())
            if temp is None:
                temp = v60
            if action is not None and hasattr(action, "v61".split('[')[0].split('.')[0]):
                action.v61 = temp
            else:
                v61 = temp 


            temp = get_nested_attribute(action, '"brown"', locals())
            if temp is None:
                temp = "brown"
            if action is not None and hasattr(action, "v62".split('[')[0].split('.')[0]):
                action.v62 = temp
            else:
                v62 = temp 


            temp = get_nested_attribute(action, 'v62', locals())
            if temp is None:
                temp = v62
            if action is not None and hasattr(action, "v63".split('[')[0].split('.')[0]):
                action.v63 = temp
            else:
                v63 = temp 


            temp = get_nested_attribute(action, 'v63', locals())
            if temp is None:
                temp = v63
            if action is not None and hasattr(action, "v64".split('[')[0].split('.')[0]):
                action.v64 = temp
            else:
                v64 = temp 


            if action is not None:
                action.v56.length = v61
                action.v56.fill = v64
            else:
                v56.length = v61
                v56.fill = v64

            temp = get_nested_attribute(action, 'v56', locals())
            if temp is None:
                temp = v56
            if action is not None and hasattr(action, "var__agl__diskL".split('[')[0].split('.')[0]):
                action.var__agl__diskL = temp
            else:
                var__agl__diskL = temp 
            if model is not None: 
                model.var__agl__diskL = var__agl__diskL
                model.last_var__agl__diskL = copy.deepcopy(var__agl__diskL)

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v65".split('[')[0].split('.')[0]):
                action.v65 = temp
            else:
                v65 = temp 


            temp = get_nested_attribute(action, 'v65', locals())
            if temp is None:
                temp = v65
            if action is not None and hasattr(action, "v66".split('[')[0].split('.')[0]):
                action.v66 = temp
            else:
                v66 = temp 


            temp = get_nested_attribute(action, 'v66', locals())
            if temp is None:
                temp = v66
            if action is not None and hasattr(action, "v67".split('[')[0].split('.')[0]):
                action.v67 = temp
            else:
                v67 = temp 


            temp = get_nested_attribute(action, 'v67', locals())
            if temp is None:
                temp = v67
            if action is not None and hasattr(action, "var__agl__inc".split('[')[0].split('.')[0]):
                action.var__agl__inc = temp
            else:
                var__agl__inc = temp 
            if model is not None: 
                model.var__agl__inc = var__agl__inc
                model.last_var__agl__inc = copy.deepcopy(var__agl__inc)

            temp = get_nested_attribute(action, 'var__agl__diskL', locals())
            if temp is None:
                temp = var__agl__diskL
            if action is not None and hasattr(action, "v69".split('[')[0].split('.')[0]):
                action.v69 = temp
            else:
                v69 = temp 


            temp = get_nested_attribute(action, 'var__agl__diskM', locals())
            if temp is None:
                temp = var__agl__diskM
            if action is not None and hasattr(action, "v70".split('[')[0].split('.')[0]):
                action.v70 = temp
            else:
                v70 = temp 


            temp = get_nested_attribute(action, 'var__agl__diskS', locals())
            if temp is None:
                temp = var__agl__diskS
            if action is not None and hasattr(action, "v71".split('[')[0].split('.')[0]):
                action.v71 = temp
            else:
                v71 = temp 

            v68 = [v69,v70,v71]

            temp = get_nested_attribute(action, 'v68', locals())
            if temp is None:
                temp = v68
            if action is not None and hasattr(action, "v72".split('[')[0].split('.')[0]):
                action.v72 = temp
            else:
                v72 = temp 


            temp = get_nested_attribute(action, 'v72', locals())
            if temp is None:
                temp = v72
            if action is not None and hasattr(action, "v73".split('[')[0].split('.')[0]):
                action.v73 = temp
            else:
                v73 = temp 


            temp = get_nested_attribute(action, 'v73', locals())
            if temp is None:
                temp = v73
            if action is not None and hasattr(action, "var__agl__disks".split('[')[0].split('.')[0]):
                action.var__agl__disks = temp
            else:
                var__agl__disks = temp 
            if model is not None: 
                model.var__agl__disks = var__agl__disks
                model.last_var__agl__disks = copy.deepcopy(var__agl__disks)

            temp = get_nested_attribute(action, 'False', locals())
            if temp is None:
                temp = False
            if action is not None and hasattr(action, "v97".split('[')[0].split('.')[0]):
                action.v97 = temp
            else:
                v97 = temp 


            temp = get_nested_attribute(action, 'v97', locals())
            if temp is None:
                temp = v97
            if action is not None and hasattr(action, "v98".split('[')[0].split('.')[0]):
                action.v98 = temp
            else:
                v98 = temp 


            temp = get_nested_attribute(action, 'v98', locals())
            if temp is None:
                temp = v98
            if action is not None and hasattr(action, "v99".split('[')[0].split('.')[0]):
                action.v99 = temp
            else:
                v99 = temp 


            temp = get_nested_attribute(action, 'v99', locals())
            if temp is None:
                temp = v99
            if action is not None and hasattr(action, "var__agl__active".split('[')[0].split('.')[0]):
                action.var__agl__active = temp
            else:
                var__agl__active = temp 
            if model is not None: 
                model.var__agl__active = var__agl__active
                model.last_var__agl__active = copy.deepcopy(var__agl__active)

            self.fixCoords()

        def create_object(self, view):
            action = self

            if self.var__agl__disks != self.last_var__agl__disks:

                temp = get_nested_attribute(action, '0', locals())
                if temp is None:
                    temp = 0
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
                if action is not None and hasattr(action, "var__agl__inc".split('[')[0].split('.')[0]):
                    action.var__agl__inc = temp
                else:
                    var__agl__inc = temp 


                temp = get_nested_attribute(action, '0', locals())
                if temp is None:
                    temp = 0
                if action is not None and hasattr(action, "v76".split('[')[0].split('.')[0]):
                    action.v76 = temp
                else:
                    v76 = temp 


                temp = get_nested_attribute(action, '3', locals())
                if temp is None:
                    temp = 3
                if action is not None and hasattr(action, "v77".split('[')[0].split('.')[0]):
                    action.v77 = temp
                else:
                    v77 = temp 

                for var__agl__d in range(v76, v77, 1):

                    temp = get_nested_attribute(action, 'var__agl__d', locals())
                    if temp is None:
                        temp = var__agl__d
                    if action is not None and hasattr(action, "v80".split('[')[0].split('.')[0]):
                        action.v80 = temp
                    else:
                        v80 = temp 


                    temp = get_nested_attribute(action, 'var__agl__disks[v80].state', locals())
                    if temp is None:
                        temp = var__agl__disks[v80].state
                    if action is not None and hasattr(action, "v79".split('[')[0].split('.')[0]):
                        action.v79 = temp
                    else:
                        v79 = temp 


                    temp = get_nested_attribute(action, '"normal"', locals())
                    if temp is None:
                        temp = "normal"
                    if action is not None and hasattr(action, "v81".split('[')[0].split('.')[0]):
                        action.v81 = temp
                    else:
                        v81 = temp 

                    v78 = np.array(v79) == np.array(v81); v78 = tuple(v78) if isinstance(v78, np.ndarray) else v78
                    if v78:

                        temp = get_nested_attribute(action, 'var__agl__inc', locals())
                        if temp is None:
                            temp = var__agl__inc
                        if action is not None and hasattr(action, "v83".split('[')[0].split('.')[0]):
                            action.v83 = temp
                        else:
                            v83 = temp 


                        temp = get_nested_attribute(action, '1', locals())
                        if temp is None:
                            temp = 1
                        if action is not None and hasattr(action, "v84".split('[')[0].split('.')[0]):
                            action.v84 = temp
                        else:
                            v84 = temp 

                        v82 = np.array(v83) + np.array(v84); v82 = tuple(v82) if isinstance(v82, np.ndarray) else v82

                        temp = get_nested_attribute(action, 'v82', locals())
                        if temp is None:
                            temp = v82
                        if action is not None and hasattr(action, "v85".split('[')[0].split('.')[0]):
                            action.v85 = temp
                        else:
                            v85 = temp 


                        temp = get_nested_attribute(action, 'v85', locals())
                        if temp is None:
                            temp = v85
                        if action is not None and hasattr(action, "var__agl__inc".split('[')[0].split('.')[0]):
                            action.var__agl__inc = temp
                        else:
                            var__agl__inc = temp 


                        temp = get_nested_attribute(action, 'var__agl__d', locals())
                        if temp is None:
                            temp = var__agl__d
                        if action is not None and hasattr(action, "v86".split('[')[0].split('.')[0]):
                            action.v86 = temp
                        else:
                            v86 = temp 


                        temp = get_nested_attribute(action, '0', locals())
                        if temp is None:
                            temp = 0
                        if action is not None and hasattr(action, "v89".split('[')[0].split('.')[0]):
                            action.v89 = temp
                        else:
                            v89 = temp 


                        temp = get_nested_attribute(action, 'var__agl__base.origin[v89]', locals())
                        if temp is None:
                            temp = var__agl__base.origin[v89]
                        if action is not None and hasattr(action, "v88".split('[')[0].split('.')[0]):
                            action.v88 = temp
                        else:
                            v88 = temp 


                        temp = get_nested_attribute(action, 'var__agl__inc', locals())
                        if temp is None:
                            temp = var__agl__inc
                        if action is not None and hasattr(action, "v93".split('[')[0].split('.')[0]):
                            action.v93 = temp
                        else:
                            v93 = temp 


                        temp = get_nested_attribute(action, '1', locals())
                        if temp is None:
                            temp = 1
                        if action is not None and hasattr(action, "v94".split('[')[0].split('.')[0]):
                            action.v94 = temp
                        else:
                            v94 = temp 

                        v92 = np.array(v93) + np.array(v94); v92 = tuple(v92) if isinstance(v92, np.ndarray) else v92

                        temp = get_nested_attribute(action, '30', locals())
                        if temp is None:
                            temp = 30
                        if action is not None and hasattr(action, "v95".split('[')[0].split('.')[0]):
                            action.v95 = temp
                        else:
                            v95 = temp 

                        v91 = np.dot(np.array(v92) , np.array(v95)); v91 = tuple(v91) if isinstance(v91, np.ndarray) else v91

                        temp = get_nested_attribute(action, '75', locals())
                        if temp is None:
                            temp = 75
                        if action is not None and hasattr(action, "v96".split('[')[0].split('.')[0]):
                            action.v96 = temp
                        else:
                            v96 = temp 

                        v90 = np.array(v91) - np.array(v96); v90 = tuple(v90) if isinstance(v90, np.ndarray) else v90
                        v87 = (v88 , v90); v87 = tuple(v87) if isinstance(v87, np.ndarray) else v87
                        if action is not None:
                            action.var__agl__disks[v86].move_absolute(v87)
                        else:
                            var__agl__disks[v86].move_absolute(v87)    
                self.last_var__agl__disks = copy.deepcopy(self.var__agl__disks)


            if self.var__agl__active != self.last_var__agl__active:

                temp = get_nested_attribute(action, '0', locals())
                if temp is None:
                    temp = 0
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
                if action is not None and hasattr(action, "var__agl__inc".split('[')[0].split('.')[0]):
                    action.var__agl__inc = temp
                else:
                    var__agl__inc = temp 


                temp = get_nested_attribute(action, 'var__agl__active', locals())
                if temp is None:
                    temp = var__agl__active
                if action is not None and hasattr(action, "v102".split('[')[0].split('.')[0]):
                    action.v102 = temp
                else:
                    v102 = temp 

                if v102:

                    temp = get_nested_attribute(action, '2', locals())
                    if temp is None:
                        temp = 2
                    if action is not None and hasattr(action, "v103".split('[')[0].split('.')[0]):
                        action.v103 = temp
                    else:
                        v103 = temp 


                    temp = get_nested_attribute(action, '1', locals())
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v104".split('[')[0].split('.')[0]):
                        action.v104 = temp
                    else:
                        v104 = temp 

                    v105 = - np.array(v104)

                    temp = get_nested_attribute(action, '1', locals())
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v106".split('[')[0].split('.')[0]):
                        action.v106 = temp
                    else:
                        v106 = temp 

                    v107 = - np.array(v106)
                    for var__agl__d in range(v103, v105, v107):

                        temp = get_nested_attribute(action, 'var__agl__inc', locals())
                        if temp is None:
                            temp = var__agl__inc
                        if action is not None and hasattr(action, "v110".split('[')[0].split('.')[0]):
                            action.v110 = temp
                        else:
                            v110 = temp 


                        temp = get_nested_attribute(action, '0', locals())
                        if temp is None:
                            temp = 0
                        if action is not None and hasattr(action, "v111".split('[')[0].split('.')[0]):
                            action.v111 = temp
                        else:
                            v111 = temp 

                        v109 = np.array(v110) == np.array(v111); v109 = tuple(v109) if isinstance(v109, np.ndarray) else v109

                        temp = get_nested_attribute(action, 'var__agl__d', locals())
                        if temp is None:
                            temp = var__agl__d
                        if action is not None and hasattr(action, "v114".split('[')[0].split('.')[0]):
                            action.v114 = temp
                        else:
                            v114 = temp 


                        temp = get_nested_attribute(action, 'var__agl__disks[v114].state', locals())
                        if temp is None:
                            temp = var__agl__disks[v114].state
                        if action is not None and hasattr(action, "v113".split('[')[0].split('.')[0]):
                            action.v113 = temp
                        else:
                            v113 = temp 


                        temp = get_nested_attribute(action, '"normal"', locals())
                        if temp is None:
                            temp = "normal"
                        if action is not None and hasattr(action, "v115".split('[')[0].split('.')[0]):
                            action.v115 = temp
                        else:
                            v115 = temp 

                        v112 = np.array(v113) == np.array(v115); v112 = tuple(v112) if isinstance(v112, np.ndarray) else v112
                        v108 = v109 and v112; v108 = tuple(v108) if isinstance(v108, np.ndarray) else v108
                        if v108:

                            temp = get_nested_attribute(action, '"blue"', locals())
                            if temp is None:
                                temp = "blue"
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


                            temp = get_nested_attribute(action, 'var__agl__d', locals())
                            if temp is None:
                                temp = var__agl__d
                            if action is not None and hasattr(action, "v118".split('[')[0].split('.')[0]):
                                action.v118 = temp
                            else:
                                v118 = temp 


                            temp = get_nested_attribute(action, 'v117', locals())
                            if temp is None:
                                temp = v117
                            if action is not None and hasattr(action, "var__agl__disks[v118].fill".split('[')[0].split('.')[0]):
                                action.var__agl__disks[v118].fill = temp
                            else:
                                var__agl__disks[v118].fill = temp 


                            temp = get_nested_attribute(action, 'var__agl__inc', locals())
                            if temp is None:
                                temp = var__agl__inc
                            if action is not None and hasattr(action, "v120".split('[')[0].split('.')[0]):
                                action.v120 = temp
                            else:
                                v120 = temp 


                            temp = get_nested_attribute(action, '1', locals())
                            if temp is None:
                                temp = 1
                            if action is not None and hasattr(action, "v121".split('[')[0].split('.')[0]):
                                action.v121 = temp
                            else:
                                v121 = temp 

                            v119 = np.array(v120) + np.array(v121); v119 = tuple(v119) if isinstance(v119, np.ndarray) else v119

                            temp = get_nested_attribute(action, 'v119', locals())
                            if temp is None:
                                temp = v119
                            if action is not None and hasattr(action, "v122".split('[')[0].split('.')[0]):
                                action.v122 = temp
                            else:
                                v122 = temp 


                            temp = get_nested_attribute(action, 'v122', locals())
                            if temp is None:
                                temp = v122
                            if action is not None and hasattr(action, "var__agl__inc".split('[')[0].split('.')[0]):
                                action.var__agl__inc = temp
                            else:
                                var__agl__inc = temp 
                                
                else:

                    temp = get_nested_attribute(action, '2', locals())
                    if temp is None:
                        temp = 2
                    if action is not None and hasattr(action, "v123".split('[')[0].split('.')[0]):
                        action.v123 = temp
                    else:
                        v123 = temp 


                    temp = get_nested_attribute(action, '1', locals())
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v124".split('[')[0].split('.')[0]):
                        action.v124 = temp
                    else:
                        v124 = temp 

                    v125 = - np.array(v124)

                    temp = get_nested_attribute(action, '1', locals())
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v126".split('[')[0].split('.')[0]):
                        action.v126 = temp
                    else:
                        v126 = temp 

                    v127 = - np.array(v126)
                    for var__agl__d in range(v123, v125, v127):

                        temp = get_nested_attribute(action, '"brown"', locals())
                        if temp is None:
                            temp = "brown"
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


                        temp = get_nested_attribute(action, 'var__agl__d', locals())
                        if temp is None:
                            temp = var__agl__d
                        if action is not None and hasattr(action, "v130".split('[')[0].split('.')[0]):
                            action.v130 = temp
                        else:
                            v130 = temp 


                        temp = get_nested_attribute(action, 'v129', locals())
                        if temp is None:
                            temp = v129
                        if action is not None and hasattr(action, "var__agl__disks[v130].fill".split('[')[0].split('.')[0]):
                            action.var__agl__disks[v130].fill = temp
                        else:
                            var__agl__disks[v130].fill = temp 

                    
                self.last_var__agl__active = copy.deepcopy(self.var__agl__active)
        
            action = None
            super().create_object(view)
            model = None

        def __deepcopy__(self, memo=None):
            """Create a deep copy of the model."""
            if memo is None:
                memo = {} # this is required by the deepcopy protocol
            new_model = Tower()

            self.copyAttributesTo(new_model)
            new_model.view = self.view
            new_model.root = self.root
            return new_model       

    #################################################################
    #################################################################
    ## Model
    #################################################################
    class Game(Model):
        def __init__(self, root_local: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root_local, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v133".split('[')[0].split('.')[0]):
                action.v133 = temp
            else:
                v133 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v134".split('[')[0].split('.')[0]):
                action.v134 = temp
            else:
                v134 = temp 

            v135 = - np.array(v134)
            v132 = (v133 , v135); v132 = tuple(v132) if isinstance(v132, np.ndarray) else v132

            if model is not None:
                model_backup = model
                v131 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v131) # add object to model
            else:
                v131 = Tower(root_local = root, view = last_view)
            v131.move_absolute(v132)  

            temp = get_nested_attribute(action, 'v131', locals())
            if temp is None:
                temp = v131
            if action is not None and hasattr(action, "v136".split('[')[0].split('.')[0]):
                action.v136 = temp
            else:
                v136 = temp 


            temp = get_nested_attribute(action, 'v136', locals())
            if temp is None:
                temp = v136
            if action is not None and hasattr(action, "var__agl__tower1".split('[')[0].split('.')[0]):
                action.var__agl__tower1 = temp
            else:
                var__agl__tower1 = temp 
            if model is not None: 
                model.var__agl__tower1 = var__agl__tower1
                model.last_var__agl__tower1 = copy.deepcopy(var__agl__tower1)

            temp = get_nested_attribute(action, '500', locals())
            if temp is None:
                temp = 500
            if action is not None and hasattr(action, "v139".split('[')[0].split('.')[0]):
                action.v139 = temp
            else:
                v139 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v140".split('[')[0].split('.')[0]):
                action.v140 = temp
            else:
                v140 = temp 

            v141 = - np.array(v140)
            v138 = (v139 , v141); v138 = tuple(v138) if isinstance(v138, np.ndarray) else v138

            if model is not None:
                model_backup = model
                v137 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v137) # add object to model
            else:
                v137 = Tower(root_local = root, view = last_view)
            v137.move_absolute(v138)  

            temp = get_nested_attribute(action, 'v137', locals())
            if temp is None:
                temp = v137
            if action is not None and hasattr(action, "v142".split('[')[0].split('.')[0]):
                action.v142 = temp
            else:
                v142 = temp 


            temp = get_nested_attribute(action, 'v142', locals())
            if temp is None:
                temp = v142
            if action is not None and hasattr(action, "var__agl__tower2".split('[')[0].split('.')[0]):
                action.var__agl__tower2 = temp
            else:
                var__agl__tower2 = temp 
            if model is not None: 
                model.var__agl__tower2 = var__agl__tower2
                model.last_var__agl__tower2 = copy.deepcopy(var__agl__tower2)

            temp = get_nested_attribute(action, '1000', locals())
            if temp is None:
                temp = 1000
            if action is not None and hasattr(action, "v145".split('[')[0].split('.')[0]):
                action.v145 = temp
            else:
                v145 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v146".split('[')[0].split('.')[0]):
                action.v146 = temp
            else:
                v146 = temp 

            v147 = - np.array(v146)
            v144 = (v145 , v147); v144 = tuple(v144) if isinstance(v144, np.ndarray) else v144

            if model is not None:
                model_backup = model
                v143 = Tower() # this makes model = None in the end!
                model = model_backup
                model.add_object(v143) # add object to model
            else:
                v143 = Tower(root_local = root, view = last_view)
            v143.move_absolute(v144)  

            temp = get_nested_attribute(action, 'v143', locals())
            if temp is None:
                temp = v143
            if action is not None and hasattr(action, "v148".split('[')[0].split('.')[0]):
                action.v148 = temp
            else:
                v148 = temp 


            temp = get_nested_attribute(action, 'v148', locals())
            if temp is None:
                temp = v148
            if action is not None and hasattr(action, "var__agl__tower3".split('[')[0].split('.')[0]):
                action.var__agl__tower3 = temp
            else:
                var__agl__tower3 = temp 
            if model is not None: 
                model.var__agl__tower3 = var__agl__tower3
                model.last_var__agl__tower3 = copy.deepcopy(var__agl__tower3)

            temp = get_nested_attribute(action, 'var__agl__tower2', locals())
            if temp is None:
                temp = var__agl__tower2
            if action is not None and hasattr(action, "v150".split('[')[0].split('.')[0]):
                action.v150 = temp
            else:
                v150 = temp 


            temp = get_nested_attribute(action, 'var__agl__tower3', locals())
            if temp is None:
                temp = var__agl__tower3
            if action is not None and hasattr(action, "v151".split('[')[0].split('.')[0]):
                action.v151 = temp
            else:
                v151 = temp 

            v149 = [v150,v151]

            temp = get_nested_attribute(action, 'v149', locals())
            if temp is None:
                temp = v149
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
            if action is not None and hasattr(action, "var__agl__towersToCheck".split('[')[0].split('.')[0]):
                action.var__agl__towersToCheck = temp
            else:
                var__agl__towersToCheck = temp 
            if model is not None: 
                model.var__agl__towersToCheck = var__agl__towersToCheck
                model.last_var__agl__towersToCheck = copy.deepcopy(var__agl__towersToCheck)

            temp = get_nested_attribute(action, 'False', locals())
            if temp is None:
                temp = False
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
            if action is not None and hasattr(action, "var__agl__isSolved".split('[')[0].split('.')[0]):
                action.var__agl__isSolved = temp
            else:
                var__agl__isSolved = temp 
            if model is not None: 
                model.var__agl__isSolved = var__agl__isSolved
                model.last_var__agl__isSolved = copy.deepcopy(var__agl__isSolved)

            temp = get_nested_attribute(action, 'False', locals())
            if temp is None:
                temp = False
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
            if action is not None and hasattr(action, "var__agl__checkWin".split('[')[0].split('.')[0]):
                action.var__agl__checkWin = temp
            else:
                var__agl__checkWin = temp 
            if model is not None: 
                model.var__agl__checkWin = var__agl__checkWin
                model.last_var__agl__checkWin = copy.deepcopy(var__agl__checkWin)

            self.fixCoords()

        def create_object(self, view):
            action = self

            if self.var__agl__checkWin != self.last_var__agl__checkWin:

                temp = get_nested_attribute(action, '0', locals())
                if temp is None:
                    temp = 0
                if action is not None and hasattr(action, "v160".split('[')[0].split('.')[0]):
                    action.v160 = temp
                else:
                    v160 = temp 


                temp = get_nested_attribute(action, '2', locals())
                if temp is None:
                    temp = 2
                if action is not None and hasattr(action, "v161".split('[')[0].split('.')[0]):
                    action.v161 = temp
                else:
                    v161 = temp 

                for var__agl__t in range(v160, v161, 1):

                    temp = get_nested_attribute(action, 'var__agl__checkWin', locals())
                    if temp is None:
                        temp = var__agl__checkWin
                    if action is not None and hasattr(action, "v162".split('[')[0].split('.')[0]):
                        action.v162 = temp
                    else:
                        v162 = temp 

                    v163 = not v162
                    if v163:

                        temp = get_nested_attribute(action, 'True', locals())
                        if temp is None:
                            temp = True
                        if action is not None and hasattr(action, "v164".split('[')[0].split('.')[0]):
                            action.v164 = temp
                        else:
                            v164 = temp 


                        temp = get_nested_attribute(action, 'v164', locals())
                        if temp is None:
                            temp = v164
                        if action is not None and hasattr(action, "v165".split('[')[0].split('.')[0]):
                            action.v165 = temp
                        else:
                            v165 = temp 


                        temp = get_nested_attribute(action, 'v165', locals())
                        if temp is None:
                            temp = v165
                        if action is not None and hasattr(action, "var__agl__checkWin".split('[')[0].split('.')[0]):
                            action.var__agl__checkWin = temp
                        else:
                            var__agl__checkWin = temp 
                        

                    temp = get_nested_attribute(action, '2', locals())
                    if temp is None:
                        temp = 2
                    if action is not None and hasattr(action, "v166".split('[')[0].split('.')[0]):
                        action.v166 = temp
                    else:
                        v166 = temp 


                    temp = get_nested_attribute(action, '1', locals())
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v167".split('[')[0].split('.')[0]):
                        action.v167 = temp
                    else:
                        v167 = temp 

                    v168 = - np.array(v167)

                    temp = get_nested_attribute(action, '1', locals())
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v169".split('[')[0].split('.')[0]):
                        action.v169 = temp
                    else:
                        v169 = temp 

                    v170 = - np.array(v169)
                    for var__agl__d in range(v166, v168, v170):

                        temp = get_nested_attribute(action, 'var__agl__t', locals())
                        if temp is None:
                            temp = var__agl__t
                        if action is not None and hasattr(action, "v173".split('[')[0].split('.')[0]):
                            action.v173 = temp
                        else:
                            v173 = temp 


                        temp = get_nested_attribute(action, 'var__agl__d', locals())
                        if temp is None:
                            temp = var__agl__d
                        if action is not None and hasattr(action, "v174".split('[')[0].split('.')[0]):
                            action.v174 = temp
                        else:
                            v174 = temp 


                        temp = get_nested_attribute(action, 'var__agl__towersToCheck[v173].var__agl__disks[v174].state', locals())
                        if temp is None:
                            temp = var__agl__towersToCheck[v173].var__agl__disks[v174].state
                        if action is not None and hasattr(action, "v172".split('[')[0].split('.')[0]):
                            action.v172 = temp
                        else:
                            v172 = temp 


                        temp = get_nested_attribute(action, '"normal"', locals())
                        if temp is None:
                            temp = "normal"
                        if action is not None and hasattr(action, "v175".split('[')[0].split('.')[0]):
                            action.v175 = temp
                        else:
                            v175 = temp 

                        v171 = np.array(v172) != np.array(v175); v171 = tuple(v171) if isinstance(v171, np.ndarray) else v171
                        if v171:

                            temp = get_nested_attribute(action, 'False', locals())
                            if temp is None:
                                temp = False
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


                            temp = get_nested_attribute(action, 'v177', locals())
                            if temp is None:
                                temp = v177
                            if action is not None and hasattr(action, "var__agl__checkWin".split('[')[0].split('.')[0]):
                                action.var__agl__checkWin = temp
                            else:
                                var__agl__checkWin = temp 
                            

                    temp = get_nested_attribute(action, 'var__agl__checkWin', locals())
                    if temp is None:
                        temp = var__agl__checkWin
                    if action is not None and hasattr(action, "v178".split('[')[0].split('.')[0]):
                        action.v178 = temp
                    else:
                        v178 = temp 

                    if v178:

                        temp = get_nested_attribute(action, '"Solved!!!"', locals())
                        if temp is None:
                            temp = "Solved!!!"
                        if action is not None and hasattr(action, "v179".split('[')[0].split('.')[0]):
                            action.v179 = temp
                        else:
                            v179 = temp 

                        print(v179)

                        temp = get_nested_attribute(action, '"normal"', locals())
                        if temp is None:
                            temp = "normal"
                        if action is not None and hasattr(action, "v180".split('[')[0].split('.')[0]):
                            action.v180 = temp
                        else:
                            v180 = temp 


                        temp = get_nested_attribute(action, 'v180', locals())
                        if temp is None:
                            temp = v180
                        if action is not None and hasattr(action, "v181".split('[')[0].split('.')[0]):
                            action.v181 = temp
                        else:
                            v181 = temp 


                        temp = get_nested_attribute(action, 'var__agl__t', locals())
                        if temp is None:
                            temp = var__agl__t
                        if action is not None and hasattr(action, "v182".split('[')[0].split('.')[0]):
                            action.v182 = temp
                        else:
                            v182 = temp 


                        temp = get_nested_attribute(action, 'v181', locals())
                        if temp is None:
                            temp = v181
                        if action is not None and hasattr(action, "var__agl__towersToCheck[v182].var__agl__base.var__agl__solved.state".split('[')[0].split('.')[0]):
                            action.var__agl__towersToCheck[v182].var__agl__base.var__agl__solved.state = temp
                        else:
                            var__agl__towersToCheck[v182].var__agl__base.var__agl__solved.state = temp 


                        temp = get_nested_attribute(action, 'True', locals())
                        if temp is None:
                            temp = True
                        if action is not None and hasattr(action, "v183".split('[')[0].split('.')[0]):
                            action.v183 = temp
                        else:
                            v183 = temp 


                        temp = get_nested_attribute(action, 'v183', locals())
                        if temp is None:
                            temp = v183
                        if action is not None and hasattr(action, "v184".split('[')[0].split('.')[0]):
                            action.v184 = temp
                        else:
                            v184 = temp 


                        temp = get_nested_attribute(action, 'v184', locals())
                        if temp is None:
                            temp = v184
                        if action is not None and hasattr(action, "var__agl__isSolved".split('[')[0].split('.')[0]):
                            action.var__agl__isSolved = temp
                        else:
                            var__agl__isSolved = temp 
                        

                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
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


                temp = get_nested_attribute(action, 'v186', locals())
                if temp is None:
                    temp = v186
                if action is not None and hasattr(action, "var__agl__checkWin".split('[')[0].split('.')[0]):
                    action.var__agl__checkWin = temp
                else:
                    var__agl__checkWin = temp 

                self.last_var__agl__checkWin = copy.deepcopy(self.var__agl__checkWin)
        
            action = None
            super().create_object(view)
            model = None

        def __deepcopy__(self, memo=None):
            """Create a deep copy of the model."""
            if memo is None:
                memo = {} # this is required by the deepcopy protocol
            new_model = Game()

            self.copyAttributesTo(new_model)
            new_model.view = self.view
            new_model.root = self.root
            return new_model       

    #################################################################

    if model is not None:
        v187 = View()
        model.add_object(v187) # add object to model
    else:
        v187 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v187
    root.last_view = last_view

    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
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


    temp = get_nested_attribute(action, 'v189', locals())
    if temp is None:
        temp = v189
    if action is not None and hasattr(action, "v190".split('[')[0].split('.')[0]):
        action.v190 = temp
    else:
        v190 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v191".split('[')[0].split('.')[0]):
        action.v191 = temp
    else:
        v191 = temp 


    temp = get_nested_attribute(action, 'v191', locals())
    if temp is None:
        temp = v191
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


    temp = get_nested_attribute(action, '"Tower 1"', locals())
    if temp is None:
        temp = "Tower 1"
    if action is not None and hasattr(action, "v194".split('[')[0].split('.')[0]):
        action.v194 = temp
    else:
        v194 = temp 


    temp = get_nested_attribute(action, 'v194', locals())
    if temp is None:
        temp = v194
    if action is not None and hasattr(action, "v195".split('[')[0].split('.')[0]):
        action.v195 = temp
    else:
        v195 = temp 


    temp = get_nested_attribute(action, 'v195', locals())
    if temp is None:
        temp = v195
    if action is not None and hasattr(action, "v196".split('[')[0].split('.')[0]):
        action.v196 = temp
    else:
        v196 = temp 


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
    if action is not None and hasattr(action, "v197".split('[')[0].split('.')[0]):
        action.v197 = temp
    else:
        v197 = temp 


    temp = get_nested_attribute(action, 'v197', locals())
    if temp is None:
        temp = v197
    if action is not None and hasattr(action, "v198".split('[')[0].split('.')[0]):
        action.v198 = temp
    else:
        v198 = temp 


    temp = get_nested_attribute(action, 'v198', locals())
    if temp is None:
        temp = v198
    if action is not None and hasattr(action, "v199".split('[')[0].split('.')[0]):
        action.v199 = temp
    else:
        v199 = temp 


    if action is not None:
        action.v187.width = v190
        action.v187.height = v193
        action.v187.title = v196
        action.v187.background = v199
    else:
        v187.width = v190
        v187.height = v193
        v187.title = v196
        v187.background = v199

    temp = get_nested_attribute(action, 'v187', locals())
    if temp is None:
        temp = v187
    if action is not None and hasattr(action, "var__agl__view1".split('[')[0].split('.')[0]):
        action.var__agl__view1 = temp
    else:
        var__agl__view1 = temp 
    if model is not None: 
        model.var__agl__view1 = var__agl__view1
        model.last_var__agl__view1 = copy.deepcopy(var__agl__view1)

    if model is not None:
        v200 = View()
        model.add_object(v200) # add object to model
    else:
        v200 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v200
    root.last_view = last_view

    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
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
    if action is not None and hasattr(action, "v203".split('[')[0].split('.')[0]):
        action.v203 = temp
    else:
        v203 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v204".split('[')[0].split('.')[0]):
        action.v204 = temp
    else:
        v204 = temp 


    temp = get_nested_attribute(action, 'v204', locals())
    if temp is None:
        temp = v204
    if action is not None and hasattr(action, "v205".split('[')[0].split('.')[0]):
        action.v205 = temp
    else:
        v205 = temp 


    temp = get_nested_attribute(action, 'v205', locals())
    if temp is None:
        temp = v205
    if action is not None and hasattr(action, "v206".split('[')[0].split('.')[0]):
        action.v206 = temp
    else:
        v206 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v207".split('[')[0].split('.')[0]):
        action.v207 = temp
    else:
        v207 = temp 


    temp = get_nested_attribute(action, 'v207', locals())
    if temp is None:
        temp = v207
    if action is not None and hasattr(action, "v208".split('[')[0].split('.')[0]):
        action.v208 = temp
    else:
        v208 = temp 


    temp = get_nested_attribute(action, 'v208', locals())
    if temp is None:
        temp = v208
    if action is not None and hasattr(action, "v209".split('[')[0].split('.')[0]):
        action.v209 = temp
    else:
        v209 = temp 


    temp = get_nested_attribute(action, '"Tower 2"', locals())
    if temp is None:
        temp = "Tower 2"
    if action is not None and hasattr(action, "v210".split('[')[0].split('.')[0]):
        action.v210 = temp
    else:
        v210 = temp 


    temp = get_nested_attribute(action, 'v210', locals())
    if temp is None:
        temp = v210
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


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
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
    if action is not None and hasattr(action, "v215".split('[')[0].split('.')[0]):
        action.v215 = temp
    else:
        v215 = temp 


    if action is not None:
        action.v200.Ox = v203
        action.v200.width = v206
        action.v200.height = v209
        action.v200.title = v212
        action.v200.background = v215
    else:
        v200.Ox = v203
        v200.width = v206
        v200.height = v209
        v200.title = v212
        v200.background = v215

    temp = get_nested_attribute(action, 'v200', locals())
    if temp is None:
        temp = v200
    if action is not None and hasattr(action, "var__agl__view2".split('[')[0].split('.')[0]):
        action.var__agl__view2 = temp
    else:
        var__agl__view2 = temp 
    if model is not None: 
        model.var__agl__view2 = var__agl__view2
        model.last_var__agl__view2 = copy.deepcopy(var__agl__view2)

    if model is not None:
        v216 = View()
        model.add_object(v216) # add object to model
    else:
        v216 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v216
    root.last_view = last_view

    temp = get_nested_attribute(action, '1000', locals())
    if temp is None:
        temp = 1000
    if action is not None and hasattr(action, "v217".split('[')[0].split('.')[0]):
        action.v217 = temp
    else:
        v217 = temp 


    temp = get_nested_attribute(action, 'v217', locals())
    if temp is None:
        temp = v217
    if action is not None and hasattr(action, "v218".split('[')[0].split('.')[0]):
        action.v218 = temp
    else:
        v218 = temp 


    temp = get_nested_attribute(action, 'v218', locals())
    if temp is None:
        temp = v218
    if action is not None and hasattr(action, "v219".split('[')[0].split('.')[0]):
        action.v219 = temp
    else:
        v219 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
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
    if action is not None and hasattr(action, "v222".split('[')[0].split('.')[0]):
        action.v222 = temp
    else:
        v222 = temp 


    temp = get_nested_attribute(action, '500', locals())
    if temp is None:
        temp = 500
    if action is not None and hasattr(action, "v223".split('[')[0].split('.')[0]):
        action.v223 = temp
    else:
        v223 = temp 


    temp = get_nested_attribute(action, 'v223', locals())
    if temp is None:
        temp = v223
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


    temp = get_nested_attribute(action, '"Tower 3"', locals())
    if temp is None:
        temp = "Tower 3"
    if action is not None and hasattr(action, "v226".split('[')[0].split('.')[0]):
        action.v226 = temp
    else:
        v226 = temp 


    temp = get_nested_attribute(action, 'v226', locals())
    if temp is None:
        temp = v226
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


    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
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
    if action is not None and hasattr(action, "v231".split('[')[0].split('.')[0]):
        action.v231 = temp
    else:
        v231 = temp 


    if action is not None:
        action.v216.Ox = v219
        action.v216.width = v222
        action.v216.height = v225
        action.v216.title = v228
        action.v216.background = v231
    else:
        v216.Ox = v219
        v216.width = v222
        v216.height = v225
        v216.title = v228
        v216.background = v231

    temp = get_nested_attribute(action, 'v216', locals())
    if temp is None:
        temp = v216
    if action is not None and hasattr(action, "var__agl__view3".split('[')[0].split('.')[0]):
        action.var__agl__view3 = temp
    else:
        var__agl__view3 = temp 
    if model is not None: 
        model.var__agl__view3 = var__agl__view3
        model.last_var__agl__view3 = copy.deepcopy(var__agl__view3)

    if model is not None:
        model_backup = model
        v232 = Game() # this makes model = None in the end!
        model = model_backup
        model.add_object(v232) # add object to model
    else:
        v232 = Game(root_local = root, view = last_view)
      

    temp = get_nested_attribute(action, 'v232', locals())
    if temp is None:
        temp = v232
    if action is not None and hasattr(action, "v233".split('[')[0].split('.')[0]):
        action.v233 = temp
    else:
        v233 = temp 


    temp = get_nested_attribute(action, 'v233', locals())
    if temp is None:
        temp = v233
    if action is not None and hasattr(action, "var__agl__game".split('[')[0].split('.')[0]):
        action.var__agl__game = temp
    else:
        var__agl__game = temp 
    if model is not None: 
        model.var__agl__game = var__agl__game
        model.last_var__agl__game = copy.deepcopy(var__agl__game)

    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v234".split('[')[0].split('.')[0]):
        action.v234 = temp
    else:
        v234 = temp 


    temp = get_nested_attribute(action, '3', locals())
    if temp is None:
        temp = 3
    if action is not None and hasattr(action, "v235".split('[')[0].split('.')[0]):
        action.v235 = temp
    else:
        v235 = temp 

    for var__agl__d in range(v234, v235, 1):

        temp = get_nested_attribute(action, '"hidden"', locals())
        if temp is None:
            temp = "hidden"
        if action is not None and hasattr(action, "v236".split('[')[0].split('.')[0]):
            action.v236 = temp
        else:
            v236 = temp 


        temp = get_nested_attribute(action, 'v236', locals())
        if temp is None:
            temp = v236
        if action is not None and hasattr(action, "v237".split('[')[0].split('.')[0]):
            action.v237 = temp
        else:
            v237 = temp 


        temp = get_nested_attribute(action, 'var__agl__d', locals())
        if temp is None:
            temp = var__agl__d
        if action is not None and hasattr(action, "v238".split('[')[0].split('.')[0]):
            action.v238 = temp
        else:
            v238 = temp 


        temp = get_nested_attribute(action, 'v237', locals())
        if temp is None:
            temp = v237
        if action is not None and hasattr(action, "var__agl__game.var__agl__tower2.var__agl__disks[v238].state".split('[')[0].split('.')[0]):
            action.var__agl__game.var__agl__tower2.var__agl__disks[v238].state = temp
        else:
            var__agl__game.var__agl__tower2.var__agl__disks[v238].state = temp 


        temp = get_nested_attribute(action, '"hidden"', locals())
        if temp is None:
            temp = "hidden"
        if action is not None and hasattr(action, "v239".split('[')[0].split('.')[0]):
            action.v239 = temp
        else:
            v239 = temp 


        temp = get_nested_attribute(action, 'v239', locals())
        if temp is None:
            temp = v239
        if action is not None and hasattr(action, "v240".split('[')[0].split('.')[0]):
            action.v240 = temp
        else:
            v240 = temp 


        temp = get_nested_attribute(action, 'var__agl__d', locals())
        if temp is None:
            temp = var__agl__d
        if action is not None and hasattr(action, "v241".split('[')[0].split('.')[0]):
            action.v241 = temp
        else:
            v241 = temp 


        temp = get_nested_attribute(action, 'v240', locals())
        if temp is None:
            temp = v240
        if action is not None and hasattr(action, "var__agl__game.var__agl__tower3.var__agl__disks[v241].state".split('[')[0].split('.')[0]):
            action.var__agl__game.var__agl__tower3.var__agl__disks[v241].state = temp
        else:
            var__agl__game.var__agl__tower3.var__agl__disks[v241].state = temp 


    last_refresh = time.time()
    var__agl__view1.update()

    last_refresh = time.time()
    var__agl__view2.update()

    last_refresh = time.time()
    var__agl__view3.update()


    if model is not None:
        model_backup = model
        v242 = Tower() # this makes model = None in the end!
        model = model_backup
        model.add_object(v242) # add object to model
    else:
        v242 = Tower(root_local = root, view = last_view)
      

    temp = get_nested_attribute(action, 'v242', locals())
    if temp is None:
        temp = v242
    if action is not None and hasattr(action, "v243".split('[')[0].split('.')[0]):
        action.v243 = temp
    else:
        v243 = temp 


    temp = get_nested_attribute(action, 'v243', locals())
    if temp is None:
        temp = v243
    if action is not None and hasattr(action, "var__agl__from_tower".split('[')[0].split('.')[0]):
        action.var__agl__from_tower = temp
    else:
        var__agl__from_tower = temp 
    if model is not None: 
        model.var__agl__from_tower = var__agl__from_tower
        model.last_var__agl__from_tower = copy.deepcopy(var__agl__from_tower)

    temp = get_nested_attribute(action, '"hidden"', locals())
    if temp is None:
        temp = "hidden"
    if action is not None and hasattr(action, "v244".split('[')[0].split('.')[0]):
        action.v244 = temp
    else:
        v244 = temp 


    temp = get_nested_attribute(action, 'v244', locals())
    if temp is None:
        temp = v244
    if action is not None and hasattr(action, "v245".split('[')[0].split('.')[0]):
        action.v245 = temp
    else:
        v245 = temp 


    temp = get_nested_attribute(action, 'v245', locals())
    if temp is None:
        temp = v245
    if action is not None and hasattr(action, "var__agl__from_tower.state".split('[')[0].split('.')[0]):
        action.var__agl__from_tower.state = temp
    else:
        var__agl__from_tower.state = temp 


    if model is not None:
        model_backup = model
        v246 = Tower() # this makes model = None in the end!
        model = model_backup
        model.add_object(v246) # add object to model
    else:
        v246 = Tower(root_local = root, view = last_view)
      

    temp = get_nested_attribute(action, 'v246', locals())
    if temp is None:
        temp = v246
    if action is not None and hasattr(action, "v247".split('[')[0].split('.')[0]):
        action.v247 = temp
    else:
        v247 = temp 


    temp = get_nested_attribute(action, 'v247', locals())
    if temp is None:
        temp = v247
    if action is not None and hasattr(action, "var__agl__to_tower".split('[')[0].split('.')[0]):
        action.var__agl__to_tower = temp
    else:
        var__agl__to_tower = temp 
    if model is not None: 
        model.var__agl__to_tower = var__agl__to_tower
        model.last_var__agl__to_tower = copy.deepcopy(var__agl__to_tower)

    temp = get_nested_attribute(action, '"hidden"', locals())
    if temp is None:
        temp = "hidden"
    if action is not None and hasattr(action, "v248".split('[')[0].split('.')[0]):
        action.v248 = temp
    else:
        v248 = temp 


    temp = get_nested_attribute(action, 'v248', locals())
    if temp is None:
        temp = v248
    if action is not None and hasattr(action, "v249".split('[')[0].split('.')[0]):
        action.v249 = temp
    else:
        v249 = temp 


    temp = get_nested_attribute(action, 'v249', locals())
    if temp is None:
        temp = v249
    if action is not None and hasattr(action, "var__agl__to_tower.state".split('[')[0].split('.')[0]):
        action.var__agl__to_tower.state = temp
    else:
        var__agl__to_tower.state = temp 


    temp = get_nested_attribute(action, 'var__agl__game.var__agl__isSolved', locals())
    if temp is None:
        temp = var__agl__game.var__agl__isSolved
    if action is not None and hasattr(action, "v250".split('[')[0].split('.')[0]):
        action.v250 = temp
    else:
        v250 = temp 

    while True:
        v251 = root.waitClick()

        temp = get_nested_attribute(action, 'v251', locals())
        if temp is None:
            temp = v251
        if action is not None and hasattr(action, "v252".split('[')[0].split('.')[0]):
            action.v252 = temp
        else:
            v252 = temp 


        temp = get_nested_attribute(action, 'v252', locals())
        if temp is None:
            temp = v252
        if action is not None and hasattr(action, "v253".split('[')[0].split('.')[0]):
            action.v253 = temp
        else:
            v253 = temp 


        temp = get_nested_attribute(action, 'v253', locals())
        if temp is None:
            temp = v253
        if action is not None and hasattr(action, "var__agl__p1".split('[')[0].split('.')[0]):
            action.var__agl__p1 = temp
        else:
            var__agl__p1 = temp 
        if model is not None: 
            model.var__agl__p1 = var__agl__p1
            model.last_var__agl__p1 = copy.deepcopy(var__agl__p1)

        temp = get_nested_attribute(action, '0', locals())
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v256".split('[')[0].split('.')[0]):
            action.v256 = temp
        else:
            v256 = temp 


        temp = get_nested_attribute(action, 'var__agl__p1[v256]', locals())
        if temp is None:
            temp = var__agl__p1[v256]
        if action is not None and hasattr(action, "v255".split('[')[0].split('.')[0]):
            action.v255 = temp
        else:
            v255 = temp 


        temp = get_nested_attribute(action, '250', locals())
        if temp is None:
            temp = 250
        if action is not None and hasattr(action, "v257".split('[')[0].split('.')[0]):
            action.v257 = temp
        else:
            v257 = temp 

        v254 = np.array(v255) < np.array(v257); v254 = tuple(v254) if isinstance(v254, np.ndarray) else v254
        if v254:

            temp = get_nested_attribute(action, '"From Tower 1"', locals())
            if temp is None:
                temp = "From Tower 1"
            if action is not None and hasattr(action, "v258".split('[')[0].split('.')[0]):
                action.v258 = temp
            else:
                v258 = temp 

            print(v258)

            temp = get_nested_attribute(action, 'True', locals())
            if temp is None:
                temp = True
            if action is not None and hasattr(action, "v259".split('[')[0].split('.')[0]):
                action.v259 = temp
            else:
                v259 = temp 


            temp = get_nested_attribute(action, 'v259', locals())
            if temp is None:
                temp = v259
            if action is not None and hasattr(action, "v260".split('[')[0].split('.')[0]):
                action.v260 = temp
            else:
                v260 = temp 


            temp = get_nested_attribute(action, 'v260', locals())
            if temp is None:
                temp = v260
            if action is not None and hasattr(action, "var__agl__game.var__agl__tower1.var__agl__active".split('[')[0].split('.')[0]):
                action.var__agl__game.var__agl__tower1.var__agl__active = temp
            else:
                var__agl__game.var__agl__tower1.var__agl__active = temp 


            temp = get_nested_attribute(action, 'False', locals())
            if temp is None:
                temp = False
            if action is not None and hasattr(action, "v261".split('[')[0].split('.')[0]):
                action.v261 = temp
            else:
                v261 = temp 


            temp = get_nested_attribute(action, 'v261', locals())
            if temp is None:
                temp = v261
            if action is not None and hasattr(action, "v262".split('[')[0].split('.')[0]):
                action.v262 = temp
            else:
                v262 = temp 


            temp = get_nested_attribute(action, 'v262', locals())
            if temp is None:
                temp = v262
            if action is not None and hasattr(action, "var__agl__game.var__agl__tower2.var__agl__active".split('[')[0].split('.')[0]):
                action.var__agl__game.var__agl__tower2.var__agl__active = temp
            else:
                var__agl__game.var__agl__tower2.var__agl__active = temp 


            temp = get_nested_attribute(action, 'False', locals())
            if temp is None:
                temp = False
            if action is not None and hasattr(action, "v263".split('[')[0].split('.')[0]):
                action.v263 = temp
            else:
                v263 = temp 


            temp = get_nested_attribute(action, 'v263', locals())
            if temp is None:
                temp = v263
            if action is not None and hasattr(action, "v264".split('[')[0].split('.')[0]):
                action.v264 = temp
            else:
                v264 = temp 


            temp = get_nested_attribute(action, 'v264', locals())
            if temp is None:
                temp = v264
            if action is not None and hasattr(action, "var__agl__game.var__agl__tower3.var__agl__active".split('[')[0].split('.')[0]):
                action.var__agl__game.var__agl__tower3.var__agl__active = temp
            else:
                var__agl__game.var__agl__tower3.var__agl__active = temp 


            temp = get_nested_attribute(action, 'var__agl__game.var__agl__tower1', locals())
            if temp is None:
                temp = var__agl__game.var__agl__tower1
            if action is not None and hasattr(action, "v265".split('[')[0].split('.')[0]):
                action.v265 = temp
            else:
                v265 = temp 


            temp = get_nested_attribute(action, 'v265', locals())
            if temp is None:
                temp = v265
            if action is not None and hasattr(action, "v266".split('[')[0].split('.')[0]):
                action.v266 = temp
            else:
                v266 = temp 


            temp = get_nested_attribute(action, 'v266', locals())
            if temp is None:
                temp = v266
            if action is not None and hasattr(action, "var__agl__from_tower".split('[')[0].split('.')[0]):
                action.var__agl__from_tower = temp
            else:
                var__agl__from_tower = temp 
            
        else:

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v269".split('[')[0].split('.')[0]):
                action.v269 = temp
            else:
                v269 = temp 


            temp = get_nested_attribute(action, 'var__agl__p1[v269]', locals())
            if temp is None:
                temp = var__agl__p1[v269]
            if action is not None and hasattr(action, "v268".split('[')[0].split('.')[0]):
                action.v268 = temp
            else:
                v268 = temp 


            temp = get_nested_attribute(action, '750', locals())
            if temp is None:
                temp = 750
            if action is not None and hasattr(action, "v270".split('[')[0].split('.')[0]):
                action.v270 = temp
            else:
                v270 = temp 

            v267 = np.array(v268) < np.array(v270); v267 = tuple(v267) if isinstance(v267, np.ndarray) else v267
            if v267:

                temp = get_nested_attribute(action, '"From Tower 2"', locals())
                if temp is None:
                    temp = "From Tower 2"
                if action is not None and hasattr(action, "v271".split('[')[0].split('.')[0]):
                    action.v271 = temp
                else:
                    v271 = temp 

                print(v271)

                temp = get_nested_attribute(action, 'True', locals())
                if temp is None:
                    temp = True
                if action is not None and hasattr(action, "v272".split('[')[0].split('.')[0]):
                    action.v272 = temp
                else:
                    v272 = temp 


                temp = get_nested_attribute(action, 'v272', locals())
                if temp is None:
                    temp = v272
                if action is not None and hasattr(action, "v273".split('[')[0].split('.')[0]):
                    action.v273 = temp
                else:
                    v273 = temp 


                temp = get_nested_attribute(action, 'v273', locals())
                if temp is None:
                    temp = v273
                if action is not None and hasattr(action, "var__agl__game.var__agl__tower2.var__agl__active".split('[')[0].split('.')[0]):
                    action.var__agl__game.var__agl__tower2.var__agl__active = temp
                else:
                    var__agl__game.var__agl__tower2.var__agl__active = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
                if action is not None and hasattr(action, "v274".split('[')[0].split('.')[0]):
                    action.v274 = temp
                else:
                    v274 = temp 


                temp = get_nested_attribute(action, 'v274', locals())
                if temp is None:
                    temp = v274
                if action is not None and hasattr(action, "v275".split('[')[0].split('.')[0]):
                    action.v275 = temp
                else:
                    v275 = temp 


                temp = get_nested_attribute(action, 'v275', locals())
                if temp is None:
                    temp = v275
                if action is not None and hasattr(action, "var__agl__game.var__agl__tower1.var__agl__active".split('[')[0].split('.')[0]):
                    action.var__agl__game.var__agl__tower1.var__agl__active = temp
                else:
                    var__agl__game.var__agl__tower1.var__agl__active = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
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
                if action is not None and hasattr(action, "var__agl__game.var__agl__tower3.var__agl__active".split('[')[0].split('.')[0]):
                    action.var__agl__game.var__agl__tower3.var__agl__active = temp
                else:
                    var__agl__game.var__agl__tower3.var__agl__active = temp 


                temp = get_nested_attribute(action, 'var__agl__game.var__agl__tower2', locals())
                if temp is None:
                    temp = var__agl__game.var__agl__tower2
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
                if action is not None and hasattr(action, "var__agl__from_tower".split('[')[0].split('.')[0]):
                    action.var__agl__from_tower = temp
                else:
                    var__agl__from_tower = temp 
                
            else:

                temp = get_nested_attribute(action, '"From Tower 3"', locals())
                if temp is None:
                    temp = "From Tower 3"
                if action is not None and hasattr(action, "v280".split('[')[0].split('.')[0]):
                    action.v280 = temp
                else:
                    v280 = temp 

                print(v280)

                temp = get_nested_attribute(action, 'True', locals())
                if temp is None:
                    temp = True
                if action is not None and hasattr(action, "v281".split('[')[0].split('.')[0]):
                    action.v281 = temp
                else:
                    v281 = temp 


                temp = get_nested_attribute(action, 'v281', locals())
                if temp is None:
                    temp = v281
                if action is not None and hasattr(action, "v282".split('[')[0].split('.')[0]):
                    action.v282 = temp
                else:
                    v282 = temp 


                temp = get_nested_attribute(action, 'v282', locals())
                if temp is None:
                    temp = v282
                if action is not None and hasattr(action, "var__agl__game.var__agl__tower3.var__agl__active".split('[')[0].split('.')[0]):
                    action.var__agl__game.var__agl__tower3.var__agl__active = temp
                else:
                    var__agl__game.var__agl__tower3.var__agl__active = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
                if action is not None and hasattr(action, "v283".split('[')[0].split('.')[0]):
                    action.v283 = temp
                else:
                    v283 = temp 


                temp = get_nested_attribute(action, 'v283', locals())
                if temp is None:
                    temp = v283
                if action is not None and hasattr(action, "v284".split('[')[0].split('.')[0]):
                    action.v284 = temp
                else:
                    v284 = temp 


                temp = get_nested_attribute(action, 'v284', locals())
                if temp is None:
                    temp = v284
                if action is not None and hasattr(action, "var__agl__game.var__agl__tower1.var__agl__active".split('[')[0].split('.')[0]):
                    action.var__agl__game.var__agl__tower1.var__agl__active = temp
                else:
                    var__agl__game.var__agl__tower1.var__agl__active = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
                if action is not None and hasattr(action, "v285".split('[')[0].split('.')[0]):
                    action.v285 = temp
                else:
                    v285 = temp 


                temp = get_nested_attribute(action, 'v285', locals())
                if temp is None:
                    temp = v285
                if action is not None and hasattr(action, "v286".split('[')[0].split('.')[0]):
                    action.v286 = temp
                else:
                    v286 = temp 


                temp = get_nested_attribute(action, 'v286', locals())
                if temp is None:
                    temp = v286
                if action is not None and hasattr(action, "var__agl__game.var__agl__tower2.var__agl__active".split('[')[0].split('.')[0]):
                    action.var__agl__game.var__agl__tower2.var__agl__active = temp
                else:
                    var__agl__game.var__agl__tower2.var__agl__active = temp 


                temp = get_nested_attribute(action, 'var__agl__game.var__agl__tower3', locals())
                if temp is None:
                    temp = var__agl__game.var__agl__tower3
                if action is not None and hasattr(action, "v287".split('[')[0].split('.')[0]):
                    action.v287 = temp
                else:
                    v287 = temp 


                temp = get_nested_attribute(action, 'v287', locals())
                if temp is None:
                    temp = v287
                if action is not None and hasattr(action, "v288".split('[')[0].split('.')[0]):
                    action.v288 = temp
                else:
                    v288 = temp 


                temp = get_nested_attribute(action, 'v288', locals())
                if temp is None:
                    temp = v288
                if action is not None and hasattr(action, "var__agl__from_tower".split('[')[0].split('.')[0]):
                    action.var__agl__from_tower = temp
                else:
                    var__agl__from_tower = temp 

                
            
        last_refresh = time.time()
        var__agl__view1.update()

        last_refresh = time.time()
        var__agl__view2.update()

        last_refresh = time.time()
        var__agl__view3.update()

        v289 = root.waitClick()

        temp = get_nested_attribute(action, 'v289', locals())
        if temp is None:
            temp = v289
        if action is not None and hasattr(action, "v290".split('[')[0].split('.')[0]):
            action.v290 = temp
        else:
            v290 = temp 


        temp = get_nested_attribute(action, 'v290', locals())
        if temp is None:
            temp = v290
        if action is not None and hasattr(action, "v291".split('[')[0].split('.')[0]):
            action.v291 = temp
        else:
            v291 = temp 


        temp = get_nested_attribute(action, 'v291', locals())
        if temp is None:
            temp = v291
        if action is not None and hasattr(action, "var__agl__p2".split('[')[0].split('.')[0]):
            action.var__agl__p2 = temp
        else:
            var__agl__p2 = temp 
        if model is not None: 
            model.var__agl__p2 = var__agl__p2
            model.last_var__agl__p2 = copy.deepcopy(var__agl__p2)

        temp = get_nested_attribute(action, '0', locals())
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v294".split('[')[0].split('.')[0]):
            action.v294 = temp
        else:
            v294 = temp 


        temp = get_nested_attribute(action, 'var__agl__p2[v294]', locals())
        if temp is None:
            temp = var__agl__p2[v294]
        if action is not None and hasattr(action, "v293".split('[')[0].split('.')[0]):
            action.v293 = temp
        else:
            v293 = temp 


        temp = get_nested_attribute(action, '250', locals())
        if temp is None:
            temp = 250
        if action is not None and hasattr(action, "v295".split('[')[0].split('.')[0]):
            action.v295 = temp
        else:
            v295 = temp 

        v292 = np.array(v293) < np.array(v295); v292 = tuple(v292) if isinstance(v292, np.ndarray) else v292
        if v292:

            temp = get_nested_attribute(action, '"To Tower 1"', locals())
            if temp is None:
                temp = "To Tower 1"
            if action is not None and hasattr(action, "v296".split('[')[0].split('.')[0]):
                action.v296 = temp
            else:
                v296 = temp 

            print(v296)

            temp = get_nested_attribute(action, 'var__agl__game.var__agl__tower1', locals())
            if temp is None:
                temp = var__agl__game.var__agl__tower1
            if action is not None and hasattr(action, "v297".split('[')[0].split('.')[0]):
                action.v297 = temp
            else:
                v297 = temp 


            temp = get_nested_attribute(action, 'v297', locals())
            if temp is None:
                temp = v297
            if action is not None and hasattr(action, "v298".split('[')[0].split('.')[0]):
                action.v298 = temp
            else:
                v298 = temp 


            temp = get_nested_attribute(action, 'v298', locals())
            if temp is None:
                temp = v298
            if action is not None and hasattr(action, "var__agl__to_tower".split('[')[0].split('.')[0]):
                action.var__agl__to_tower = temp
            else:
                var__agl__to_tower = temp 
            
        else:

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v301".split('[')[0].split('.')[0]):
                action.v301 = temp
            else:
                v301 = temp 


            temp = get_nested_attribute(action, 'var__agl__p2[v301]', locals())
            if temp is None:
                temp = var__agl__p2[v301]
            if action is not None and hasattr(action, "v300".split('[')[0].split('.')[0]):
                action.v300 = temp
            else:
                v300 = temp 


            temp = get_nested_attribute(action, '750', locals())
            if temp is None:
                temp = 750
            if action is not None and hasattr(action, "v302".split('[')[0].split('.')[0]):
                action.v302 = temp
            else:
                v302 = temp 

            v299 = np.array(v300) < np.array(v302); v299 = tuple(v299) if isinstance(v299, np.ndarray) else v299
            if v299:

                temp = get_nested_attribute(action, '"To Tower 2"', locals())
                if temp is None:
                    temp = "To Tower 2"
                if action is not None and hasattr(action, "v303".split('[')[0].split('.')[0]):
                    action.v303 = temp
                else:
                    v303 = temp 

                print(v303)

                temp = get_nested_attribute(action, 'var__agl__game.var__agl__tower2', locals())
                if temp is None:
                    temp = var__agl__game.var__agl__tower2
                if action is not None and hasattr(action, "v304".split('[')[0].split('.')[0]):
                    action.v304 = temp
                else:
                    v304 = temp 


                temp = get_nested_attribute(action, 'v304', locals())
                if temp is None:
                    temp = v304
                if action is not None and hasattr(action, "v305".split('[')[0].split('.')[0]):
                    action.v305 = temp
                else:
                    v305 = temp 


                temp = get_nested_attribute(action, 'v305', locals())
                if temp is None:
                    temp = v305
                if action is not None and hasattr(action, "var__agl__to_tower".split('[')[0].split('.')[0]):
                    action.var__agl__to_tower = temp
                else:
                    var__agl__to_tower = temp 
                
            else:

                temp = get_nested_attribute(action, '"To Tower 3"', locals())
                if temp is None:
                    temp = "To Tower 3"
                if action is not None and hasattr(action, "v306".split('[')[0].split('.')[0]):
                    action.v306 = temp
                else:
                    v306 = temp 

                print(v306)

                temp = get_nested_attribute(action, 'var__agl__game.var__agl__tower3', locals())
                if temp is None:
                    temp = var__agl__game.var__agl__tower3
                if action is not None and hasattr(action, "v307".split('[')[0].split('.')[0]):
                    action.v307 = temp
                else:
                    v307 = temp 


                temp = get_nested_attribute(action, 'v307', locals())
                if temp is None:
                    temp = v307
                if action is not None and hasattr(action, "v308".split('[')[0].split('.')[0]):
                    action.v308 = temp
                else:
                    v308 = temp 


                temp = get_nested_attribute(action, 'v308', locals())
                if temp is None:
                    temp = v308
                if action is not None and hasattr(action, "var__agl__to_tower".split('[')[0].split('.')[0]):
                    action.var__agl__to_tower = temp
                else:
                    var__agl__to_tower = temp 

                
            

        temp = get_nested_attribute(action, 'var__agl__from_tower', locals())
        if temp is None:
            temp = var__agl__from_tower
        if action is not None and hasattr(action, "v310".split('[')[0].split('.')[0]):
            action.v310 = temp
        else:
            v310 = temp 


        temp = get_nested_attribute(action, 'var__agl__to_tower', locals())
        if temp is None:
            temp = var__agl__to_tower
        if action is not None and hasattr(action, "v311".split('[')[0].split('.')[0]):
            action.v311 = temp
        else:
            v311 = temp 

        v309 = np.array(v310) != np.array(v311); v309 = tuple(v309) if isinstance(v309, np.ndarray) else v309
        if v309:

            temp = get_nested_attribute(action, '2', locals())
            if temp is None:
                temp = 2
            if action is not None and hasattr(action, "v312".split('[')[0].split('.')[0]):
                action.v312 = temp
            else:
                v312 = temp 


            temp = get_nested_attribute(action, '1', locals())
            if temp is None:
                temp = 1
            if action is not None and hasattr(action, "v313".split('[')[0].split('.')[0]):
                action.v313 = temp
            else:
                v313 = temp 

            v314 = - np.array(v313)

            temp = get_nested_attribute(action, '1', locals())
            if temp is None:
                temp = 1
            if action is not None and hasattr(action, "v315".split('[')[0].split('.')[0]):
                action.v315 = temp
            else:
                v315 = temp 

            v316 = - np.array(v315)
            for var__agl__d in range(v312, v314, v316):

                temp = get_nested_attribute(action, 'var__agl__d', locals())
                if temp is None:
                    temp = var__agl__d
                if action is not None and hasattr(action, "v319".split('[')[0].split('.')[0]):
                    action.v319 = temp
                else:
                    v319 = temp 


                temp = get_nested_attribute(action, 'var__agl__from_tower.var__agl__disks[v319].fill', locals())
                if temp is None:
                    temp = var__agl__from_tower.var__agl__disks[v319].fill
                if action is not None and hasattr(action, "v318".split('[')[0].split('.')[0]):
                    action.v318 = temp
                else:
                    v318 = temp 


                temp = get_nested_attribute(action, '"blue"', locals())
                if temp is None:
                    temp = "blue"
                if action is not None and hasattr(action, "v320".split('[')[0].split('.')[0]):
                    action.v320 = temp
                else:
                    v320 = temp 

                v317 = np.array(v318) == np.array(v320); v317 = tuple(v317) if isinstance(v317, np.ndarray) else v317
                if v317:

                    temp = get_nested_attribute(action, 'var__agl__d', locals())
                    if temp is None:
                        temp = var__agl__d
                    if action is not None and hasattr(action, "v321".split('[')[0].split('.')[0]):
                        action.v321 = temp
                    else:
                        v321 = temp 


                    temp = get_nested_attribute(action, 'v321', locals())
                    if temp is None:
                        temp = v321
                    if action is not None and hasattr(action, "v322".split('[')[0].split('.')[0]):
                        action.v322 = temp
                    else:
                        v322 = temp 


                    temp = get_nested_attribute(action, 'v322', locals())
                    if temp is None:
                        temp = v322
                    if action is not None and hasattr(action, "v323".split('[')[0].split('.')[0]):
                        action.v323 = temp
                    else:
                        v323 = temp 


                    temp = get_nested_attribute(action, 'v323', locals())
                    if temp is None:
                        temp = v323
                    if action is not None and hasattr(action, "var__agl__toChange".split('[')[0].split('.')[0]):
                        action.var__agl__toChange = temp
                    else:
                        var__agl__toChange = temp 
                    if model is not None: 
                        model.var__agl__toChange = var__agl__toChange
                        model.last_var__agl__toChange = copy.deepcopy(var__agl__toChange)    

            temp = get_nested_attribute(action, 'False', locals())
            if temp is None:
                temp = False
            if action is not None and hasattr(action, "v324".split('[')[0].split('.')[0]):
                action.v324 = temp
            else:
                v324 = temp 


            temp = get_nested_attribute(action, 'v324', locals())
            if temp is None:
                temp = v324
            if action is not None and hasattr(action, "v325".split('[')[0].split('.')[0]):
                action.v325 = temp
            else:
                v325 = temp 


            temp = get_nested_attribute(action, 'v325', locals())
            if temp is None:
                temp = v325
            if action is not None and hasattr(action, "v326".split('[')[0].split('.')[0]):
                action.v326 = temp
            else:
                v326 = temp 


            temp = get_nested_attribute(action, 'v326', locals())
            if temp is None:
                temp = v326
            if action is not None and hasattr(action, "var__agl__hasValues".split('[')[0].split('.')[0]):
                action.var__agl__hasValues = temp
            else:
                var__agl__hasValues = temp 
            if model is not None: 
                model.var__agl__hasValues = var__agl__hasValues
                model.last_var__agl__hasValues = copy.deepcopy(var__agl__hasValues)

            temp = get_nested_attribute(action, '2', locals())
            if temp is None:
                temp = 2
            if action is not None and hasattr(action, "v327".split('[')[0].split('.')[0]):
                action.v327 = temp
            else:
                v327 = temp 


            temp = get_nested_attribute(action, '1', locals())
            if temp is None:
                temp = 1
            if action is not None and hasattr(action, "v328".split('[')[0].split('.')[0]):
                action.v328 = temp
            else:
                v328 = temp 

            v329 = - np.array(v328)

            temp = get_nested_attribute(action, '1', locals())
            if temp is None:
                temp = 1
            if action is not None and hasattr(action, "v330".split('[')[0].split('.')[0]):
                action.v330 = temp
            else:
                v330 = temp 

            v331 = - np.array(v330)
            for var__agl__d in range(v327, v329, v331):

                temp = get_nested_attribute(action, 'var__agl__d', locals())
                if temp is None:
                    temp = var__agl__d
                if action is not None and hasattr(action, "v335".split('[')[0].split('.')[0]):
                    action.v335 = temp
                else:
                    v335 = temp 


                temp = get_nested_attribute(action, 'var__agl__to_tower.var__agl__disks[v335].state', locals())
                if temp is None:
                    temp = var__agl__to_tower.var__agl__disks[v335].state
                if action is not None and hasattr(action, "v334".split('[')[0].split('.')[0]):
                    action.v334 = temp
                else:
                    v334 = temp 


                temp = get_nested_attribute(action, '"normal"', locals())
                if temp is None:
                    temp = "normal"
                if action is not None and hasattr(action, "v336".split('[')[0].split('.')[0]):
                    action.v336 = temp
                else:
                    v336 = temp 

                v333 = np.array(v334) == np.array(v336); v333 = tuple(v333) if isinstance(v333, np.ndarray) else v333

                temp = get_nested_attribute(action, 'var__agl__hasValues', locals())
                if temp is None:
                    temp = var__agl__hasValues
                if action is not None and hasattr(action, "v338".split('[')[0].split('.')[0]):
                    action.v338 = temp
                else:
                    v338 = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
                if action is not None and hasattr(action, "v339".split('[')[0].split('.')[0]):
                    action.v339 = temp
                else:
                    v339 = temp 

                v337 = np.array(v338) == np.array(v339); v337 = tuple(v337) if isinstance(v337, np.ndarray) else v337
                v332 = v333 and v337; v332 = tuple(v332) if isinstance(v332, np.ndarray) else v332
                if v332:

                    temp = get_nested_attribute(action, 'var__agl__toChange', locals())
                    if temp is None:
                        temp = var__agl__toChange
                    if action is not None and hasattr(action, "v341".split('[')[0].split('.')[0]):
                        action.v341 = temp
                    else:
                        v341 = temp 


                    temp = get_nested_attribute(action, '0', locals())
                    if temp is None:
                        temp = 0
                    if action is not None and hasattr(action, "v342".split('[')[0].split('.')[0]):
                        action.v342 = temp
                    else:
                        v342 = temp 


                    temp = get_nested_attribute(action, 'var__agl__from_tower.var__agl__disks[v341].length[v342]', locals())
                    if temp is None:
                        temp = var__agl__from_tower.var__agl__disks[v341].length[v342]
                    if action is not None and hasattr(action, "v340".split('[')[0].split('.')[0]):
                        action.v340 = temp
                    else:
                        v340 = temp 

                    print(v340)

                    temp = get_nested_attribute(action, 'var__agl__d', locals())
                    if temp is None:
                        temp = var__agl__d
                    if action is not None and hasattr(action, "v344".split('[')[0].split('.')[0]):
                        action.v344 = temp
                    else:
                        v344 = temp 


                    temp = get_nested_attribute(action, '0', locals())
                    if temp is None:
                        temp = 0
                    if action is not None and hasattr(action, "v345".split('[')[0].split('.')[0]):
                        action.v345 = temp
                    else:
                        v345 = temp 


                    temp = get_nested_attribute(action, 'var__agl__to_tower.var__agl__disks[v344].length[v345]', locals())
                    if temp is None:
                        temp = var__agl__to_tower.var__agl__disks[v344].length[v345]
                    if action is not None and hasattr(action, "v343".split('[')[0].split('.')[0]):
                        action.v343 = temp
                    else:
                        v343 = temp 

                    print(v343)

                    temp = get_nested_attribute(action, 'var__agl__toChange', locals())
                    if temp is None:
                        temp = var__agl__toChange
                    if action is not None and hasattr(action, "v348".split('[')[0].split('.')[0]):
                        action.v348 = temp
                    else:
                        v348 = temp 


                    temp = get_nested_attribute(action, '0', locals())
                    if temp is None:
                        temp = 0
                    if action is not None and hasattr(action, "v349".split('[')[0].split('.')[0]):
                        action.v349 = temp
                    else:
                        v349 = temp 


                    temp = get_nested_attribute(action, 'var__agl__from_tower.var__agl__disks[v348].length[v349]', locals())
                    if temp is None:
                        temp = var__agl__from_tower.var__agl__disks[v348].length[v349]
                    if action is not None and hasattr(action, "v347".split('[')[0].split('.')[0]):
                        action.v347 = temp
                    else:
                        v347 = temp 


                    temp = get_nested_attribute(action, 'var__agl__d', locals())
                    if temp is None:
                        temp = var__agl__d
                    if action is not None and hasattr(action, "v351".split('[')[0].split('.')[0]):
                        action.v351 = temp
                    else:
                        v351 = temp 


                    temp = get_nested_attribute(action, '0', locals())
                    if temp is None:
                        temp = 0
                    if action is not None and hasattr(action, "v352".split('[')[0].split('.')[0]):
                        action.v352 = temp
                    else:
                        v352 = temp 


                    temp = get_nested_attribute(action, 'var__agl__to_tower.var__agl__disks[v351].length[v352]', locals())
                    if temp is None:
                        temp = var__agl__to_tower.var__agl__disks[v351].length[v352]
                    if action is not None and hasattr(action, "v350".split('[')[0].split('.')[0]):
                        action.v350 = temp
                    else:
                        v350 = temp 

                    v346 = np.array(v347) < np.array(v350); v346 = tuple(v346) if isinstance(v346, np.ndarray) else v346
                    if v346:

                        temp = get_nested_attribute(action, '"hidden"', locals())
                        if temp is None:
                            temp = "hidden"
                        if action is not None and hasattr(action, "v353".split('[')[0].split('.')[0]):
                            action.v353 = temp
                        else:
                            v353 = temp 


                        temp = get_nested_attribute(action, 'v353', locals())
                        if temp is None:
                            temp = v353
                        if action is not None and hasattr(action, "v354".split('[')[0].split('.')[0]):
                            action.v354 = temp
                        else:
                            v354 = temp 


                        temp = get_nested_attribute(action, 'var__agl__toChange', locals())
                        if temp is None:
                            temp = var__agl__toChange
                        if action is not None and hasattr(action, "v355".split('[')[0].split('.')[0]):
                            action.v355 = temp
                        else:
                            v355 = temp 


                        temp = get_nested_attribute(action, 'v354', locals())
                        if temp is None:
                            temp = v354
                        if action is not None and hasattr(action, "var__agl__from_tower.var__agl__disks[v355].state".split('[')[0].split('.')[0]):
                            action.var__agl__from_tower.var__agl__disks[v355].state = temp
                        else:
                            var__agl__from_tower.var__agl__disks[v355].state = temp 


                        temp = get_nested_attribute(action, '"normal"', locals())
                        if temp is None:
                            temp = "normal"
                        if action is not None and hasattr(action, "v356".split('[')[0].split('.')[0]):
                            action.v356 = temp
                        else:
                            v356 = temp 


                        temp = get_nested_attribute(action, 'v356', locals())
                        if temp is None:
                            temp = v356
                        if action is not None and hasattr(action, "v357".split('[')[0].split('.')[0]):
                            action.v357 = temp
                        else:
                            v357 = temp 


                        temp = get_nested_attribute(action, 'var__agl__toChange', locals())
                        if temp is None:
                            temp = var__agl__toChange
                        if action is not None and hasattr(action, "v358".split('[')[0].split('.')[0]):
                            action.v358 = temp
                        else:
                            v358 = temp 


                        temp = get_nested_attribute(action, 'v357', locals())
                        if temp is None:
                            temp = v357
                        if action is not None and hasattr(action, "var__agl__to_tower.var__agl__disks[v358].state".split('[')[0].split('.')[0]):
                            action.var__agl__to_tower.var__agl__disks[v358].state = temp
                        else:
                            var__agl__to_tower.var__agl__disks[v358].state = temp 


                        temp = get_nested_attribute(action, 'False', locals())
                        if temp is None:
                            temp = False
                        if action is not None and hasattr(action, "v359".split('[')[0].split('.')[0]):
                            action.v359 = temp
                        else:
                            v359 = temp 


                        temp = get_nested_attribute(action, 'v359', locals())
                        if temp is None:
                            temp = v359
                        if action is not None and hasattr(action, "v360".split('[')[0].split('.')[0]):
                            action.v360 = temp
                        else:
                            v360 = temp 


                        temp = get_nested_attribute(action, 'v360', locals())
                        if temp is None:
                            temp = v360
                        if action is not None and hasattr(action, "var__agl__from_tower.var__agl__active".split('[')[0].split('.')[0]):
                            action.var__agl__from_tower.var__agl__active = temp
                        else:
                            var__agl__from_tower.var__agl__active = temp 
                        

                    temp = get_nested_attribute(action, 'True', locals())
                    if temp is None:
                        temp = True
                    if action is not None and hasattr(action, "v361".split('[')[0].split('.')[0]):
                        action.v361 = temp
                    else:
                        v361 = temp 


                    temp = get_nested_attribute(action, 'v361', locals())
                    if temp is None:
                        temp = v361
                    if action is not None and hasattr(action, "v362".split('[')[0].split('.')[0]):
                        action.v362 = temp
                    else:
                        v362 = temp 


                    temp = get_nested_attribute(action, 'v362', locals())
                    if temp is None:
                        temp = v362
                    if action is not None and hasattr(action, "var__agl__hasValues".split('[')[0].split('.')[0]):
                        action.var__agl__hasValues = temp
                    else:
                        var__agl__hasValues = temp 
                    

            temp = get_nested_attribute(action, 'var__agl__hasValues', locals())
            if temp is None:
                temp = var__agl__hasValues
            if action is not None and hasattr(action, "v363".split('[')[0].split('.')[0]):
                action.v363 = temp
            else:
                v363 = temp 

            v364 = not v363
            if v364:

                temp = get_nested_attribute(action, '"hidden"', locals())
                if temp is None:
                    temp = "hidden"
                if action is not None and hasattr(action, "v365".split('[')[0].split('.')[0]):
                    action.v365 = temp
                else:
                    v365 = temp 


                temp = get_nested_attribute(action, 'v365', locals())
                if temp is None:
                    temp = v365
                if action is not None and hasattr(action, "v366".split('[')[0].split('.')[0]):
                    action.v366 = temp
                else:
                    v366 = temp 


                temp = get_nested_attribute(action, 'var__agl__toChange', locals())
                if temp is None:
                    temp = var__agl__toChange
                if action is not None and hasattr(action, "v367".split('[')[0].split('.')[0]):
                    action.v367 = temp
                else:
                    v367 = temp 


                temp = get_nested_attribute(action, 'v366', locals())
                if temp is None:
                    temp = v366
                if action is not None and hasattr(action, "var__agl__from_tower.var__agl__disks[v367].state".split('[')[0].split('.')[0]):
                    action.var__agl__from_tower.var__agl__disks[v367].state = temp
                else:
                    var__agl__from_tower.var__agl__disks[v367].state = temp 


                temp = get_nested_attribute(action, '"normal"', locals())
                if temp is None:
                    temp = "normal"
                if action is not None and hasattr(action, "v368".split('[')[0].split('.')[0]):
                    action.v368 = temp
                else:
                    v368 = temp 


                temp = get_nested_attribute(action, 'v368', locals())
                if temp is None:
                    temp = v368
                if action is not None and hasattr(action, "v369".split('[')[0].split('.')[0]):
                    action.v369 = temp
                else:
                    v369 = temp 


                temp = get_nested_attribute(action, 'var__agl__toChange', locals())
                if temp is None:
                    temp = var__agl__toChange
                if action is not None and hasattr(action, "v370".split('[')[0].split('.')[0]):
                    action.v370 = temp
                else:
                    v370 = temp 


                temp = get_nested_attribute(action, 'v369', locals())
                if temp is None:
                    temp = v369
                if action is not None and hasattr(action, "var__agl__to_tower.var__agl__disks[v370].state".split('[')[0].split('.')[0]):
                    action.var__agl__to_tower.var__agl__disks[v370].state = temp
                else:
                    var__agl__to_tower.var__agl__disks[v370].state = temp 


                temp = get_nested_attribute(action, 'False', locals())
                if temp is None:
                    temp = False
                if action is not None and hasattr(action, "v371".split('[')[0].split('.')[0]):
                    action.v371 = temp
                else:
                    v371 = temp 


                temp = get_nested_attribute(action, 'v371', locals())
                if temp is None:
                    temp = v371
                if action is not None and hasattr(action, "v372".split('[')[0].split('.')[0]):
                    action.v372 = temp
                else:
                    v372 = temp 


                temp = get_nested_attribute(action, 'v372', locals())
                if temp is None:
                    temp = v372
                if action is not None and hasattr(action, "var__agl__from_tower.var__agl__active".split('[')[0].split('.')[0]):
                    action.var__agl__from_tower.var__agl__active = temp
                else:
                    var__agl__from_tower.var__agl__active = temp 
                

            temp = get_nested_attribute(action, 'True', locals())
            if temp is None:
                temp = True
            if action is not None and hasattr(action, "v373".split('[')[0].split('.')[0]):
                action.v373 = temp
            else:
                v373 = temp 


            temp = get_nested_attribute(action, 'v373', locals())
            if temp is None:
                temp = v373
            if action is not None and hasattr(action, "v374".split('[')[0].split('.')[0]):
                action.v374 = temp
            else:
                v374 = temp 


            temp = get_nested_attribute(action, 'v374', locals())
            if temp is None:
                temp = v374
            if action is not None and hasattr(action, "var__agl__game.var__agl__checkWin".split('[')[0].split('.')[0]):
                action.var__agl__game.var__agl__checkWin = temp
            else:
                var__agl__game.var__agl__checkWin = temp 

            last_refresh = time.time()
            var__agl__view1.update()

            last_refresh = time.time()
            var__agl__view2.update()

            last_refresh = time.time()
            var__agl__view3.update()
            
        else:

            temp = get_nested_attribute(action, '"Invalid transaction"', locals())
            if temp is None:
                temp = "Invalid transaction"
            if action is not None and hasattr(action, "v375".split('[')[0].split('.')[0]):
                action.v375 = temp
            else:
                v375 = temp 

            print(v375)

            temp = get_nested_attribute(action, 'False', locals())
            if temp is None:
                temp = False
            if action is not None and hasattr(action, "v376".split('[')[0].split('.')[0]):
                action.v376 = temp
            else:
                v376 = temp 


            temp = get_nested_attribute(action, 'v376', locals())
            if temp is None:
                temp = v376
            if action is not None and hasattr(action, "v377".split('[')[0].split('.')[0]):
                action.v377 = temp
            else:
                v377 = temp 


            temp = get_nested_attribute(action, 'v377', locals())
            if temp is None:
                temp = v377
            if action is not None and hasattr(action, "var__agl__from_tower.var__agl__active".split('[')[0].split('.')[0]):
                action.var__agl__from_tower.var__agl__active = temp
            else:
                var__agl__from_tower.var__agl__active = temp 

            last_refresh = time.time()
            var__agl__view1.update()

            last_refresh = time.time()
            var__agl__view2.update()

            last_refresh = time.time()
            var__agl__view3.update()

            
        # refresh the condition

        temp = get_nested_attribute(action, 'var__agl__game.var__agl__isSolved', locals())
        if temp is None:
            temp = var__agl__game.var__agl__isSolved
        if action is not None and hasattr(action, "v250".split('[')[0].split('.')[0]):
            action.v250 = temp
        else:
            v250 = temp 

        ##
        if v250:
            break   # Repeat until condition is false
    v378 = root.waitClick()

    temp = get_nested_attribute(action, 'v378', locals())
    if temp is None:
        temp = v378
    if action is not None and hasattr(action, "v379".split('[')[0].split('.')[0]):
        action.v379 = temp
    else:
        v379 = temp 


    temp = get_nested_attribute(action, 'v379', locals())
    if temp is None:
        temp = v379
    if action is not None and hasattr(action, "v380".split('[')[0].split('.')[0]):
        action.v380 = temp
    else:
        v380 = temp 


    temp = get_nested_attribute(action, 'v380', locals())
    if temp is None:
        temp = v380
    if action is not None and hasattr(action, "var__agl__p".split('[')[0].split('.')[0]):
        action.var__agl__p = temp
    else:
        var__agl__p = temp 
    if model is not None: 
        model.var__agl__p = var__agl__p
        model.last_var__agl__p = copy.deepcopy(var__agl__p)
    var__agl__view1.close(); views.remove(var__agl__view1) if last_view != var__agl__view1 else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == var__agl__view1 else last_view
    root.last_view = last_view
    var__agl__view2.close(); views.remove(var__agl__view2) if last_view != var__agl__view2 else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == var__agl__view2 else last_view
    root.last_view = last_view
    var__agl__view3.close(); views.remove(var__agl__view3) if last_view != var__agl__view3 else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == var__agl__view3 else last_view
    root.last_view = last_view
