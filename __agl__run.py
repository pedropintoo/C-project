from tkinter import *
from src.XAGL.AGLClasses import *
import math
import time, os, sys
import copy
from enum import Enum, auto
import numpy as np
from antlr4 import *
from src.XAGL.XAGLLexer import XAGLLexer
from src.XAGL.XAGLParser import XAGLParser
from src.XAGL.Interpreter import Interpreter
from src.XAGL.Semantic import Semantic
from src.XAGL.VarTypes import *

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
#################################################################
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
def transform_dict(original_dict):
    new_dict = {}
    for key, value in original_dict.items():
        if (key != 'root'):
            new_dict[key] = Var(value)
    return new_dict        
#################################################################

if __name__ == "__main__":
    root = Root(views, last_view)

    #################################################################
    ## Model
    #################################################################
    class Pacman(Model):
        def __init__(self, root_local: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root_local, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v1".split('[')[0].split('.')[0]):
                action.v1 = temp
            else:
                v1 = temp 


            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v2".split('[')[0].split('.')[0]):
                action.v2 = temp
            else:
                v2 = temp 

            v0 = (v1 , v2); v0 = tuple(v0) if isinstance(v0, np.ndarray) else v0

            if model is not None:
                v3 = PieSlice()
                model.add_object(v3) # add object to model
            else:
                v3 = PieSlice(root = root)
            v3.origin = v0

            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v5".split('[')[0].split('.')[0]):
                action.v5 = temp
            else:
                v5 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v6".split('[')[0].split('.')[0]):
                action.v6 = temp
            else:
                v6 = temp 

            v4 = (v5 , v6); v4 = tuple(v4) if isinstance(v4, np.ndarray) else v4

            temp = get_nested_attribute(action, 'v4', locals())
            if temp is None:
                temp = v4
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


            temp = get_nested_attribute(action, '"pink"', locals())
            if temp is None:
                temp = "pink"
            if action is not None and hasattr(action, "v9".split('[')[0].split('.')[0]):
                action.v9 = temp
            else:
                v9 = temp 


            temp = get_nested_attribute(action, 'v9', locals())
            if temp is None:
                temp = v9
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


            temp = get_nested_attribute(action, '30', locals())
            if temp is None:
                temp = 30
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


            temp = get_nested_attribute(action, '300', locals())
            if temp is None:
                temp = 300
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


            temp = get_nested_attribute(action, 'v16', locals())
            if temp is None:
                temp = v16
            if action is not None and hasattr(action, "v17".split('[')[0].split('.')[0]):
                action.v17 = temp
            else:
                v17 = temp 


            if action is not None:
                action.v3.length = v8
                action.v3.fill = v11
                action.v3.start = v14
                action.v3.extent = v17
            else:
                v3.length = v8
                v3.fill = v11
                v3.start = v14
                v3.extent = v17

            temp = get_nested_attribute(action, 'v3', locals())
            if temp is None:
                temp = v3
            if action is not None and hasattr(action, "var__agl__face".split('[')[0].split('.')[0]):
                action.var__agl__face = temp
            else:
                var__agl__face = temp 
            if model is not None: 
                model.var__agl__face = var__agl__face
                model.last_var__agl__face = copy.deepcopy(var__agl__face)

            temp = get_nested_attribute(action, '20', locals())
            if temp is None:
                temp = 20
            if action is not None and hasattr(action, "v19".split('[')[0].split('.')[0]):
                action.v19 = temp
            else:
                v19 = temp 


            temp = get_nested_attribute(action, '35', locals())
            if temp is None:
                temp = 35
            if action is not None and hasattr(action, "v20".split('[')[0].split('.')[0]):
                action.v20 = temp
            else:
                v20 = temp 

            v18 = (v19 , v20); v18 = tuple(v18) if isinstance(v18, np.ndarray) else v18

            if model is not None:
                v21 = Ellipse()
                model.add_object(v21) # add object to model
            else:
                v21 = Ellipse(root = root)
            v21.origin = v18

            temp = get_nested_attribute(action, '"black"', locals())
            if temp is None:
                temp = "black"
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


            temp = get_nested_attribute(action, 'v23', locals())
            if temp is None:
                temp = v23
            if action is not None and hasattr(action, "v24".split('[')[0].split('.')[0]):
                action.v24 = temp
            else:
                v24 = temp 


            temp = get_nested_attribute(action, '5', locals())
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v26".split('[')[0].split('.')[0]):
                action.v26 = temp
            else:
                v26 = temp 


            temp = get_nested_attribute(action, '5', locals())
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v27".split('[')[0].split('.')[0]):
                action.v27 = temp
            else:
                v27 = temp 

            v25 = (v26 , v27); v25 = tuple(v25) if isinstance(v25, np.ndarray) else v25

            temp = get_nested_attribute(action, 'v25', locals())
            if temp is None:
                temp = v25
            if action is not None and hasattr(action, "v28".split('[')[0].split('.')[0]):
                action.v28 = temp
            else:
                v28 = temp 


            temp = get_nested_attribute(action, 'v28', locals())
            if temp is None:
                temp = v28
            if action is not None and hasattr(action, "v29".split('[')[0].split('.')[0]):
                action.v29 = temp
            else:
                v29 = temp 


            if action is not None:
                action.v21.fill = v24
                action.v21.length = v29
            else:
                v21.fill = v24
                v21.length = v29
            class v30(Enum):
                var__agl__Open = auto()
                var__agl__Close = auto() 
            global var__agl__Open; var__agl__Open = v30.var__agl__Open
            global var__agl__Close; var__agl__Close = v30.var__agl__Close   
            v31 = v30(1) # first is default

            temp = get_nested_attribute(action, 'v31', locals())
            if temp is None:
                temp = v31
            if action is not None and hasattr(action, "v32".split('[')[0].split('.')[0]):
                action.v32 = temp
            else:
                v32 = temp 


            temp = get_nested_attribute(action, 'v32', locals())
            if temp is None:
                temp = v32
            if action is not None and hasattr(action, "var__agl__mouth".split('[')[0].split('.')[0]):
                action.var__agl__mouth = temp
            else:
                var__agl__mouth = temp 
            if model is not None: 
                model.var__agl__mouth = var__agl__mouth
                model.last_var__agl__mouth = copy.deepcopy(var__agl__mouth)

            self.fixCoords()

        def create_object(self, view):
            action = self

            if self.var__agl__mouth != self.last_var__agl__mouth:

                temp = get_nested_attribute(action, 'var__agl__mouth', locals())
                if temp is None:
                    temp = var__agl__mouth
                if action is not None and hasattr(action, "v34".split('[')[0].split('.')[0]):
                    action.v34 = temp
                else:
                    v34 = temp 


                temp = get_nested_attribute(action, 'var__agl__Open', locals())
                if temp is None:
                    temp = var__agl__Open
                if action is not None and hasattr(action, "v35".split('[')[0].split('.')[0]):
                    action.v35 = temp
                else:
                    v35 = temp 

                v33 = np.array(v34) == np.array(v35); v33 = tuple(v33) if isinstance(v33, np.ndarray) else v33
                if v33:

                    temp = get_nested_attribute(action, '30', locals())
                    if temp is None:
                        temp = 30
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


                    temp = get_nested_attribute(action, '300', locals())
                    if temp is None:
                        temp = 300
                    if action is not None and hasattr(action, "v39".split('[')[0].split('.')[0]):
                        action.v39 = temp
                    else:
                        v39 = temp 


                    temp = get_nested_attribute(action, 'v39', locals())
                    if temp is None:
                        temp = v39
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


                    if action is not None:
                        action.var__agl__face.start = v38
                        action.var__agl__face.extent = v41
                    else:
                        var__agl__face.start = v38
                        var__agl__face.extent = v41    
                else:

                    temp = get_nested_attribute(action, '1', locals())
                    if temp is None:
                        temp = 1
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


                    temp = get_nested_attribute(action, '359', locals())
                    if temp is None:
                        temp = 359
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


                    temp = get_nested_attribute(action, 'v46', locals())
                    if temp is None:
                        temp = v46
                    if action is not None and hasattr(action, "v47".split('[')[0].split('.')[0]):
                        action.v47 = temp
                    else:
                        v47 = temp 


                    if action is not None:
                        action.var__agl__face.start = v44
                        action.var__agl__face.extent = v47
                    else:
                        var__agl__face.start = v44
                        var__agl__face.extent = v47
                    
                self.last_var__agl__mouth = copy.deepcopy(self.var__agl__mouth)
        
            action = None
            super().create_object(view)
            model = None

        def __deepcopy__(self, memo=None):
            """Create a deep copy of the model."""
            if memo is None:
                memo = {} # this is required by the deepcopy protocol
            new_model = Pacman()

            self.copyAttributesTo(new_model)
            new_model.view = self.view
            new_model.root = self.root
            return new_model       

    #################################################################

    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v49".split('[')[0].split('.')[0]):
        action.v49 = temp
    else:
        v49 = temp 


    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v50".split('[')[0].split('.')[0]):
        action.v50 = temp
    else:
        v50 = temp 

    v48 = (v49 , v50); v48 = tuple(v48) if isinstance(v48, np.ndarray) else v48

    if model is not None:
        v51 = Rectangle()
        model.add_object(v51) # add object to model
    else:
        v51 = Rectangle(root = root)
    v51.origin = v48

    temp = get_nested_attribute(action, '1000', locals())
    if temp is None:
        temp = 1000
    if action is not None and hasattr(action, "v53".split('[')[0].split('.')[0]):
        action.v53 = temp
    else:
        v53 = temp 


    temp = get_nested_attribute(action, '70', locals())
    if temp is None:
        temp = 70
    if action is not None and hasattr(action, "v54".split('[')[0].split('.')[0]):
        action.v54 = temp
    else:
        v54 = temp 

    v52 = (v53 , v54); v52 = tuple(v52) if isinstance(v52, np.ndarray) else v52

    temp = get_nested_attribute(action, 'v52', locals())
    if temp is None:
        temp = v52
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


    temp = get_nested_attribute(action, '"blue"', locals())
    if temp is None:
        temp = "blue"
    if action is not None and hasattr(action, "v57".split('[')[0].split('.')[0]):
        action.v57 = temp
    else:
        v57 = temp 


    temp = get_nested_attribute(action, 'v57', locals())
    if temp is None:
        temp = v57
    if action is not None and hasattr(action, "v58".split('[')[0].split('.')[0]):
        action.v58 = temp
    else:
        v58 = temp 


    temp = get_nested_attribute(action, 'v58', locals())
    if temp is None:
        temp = v58
    if action is not None and hasattr(action, "v59".split('[')[0].split('.')[0]):
        action.v59 = temp
    else:
        v59 = temp 


    if action is not None:
        action.v51.length = v56
        action.v51.fill = v59
    else:
        v51.length = v56
        v51.fill = v59

    if model is not None:
        v60 = View()
        model.add_object(v60) # add object to model
    else:
        v60 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v60
    root.last_view = last_view

    temp = get_nested_attribute(action, '450', locals())
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v61".split('[')[0].split('.')[0]):
        action.v61 = temp
    else:
        v61 = temp 

    v62 = - np.array(v61)

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


    temp = get_nested_attribute(action, '401', locals())
    if temp is None:
        temp = 401
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
    if action is not None and hasattr(action, "v70".split('[')[0].split('.')[0]):
        action.v70 = temp
    else:
        v70 = temp 


    temp = get_nested_attribute(action, '401', locals())
    if temp is None:
        temp = 401
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


    temp = get_nested_attribute(action, 'v72', locals())
    if temp is None:
        temp = v72
    if action is not None and hasattr(action, "v73".split('[')[0].split('.')[0]):
        action.v73 = temp
    else:
        v73 = temp 


    temp = get_nested_attribute(action, '"Illustrating a moving pacman"', locals())
    if temp is None:
        temp = "Illustrating a moving pacman"
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
    if action is not None and hasattr(action, "v76".split('[')[0].split('.')[0]):
        action.v76 = temp
    else:
        v76 = temp 


    temp = get_nested_attribute(action, '"alice blue"', locals())
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v77".split('[')[0].split('.')[0]):
        action.v77 = temp
    else:
        v77 = temp 


    temp = get_nested_attribute(action, 'v77', locals())
    if temp is None:
        temp = v77
    if action is not None and hasattr(action, "v78".split('[')[0].split('.')[0]):
        action.v78 = temp
    else:
        v78 = temp 


    temp = get_nested_attribute(action, 'v78', locals())
    if temp is None:
        temp = v78
    if action is not None and hasattr(action, "v79".split('[')[0].split('.')[0]):
        action.v79 = temp
    else:
        v79 = temp 


    if action is not None:
        action.v60.Ox = v64
        action.v60.Oy = v67
        action.v60.width = v70
        action.v60.height = v73
        action.v60.title = v76
        action.v60.background = v79
    else:
        v60.Ox = v64
        v60.Oy = v67
        v60.width = v70
        v60.height = v73
        v60.title = v76
        v60.background = v79

    temp = get_nested_attribute(action, 'v60', locals())
    if temp is None:
        temp = v60
    if action is not None and hasattr(action, "var__agl__view".split('[')[0].split('.')[0]):
        action.var__agl__view = temp
    else:
        var__agl__view = temp 
    if model is not None: 
        model.var__agl__view = var__agl__view
        model.last_var__agl__view = copy.deepcopy(var__agl__view)

    temp = get_nested_attribute(action, '450', locals())
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v82".split('[')[0].split('.')[0]):
        action.v82 = temp
    else:
        v82 = temp 

    v83 = - np.array(v82)

    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v84".split('[')[0].split('.')[0]):
        action.v84 = temp
    else:
        v84 = temp 

    v81 = (v83 , v84); v81 = tuple(v81) if isinstance(v81, np.ndarray) else v81

    if model is not None:
        model_backup = model
        v80 = Pacman() # this makes model = None in the end!
        model = model_backup
        model.add_object(v80) # add object to model
    else:
        v80 = Pacman(root_local = root, view = last_view)
    v80.move_absolute(v81)  

    temp = get_nested_attribute(action, 'v80', locals())
    if temp is None:
        temp = v80
    if action is not None and hasattr(action, "v85".split('[')[0].split('.')[0]):
        action.v85 = temp
    else:
        v85 = temp 


    temp = get_nested_attribute(action, 'v85', locals())
    if temp is None:
        temp = v85
    if action is not None and hasattr(action, "var__agl__pacman".split('[')[0].split('.')[0]):
        action.var__agl__pacman = temp
    else:
        var__agl__pacman = temp 
    if model is not None: 
        model.var__agl__pacman = var__agl__pacman
        model.last_var__agl__pacman = copy.deepcopy(var__agl__pacman)

    last_refresh = time.time()
    var__agl__view.update()


    temp = get_nested_attribute(action, '"doc/examples/s0.xagl"', locals())
    if temp is None:
        temp = "doc/examples/s0.xagl"
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
    if action is not None and hasattr(action, "v88".split('[')[0].split('.')[0]):
        action.v88 = temp
    else:
        v88 = temp 


    temp = get_nested_attribute(action, 'v88', locals())
    if temp is None:
        temp = v88
    if action is not None and hasattr(action, "var__agl__s1".split('[')[0].split('.')[0]):
        action.var__agl__s1 = temp
    else:
        var__agl__s1 = temp 
    if model is not None: 
        model.var__agl__s1 = var__agl__s1
        model.last_var__agl__s1 = copy.deepcopy(var__agl__s1)

    temp = get_nested_attribute(action, 'var__agl__pacman', locals())
    if temp is None:
        temp = var__agl__pacman
    if action is not None and hasattr(action, "v90".split('[')[0].split('.')[0]):
        action.v90 = temp
    else:
        v90 = temp 


    temp = get_nested_attribute(action, 'v90', locals())
    if temp is None:
        temp = v90
    if action is not None and hasattr(action, "v91".split('[')[0].split('.')[0]):
        action.v91 = temp
    else:
        v91 = temp 


    temp = get_nested_attribute(action, 'v91', locals())
    if temp is None:
        temp = v91
    if action is not None and hasattr(action, "v89".split('[')[0].split('.')[0]):
        action.v89 = temp
    else:
        v89 = temp 


    temp = get_nested_attribute(action, 'var__agl__view', locals())
    if temp is None:
        temp = var__agl__view
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
    if action is not None and hasattr(action, "v92".split('[')[0].split('.')[0]):
        action.v92 = temp
    else:
        v92 = temp 


    # Play with XAGL file
    file = var__agl__s1
    vars1 = {"root":root, "m":v89,"v":v92}
    vars0 = transform_dict(vars1)

    #visitor0 = Semantic(vars0)
    visitor1 = Interpreter(vars1)
    input_stream = FileStream(file)
    lexer = XAGLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = XAGLParser(stream)

    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() == 0:
        #visitor0.visit(tree)
        #if not visitor0.error:
        visitor1.visit(tree)

    v95 = input("Insert a XAgl script to make pacman move 100 units to the right\n")

    temp = get_nested_attribute(action, 'v95', locals())
    if temp is None:
        temp = v95
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
    if action is not None and hasattr(action, "var__agl__s2".split('[')[0].split('.')[0]):
        action.var__agl__s2 = temp
    else:
        var__agl__s2 = temp 
    if model is not None: 
        model.var__agl__s2 = var__agl__s2
        model.last_var__agl__s2 = copy.deepcopy(var__agl__s2)

    temp = get_nested_attribute(action, '"Press any mouse button to quit"', locals())
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v98".split('[')[0].split('.')[0]):
        action.v98 = temp
    else:
        v98 = temp 

    print(v98)
    v99 = root.waitClick()

    temp = get_nested_attribute(action, 'v99', locals())
    if temp is None:
        temp = v99
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
    if action is not None and hasattr(action, "var__agl__pos".split('[')[0].split('.')[0]):
        action.var__agl__pos = temp
    else:
        var__agl__pos = temp 
    if model is not None: 
        model.var__agl__pos = var__agl__pos
        model.last_var__agl__pos = copy.deepcopy(var__agl__pos)

    var__agl__view.close(); views.remove(var__agl__view) if last_view != var__agl__view else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == var__agl__view else last_view
    root.last_view = last_view
