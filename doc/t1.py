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


    temp = get_nested_attribute(action, '2', locals())
    if temp is None:
        temp = 2
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
    if action is not None and hasattr(action, "var__agl__a".split('[')[0].split('.')[0]):
        action.var__agl__a = temp
    else:
        var__agl__a = temp 
    if model is not None: 
        model.var__agl__a = var__agl__a
        model.last_var__agl__a = copy.deepcopy(var__agl__a)

    temp = get_nested_attribute(action, '3', locals())
    if temp is None:
        temp = 3
    if action is not None and hasattr(action, "v3".split('[')[0].split('.')[0]):
        action.v3 = temp
    else:
        v3 = temp 


    temp = get_nested_attribute(action, 'v3', locals())
    if temp is None:
        temp = v3
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


    temp = get_nested_attribute(action, 'v5', locals())
    if temp is None:
        temp = v5
    if action is not None and hasattr(action, "var__agl__b".split('[')[0].split('.')[0]):
        action.var__agl__b = temp
    else:
        var__agl__b = temp 
    if model is not None: 
        model.var__agl__b = var__agl__b
        model.last_var__agl__b = copy.deepcopy(var__agl__b)

    temp = get_nested_attribute(action, 'var__agl__a', locals())
    if temp is None:
        temp = var__agl__a
    if action is not None and hasattr(action, "v8".split('[')[0].split('.')[0]):
        action.v8 = temp
    else:
        v8 = temp 


    temp = get_nested_attribute(action, 'var__agl__b', locals())
    if temp is None:
        temp = var__agl__b
    if action is not None and hasattr(action, "v9".split('[')[0].split('.')[0]):
        action.v9 = temp
    else:
        v9 = temp 

    v7 = np.array(v8) + np.array(v9); v7 = tuple(v7) if isinstance(v7, np.ndarray) else v7

    temp = get_nested_attribute(action, '10', locals())
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v10".split('[')[0].split('.')[0]):
        action.v10 = temp
    else:
        v10 = temp 

    v6 = np.array(v7) >= np.array(v10); v6 = tuple(v6) if isinstance(v6, np.ndarray) else v6
    v11 = not v6

    while v11:

        temp = get_nested_attribute(action, 'var__agl__a', locals())
        if temp is None:
            temp = var__agl__a
        if action is not None and hasattr(action, "v13".split('[')[0].split('.')[0]):
            action.v13 = temp
        else:
            v13 = temp 


        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v14".split('[')[0].split('.')[0]):
            action.v14 = temp
        else:
            v14 = temp 

        v12 = np.array(v13) + np.array(v14); v12 = tuple(v12) if isinstance(v12, np.ndarray) else v12

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
        if action is not None and hasattr(action, "var__agl__a".split('[')[0].split('.')[0]):
            action.var__agl__a = temp
        else:
            var__agl__a = temp 


        temp = get_nested_attribute(action, 'var__agl__a', locals())
        if temp is None:
            temp = var__agl__a
        if action is not None and hasattr(action, "v16".split('[')[0].split('.')[0]):
            action.v16 = temp
        else:
            v16 = temp 

        print(v16)
        # refresh the condition

        temp = get_nested_attribute(action, 'var__agl__a', locals())
        if temp is None:
            temp = var__agl__a
        if action is not None and hasattr(action, "v8".split('[')[0].split('.')[0]):
            action.v8 = temp
        else:
            v8 = temp 


        temp = get_nested_attribute(action, 'var__agl__b', locals())
        if temp is None:
            temp = var__agl__b
        if action is not None and hasattr(action, "v9".split('[')[0].split('.')[0]):
            action.v9 = temp
        else:
            v9 = temp 

        v7 = np.array(v8) + np.array(v9); v7 = tuple(v7) if isinstance(v7, np.ndarray) else v7

        temp = get_nested_attribute(action, '10', locals())
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v10".split('[')[0].split('.')[0]):
            action.v10 = temp
        else:
            v10 = temp 

        v6 = np.array(v7) >= np.array(v10); v6 = tuple(v6) if isinstance(v6, np.ndarray) else v6
        v11 = not v6
        ##

    temp = get_nested_attribute(action, '2', locals())
    if temp is None:
        temp = 2
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
    if action is not None and hasattr(action, "var__agl__a".split('[')[0].split('.')[0]):
        action.var__agl__a = temp
    else:
        var__agl__a = temp 


    temp = get_nested_attribute(action, 'var__agl__a', locals())
    if temp is None:
        temp = var__agl__a
    if action is not None and hasattr(action, "v21".split('[')[0].split('.')[0]):
        action.v21 = temp
    else:
        v21 = temp 


    temp = get_nested_attribute(action, 'var__agl__b', locals())
    if temp is None:
        temp = var__agl__b
    if action is not None and hasattr(action, "v22".split('[')[0].split('.')[0]):
        action.v22 = temp
    else:
        v22 = temp 

    v20 = np.array(v21) + np.array(v22); v20 = tuple(v20) if isinstance(v20, np.ndarray) else v20

    temp = get_nested_attribute(action, '10', locals())
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v23".split('[')[0].split('.')[0]):
        action.v23 = temp
    else:
        v23 = temp 

    v19 = np.array(v20) >= np.array(v23); v19 = tuple(v19) if isinstance(v19, np.ndarray) else v19
    while True:

        temp = get_nested_attribute(action, 'var__agl__a', locals())
        if temp is None:
            temp = var__agl__a
        if action is not None and hasattr(action, "v25".split('[')[0].split('.')[0]):
            action.v25 = temp
        else:
            v25 = temp 


        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v26".split('[')[0].split('.')[0]):
            action.v26 = temp
        else:
            v26 = temp 

        v24 = np.array(v25) + np.array(v26); v24 = tuple(v24) if isinstance(v24, np.ndarray) else v24

        temp = get_nested_attribute(action, 'v24', locals())
        if temp is None:
            temp = v24
        if action is not None and hasattr(action, "v27".split('[')[0].split('.')[0]):
            action.v27 = temp
        else:
            v27 = temp 


        temp = get_nested_attribute(action, 'v27', locals())
        if temp is None:
            temp = v27
        if action is not None and hasattr(action, "var__agl__a".split('[')[0].split('.')[0]):
            action.var__agl__a = temp
        else:
            var__agl__a = temp 


        temp = get_nested_attribute(action, 'var__agl__a', locals())
        if temp is None:
            temp = var__agl__a
        if action is not None and hasattr(action, "v28".split('[')[0].split('.')[0]):
            action.v28 = temp
        else:
            v28 = temp 

        print(v28)
        # refresh the condition

        temp = get_nested_attribute(action, 'var__agl__a', locals())
        if temp is None:
            temp = var__agl__a
        if action is not None and hasattr(action, "v21".split('[')[0].split('.')[0]):
            action.v21 = temp
        else:
            v21 = temp 


        temp = get_nested_attribute(action, 'var__agl__b', locals())
        if temp is None:
            temp = var__agl__b
        if action is not None and hasattr(action, "v22".split('[')[0].split('.')[0]):
            action.v22 = temp
        else:
            v22 = temp 

        v20 = np.array(v21) + np.array(v22); v20 = tuple(v20) if isinstance(v20, np.ndarray) else v20

        temp = get_nested_attribute(action, '10', locals())
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v23".split('[')[0].split('.')[0]):
            action.v23 = temp
        else:
            v23 = temp 

        v19 = np.array(v20) >= np.array(v23); v19 = tuple(v19) if isinstance(v19, np.ndarray) else v19
        ##
        if v19:
            break   # Repeat until condition is false
