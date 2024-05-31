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


    if model is not None:
        v0 = View()
        model.add_object(v0) # add object to model
    else:
        v0 = View(root = root)
    last_view = v0

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v1".split('.')[0]):
        action.v1 = temp
    else:
        v1 = temp 


    temp = get_nested_attribute(action, 'v1')
    if temp is None:
        temp = v1
    if action is not None and hasattr(action, "v2".split('.')[0]):
        action.v2 = temp
    else:
        v2 = temp 


    temp = get_nested_attribute(action, 'v2')
    if temp is None:
        temp = v2
    if action is not None and hasattr(action, "v3".split('.')[0]):
        action.v3 = temp
    else:
        v3 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v4".split('.')[0]):
        action.v4 = temp
    else:
        v4 = temp 


    temp = get_nested_attribute(action, 'v4')
    if temp is None:
        temp = v4
    if action is not None and hasattr(action, "v5".split('.')[0]):
        action.v5 = temp
    else:
        v5 = temp 


    temp = get_nested_attribute(action, 'v5')
    if temp is None:
        temp = v5
    if action is not None and hasattr(action, "v6".split('.')[0]):
        action.v6 = temp
    else:
        v6 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
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


    temp = get_nested_attribute(action, 'v8')
    if temp is None:
        temp = v8
    if action is not None and hasattr(action, "v9".split('.')[0]):
        action.v9 = temp
    else:
        v9 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
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


    temp = get_nested_attribute(action, 'v11')
    if temp is None:
        temp = v11
    if action is not None and hasattr(action, "v12".split('.')[0]):
        action.v12 = temp
    else:
        v12 = temp 


    temp = get_nested_attribute(action, '"Illustrating a moving pacman"')
    if temp is None:
        temp = "Illustrating a moving pacman"
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


    temp = get_nested_attribute(action, 'v14')
    if temp is None:
        temp = v14
    if action is not None and hasattr(action, "v15".split('.')[0]):
        action.v15 = temp
    else:
        v15 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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


    temp = get_nested_attribute(action, 'v17')
    if temp is None:
        temp = v17
    if action is not None and hasattr(action, "v18".split('.')[0]):
        action.v18 = temp
    else:
        v18 = temp 


    if action is not None:
        action.v0.Ox = v3
        action.v0.Oy = v6
        action.v0.width = v9
        action.v0.height = v12
        action.v0.title = v15
        action.v0.background = v18
    else:
        v0.Ox = v3
        v0.Oy = v6
        v0.width = v9
        v0.height = v12
        v0.title = v15
        v0.background = v18

    temp = get_nested_attribute(action, 'v0')
    if temp is None:
        temp = v0
    if action is not None and hasattr(action, "view".split('.')[0]):
        action.view = temp
    else:
        view = temp 
    if model is not None: 
        model.view = view
        model.last_view = copy.deepcopy(view)

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v20".split('.')[0]):
        action.v20 = temp
    else:
        v20 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v21".split('.')[0]):
        action.v21 = temp
    else:
        v21 = temp 

    v19 = (v20 , v21)

    if model is not None:
        v22 = PolyLine()
        model.add_object(v22) # add object to model
    else:
        v22 = PolyLine(root = root)
    v22.origin = v19

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v25".split('.')[0]):
        action.v25 = temp
    else:
        v25 = temp 

    v23 = np.array(v24) == np.array(v25); v23 = tuple(v23) if isinstance(v23, np.ndarray) else v23
    if v23:
        temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v26".split('.')[0]):
        action.v26 = temp
    else:
        v26 = temp 

    v24 = (v25 , v26)

    temp = get_nested_attribute(action, '10')
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v28".split('.')[0]):
        action.v28 = temp
    else:
        v28 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v29".split('.')[0]):
        action.v29 = temp
    else:
        v29 = temp 

    v27 = (v28 , v29)

    temp = get_nested_attribute(action, '10')
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v31".split('.')[0]):
        action.v31 = temp
    else:
        v31 = temp 


    temp = get_nested_attribute(action, '10')
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v32".split('.')[0]):
        action.v32 = temp
    else:
        v32 = temp 

    v30 = (v31 , v32)

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v34".split('.')[0]):
        action.v34 = temp
    else:
        v34 = temp 


    temp = get_nested_attribute(action, '10')
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v35".split('.')[0]):
        action.v35 = temp
    else:
        v35 = temp 

    v33 = (v34 , v35)
    v23 = [v24,v27,v30,v33]

    temp = get_nested_attribute(action, 'v23')
    if temp is None:
        temp = v23
    if action is not None and hasattr(action, "v36".split('.')[0]):
        action.v36 = temp
    else:
        v36 = temp 


    temp = get_nested_attribute(action, 'v36')
    if temp is None:
        temp = v36
    if action is not None and hasattr(action, "v37".split('.')[0]):
        action.v37 = temp
    else:
        v37 = temp 

            v35 = (v36 , v37); v35 = tuple(v35) if isinstance(v35, np.ndarray) else v35

    temp = get_nested_attribute(action, '"black"')
    if temp is None:
        temp = "black"
    if action is not None and hasattr(action, "v38".split('.')[0]):
        action.v38 = temp
    else:
        v38 = temp 


    temp = get_nested_attribute(action, 'v38')
    if temp is None:
        temp = v38
    if action is not None and hasattr(action, "v39".split('.')[0]):
        action.v39 = temp
    else:
        v39 = temp 


    temp = get_nested_attribute(action, 'v39')
    if temp is None:
        temp = v39
    if action is not None and hasattr(action, "v40".split('.')[0]):
        action.v40 = temp
    else:
        v40 = temp 


    temp = get_nested_attribute(action, '2')
    if temp is None:
        temp = 2
    if action is not None and hasattr(action, "v41".split('.')[0]):
        action.v41 = temp
    else:
        v41 = temp 


    temp = get_nested_attribute(action, 'v41')
    if temp is None:
        temp = v41
    if action is not None and hasattr(action, "v42".split('.')[0]):
        action.v42 = temp
    else:
        v42 = temp 


    temp = get_nested_attribute(action, 'v42')
    if temp is None:
        temp = v42
    if action is not None and hasattr(action, "v43".split('.')[0]):
        action.v43 = temp
    else:
        v43 = temp 


    if action is not None:
        action.v22.points = v37
        action.v22.color = v40
        action.v22.width = v43
    else:
        v22.points = v37
        v22.color = v40
        v22.width = v43

    temp = get_nested_attribute(action, 'v22')
    if temp is None:
        temp = v22
    if action is not None and hasattr(action, "poly".split('.')[0]):
        action.poly = temp
    else:
        poly = temp 
    if model is not None: 
        model.poly = poly
        model.last_poly = copy.deepcopy(poly)
    last_refresh = time.time()
    view.update()
    view.update()


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v44".split('.')[0]):
        action.v44 = temp
    else:
        v44 = temp 


    temp = get_nested_attribute(action, '10')
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v45".split('.')[0]):
        action.v45 = temp
    else:
        v45 = temp 

    for i in range(v44, v45, 1):
         

        temp = get_nested_attribute(action, '25')
        if temp is None:
            temp = 25
        if action is not None and hasattr(action, "v46".split('.')[0]):
            action.v46 = temp
        else:
            v46 = temp 

        while (time.time() - last_refresh <= v46/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '20')
        if temp is None:
            temp = 20
        if action is not None and hasattr(action, "v48".split('.')[0]):
            action.v48 = temp
        else:
            v48 = temp 


        temp = get_nested_attribute(action, '100')
        if temp is None:
            temp = 100
        if action is not None and hasattr(action, "v49".split('.')[0]):
            action.v49 = temp
        else:
            v49 = temp 

        v47 = (v48 , v49)
        if action is not None:
            action.poly.move_absolute(v47)
        else:
            poly.move_absolute(v47)
         

        temp = get_nested_attribute(action, '25')
        if temp is None:
            temp = 25
        if action is not None and hasattr(action, "v50".split('.')[0]):
            action.v50 = temp
        else:
            v50 = temp 

        while (time.time() - last_refresh <= v50/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v52".split('.')[0]):
            action.v52 = temp
        else:
            v52 = temp 


        temp = get_nested_attribute(action, '0')
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v53".split('.')[0]):
            action.v53 = temp
        else:
            v53 = temp 

        v51 = (v52 , v53)
        if action is not None:
            action.poly.move_absolute(v51)
        else:
            poly.move_absolute(v51)
