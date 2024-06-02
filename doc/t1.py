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


    temp = get_nested_attribute(action, '650')
    if temp is None:
        temp = 650
    if action is not None and hasattr(action, "v1".split('.')[0]):
        action.v1 = temp
    else:
        v1 = temp 

    v2 = - np.array(v1)

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v3".split('.')[0]):
        action.v3 = temp
    else:
        v3 = temp 

    v0 = (v2 , v3); v0 = tuple(v0) if isinstance(v0, np.ndarray) else v0

    if model is not None:
        v4 = Ellipse()
        model.add_object(v4) # add object to model
    else:
        v4 = Ellipse(root = root)
    v4.origin = v0

    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v6".split('.')[0]):
        action.v6 = temp
    else:
        v6 = temp 


    temp = get_nested_attribute(action, '135')
    if temp is None:
        temp = 135
    if action is not None and hasattr(action, "v7".split('.')[0]):
        action.v7 = temp
    else:
        v7 = temp 

    v5 = (v6 , v7); v5 = tuple(v5) if isinstance(v5, np.ndarray) else v5

    temp = get_nested_attribute(action, 'v5')
    if temp is None:
        temp = v5
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
    temp = get_nested_attribute(action, 'v8')
    if temp is None:
        temp = v8
    if action is not None and hasattr(action, "v9".split('.')[0]):
        action.v9 = temp
    else:
        v9 = temp 


    temp = get_nested_attribute(action, '"black"')
    if temp is None:
        temp = "black"
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
    temp = get_nested_attribute(action, 'v11')
    if temp is None:
        temp = v11
    if action is not None and hasattr(action, "v12".split('.')[0]):
        action.v12 = temp
    else:
        v12 = temp 


    if action is not None:
        action.v4.length = v9
        action.v4.fill = v12
    else:
        v4.length = v9
        v4.fill = v12

    temp = get_nested_attribute(action, 'v4')
    if temp is None:
        temp = v4
    if action is not None and hasattr(action, "elipse".split('.')[0]):
        action.elipse = temp
    else:
        elipse = temp 
    if model is not None: 
        model.elipse = elipse
        model.last_elipse = copy.deepcopy(elipse)

    if model is not None:
        v13 = View()
        model.add_object(v13) # add object to model
    else:
        v13 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v13

    temp = get_nested_attribute(action, '30')
    if temp is None:
        temp = 30
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
    temp = get_nested_attribute(action, 'v14')
    if temp is None:
        temp = v14
    if action is not None and hasattr(action, "v15".split('.')[0]):
        action.v15 = temp
    else:
        v15 = temp 


    temp = get_nested_attribute(action, 'v15')
    if temp is None:
        temp = v15
    if action is not None and hasattr(action, "v16".split('.')[0]):
        action.v16 = temp
    else:
        v16 = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
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
    temp = get_nested_attribute(action, 'v17')
    if temp is None:
        temp = v17
    if action is not None and hasattr(action, "v18".split('.')[0]):
        action.v18 = temp
    else:
        v18 = temp 


    temp = get_nested_attribute(action, 'v18')
    if temp is None:
        temp = v18
    if action is not None and hasattr(action, "v19".split('.')[0]):
        action.v19 = temp
    else:
        v19 = temp 
    temp = get_nested_attribute(action, 'v18')
    if temp is None:
        temp = v18
    if action is not None and hasattr(action, "v19".split('.')[0]):
        action.v19 = temp
    else:
        v19 = temp 


    temp = get_nested_attribute(action, '1800')
    if temp is None:
        temp = 1800
    if action is not None and hasattr(action, "v20".split('.')[0]):
        action.v20 = temp
    else:
        v20 = temp 


    temp = get_nested_attribute(action, 'v20')
    if temp is None:
        temp = v20
    if action is not None and hasattr(action, "v21".split('.')[0]):
        action.v21 = temp
    else:
        v21 = temp 


    temp = get_nested_attribute(action, 'v21')
    if temp is None:
        temp = v21
    if action is not None and hasattr(action, "v22".split('.')[0]):
        action.v22 = temp
    else:
        v22 = temp 
    temp = get_nested_attribute(action, 'v21')
    if temp is None:
        temp = v21
    if action is not None and hasattr(action, "v22".split('.')[0]):
        action.v22 = temp
    else:
        v22 = temp 


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
    if action is not None and hasattr(action, "v23".split('.')[0]):
        action.v23 = temp
    else:
        v23 = temp 


    temp = get_nested_attribute(action, 'v23')
    if temp is None:
        temp = v23
    if action is not None and hasattr(action, "v24".split('.')[0]):
        action.v24 = temp
    else:
        v24 = temp 


    temp = get_nested_attribute(action, 'v24')
    if temp is None:
        temp = v24
    if action is not None and hasattr(action, "v25".split('.')[0]):
        action.v25 = temp
    else:
        v25 = temp 
    temp = get_nested_attribute(action, 'v24')
    if temp is None:
        temp = v24
    if action is not None and hasattr(action, "v25".split('.')[0]):
        action.v25 = temp
    else:
        v25 = temp 


    temp = get_nested_attribute(action, '"1"')
    if temp is None:
        temp = "1"
    if action is not None and hasattr(action, "v26".split('.')[0]):
        action.v26 = temp
    else:
        v26 = temp 


    temp = get_nested_attribute(action, 'v26')
    if temp is None:
        temp = v26
    if action is not None and hasattr(action, "v27".split('.')[0]):
        action.v27 = temp
    else:
        v27 = temp 


    temp = get_nested_attribute(action, 'v27')
    if temp is None:
        temp = v27
    if action is not None and hasattr(action, "v28".split('.')[0]):
        action.v28 = temp
    else:
        v28 = temp 
    temp = get_nested_attribute(action, 'v27')
    if temp is None:
        temp = v27
    if action is not None and hasattr(action, "v28".split('.')[0]):
        action.v28 = temp
    else:
        v28 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v29".split('.')[0]):
        action.v29 = temp
    else:
        v29 = temp 


    temp = get_nested_attribute(action, 'v29')
    if temp is None:
        temp = v29
    if action is not None and hasattr(action, "v30".split('.')[0]):
        action.v30 = temp
    else:
        v30 = temp 


    temp = get_nested_attribute(action, 'v30')
    if temp is None:
        temp = v30
    if action is not None and hasattr(action, "v31".split('.')[0]):
        action.v31 = temp
    else:
        v31 = temp 
    temp = get_nested_attribute(action, 'v30')
    if temp is None:
        temp = v30
    if action is not None and hasattr(action, "v31".split('.')[0]):
        action.v31 = temp
    else:
        v31 = temp 


    if action is not None:
        action.v13.Ox = v16
        action.v13.Oy = v19
        action.v13.width = v22
        action.v13.height = v25
        action.v13.title = v28
        action.v13.background = v31
    else:
        v13.Ox = v16
        v13.Oy = v19
        v13.width = v22
        v13.height = v25
        v13.title = v28
        v13.background = v31

    temp = get_nested_attribute(action, 'v13')
    if temp is None:
        temp = v13
    if action is not None and hasattr(action, "view".split('.')[0]):
        action.view = temp
    else:
        view = temp 
    if model is not None: 
        model.view = view
        model.last_view = copy.deepcopy(view)

    last_refresh = time.time()
    view.update()


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v32".split('.')[0]):
        action.v32 = temp
    else:
        v32 = temp 


    temp = get_nested_attribute(action, '20')
    if temp is None:
        temp = 20
    if action is not None and hasattr(action, "v33".split('.')[0]):
        action.v33 = temp
    else:
        v33 = temp 

    for i in range(v32, v33, 1):

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v34".split('.')[0]):
            action.v34 = temp
        else:
            v34 = temp 

        if action is not None:
            action.elipse.rotate(v34)
        else:
            elipse.rotate(v34)

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v35".split('.')[0]):
            action.v35 = temp
        else:
            v35 = temp 

         
        while (time.time() - last_refresh <= v35):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v36".split('.')[0]):
        action.v36 = temp
    else:
        v36 = temp 

    print(v36)
    if action is not None:
        v37 = action.view.waitClick()
    else:
        v37 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v37')
    if temp is None:
        temp = v37
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
    if action is not None and hasattr(action, "p".split('.')[0]):
        action.p = temp
    else:
        p = temp 
        p = temp 
    if model is not None: 
        model.p = p
        model.last_p = copy.deepcopy(p)
        model.p = p
        model.last_p = copy.deepcopy(p)

    temp = get_nested_attribute(action, 'p')
    temp = get_nested_attribute(action, 'p')
    if temp is None:
        temp = p
    if action is not None and hasattr(action, "v40".split('.')[0]):
        action.v40 = temp
    else:
        v40 = temp 

    print(v40)
    view.close(); views.remove(view) if last_view != view else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == view else last_view
