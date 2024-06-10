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
    class var__agl__Ex1(Model):
        def __init__(self, root_local: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root_local, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '200', locals())
            if temp is None:
                temp = 200
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
                model.addAttributes("var__agl__cellSize".replace("var__agl__", ""), var__agl__cellSize)
                model.addAttributes("last_var__agl__cellSize".replace("var__agl__", ""), model.last_var__agl__cellSize)

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
                model.addAttributes("var__agl__rec".replace("var__agl__", ""), var__agl__rec)
                model.addAttributes("last_var__agl__rec".replace("var__agl__", ""), model.last_var__agl__rec)

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
                model.addAttributes("var__agl__ell".replace("var__agl__", ""), var__agl__ell)
                model.addAttributes("last_var__agl__ell".replace("var__agl__", ""), model.last_var__agl__ell)

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
            new_model = var__agl__Ex1()

            self.copyAttributesTo(new_model)
            new_model.view = self.view
            new_model.root = self.root
            return new_model       

    #################################################################

    if model is not None:
        v27 = View()
        model.add_object(v27) # add object to model
    else:
        v27 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v27
    root.last_view = last_view

    temp = get_nested_attribute(action, '800', locals())
    if temp is None:
        temp = 800
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


    temp = get_nested_attribute(action, 'v29', locals())
    if temp is None:
        temp = v29
    if action is not None and hasattr(action, "v30".split('[')[0].split('.')[0]):
        action.v30 = temp
    else:
        v30 = temp 


    temp = get_nested_attribute(action, '600', locals())
    if temp is None:
        temp = 600
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


    temp = get_nested_attribute(action, 'v32', locals())
    if temp is None:
        temp = v32
    if action is not None and hasattr(action, "v33".split('[')[0].split('.')[0]):
        action.v33 = temp
    else:
        v33 = temp 


    temp = get_nested_attribute(action, '"black"', locals())
    if temp is None:
        temp = "black"
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


    temp = get_nested_attribute(action, 'v35', locals())
    if temp is None:
        temp = v35
    if action is not None and hasattr(action, "v36".split('[')[0].split('.')[0]):
        action.v36 = temp
    else:
        v36 = temp 


    if action is not None:
        action.v27.width = v30
        action.v27.height = v33
        action.v27.background = v36
    else:
        v27.width = v30
        v27.height = v33
        v27.background = v36

    temp = get_nested_attribute(action, 'v27', locals())
    if temp is None:
        temp = v27
    if action is not None and hasattr(action, "var__agl__view".split('[')[0].split('.')[0]):
        action.var__agl__view = temp
    else:
        var__agl__view = temp 
    if model is not None: 
        model.var__agl__view = var__agl__view
        model.last_var__agl__view = copy.deepcopy(var__agl__view)
        model.addAttributes("var__agl__view".replace("var__agl__", ""), var__agl__view)
        model.addAttributes("last_var__agl__view".replace("var__agl__", ""), model.last_var__agl__view)

    if model is not None:
        model_backup = model
        v37 = var__agl__Ex1() # this makes model = None in the end!
        model = model_backup
        model.add_object(v37) # add object to model
    else:
        v37 = var__agl__Ex1(root_local = root, view = last_view)
      

    temp = get_nested_attribute(action, 'v37', locals())
    if temp is None:
        temp = v37
    if action is not None and hasattr(action, "v38".split('[')[0].split('.')[0]):
        action.v38 = temp
    else:
        v38 = temp 


    temp = get_nested_attribute(action, 'v38', locals())
    if temp is None:
        temp = v38
    if action is not None and hasattr(action, "var__agl__ex1".split('[')[0].split('.')[0]):
        action.var__agl__ex1 = temp
    else:
        var__agl__ex1 = temp 
    if model is not None: 
        model.var__agl__ex1 = var__agl__ex1
        model.last_var__agl__ex1 = copy.deepcopy(var__agl__ex1)
        model.addAttributes("var__agl__ex1".replace("var__agl__", ""), var__agl__ex1)
        model.addAttributes("last_var__agl__ex1".replace("var__agl__", ""), model.last_var__agl__ex1)

    temp = get_nested_attribute(action, 'var__agl__ex1.var__agl__rec.origin', locals())
    if temp is None:
        temp = var__agl__ex1.var__agl__rec.origin
    if action is not None and hasattr(action, "v39".split('[')[0].split('.')[0]):
        action.v39 = temp
    else:
        v39 = temp 


    v40 = copy.deepcopy(var__agl__ex1.var__agl__ell)
    v40.move_absolute(v39)  

    if model is not None: 
        model.v40 = v40
        model.last_v40 = copy.deepcopy(v40)
        model.add_object(v40) # add object to model
        model.addAttributes("v40".replace("var__agl__", ""), v40)
        model.addAttributes("last_v40".replace("var__agl__", ""), model.last_v40)
    else:
        root.add_object(v40)

    temp = get_nested_attribute(action, 'v40', locals())
    if temp is None:
        temp = v40
    if action is not None and hasattr(action, "v41".split('[')[0].split('.')[0]):
        action.v41 = temp
    else:
        v41 = temp 


    temp = get_nested_attribute(action, 'v41', locals())
    if temp is None:
        temp = v41
    if action is not None and hasattr(action, "v42".split('[')[0].split('.')[0]):
        action.v42 = temp
    else:
        v42 = temp 


    temp = get_nested_attribute(action, 'v42', locals())
    if temp is None:
        temp = v42
    if action is not None and hasattr(action, "var__agl__lineRec".split('[')[0].split('.')[0]):
        action.var__agl__lineRec = temp
    else:
        var__agl__lineRec = temp 
    if model is not None: 
        model.var__agl__lineRec = var__agl__lineRec
        model.last_var__agl__lineRec = copy.deepcopy(var__agl__lineRec)
        model.addAttributes("var__agl__lineRec".replace("var__agl__", ""), var__agl__lineRec)
        model.addAttributes("last_var__agl__lineRec".replace("var__agl__", ""), model.last_var__agl__lineRec)

    temp = get_nested_attribute(action, '"red"', locals())
    if temp is None:
        temp = "red"
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


    temp = get_nested_attribute(action, 'v44', locals())
    if temp is None:
        temp = v44
    if action is not None and hasattr(action, "var__agl__lineRec.fill".split('[')[0].split('.')[0]):
        action.var__agl__lineRec.fill = temp
    else:
        var__agl__lineRec.fill = temp 

    last_refresh = time.time()
    var__agl__view.update()

    v45 = root.waitClick()

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


    temp = get_nested_attribute(action, 'v47', locals())
    if temp is None:
        temp = v47
    if action is not None and hasattr(action, "var__agl__p".split('[')[0].split('.')[0]):
        action.var__agl__p = temp
    else:
        var__agl__p = temp 
    if model is not None: 
        model.var__agl__p = var__agl__p
        model.last_var__agl__p = copy.deepcopy(var__agl__p)
        model.addAttributes("var__agl__p".replace("var__agl__", ""), var__agl__p)
        model.addAttributes("last_var__agl__p".replace("var__agl__", ""), model.last_var__agl__p)

    temp = get_nested_attribute(action, '1', locals())
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v48".split('[')[0].split('.')[0]):
        action.v48 = temp
    else:
        v48 = temp 


    temp = get_nested_attribute(action, '360', locals())
    if temp is None:
        temp = 360
    if action is not None and hasattr(action, "v49".split('[')[0].split('.')[0]):
        action.v49 = temp
    else:
        v49 = temp 

    for var__agl__i in range(v48, v49, 1):

        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v50".split('[')[0].split('.')[0]):
            action.v50 = temp
        else:
            v50 = temp 

        if action is not None:
            action.var__agl__ex1.rotate(v50)
        else:
            var__agl__ex1.rotate(v50)

        temp = get_nested_attribute(action, 'var__agl__ex1.var__agl__rec.origin', locals())
        if temp is None:
            temp = var__agl__ex1.var__agl__rec.origin
        if action is not None and hasattr(action, "v51".split('[')[0].split('.')[0]):
            action.v51 = temp
        else:
            v51 = temp 

        if action is not None:
            action.var__agl__lineRec.move_absolute(v51)
        else:
            var__agl__lineRec.move_absolute(v51)

        temp = get_nested_attribute(action, '5', locals())
        if temp is None:
            temp = 5
        if action is not None and hasattr(action, "v52".split('[')[0].split('.')[0]):
            action.v52 = temp
        else:
            v52 = temp 

        v53 = - np.array(v52)
        if action is not None:
            action.var__agl__lineRec.rotate(v53)
        else:
            var__agl__lineRec.rotate(v53)

        temp = get_nested_attribute(action, '0.01', locals())
        if temp is None:
            temp = 0.01
        if action is not None and hasattr(action, "v54".split('[')[0].split('.')[0]):
            action.v54 = temp
        else:
            v54 = temp 

         
        while (time.time() - last_refresh <= v54):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        var__agl__view.update()


    last_refresh = time.time()
    var__agl__view.update()

    v55 = root.waitClick()

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
    if action is not None and hasattr(action, "var__agl__p".split('[')[0].split('.')[0]):
        action.var__agl__p = temp
    else:
        var__agl__p = temp 

