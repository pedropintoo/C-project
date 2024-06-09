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
    class model1(Model):
        def __init__(self, root_local: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root_local, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
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
            if action is not None and hasattr(action, "var__agl__cellSize".split('[')[0].split('.')[0]):
                action.var__agl__cellSize = temp
            else:
                var__agl__cellSize = temp 
            if model is not None: 
                model.var__agl__cellSize = var__agl__cellSize
                model.last_var__agl__cellSize = copy.deepcopy(var__agl__cellSize)

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v4".split('[')[0].split('.')[0]):
                action.v4 = temp
            else:
                v4 = temp 


            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v5".split('[')[0].split('.')[0]):
                action.v5 = temp
            else:
                v5 = temp 

            v3 = (v4 , v5); v3 = tuple(v3) if isinstance(v3, np.ndarray) else v3

            if model is not None:
                v6 = Rectangle()
                model.add_object(v6) # add object to model
            else:
                v6 = Rectangle(root = root)
            v6.origin = v3

            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v8".split('[')[0].split('.')[0]):
                action.v8 = temp
            else:
                v8 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v9".split('[')[0].split('.')[0]):
                action.v9 = temp
            else:
                v9 = temp 

            v7 = (v8 , v9); v7 = tuple(v7) if isinstance(v7, np.ndarray) else v7

            temp = get_nested_attribute(action, 'v7', locals())
            if temp is None:
                temp = v7
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


            temp = get_nested_attribute(action, '"orange"', locals())
            if temp is None:
                temp = "orange"
            if action is not None and hasattr(action, "v12".split('[')[0].split('.')[0]):
                action.v12 = temp
            else:
                v12 = temp 


            temp = get_nested_attribute(action, 'v12', locals())
            if temp is None:
                temp = v12
            if action is not None and hasattr(action, "v13".split('[')[0].split('.')[0]):
                action.v13 = temp
            else:
                v13 = temp 


            temp = get_nested_attribute(action, 'v13', locals())
            if temp is None:
                temp = v13
            if action is not None and hasattr(action, "v14".split('[')[0].split('.')[0]):
                action.v14 = temp
            else:
                v14 = temp 


            if action is not None:
                action.v6.length = v11
                action.v6.fill = v14
            else:
                v6.length = v11
                v6.fill = v14

            temp = get_nested_attribute(action, 'v6', locals())
            if temp is None:
                temp = v6
            if action is not None and hasattr(action, "var__agl__rec".split('[')[0].split('.')[0]):
                action.var__agl__rec = temp
            else:
                var__agl__rec = temp 
            if model is not None: 
                model.var__agl__rec = var__agl__rec
                model.last_var__agl__rec = copy.deepcopy(var__agl__rec)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v16".split('[')[0].split('.')[0]):
                action.v16 = temp
            else:
                v16 = temp 


            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v17".split('[')[0].split('.')[0]):
                action.v17 = temp
            else:
                v17 = temp 

            v15 = (v16 , v17); v15 = tuple(v15) if isinstance(v15, np.ndarray) else v15

            if model is not None:
                v18 = Ellipse()
                model.add_object(v18) # add object to model
            else:
                v18 = Ellipse(root = root)
            v18.origin = v15

            temp = get_nested_attribute(action, '60', locals())
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v20".split('[')[0].split('.')[0]):
                action.v20 = temp
            else:
                v20 = temp 


            temp = get_nested_attribute(action, '40', locals())
            if temp is None:
                temp = 40
            if action is not None and hasattr(action, "v21".split('[')[0].split('.')[0]):
                action.v21 = temp
            else:
                v21 = temp 

            v19 = (v20 , v21); v19 = tuple(v19) if isinstance(v19, np.ndarray) else v19

            temp = get_nested_attribute(action, 'v19', locals())
            if temp is None:
                temp = v19
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


            temp = get_nested_attribute(action, '"blue"', locals())
            if temp is None:
                temp = "blue"
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


            temp = get_nested_attribute(action, 'v25', locals())
            if temp is None:
                temp = v25
            if action is not None and hasattr(action, "v26".split('[')[0].split('.')[0]):
                action.v26 = temp
            else:
                v26 = temp 


            if action is not None:
                action.v18.length = v23
                action.v18.fill = v26
            else:
                v18.length = v23
                v18.fill = v26

            temp = get_nested_attribute(action, 'v18', locals())
            if temp is None:
                temp = v18
            if action is not None and hasattr(action, "var__agl__ell".split('[')[0].split('.')[0]):
                action.var__agl__ell = temp
            else:
                var__agl__ell = temp 
            if model is not None: 
                model.var__agl__ell = var__agl__ell
                model.last_var__agl__ell = copy.deepcopy(var__agl__ell)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v28".split('[')[0].split('.')[0]):
                action.v28 = temp
            else:
                v28 = temp 

            v29 = - np.array(v28)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v30".split('[')[0].split('.')[0]):
                action.v30 = temp
            else:
                v30 = temp 

            v31 = - np.array(v30)
            v27 = (v29 , v31); v27 = tuple(v27) if isinstance(v27, np.ndarray) else v27

            if model is not None:
                v32 = Arc()
                model.add_object(v32) # add object to model
            else:
                v32 = Arc(root = root)
            v32.origin = v27

            temp = get_nested_attribute(action, '30', locals())
            if temp is None:
                temp = 30
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


            temp = get_nested_attribute(action, '90', locals())
            if temp is None:
                temp = 90
            if action is not None and hasattr(action, "v36".split('[')[0].split('.')[0]):
                action.v36 = temp
            else:
                v36 = temp 


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
            if action is not None and hasattr(action, "v38".split('[')[0].split('.')[0]):
                action.v38 = temp
            else:
                v38 = temp 


            temp = get_nested_attribute(action, '60', locals())
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v40".split('[')[0].split('.')[0]):
                action.v40 = temp
            else:
                v40 = temp 


            temp = get_nested_attribute(action, '40', locals())
            if temp is None:
                temp = 40
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


            temp = get_nested_attribute(action, '"green"', locals())
            if temp is None:
                temp = "green"
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
                action.v32.start = v35
                action.v32.extent = v38
                action.v32.length = v43
                action.v32.outline = v46
            else:
                v32.start = v35
                v32.extent = v38
                v32.length = v43
                v32.outline = v46

            temp = get_nested_attribute(action, 'v32', locals())
            if temp is None:
                temp = v32
            if action is not None and hasattr(action, "var__agl__arc".split('[')[0].split('.')[0]):
                action.var__agl__arc = temp
            else:
                var__agl__arc = temp 
            if model is not None: 
                model.var__agl__arc = var__agl__arc
                model.last_var__agl__arc = copy.deepcopy(var__agl__arc)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v48".split('[')[0].split('.')[0]):
                action.v48 = temp
            else:
                v48 = temp 


            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v49".split('[')[0].split('.')[0]):
                action.v49 = temp
            else:
                v49 = temp 

            v50 = - np.array(v49)
            v47 = (v48 , v50); v47 = tuple(v47) if isinstance(v47, np.ndarray) else v47

            if model is not None:
                v51 = ArcChord()
                model.add_object(v51) # add object to model
            else:
                v51 = ArcChord(root = root)
            v51.origin = v47

            temp = get_nested_attribute(action, '30', locals())
            if temp is None:
                temp = 30
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
            if action is not None and hasattr(action, "v54".split('[')[0].split('.')[0]):
                action.v54 = temp
            else:
                v54 = temp 


            temp = get_nested_attribute(action, '200', locals())
            if temp is None:
                temp = 200
            if action is not None and hasattr(action, "v55".split('[')[0].split('.')[0]):
                action.v55 = temp
            else:
                v55 = temp 


            temp = get_nested_attribute(action, 'v55', locals())
            if temp is None:
                temp = v55
            if action is not None and hasattr(action, "v56".split('[')[0].split('.')[0]):
                action.v56 = temp
            else:
                v56 = temp 


            temp = get_nested_attribute(action, 'v56', locals())
            if temp is None:
                temp = v56
            if action is not None and hasattr(action, "v57".split('[')[0].split('.')[0]):
                action.v57 = temp
            else:
                v57 = temp 


            temp = get_nested_attribute(action, '60', locals())
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v59".split('[')[0].split('.')[0]):
                action.v59 = temp
            else:
                v59 = temp 


            temp = get_nested_attribute(action, '40', locals())
            if temp is None:
                temp = 40
            if action is not None and hasattr(action, "v60".split('[')[0].split('.')[0]):
                action.v60 = temp
            else:
                v60 = temp 

            v58 = (v59 , v60); v58 = tuple(v58) if isinstance(v58, np.ndarray) else v58

            temp = get_nested_attribute(action, 'v58', locals())
            if temp is None:
                temp = v58
            if action is not None and hasattr(action, "v61".split('[')[0].split('.')[0]):
                action.v61 = temp
            else:
                v61 = temp 


            temp = get_nested_attribute(action, 'v61', locals())
            if temp is None:
                temp = v61
            if action is not None and hasattr(action, "v62".split('[')[0].split('.')[0]):
                action.v62 = temp
            else:
                v62 = temp 


            temp = get_nested_attribute(action, '"red"', locals())
            if temp is None:
                temp = "red"
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


            temp = get_nested_attribute(action, 'v64', locals())
            if temp is None:
                temp = v64
            if action is not None and hasattr(action, "v65".split('[')[0].split('.')[0]):
                action.v65 = temp
            else:
                v65 = temp 


            temp = get_nested_attribute(action, '"blue"', locals())
            if temp is None:
                temp = "blue"
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
            if action is not None and hasattr(action, "v68".split('[')[0].split('.')[0]):
                action.v68 = temp
            else:
                v68 = temp 


            if action is not None:
                action.v51.start = v54
                action.v51.extent = v57
                action.v51.length = v62
                action.v51.fill = v65
                action.v51.outline = v68
            else:
                v51.start = v54
                v51.extent = v57
                v51.length = v62
                v51.fill = v65
                v51.outline = v68

            temp = get_nested_attribute(action, 'v51', locals())
            if temp is None:
                temp = v51
            if action is not None and hasattr(action, "var__agl__arcchord".split('[')[0].split('.')[0]):
                action.var__agl__arcchord = temp
            else:
                var__agl__arcchord = temp 
            if model is not None: 
                model.var__agl__arcchord = var__agl__arcchord
                model.last_var__agl__arcchord = copy.deepcopy(var__agl__arcchord)

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
            new_model = model1()

            self.copyAttributesTo(new_model)
            new_model.view = self.view
            new_model.root = self.root
            return new_model       

    #################################################################
    #################################################################
    ## Model
    #################################################################
    class model2(Model):
        def __init__(self, root_local: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root_local, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '100', locals())
            if temp is None:
                temp = 100
            if action is not None and hasattr(action, "v69".split('[')[0].split('.')[0]):
                action.v69 = temp
            else:
                v69 = temp 


            temp = get_nested_attribute(action, 'v69', locals())
            if temp is None:
                temp = v69
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
            if action is not None and hasattr(action, "var__agl__cellSize".split('[')[0].split('.')[0]):
                action.var__agl__cellSize = temp
            else:
                var__agl__cellSize = temp 
            if model is not None: 
                model.var__agl__cellSize = var__agl__cellSize
                model.last_var__agl__cellSize = copy.deepcopy(var__agl__cellSize)

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v73".split('[')[0].split('.')[0]):
                action.v73 = temp
            else:
                v73 = temp 


            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v74".split('[')[0].split('.')[0]):
                action.v74 = temp
            else:
                v74 = temp 

            v72 = (v73 , v74); v72 = tuple(v72) if isinstance(v72, np.ndarray) else v72

            if model is not None:
                v75 = Rectangle()
                model.add_object(v75) # add object to model
            else:
                v75 = Rectangle(root = root)
            v75.origin = v72

            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v77".split('[')[0].split('.')[0]):
                action.v77 = temp
            else:
                v77 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v78".split('[')[0].split('.')[0]):
                action.v78 = temp
            else:
                v78 = temp 

            v76 = (v77 , v78); v76 = tuple(v76) if isinstance(v76, np.ndarray) else v76

            temp = get_nested_attribute(action, 'v76', locals())
            if temp is None:
                temp = v76
            if action is not None and hasattr(action, "v79".split('[')[0].split('.')[0]):
                action.v79 = temp
            else:
                v79 = temp 


            temp = get_nested_attribute(action, 'v79', locals())
            if temp is None:
                temp = v79
            if action is not None and hasattr(action, "v80".split('[')[0].split('.')[0]):
                action.v80 = temp
            else:
                v80 = temp 


            temp = get_nested_attribute(action, '"orange"', locals())
            if temp is None:
                temp = "orange"
            if action is not None and hasattr(action, "v81".split('[')[0].split('.')[0]):
                action.v81 = temp
            else:
                v81 = temp 


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
            if action is not None and hasattr(action, "v83".split('[')[0].split('.')[0]):
                action.v83 = temp
            else:
                v83 = temp 


            if action is not None:
                action.v75.length = v80
                action.v75.fill = v83
            else:
                v75.length = v80
                v75.fill = v83

            temp = get_nested_attribute(action, 'v75', locals())
            if temp is None:
                temp = v75
            if action is not None and hasattr(action, "var__agl__rec".split('[')[0].split('.')[0]):
                action.var__agl__rec = temp
            else:
                var__agl__rec = temp 
            if model is not None: 
                model.var__agl__rec = var__agl__rec
                model.last_var__agl__rec = copy.deepcopy(var__agl__rec)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v85".split('[')[0].split('.')[0]):
                action.v85 = temp
            else:
                v85 = temp 


            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v86".split('[')[0].split('.')[0]):
                action.v86 = temp
            else:
                v86 = temp 

            v84 = (v85 , v86); v84 = tuple(v84) if isinstance(v84, np.ndarray) else v84

            if model is not None:
                v87 = Ellipse()
                model.add_object(v87) # add object to model
            else:
                v87 = Ellipse(root = root)
            v87.origin = v84

            temp = get_nested_attribute(action, '60', locals())
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v89".split('[')[0].split('.')[0]):
                action.v89 = temp
            else:
                v89 = temp 


            temp = get_nested_attribute(action, '40', locals())
            if temp is None:
                temp = 40
            if action is not None and hasattr(action, "v90".split('[')[0].split('.')[0]):
                action.v90 = temp
            else:
                v90 = temp 

            v88 = (v89 , v90); v88 = tuple(v88) if isinstance(v88, np.ndarray) else v88

            temp = get_nested_attribute(action, 'v88', locals())
            if temp is None:
                temp = v88
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


            temp = get_nested_attribute(action, '"blue"', locals())
            if temp is None:
                temp = "blue"
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
            if action is not None and hasattr(action, "v95".split('[')[0].split('.')[0]):
                action.v95 = temp
            else:
                v95 = temp 


            if action is not None:
                action.v87.length = v92
                action.v87.fill = v95
            else:
                v87.length = v92
                v87.fill = v95

            temp = get_nested_attribute(action, 'v87', locals())
            if temp is None:
                temp = v87
            if action is not None and hasattr(action, "var__agl__ell".split('[')[0].split('.')[0]):
                action.var__agl__ell = temp
            else:
                var__agl__ell = temp 
            if model is not None: 
                model.var__agl__ell = var__agl__ell
                model.last_var__agl__ell = copy.deepcopy(var__agl__ell)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v97".split('[')[0].split('.')[0]):
                action.v97 = temp
            else:
                v97 = temp 

            v98 = - np.array(v97)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v99".split('[')[0].split('.')[0]):
                action.v99 = temp
            else:
                v99 = temp 

            v100 = - np.array(v99)
            v96 = (v98 , v100); v96 = tuple(v96) if isinstance(v96, np.ndarray) else v96

            if model is not None:
                v101 = Arc()
                model.add_object(v101) # add object to model
            else:
                v101 = Arc(root = root)
            v101.origin = v96

            temp = get_nested_attribute(action, '30', locals())
            if temp is None:
                temp = 30
            if action is not None and hasattr(action, "v102".split('[')[0].split('.')[0]):
                action.v102 = temp
            else:
                v102 = temp 


            temp = get_nested_attribute(action, 'v102', locals())
            if temp is None:
                temp = v102
            if action is not None and hasattr(action, "v103".split('[')[0].split('.')[0]):
                action.v103 = temp
            else:
                v103 = temp 


            temp = get_nested_attribute(action, 'v103', locals())
            if temp is None:
                temp = v103
            if action is not None and hasattr(action, "v104".split('[')[0].split('.')[0]):
                action.v104 = temp
            else:
                v104 = temp 


            temp = get_nested_attribute(action, '90', locals())
            if temp is None:
                temp = 90
            if action is not None and hasattr(action, "v105".split('[')[0].split('.')[0]):
                action.v105 = temp
            else:
                v105 = temp 


            temp = get_nested_attribute(action, 'v105', locals())
            if temp is None:
                temp = v105
            if action is not None and hasattr(action, "v106".split('[')[0].split('.')[0]):
                action.v106 = temp
            else:
                v106 = temp 


            temp = get_nested_attribute(action, 'v106', locals())
            if temp is None:
                temp = v106
            if action is not None and hasattr(action, "v107".split('[')[0].split('.')[0]):
                action.v107 = temp
            else:
                v107 = temp 


            temp = get_nested_attribute(action, '60', locals())
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v109".split('[')[0].split('.')[0]):
                action.v109 = temp
            else:
                v109 = temp 


            temp = get_nested_attribute(action, '40', locals())
            if temp is None:
                temp = 40
            if action is not None and hasattr(action, "v110".split('[')[0].split('.')[0]):
                action.v110 = temp
            else:
                v110 = temp 

            v108 = (v109 , v110); v108 = tuple(v108) if isinstance(v108, np.ndarray) else v108

            temp = get_nested_attribute(action, 'v108', locals())
            if temp is None:
                temp = v108
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


            temp = get_nested_attribute(action, '"green"', locals())
            if temp is None:
                temp = "green"
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


            temp = get_nested_attribute(action, 'v114', locals())
            if temp is None:
                temp = v114
            if action is not None and hasattr(action, "v115".split('[')[0].split('.')[0]):
                action.v115 = temp
            else:
                v115 = temp 


            if action is not None:
                action.v101.start = v104
                action.v101.extent = v107
                action.v101.length = v112
                action.v101.outline = v115
            else:
                v101.start = v104
                v101.extent = v107
                v101.length = v112
                v101.outline = v115

            temp = get_nested_attribute(action, 'v101', locals())
            if temp is None:
                temp = v101
            if action is not None and hasattr(action, "var__agl__arc".split('[')[0].split('.')[0]):
                action.var__agl__arc = temp
            else:
                var__agl__arc = temp 
            if model is not None: 
                model.var__agl__arc = var__agl__arc
                model.last_var__agl__arc = copy.deepcopy(var__agl__arc)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v117".split('[')[0].split('.')[0]):
                action.v117 = temp
            else:
                v117 = temp 


            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v118".split('[')[0].split('.')[0]):
                action.v118 = temp
            else:
                v118 = temp 

            v119 = - np.array(v118)
            v116 = (v117 , v119); v116 = tuple(v116) if isinstance(v116, np.ndarray) else v116

            if model is not None:
                v120 = ArcChord()
                model.add_object(v120) # add object to model
            else:
                v120 = ArcChord(root = root)
            v120.origin = v116

            temp = get_nested_attribute(action, '30', locals())
            if temp is None:
                temp = 30
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


            temp = get_nested_attribute(action, '200', locals())
            if temp is None:
                temp = 200
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


            temp = get_nested_attribute(action, '60', locals())
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v128".split('[')[0].split('.')[0]):
                action.v128 = temp
            else:
                v128 = temp 


            temp = get_nested_attribute(action, '40', locals())
            if temp is None:
                temp = 40
            if action is not None and hasattr(action, "v129".split('[')[0].split('.')[0]):
                action.v129 = temp
            else:
                v129 = temp 

            v127 = (v128 , v129); v127 = tuple(v127) if isinstance(v127, np.ndarray) else v127

            temp = get_nested_attribute(action, 'v127', locals())
            if temp is None:
                temp = v127
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


            temp = get_nested_attribute(action, '"red"', locals())
            if temp is None:
                temp = "red"
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


            temp = get_nested_attribute(action, 'v133', locals())
            if temp is None:
                temp = v133
            if action is not None and hasattr(action, "v134".split('[')[0].split('.')[0]):
                action.v134 = temp
            else:
                v134 = temp 


            temp = get_nested_attribute(action, '"blue"', locals())
            if temp is None:
                temp = "blue"
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


            temp = get_nested_attribute(action, 'v136', locals())
            if temp is None:
                temp = v136
            if action is not None and hasattr(action, "v137".split('[')[0].split('.')[0]):
                action.v137 = temp
            else:
                v137 = temp 


            if action is not None:
                action.v120.start = v123
                action.v120.extent = v126
                action.v120.length = v131
                action.v120.fill = v134
                action.v120.outline = v137
            else:
                v120.start = v123
                v120.extent = v126
                v120.length = v131
                v120.fill = v134
                v120.outline = v137

            temp = get_nested_attribute(action, 'v120', locals())
            if temp is None:
                temp = v120
            if action is not None and hasattr(action, "var__agl__arcchord".split('[')[0].split('.')[0]):
                action.var__agl__arcchord = temp
            else:
                var__agl__arcchord = temp 
            if model is not None: 
                model.var__agl__arcchord = var__agl__arcchord
                model.last_var__agl__arcchord = copy.deepcopy(var__agl__arcchord)

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
            new_model = model2()

            self.copyAttributesTo(new_model)
            new_model.view = self.view
            new_model.root = self.root
            return new_model       

    #################################################################
    #################################################################
    ## Model
    #################################################################
    class model3(Model):
        def __init__(self, root_local: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root_local, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '200', locals())
            if temp is None:
                temp = 200
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


            temp = get_nested_attribute(action, 'v139', locals())
            if temp is None:
                temp = v139
            if action is not None and hasattr(action, "v140".split('[')[0].split('.')[0]):
                action.v140 = temp
            else:
                v140 = temp 


            temp = get_nested_attribute(action, 'v140', locals())
            if temp is None:
                temp = v140
            if action is not None and hasattr(action, "var__agl__cellSize".split('[')[0].split('.')[0]):
                action.var__agl__cellSize = temp
            else:
                var__agl__cellSize = temp 
            if model is not None: 
                model.var__agl__cellSize = var__agl__cellSize
                model.last_var__agl__cellSize = copy.deepcopy(var__agl__cellSize)

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v142".split('[')[0].split('.')[0]):
                action.v142 = temp
            else:
                v142 = temp 


            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v143".split('[')[0].split('.')[0]):
                action.v143 = temp
            else:
                v143 = temp 

            v141 = (v142 , v143); v141 = tuple(v141) if isinstance(v141, np.ndarray) else v141

            if model is not None:
                v144 = Rectangle()
                model.add_object(v144) # add object to model
            else:
                v144 = Rectangle(root = root)
            v144.origin = v141

            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v146".split('[')[0].split('.')[0]):
                action.v146 = temp
            else:
                v146 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v147".split('[')[0].split('.')[0]):
                action.v147 = temp
            else:
                v147 = temp 

            v145 = (v146 , v147); v145 = tuple(v145) if isinstance(v145, np.ndarray) else v145

            temp = get_nested_attribute(action, 'v145', locals())
            if temp is None:
                temp = v145
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


            temp = get_nested_attribute(action, '"orange"', locals())
            if temp is None:
                temp = "orange"
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


            if action is not None:
                action.v144.length = v149
                action.v144.fill = v152
            else:
                v144.length = v149
                v144.fill = v152

            temp = get_nested_attribute(action, 'v144', locals())
            if temp is None:
                temp = v144
            if action is not None and hasattr(action, "var__agl__rec".split('[')[0].split('.')[0]):
                action.var__agl__rec = temp
            else:
                var__agl__rec = temp 
            if model is not None: 
                model.var__agl__rec = var__agl__rec
                model.last_var__agl__rec = copy.deepcopy(var__agl__rec)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v154".split('[')[0].split('.')[0]):
                action.v154 = temp
            else:
                v154 = temp 


            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v155".split('[')[0].split('.')[0]):
                action.v155 = temp
            else:
                v155 = temp 

            v153 = (v154 , v155); v153 = tuple(v153) if isinstance(v153, np.ndarray) else v153

            if model is not None:
                v156 = Ellipse()
                model.add_object(v156) # add object to model
            else:
                v156 = Ellipse(root = root)
            v156.origin = v153

            temp = get_nested_attribute(action, '60', locals())
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v158".split('[')[0].split('.')[0]):
                action.v158 = temp
            else:
                v158 = temp 


            temp = get_nested_attribute(action, '40', locals())
            if temp is None:
                temp = 40
            if action is not None and hasattr(action, "v159".split('[')[0].split('.')[0]):
                action.v159 = temp
            else:
                v159 = temp 

            v157 = (v158 , v159); v157 = tuple(v157) if isinstance(v157, np.ndarray) else v157

            temp = get_nested_attribute(action, 'v157', locals())
            if temp is None:
                temp = v157
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


            temp = get_nested_attribute(action, '"blue"', locals())
            if temp is None:
                temp = "blue"
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
                action.v156.length = v161
                action.v156.fill = v164
            else:
                v156.length = v161
                v156.fill = v164

            temp = get_nested_attribute(action, 'v156', locals())
            if temp is None:
                temp = v156
            if action is not None and hasattr(action, "var__agl__ell".split('[')[0].split('.')[0]):
                action.var__agl__ell = temp
            else:
                var__agl__ell = temp 
            if model is not None: 
                model.var__agl__ell = var__agl__ell
                model.last_var__agl__ell = copy.deepcopy(var__agl__ell)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v166".split('[')[0].split('.')[0]):
                action.v166 = temp
            else:
                v166 = temp 

            v167 = - np.array(v166)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v168".split('[')[0].split('.')[0]):
                action.v168 = temp
            else:
                v168 = temp 

            v169 = - np.array(v168)
            v165 = (v167 , v169); v165 = tuple(v165) if isinstance(v165, np.ndarray) else v165

            if model is not None:
                v170 = Arc()
                model.add_object(v170) # add object to model
            else:
                v170 = Arc(root = root)
            v170.origin = v165

            temp = get_nested_attribute(action, '30', locals())
            if temp is None:
                temp = 30
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


            temp = get_nested_attribute(action, '90', locals())
            if temp is None:
                temp = 90
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
            if action is not None and hasattr(action, "v176".split('[')[0].split('.')[0]):
                action.v176 = temp
            else:
                v176 = temp 


            temp = get_nested_attribute(action, '60', locals())
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v178".split('[')[0].split('.')[0]):
                action.v178 = temp
            else:
                v178 = temp 


            temp = get_nested_attribute(action, '40', locals())
            if temp is None:
                temp = 40
            if action is not None and hasattr(action, "v179".split('[')[0].split('.')[0]):
                action.v179 = temp
            else:
                v179 = temp 

            v177 = (v178 , v179); v177 = tuple(v177) if isinstance(v177, np.ndarray) else v177

            temp = get_nested_attribute(action, 'v177', locals())
            if temp is None:
                temp = v177
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


            temp = get_nested_attribute(action, '"green"', locals())
            if temp is None:
                temp = "green"
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


            temp = get_nested_attribute(action, 'v183', locals())
            if temp is None:
                temp = v183
            if action is not None and hasattr(action, "v184".split('[')[0].split('.')[0]):
                action.v184 = temp
            else:
                v184 = temp 


            if action is not None:
                action.v170.start = v173
                action.v170.extent = v176
                action.v170.length = v181
                action.v170.outline = v184
            else:
                v170.start = v173
                v170.extent = v176
                v170.length = v181
                v170.outline = v184

            temp = get_nested_attribute(action, 'v170', locals())
            if temp is None:
                temp = v170
            if action is not None and hasattr(action, "var__agl__arc".split('[')[0].split('.')[0]):
                action.var__agl__arc = temp
            else:
                var__agl__arc = temp 
            if model is not None: 
                model.var__agl__arc = var__agl__arc
                model.last_var__agl__arc = copy.deepcopy(var__agl__arc)

            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v186".split('[')[0].split('.')[0]):
                action.v186 = temp
            else:
                v186 = temp 


            temp = get_nested_attribute(action, 'var__agl__cellSize', locals())
            if temp is None:
                temp = var__agl__cellSize
            if action is not None and hasattr(action, "v187".split('[')[0].split('.')[0]):
                action.v187 = temp
            else:
                v187 = temp 

            v188 = - np.array(v187)
            v185 = (v186 , v188); v185 = tuple(v185) if isinstance(v185, np.ndarray) else v185

            if model is not None:
                v189 = ArcChord()
                model.add_object(v189) # add object to model
            else:
                v189 = ArcChord(root = root)
            v189.origin = v185

            temp = get_nested_attribute(action, '30', locals())
            if temp is None:
                temp = 30
            if action is not None and hasattr(action, "v190".split('[')[0].split('.')[0]):
                action.v190 = temp
            else:
                v190 = temp 


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
            if action is not None and hasattr(action, "v192".split('[')[0].split('.')[0]):
                action.v192 = temp
            else:
                v192 = temp 


            temp = get_nested_attribute(action, '200', locals())
            if temp is None:
                temp = 200
            if action is not None and hasattr(action, "v193".split('[')[0].split('.')[0]):
                action.v193 = temp
            else:
                v193 = temp 


            temp = get_nested_attribute(action, 'v193', locals())
            if temp is None:
                temp = v193
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


            temp = get_nested_attribute(action, '60', locals())
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v197".split('[')[0].split('.')[0]):
                action.v197 = temp
            else:
                v197 = temp 


            temp = get_nested_attribute(action, '40', locals())
            if temp is None:
                temp = 40
            if action is not None and hasattr(action, "v198".split('[')[0].split('.')[0]):
                action.v198 = temp
            else:
                v198 = temp 

            v196 = (v197 , v198); v196 = tuple(v196) if isinstance(v196, np.ndarray) else v196

            temp = get_nested_attribute(action, 'v196', locals())
            if temp is None:
                temp = v196
            if action is not None and hasattr(action, "v199".split('[')[0].split('.')[0]):
                action.v199 = temp
            else:
                v199 = temp 


            temp = get_nested_attribute(action, 'v199', locals())
            if temp is None:
                temp = v199
            if action is not None and hasattr(action, "v200".split('[')[0].split('.')[0]):
                action.v200 = temp
            else:
                v200 = temp 


            temp = get_nested_attribute(action, '"red"', locals())
            if temp is None:
                temp = "red"
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


            temp = get_nested_attribute(action, '"blue"', locals())
            if temp is None:
                temp = "blue"
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


            if action is not None:
                action.v189.start = v192
                action.v189.extent = v195
                action.v189.length = v200
                action.v189.fill = v203
                action.v189.outline = v206
            else:
                v189.start = v192
                v189.extent = v195
                v189.length = v200
                v189.fill = v203
                v189.outline = v206

            temp = get_nested_attribute(action, 'v189', locals())
            if temp is None:
                temp = v189
            if action is not None and hasattr(action, "var__agl__arcchord".split('[')[0].split('.')[0]):
                action.var__agl__arcchord = temp
            else:
                var__agl__arcchord = temp 
            if model is not None: 
                model.var__agl__arcchord = var__agl__arcchord
                model.last_var__agl__arcchord = copy.deepcopy(var__agl__arcchord)

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
            new_model = model3()

            self.copyAttributesTo(new_model)
            new_model.view = self.view
            new_model.root = self.root
            return new_model       

    #################################################################
    #################################################################
    ## Model
    #################################################################
    class model_compose(Model):
        def __init__(self, root_local: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root_local, view=view, origin=origin)
            model = self

            if model is not None:
                model_backup = model
                v207 = model1() # this makes model = None in the end!
                model = model_backup
                model.add_object(v207) # add object to model
            else:
                v207 = model1(root_local = root, view = last_view)
              

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
            if action is not None and hasattr(action, "var__agl__Model1".split('[')[0].split('.')[0]):
                action.var__agl__Model1 = temp
            else:
                var__agl__Model1 = temp 
            if model is not None: 
                model.var__agl__Model1 = var__agl__Model1
                model.last_var__agl__Model1 = copy.deepcopy(var__agl__Model1)

            if model is not None:
                model_backup = model
                v209 = model2() # this makes model = None in the end!
                model = model_backup
                model.add_object(v209) # add object to model
            else:
                v209 = model2(root_local = root, view = last_view)
              

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
            if action is not None and hasattr(action, "var__agl__Model2".split('[')[0].split('.')[0]):
                action.var__agl__Model2 = temp
            else:
                var__agl__Model2 = temp 
            if model is not None: 
                model.var__agl__Model2 = var__agl__Model2
                model.last_var__agl__Model2 = copy.deepcopy(var__agl__Model2)

            if model is not None:
                model_backup = model
                v211 = model3() # this makes model = None in the end!
                model = model_backup
                model.add_object(v211) # add object to model
            else:
                v211 = model3(root_local = root, view = last_view)
              

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
            if action is not None and hasattr(action, "var__agl__Model3".split('[')[0].split('.')[0]):
                action.var__agl__Model3 = temp
            else:
                var__agl__Model3 = temp 
            if model is not None: 
                model.var__agl__Model3 = var__agl__Model3
                model.last_var__agl__Model3 = copy.deepcopy(var__agl__Model3)

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
            new_model = model_compose()

            self.copyAttributesTo(new_model)
            new_model.view = self.view
            new_model.root = self.root
            return new_model       

    #################################################################

    if model is not None:
        v213 = View()
        model.add_object(v213) # add object to model
    else:
        v213 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v213
    root.last_view = last_view

    temp = get_nested_attribute(action, '800', locals())
    if temp is None:
        temp = 800
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


    temp = get_nested_attribute(action, 'v215', locals())
    if temp is None:
        temp = v215
    if action is not None and hasattr(action, "v216".split('[')[0].split('.')[0]):
        action.v216 = temp
    else:
        v216 = temp 


    temp = get_nested_attribute(action, '600', locals())
    if temp is None:
        temp = 600
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


    temp = get_nested_attribute(action, '"black"', locals())
    if temp is None:
        temp = "black"
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


    if action is not None:
        action.v213.width = v216
        action.v213.height = v219
        action.v213.background = v222
    else:
        v213.width = v216
        v213.height = v219
        v213.background = v222

    temp = get_nested_attribute(action, 'v213', locals())
    if temp is None:
        temp = v213
    if action is not None and hasattr(action, "var__agl__view".split('[')[0].split('.')[0]):
        action.var__agl__view = temp
    else:
        var__agl__view = temp 
    if model is not None: 
        model.var__agl__view = var__agl__view
        model.last_var__agl__view = copy.deepcopy(var__agl__view)

    if model is not None:
        model_backup = model
        v223 = model_compose() # this makes model = None in the end!
        model = model_backup
        model.add_object(v223) # add object to model
    else:
        v223 = model_compose(root_local = root, view = last_view)
      

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
    if action is not None and hasattr(action, "var__agl__model_test".split('[')[0].split('.')[0]):
        action.var__agl__model_test = temp
    else:
        var__agl__model_test = temp 
    if model is not None: 
        model.var__agl__model_test = var__agl__model_test
        model.last_var__agl__model_test = copy.deepcopy(var__agl__model_test)

    last_refresh = time.time()
    var__agl__view.update()

    v225 = root.waitClick()

    temp = get_nested_attribute(action, 'v225', locals())
    if temp is None:
        temp = v225
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
    if action is not None and hasattr(action, "var__agl__p".split('[')[0].split('.')[0]):
        action.var__agl__p = temp
    else:
        var__agl__p = temp 
    if model is not None: 
        model.var__agl__p = var__agl__p
        model.last_var__agl__p = copy.deepcopy(var__agl__p)

    temp = get_nested_attribute(action, '1', locals())
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v228".split('[')[0].split('.')[0]):
        action.v228 = temp
    else:
        v228 = temp 


    temp = get_nested_attribute(action, '720', locals())
    if temp is None:
        temp = 720
    if action is not None and hasattr(action, "v229".split('[')[0].split('.')[0]):
        action.v229 = temp
    else:
        v229 = temp 

    for var__agl__i in range(v228, v229, 1):

        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v230".split('[')[0].split('.')[0]):
            action.v230 = temp
        else:
            v230 = temp 

        if action is not None:
            action.var__agl__model_test.rotate(v230)
        else:
            var__agl__model_test.rotate(v230)

        temp = get_nested_attribute(action, '3', locals())
        if temp is None:
            temp = 3
        if action is not None and hasattr(action, "v231".split('[')[0].split('.')[0]):
            action.v231 = temp
        else:
            v231 = temp 

        v232 = - np.array(v231)
        if action is not None:
            action.var__agl__model_test.var__agl__Model2.rotate(v232)
        else:
            var__agl__model_test.var__agl__Model2.rotate(v232)

        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v233".split('[')[0].split('.')[0]):
            action.v233 = temp
        else:
            v233 = temp 

        if action is not None:
            action.var__agl__model_test.var__agl__Model3.rotate(v233)
        else:
            var__agl__model_test.var__agl__Model3.rotate(v233)

        temp = get_nested_attribute(action, '4', locals())
        if temp is None:
            temp = 4
        if action is not None and hasattr(action, "v234".split('[')[0].split('.')[0]):
            action.v234 = temp
        else:
            v234 = temp 

        if action is not None:
            action.var__agl__model_test.var__agl__Model2.var__agl__rec.rotate(v234)
        else:
            var__agl__model_test.var__agl__Model2.var__agl__rec.rotate(v234)

        temp = get_nested_attribute(action, '3', locals())
        if temp is None:
            temp = 3
        if action is not None and hasattr(action, "v235".split('[')[0].split('.')[0]):
            action.v235 = temp
        else:
            v235 = temp 

        v236 = - np.array(v235)
        if action is not None:
            action.var__agl__model_test.var__agl__Model2.var__agl__arc.rotate(v236)
        else:
            var__agl__model_test.var__agl__Model2.var__agl__arc.rotate(v236)

        temp = get_nested_attribute(action, '5', locals())
        if temp is None:
            temp = 5
        if action is not None and hasattr(action, "v237".split('[')[0].split('.')[0]):
            action.v237 = temp
        else:
            v237 = temp 

        v238 = - np.array(v237)
        if action is not None:
            action.var__agl__model_test.var__agl__Model3.var__agl__arcchord.rotate(v238)
        else:
            var__agl__model_test.var__agl__Model3.var__agl__arcchord.rotate(v238)

        temp = get_nested_attribute(action, '5', locals())
        if temp is None:
            temp = 5
        if action is not None and hasattr(action, "v239".split('[')[0].split('.')[0]):
            action.v239 = temp
        else:
            v239 = temp 

        v240 = - np.array(v239)
        if action is not None:
            action.var__agl__model_test.var__agl__Model1.var__agl__rec.rotate(v240)
        else:
            var__agl__model_test.var__agl__Model1.var__agl__rec.rotate(v240)

        temp = get_nested_attribute(action, '0.01', locals())
        if temp is None:
            temp = 0.01
        if action is not None and hasattr(action, "v241".split('[')[0].split('.')[0]):
            action.v241 = temp
        else:
            v241 = temp 

         
        while (time.time() - last_refresh <= v241):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        var__agl__view.update()


    last_refresh = time.time()
    var__agl__view.update()

    v242 = root.waitClick()

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
    if action is not None and hasattr(action, "var__agl__p".split('[')[0].split('.')[0]):
        action.var__agl__p = temp
    else:
        var__agl__p = temp 

