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
    if last_view is not None:
        views.append(last_view)    
    last_view = v0

    temp = get_nested_attribute(action, '601')
    if temp is None:
        temp = 601
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


    temp = get_nested_attribute(action, '601')
    if temp is None:
        temp = 601
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


    temp = get_nested_attribute(action, '"All"')
    if temp is None:
        temp = "All"
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


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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


    if action is not None:
        action.v0.width = v3
        action.v0.height = v6
        action.v0.title = v9
        action.v0.background = v12
    else:
        v0.width = v3
        v0.height = v6
        v0.title = v9
        v0.background = v12

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

    if model is not None:
        v13 = View()
        model.add_object(v13) # add object to model
    else:
        v13 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v13

    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
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


    temp = get_nested_attribute(action, 'v15')
    if temp is None:
        temp = v15
    if action is not None and hasattr(action, "v16".split('.')[0]):
        action.v16 = temp
    else:
        v16 = temp 


    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
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


    temp = get_nested_attribute(action, 'v18')
    if temp is None:
        temp = v18
    if action is not None and hasattr(action, "v19".split('.')[0]):
        action.v19 = temp
    else:
        v19 = temp 


    temp = get_nested_attribute(action, '"Line"')
    if temp is None:
        temp = "Line"
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


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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


    if action is not None:
        action.v13.width = v16
        action.v13.height = v19
        action.v13.title = v22
        action.v13.background = v25
    else:
        v13.width = v16
        v13.height = v19
        v13.title = v22
        v13.background = v25

    temp = get_nested_attribute(action, 'v13')
    if temp is None:
        temp = v13
    if action is not None and hasattr(action, "view2".split('.')[0]):
        action.view2 = temp
    else:
        view2 = temp 
    if model is not None: 
        model.view2 = view2
        model.last_view2 = copy.deepcopy(view2)

    if model is not None:
        v26 = View()
        model.add_object(v26) # add object to model
    else:
        v26 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v26

    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
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


    temp = get_nested_attribute(action, 'v28')
    if temp is None:
        temp = v28
    if action is not None and hasattr(action, "v29".split('.')[0]):
        action.v29 = temp
    else:
        v29 = temp 


    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
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


    temp = get_nested_attribute(action, 'v31')
    if temp is None:
        temp = v31
    if action is not None and hasattr(action, "v32".split('.')[0]):
        action.v32 = temp
    else:
        v32 = temp 


    temp = get_nested_attribute(action, '"Rectangle"')
    if temp is None:
        temp = "Rectangle"
    if action is not None and hasattr(action, "v33".split('.')[0]):
        action.v33 = temp
    else:
        v33 = temp 


    temp = get_nested_attribute(action, 'v33')
    if temp is None:
        temp = v33
    if action is not None and hasattr(action, "v34".split('.')[0]):
        action.v34 = temp
    else:
        v34 = temp 


    temp = get_nested_attribute(action, 'v34')
    if temp is None:
        temp = v34
    if action is not None and hasattr(action, "v35".split('.')[0]):
        action.v35 = temp
    else:
        v35 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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


    temp = get_nested_attribute(action, 'v37')
    if temp is None:
        temp = v37
    if action is not None and hasattr(action, "v38".split('.')[0]):
        action.v38 = temp
    else:
        v38 = temp 


    if action is not None:
        action.v26.width = v29
        action.v26.height = v32
        action.v26.title = v35
        action.v26.background = v38
    else:
        v26.width = v29
        v26.height = v32
        v26.title = v35
        v26.background = v38

    temp = get_nested_attribute(action, 'v26')
    if temp is None:
        temp = v26
    if action is not None and hasattr(action, "view3".split('.')[0]):
        action.view3 = temp
    else:
        view3 = temp 
    if model is not None: 
        model.view3 = view3
        model.last_view3 = copy.deepcopy(view3)

    if model is not None:
        v39 = View()
        model.add_object(v39) # add object to model
    else:
        v39 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v39

    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v40".split('.')[0]):
        action.v40 = temp
    else:
        v40 = temp 


    temp = get_nested_attribute(action, 'v40')
    if temp is None:
        temp = v40
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


    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v43".split('.')[0]):
        action.v43 = temp
    else:
        v43 = temp 


    temp = get_nested_attribute(action, 'v43')
    if temp is None:
        temp = v43
    if action is not None and hasattr(action, "v44".split('.')[0]):
        action.v44 = temp
    else:
        v44 = temp 


    temp = get_nested_attribute(action, 'v44')
    if temp is None:
        temp = v44
    if action is not None and hasattr(action, "v45".split('.')[0]):
        action.v45 = temp
    else:
        v45 = temp 


    temp = get_nested_attribute(action, '"Ellipse"')
    if temp is None:
        temp = "Ellipse"
    if action is not None and hasattr(action, "v46".split('.')[0]):
        action.v46 = temp
    else:
        v46 = temp 


    temp = get_nested_attribute(action, 'v46')
    if temp is None:
        temp = v46
    if action is not None and hasattr(action, "v47".split('.')[0]):
        action.v47 = temp
    else:
        v47 = temp 


    temp = get_nested_attribute(action, 'v47')
    if temp is None:
        temp = v47
    if action is not None and hasattr(action, "v48".split('.')[0]):
        action.v48 = temp
    else:
        v48 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v49".split('.')[0]):
        action.v49 = temp
    else:
        v49 = temp 


    temp = get_nested_attribute(action, 'v49')
    if temp is None:
        temp = v49
    if action is not None and hasattr(action, "v50".split('.')[0]):
        action.v50 = temp
    else:
        v50 = temp 


    temp = get_nested_attribute(action, 'v50')
    if temp is None:
        temp = v50
    if action is not None and hasattr(action, "v51".split('.')[0]):
        action.v51 = temp
    else:
        v51 = temp 


    if action is not None:
        action.v39.width = v42
        action.v39.height = v45
        action.v39.title = v48
        action.v39.background = v51
    else:
        v39.width = v42
        v39.height = v45
        v39.title = v48
        v39.background = v51

    temp = get_nested_attribute(action, 'v39')
    if temp is None:
        temp = v39
    if action is not None and hasattr(action, "view4".split('.')[0]):
        action.view4 = temp
    else:
        view4 = temp 
    if model is not None: 
        model.view4 = view4
        model.last_view4 = copy.deepcopy(view4)

    if model is not None:
        v52 = View()
        model.add_object(v52) # add object to model
    else:
        v52 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v52

    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v53".split('.')[0]):
        action.v53 = temp
    else:
        v53 = temp 


    temp = get_nested_attribute(action, 'v53')
    if temp is None:
        temp = v53
    if action is not None and hasattr(action, "v54".split('.')[0]):
        action.v54 = temp
    else:
        v54 = temp 


    temp = get_nested_attribute(action, 'v54')
    if temp is None:
        temp = v54
    if action is not None and hasattr(action, "v55".split('.')[0]):
        action.v55 = temp
    else:
        v55 = temp 


    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v56".split('.')[0]):
        action.v56 = temp
    else:
        v56 = temp 


    temp = get_nested_attribute(action, 'v56')
    if temp is None:
        temp = v56
    if action is not None and hasattr(action, "v57".split('.')[0]):
        action.v57 = temp
    else:
        v57 = temp 


    temp = get_nested_attribute(action, 'v57')
    if temp is None:
        temp = v57
    if action is not None and hasattr(action, "v58".split('.')[0]):
        action.v58 = temp
    else:
        v58 = temp 


    temp = get_nested_attribute(action, '"Text"')
    if temp is None:
        temp = "Text"
    if action is not None and hasattr(action, "v59".split('.')[0]):
        action.v59 = temp
    else:
        v59 = temp 


    temp = get_nested_attribute(action, 'v59')
    if temp is None:
        temp = v59
    if action is not None and hasattr(action, "v60".split('.')[0]):
        action.v60 = temp
    else:
        v60 = temp 


    temp = get_nested_attribute(action, 'v60')
    if temp is None:
        temp = v60
    if action is not None and hasattr(action, "v61".split('.')[0]):
        action.v61 = temp
    else:
        v61 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v62".split('.')[0]):
        action.v62 = temp
    else:
        v62 = temp 


    temp = get_nested_attribute(action, 'v62')
    if temp is None:
        temp = v62
    if action is not None and hasattr(action, "v63".split('.')[0]):
        action.v63 = temp
    else:
        v63 = temp 


    temp = get_nested_attribute(action, 'v63')
    if temp is None:
        temp = v63
    if action is not None and hasattr(action, "v64".split('.')[0]):
        action.v64 = temp
    else:
        v64 = temp 


    if action is not None:
        action.v52.width = v55
        action.v52.height = v58
        action.v52.title = v61
        action.v52.background = v64
    else:
        v52.width = v55
        v52.height = v58
        v52.title = v61
        v52.background = v64

    temp = get_nested_attribute(action, 'v52')
    if temp is None:
        temp = v52
    if action is not None and hasattr(action, "view5".split('.')[0]):
        action.view5 = temp
    else:
        view5 = temp 
    if model is not None: 
        model.view5 = view5
        model.last_view5 = copy.deepcopy(view5)
    #################################################################
    ## Model
    #################################################################
    class Ex1(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '200')
            if temp is None:
                temp = 200
            if action is not None and hasattr(action, "v65".split('.')[0]):
                action.v65 = temp
            else:
                v65 = temp 


            temp = get_nested_attribute(action, 'v65')
            if temp is None:
                temp = v65
            if action is not None and hasattr(action, "v66".split('.')[0]):
                action.v66 = temp
            else:
                v66 = temp 


            temp = get_nested_attribute(action, 'v66')
            if temp is None:
                temp = v66
            if action is not None and hasattr(action, "v67".split('.')[0]):
                action.v67 = temp
            else:
                v67 = temp 


            temp = get_nested_attribute(action, 'v67')
            if temp is None:
                temp = v67
            if action is not None and hasattr(action, "cellSize".split('.')[0]):
                action.cellSize = temp
            else:
                cellSize = temp 
            if model is not None: 
                model.cellSize = cellSize
                model.last_cellSize = copy.deepcopy(cellSize)

            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v69".split('.')[0]):
                action.v69 = temp
            else:
                v69 = temp 

            v70 = - np.array(v69)

            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v71".split('.')[0]):
                action.v71 = temp
            else:
                v71 = temp 

            v68 = (v70 , v71); v68 = tuple(v68) if isinstance(v68, np.ndarray) else v68

            if model is not None:
                v72 = Line()
                model.add_object(v72) # add object to model
            else:
                v72 = Line(root = root)
            v72.origin = v68

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v74".split('.')[0]):
                action.v74 = temp
            else:
                v74 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v75".split('.')[0]):
                action.v75 = temp
            else:
                v75 = temp 

            v73 = (v74 , v75); v73 = tuple(v73) if isinstance(v73, np.ndarray) else v73

            temp = get_nested_attribute(action, 'v73')
            if temp is None:
                temp = v73
            if action is not None and hasattr(action, "v76".split('.')[0]):
                action.v76 = temp
            else:
                v76 = temp 


            temp = get_nested_attribute(action, 'v76')
            if temp is None:
                temp = v76
            if action is not None and hasattr(action, "v77".split('.')[0]):
                action.v77 = temp
            else:
                v77 = temp 


            temp = get_nested_attribute(action, '"red"')
            if temp is None:
                temp = "red"
            if action is not None and hasattr(action, "v78".split('.')[0]):
                action.v78 = temp
            else:
                v78 = temp 


            temp = get_nested_attribute(action, 'v78')
            if temp is None:
                temp = v78
            if action is not None and hasattr(action, "v79".split('.')[0]):
                action.v79 = temp
            else:
                v79 = temp 


            temp = get_nested_attribute(action, 'v79')
            if temp is None:
                temp = v79
            if action is not None and hasattr(action, "v80".split('.')[0]):
                action.v80 = temp
            else:
                v80 = temp 


            if action is not None:
                action.v72.length = v77
                action.v72.fill = v80
            else:
                v72.length = v77
                v72.fill = v80

            temp = get_nested_attribute(action, 'v72')
            if temp is None:
                temp = v72
            if action is not None and hasattr(action, "line".split('.')[0]):
                action.line = temp
            else:
                line = temp 
            if model is not None: 
                model.line = line
                model.last_line = copy.deepcopy(line)

            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v82".split('.')[0]):
                action.v82 = temp
            else:
                v82 = temp 


            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v83".split('.')[0]):
                action.v83 = temp
            else:
                v83 = temp 

            v81 = (v82 , v83); v81 = tuple(v81) if isinstance(v81, np.ndarray) else v81

            if model is not None:
                v84 = Rectangle()
                model.add_object(v84) # add object to model
            else:
                v84 = Rectangle(root = root)
            v84.origin = v81

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v86".split('.')[0]):
                action.v86 = temp
            else:
                v86 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v87".split('.')[0]):
                action.v87 = temp
            else:
                v87 = temp 

            v85 = (v86 , v87); v85 = tuple(v85) if isinstance(v85, np.ndarray) else v85

            temp = get_nested_attribute(action, 'v85')
            if temp is None:
                temp = v85
            if action is not None and hasattr(action, "v88".split('.')[0]):
                action.v88 = temp
            else:
                v88 = temp 


            temp = get_nested_attribute(action, 'v88')
            if temp is None:
                temp = v88
            if action is not None and hasattr(action, "v89".split('.')[0]):
                action.v89 = temp
            else:
                v89 = temp 


            temp = get_nested_attribute(action, '"orange"')
            if temp is None:
                temp = "orange"
            if action is not None and hasattr(action, "v90".split('.')[0]):
                action.v90 = temp
            else:
                v90 = temp 


            temp = get_nested_attribute(action, 'v90')
            if temp is None:
                temp = v90
            if action is not None and hasattr(action, "v91".split('.')[0]):
                action.v91 = temp
            else:
                v91 = temp 


            temp = get_nested_attribute(action, 'v91')
            if temp is None:
                temp = v91
            if action is not None and hasattr(action, "v92".split('.')[0]):
                action.v92 = temp
            else:
                v92 = temp 


            if action is not None:
                action.v84.length = v89
                action.v84.fill = v92
            else:
                v84.length = v89
                v84.fill = v92

            temp = get_nested_attribute(action, 'v84')
            if temp is None:
                temp = v84
            if action is not None and hasattr(action, "rec".split('.')[0]):
                action.rec = temp
            else:
                rec = temp 
            if model is not None: 
                model.rec = rec
                model.last_rec = copy.deepcopy(rec)

            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v94".split('.')[0]):
                action.v94 = temp
            else:
                v94 = temp 


            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v95".split('.')[0]):
                action.v95 = temp
            else:
                v95 = temp 

            v93 = (v94 , v95); v93 = tuple(v93) if isinstance(v93, np.ndarray) else v93

            if model is not None:
                v96 = Ellipse()
                model.add_object(v96) # add object to model
            else:
                v96 = Ellipse(root = root)
            v96.origin = v93

            temp = get_nested_attribute(action, '60')
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v98".split('.')[0]):
                action.v98 = temp
            else:
                v98 = temp 


            temp = get_nested_attribute(action, '40')
            if temp is None:
                temp = 40
            if action is not None and hasattr(action, "v99".split('.')[0]):
                action.v99 = temp
            else:
                v99 = temp 

            v97 = (v98 , v99); v97 = tuple(v97) if isinstance(v97, np.ndarray) else v97

            temp = get_nested_attribute(action, 'v97')
            if temp is None:
                temp = v97
            if action is not None and hasattr(action, "v100".split('.')[0]):
                action.v100 = temp
            else:
                v100 = temp 


            temp = get_nested_attribute(action, 'v100')
            if temp is None:
                temp = v100
            if action is not None and hasattr(action, "v101".split('.')[0]):
                action.v101 = temp
            else:
                v101 = temp 


            temp = get_nested_attribute(action, '"blue"')
            if temp is None:
                temp = "blue"
            if action is not None and hasattr(action, "v102".split('.')[0]):
                action.v102 = temp
            else:
                v102 = temp 


            temp = get_nested_attribute(action, 'v102')
            if temp is None:
                temp = v102
            if action is not None and hasattr(action, "v103".split('.')[0]):
                action.v103 = temp
            else:
                v103 = temp 


            temp = get_nested_attribute(action, 'v103')
            if temp is None:
                temp = v103
            if action is not None and hasattr(action, "v104".split('.')[0]):
                action.v104 = temp
            else:
                v104 = temp 


            if action is not None:
                action.v96.length = v101
                action.v96.fill = v104
            else:
                v96.length = v101
                v96.fill = v104

            temp = get_nested_attribute(action, 'v96')
            if temp is None:
                temp = v96
            if action is not None and hasattr(action, "ell".split('.')[0]):
                action.ell = temp
            else:
                ell = temp 
            if model is not None: 
                model.ell = ell
                model.last_ell = copy.deepcopy(ell)

            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v106".split('.')[0]):
                action.v106 = temp
            else:
                v106 = temp 


            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v107".split('.')[0]):
                action.v107 = temp
            else:
                v107 = temp 

            v108 = - np.array(v107)
            v105 = (v106 , v108); v105 = tuple(v105) if isinstance(v105, np.ndarray) else v105

            if model is not None:
                v109 = Text()
                model.add_object(v109) # add object to model
            else:
                v109 = Text(root = root)
            v109.origin = v105

            temp = get_nested_attribute(action, '"Bla bla ..."')
            if temp is None:
                temp = "Bla bla ..."
            if action is not None and hasattr(action, "v110".split('.')[0]):
                action.v110 = temp
            else:
                v110 = temp 


            temp = get_nested_attribute(action, 'v110')
            if temp is None:
                temp = v110
            if action is not None and hasattr(action, "v111".split('.')[0]):
                action.v111 = temp
            else:
                v111 = temp 


            temp = get_nested_attribute(action, 'v111')
            if temp is None:
                temp = v111
            if action is not None and hasattr(action, "v112".split('.')[0]):
                action.v112 = temp
            else:
                v112 = temp 


            temp = get_nested_attribute(action, '"purple"')
            if temp is None:
                temp = "purple"
            if action is not None and hasattr(action, "v113".split('.')[0]):
                action.v113 = temp
            else:
                v113 = temp 


            temp = get_nested_attribute(action, 'v113')
            if temp is None:
                temp = v113
            if action is not None and hasattr(action, "v114".split('.')[0]):
                action.v114 = temp
            else:
                v114 = temp 


            temp = get_nested_attribute(action, 'v114')
            if temp is None:
                temp = v114
            if action is not None and hasattr(action, "v115".split('.')[0]):
                action.v115 = temp
            else:
                v115 = temp 


            if action is not None:
                action.v109.text = v112
                action.v109.fill = v115
            else:
                v109.text = v112
                v109.fill = v115

            temp = get_nested_attribute(action, 'v109')
            if temp is None:
                temp = v109
            if action is not None and hasattr(action, "text".split('.')[0]):
                action.text = temp
            else:
                text = temp 
            if model is not None: 
                model.text = text
                model.last_text = copy.deepcopy(text)

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
            new_model = Ex1()

            self.copyAttributesTo(new_model)
            return new_model       

    #################################################################

    if model is not None:
        model_backup = model
        v116 = Ex1() # this makes model = None in the end!
        model = model_backup
        model.add_object(v116) # add object to model
    else:
        v116 = Ex1(root = root, view = last_view)
      

    temp = get_nested_attribute(action, 'v116')
    if temp is None:
        temp = v116
    if action is not None and hasattr(action, "v117".split('.')[0]):
        action.v117 = temp
    else:
        v117 = temp 


    temp = get_nested_attribute(action, 'v117')
    if temp is None:
        temp = v117
    if action is not None and hasattr(action, "ex1".split('.')[0]):
        action.ex1 = temp
    else:
        ex1 = temp 
    if model is not None: 
        model.ex1 = ex1
        model.last_ex1 = copy.deepcopy(ex1)

    temp = get_nested_attribute(action, '0.5')
    if temp is None:
        temp = 0.5
    if action is not None and hasattr(action, "v118".split('.')[0]):
        action.v118 = temp
    else:
        v118 = temp 

     
    while (time.time() - last_refresh <= v118):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    view.update()

    last_refresh = time.time()
    view2.update()

    last_refresh = time.time()
    view3.update()

    last_refresh = time.time()
    view4.update()

    last_refresh = time.time()
    view5.update()


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v119".split('.')[0]):
        action.v119 = temp
    else:
        v119 = temp 


    temp = get_nested_attribute(action, '1000')
    if temp is None:
        temp = 1000
    if action is not None and hasattr(action, "v120".split('.')[0]):
        action.v120 = temp
    else:
        v120 = temp 

    for i in range(v119, v120, 1):

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v121".split('.')[0]):
            action.v121 = temp
        else:
            v121 = temp 

        if action is not None:
            action.ex1.rotate(v121)
        else:
            ex1.rotate(v121)

        temp = get_nested_attribute(action, 'ex1.line.origin')
        if temp is None:
            temp = ex1.line.origin
        if action is not None and hasattr(action, "v122".split('.')[0]):
            action.v122 = temp
        else:
            v122 = temp 

        if action is not None:
            action.view2.move_absolute(v122)
        else:
            view2.move_absolute(v122)

        temp = get_nested_attribute(action, 'ex1.rec.origin')
        if temp is None:
            temp = ex1.rec.origin
        if action is not None and hasattr(action, "v123".split('.')[0]):
            action.v123 = temp
        else:
            v123 = temp 

        if action is not None:
            action.view3.move_absolute(v123)
        else:
            view3.move_absolute(v123)

        temp = get_nested_attribute(action, 'ex1.ell.origin')
        if temp is None:
            temp = ex1.ell.origin
        if action is not None and hasattr(action, "v124".split('.')[0]):
            action.v124 = temp
        else:
            v124 = temp 

        if action is not None:
            action.view4.move_absolute(v124)
        else:
            view4.move_absolute(v124)

        temp = get_nested_attribute(action, 'ex1.text.origin')
        if temp is None:
            temp = ex1.text.origin
        if action is not None and hasattr(action, "v125".split('.')[0]):
            action.v125 = temp
        else:
            v125 = temp 

        if action is not None:
            action.view5.move_absolute(v125)
        else:
            view5.move_absolute(v125)

        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v126".split('.')[0]):
            action.v126 = temp
        else:
            v126 = temp 

         
        while (time.time() - last_refresh <= v126/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()

        last_refresh = time.time()
        view2.update()

        last_refresh = time.time()
        view3.update()

        last_refresh = time.time()
        view4.update()

        last_refresh = time.time()
        view5.update()


    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v127".split('.')[0]):
        action.v127 = temp
    else:
        v127 = temp 

    print(v127)
    if action is not None:
        v128 = action.view.waitClick()
    else:
        v128 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v128')
    if temp is None:
        temp = v128
    if action is not None and hasattr(action, "v129".split('.')[0]):
        action.v129 = temp
    else:
        v129 = temp 


    temp = get_nested_attribute(action, 'v129')
    if temp is None:
        temp = v129
    if action is not None and hasattr(action, "v130".split('.')[0]):
        action.v130 = temp
    else:
        v130 = temp 


    temp = get_nested_attribute(action, 'v130')
    if temp is None:
        temp = v130
    if action is not None and hasattr(action, "p".split('.')[0]):
        action.p = temp
    else:
        p = temp 
    if model is not None: 
        model.p = p
        model.last_p = copy.deepcopy(p)

    temp = get_nested_attribute(action, 'p')
    if temp is None:
        temp = p
    if action is not None and hasattr(action, "v131".split('.')[0]):
        action.v131 = temp
    else:
        v131 = temp 

    print(v131)
    view.close(); views.remove(view) if last_view != view else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == view else last_view
