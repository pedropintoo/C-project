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
        v22 = Text()
        model.add_object(v22) # add object to model
    else:
        v22 = Text(root = root)
    v22.origin = v19

    temp = get_nested_attribute(action, '"Bla bla ..."')
    if temp is None:
        temp = "Bla bla ..."
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


    temp = get_nested_attribute(action, '"purple"')
    if temp is None:
        temp = "purple"
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


    if action is not None:
        action.v22.text = v25
        action.v22.fill = v28
    else:
        v22.text = v25
        v22.fill = v28

    temp = get_nested_attribute(action, 'v22')
    if temp is None:
        temp = v22
    if action is not None and hasattr(action, "text".split('.')[0]):
        action.text = temp
    else:
        text = temp 
    if model is not None: 
        model.text = text
        model.last_text = copy.deepcopy(text)
    last_refresh = time.time()
    view.update()
    view.update()


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v29".split('.')[0]):
        action.v29 = temp
    else:
        v29 = temp 


    temp = get_nested_attribute(action, '5')
    if temp is None:
        temp = 5
    if action is not None and hasattr(action, "v30".split('.')[0]):
        action.v30 = temp
    else:
        v30 = temp 

    for i in range(v29, v30, 1):

        temp = get_nested_attribute(action, '45')
        if temp is None:
            temp = 45
        if action is not None and hasattr(action, "v32".split('.')[0]):
            action.v32 = temp
        else:
            v32 = temp 


        temp = get_nested_attribute(action, '45')
        if temp is None:
            temp = 45
        if action is not None and hasattr(action, "v33".split('.')[0]):
            action.v33 = temp
        else:
            v33 = temp 

        v31 = (v32 , v33)
        if action is not None:
            action.text.move_relative(v31)
        else:
            text.rotate(90)
         

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v34".split('.')[0]):
            action.v34 = temp
        else:
            v34 = temp 

        while (time.time() - last_refresh <= v34):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()

