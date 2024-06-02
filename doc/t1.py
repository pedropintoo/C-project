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

    if model is not None:
        v65 = View()
        model.add_object(v65) # add object to model
    else:
        v65 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v65

    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
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
    if action is not None and hasattr(action, "v68".split('.')[0]):
        action.v68 = temp
    else:
        v68 = temp 


    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v69".split('.')[0]):
        action.v69 = temp
    else:
        v69 = temp 


    temp = get_nested_attribute(action, 'v69')
    if temp is None:
        temp = v69
    if action is not None and hasattr(action, "v70".split('.')[0]):
        action.v70 = temp
    else:
        v70 = temp 


    temp = get_nested_attribute(action, 'v70')
    if temp is None:
        temp = v70
    if action is not None and hasattr(action, "v71".split('.')[0]):
        action.v71 = temp
    else:
        v71 = temp 


    temp = get_nested_attribute(action, '"Arc"')
    if temp is None:
        temp = "Arc"
    if action is not None and hasattr(action, "v72".split('.')[0]):
        action.v72 = temp
    else:
        v72 = temp 


    temp = get_nested_attribute(action, 'v72')
    if temp is None:
        temp = v72
    if action is not None and hasattr(action, "v73".split('.')[0]):
        action.v73 = temp
    else:
        v73 = temp 


    temp = get_nested_attribute(action, 'v73')
    if temp is None:
        temp = v73
    if action is not None and hasattr(action, "v74".split('.')[0]):
        action.v74 = temp
    else:
        v74 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v75".split('.')[0]):
        action.v75 = temp
    else:
        v75 = temp 


    temp = get_nested_attribute(action, 'v75')
    if temp is None:
        temp = v75
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


    if action is not None:
        action.v65.width = v68
        action.v65.height = v71
        action.v65.title = v74
        action.v65.background = v77
    else:
        v65.width = v68
        v65.height = v71
        v65.title = v74
        v65.background = v77

    temp = get_nested_attribute(action, 'v65')
    if temp is None:
        temp = v65
    if action is not None and hasattr(action, "view6".split('.')[0]):
        action.view6 = temp
    else:
        view6 = temp 
    if model is not None: 
        model.view6 = view6
        model.last_view6 = copy.deepcopy(view6)

    if model is not None:
        v78 = View()
        model.add_object(v78) # add object to model
    else:
        v78 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v78

    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
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


    temp = get_nested_attribute(action, 'v80')
    if temp is None:
        temp = v80
    if action is not None and hasattr(action, "v81".split('.')[0]):
        action.v81 = temp
    else:
        v81 = temp 


    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v82".split('.')[0]):
        action.v82 = temp
    else:
        v82 = temp 


    temp = get_nested_attribute(action, 'v82')
    if temp is None:
        temp = v82
    if action is not None and hasattr(action, "v83".split('.')[0]):
        action.v83 = temp
    else:
        v83 = temp 


    temp = get_nested_attribute(action, 'v83')
    if temp is None:
        temp = v83
    if action is not None and hasattr(action, "v84".split('.')[0]):
        action.v84 = temp
    else:
        v84 = temp 


    temp = get_nested_attribute(action, '"ArcChord"')
    if temp is None:
        temp = "ArcChord"
    if action is not None and hasattr(action, "v85".split('.')[0]):
        action.v85 = temp
    else:
        v85 = temp 


    temp = get_nested_attribute(action, 'v85')
    if temp is None:
        temp = v85
    if action is not None and hasattr(action, "v86".split('.')[0]):
        action.v86 = temp
    else:
        v86 = temp 


    temp = get_nested_attribute(action, 'v86')
    if temp is None:
        temp = v86
    if action is not None and hasattr(action, "v87".split('.')[0]):
        action.v87 = temp
    else:
        v87 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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


    temp = get_nested_attribute(action, 'v89')
    if temp is None:
        temp = v89
    if action is not None and hasattr(action, "v90".split('.')[0]):
        action.v90 = temp
    else:
        v90 = temp 


    if action is not None:
        action.v78.width = v81
        action.v78.height = v84
        action.v78.title = v87
        action.v78.background = v90
    else:
        v78.width = v81
        v78.height = v84
        v78.title = v87
        v78.background = v90

    temp = get_nested_attribute(action, 'v78')
    if temp is None:
        temp = v78
    if action is not None and hasattr(action, "view7".split('.')[0]):
        action.view7 = temp
    else:
        view7 = temp 
    if model is not None: 
        model.view7 = view7
        model.last_view7 = copy.deepcopy(view7)

    if model is not None:
        v91 = View()
        model.add_object(v91) # add object to model
    else:
        v91 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v91

    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v92".split('.')[0]):
        action.v92 = temp
    else:
        v92 = temp 


    temp = get_nested_attribute(action, 'v92')
    if temp is None:
        temp = v92
    if action is not None and hasattr(action, "v93".split('.')[0]):
        action.v93 = temp
    else:
        v93 = temp 


    temp = get_nested_attribute(action, 'v93')
    if temp is None:
        temp = v93
    if action is not None and hasattr(action, "v94".split('.')[0]):
        action.v94 = temp
    else:
        v94 = temp 


    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v95".split('.')[0]):
        action.v95 = temp
    else:
        v95 = temp 


    temp = get_nested_attribute(action, 'v95')
    if temp is None:
        temp = v95
    if action is not None and hasattr(action, "v96".split('.')[0]):
        action.v96 = temp
    else:
        v96 = temp 


    temp = get_nested_attribute(action, 'v96')
    if temp is None:
        temp = v96
    if action is not None and hasattr(action, "v97".split('.')[0]):
        action.v97 = temp
    else:
        v97 = temp 


    temp = get_nested_attribute(action, '"PieSlice"')
    if temp is None:
        temp = "PieSlice"
    if action is not None and hasattr(action, "v98".split('.')[0]):
        action.v98 = temp
    else:
        v98 = temp 


    temp = get_nested_attribute(action, 'v98')
    if temp is None:
        temp = v98
    if action is not None and hasattr(action, "v99".split('.')[0]):
        action.v99 = temp
    else:
        v99 = temp 


    temp = get_nested_attribute(action, 'v99')
    if temp is None:
        temp = v99
    if action is not None and hasattr(action, "v100".split('.')[0]):
        action.v100 = temp
    else:
        v100 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v101".split('.')[0]):
        action.v101 = temp
    else:
        v101 = temp 


    temp = get_nested_attribute(action, 'v101')
    if temp is None:
        temp = v101
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


    if action is not None:
        action.v91.width = v94
        action.v91.height = v97
        action.v91.title = v100
        action.v91.background = v103
    else:
        v91.width = v94
        v91.height = v97
        v91.title = v100
        v91.background = v103

    temp = get_nested_attribute(action, 'v91')
    if temp is None:
        temp = v91
    if action is not None and hasattr(action, "view8".split('.')[0]):
        action.view8 = temp
    else:
        view8 = temp 
    if model is not None: 
        model.view8 = view8
        model.last_view8 = copy.deepcopy(view8)

    if model is not None:
        v104 = View()
        model.add_object(v104) # add object to model
    else:
        v104 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v104

    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v105".split('.')[0]):
        action.v105 = temp
    else:
        v105 = temp 


    temp = get_nested_attribute(action, 'v105')
    if temp is None:
        temp = v105
    if action is not None and hasattr(action, "v106".split('.')[0]):
        action.v106 = temp
    else:
        v106 = temp 


    temp = get_nested_attribute(action, 'v106')
    if temp is None:
        temp = v106
    if action is not None and hasattr(action, "v107".split('.')[0]):
        action.v107 = temp
    else:
        v107 = temp 


    temp = get_nested_attribute(action, '200')
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v108".split('.')[0]):
        action.v108 = temp
    else:
        v108 = temp 


    temp = get_nested_attribute(action, 'v108')
    if temp is None:
        temp = v108
    if action is not None and hasattr(action, "v109".split('.')[0]):
        action.v109 = temp
    else:
        v109 = temp 


    temp = get_nested_attribute(action, 'v109')
    if temp is None:
        temp = v109
    if action is not None and hasattr(action, "v110".split('.')[0]):
        action.v110 = temp
    else:
        v110 = temp 


    temp = get_nested_attribute(action, '"Dot"')
    if temp is None:
        temp = "Dot"
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


    temp = get_nested_attribute(action, 'v112')
    if temp is None:
        temp = v112
    if action is not None and hasattr(action, "v113".split('.')[0]):
        action.v113 = temp
    else:
        v113 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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


    temp = get_nested_attribute(action, 'v115')
    if temp is None:
        temp = v115
    if action is not None and hasattr(action, "v116".split('.')[0]):
        action.v116 = temp
    else:
        v116 = temp 


    if action is not None:
        action.v104.width = v107
        action.v104.height = v110
        action.v104.title = v113
        action.v104.background = v116
    else:
        v104.width = v107
        v104.height = v110
        v104.title = v113
        v104.background = v116

    temp = get_nested_attribute(action, 'v104')
    if temp is None:
        temp = v104
    if action is not None and hasattr(action, "view9".split('.')[0]):
        action.view9 = temp
    else:
        view9 = temp 
    if model is not None: 
        model.view9 = view9
        model.last_view9 = copy.deepcopy(view9)
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
            if action is not None and hasattr(action, "v117".split('.')[0]):
                action.v117 = temp
            else:
                v117 = temp 


            temp = get_nested_attribute(action, 'v117')
            if temp is None:
                temp = v117
            if action is not None and hasattr(action, "v118".split('.')[0]):
                action.v118 = temp
            else:
                v118 = temp 


            temp = get_nested_attribute(action, 'v118')
            if temp is None:
                temp = v118
            if action is not None and hasattr(action, "v119".split('.')[0]):
                action.v119 = temp
            else:
                v119 = temp 


            temp = get_nested_attribute(action, 'v119')
            if temp is None:
                temp = v119
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
            if action is not None and hasattr(action, "v121".split('.')[0]):
                action.v121 = temp
            else:
                v121 = temp 

            v122 = - np.array(v121)

            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v123".split('.')[0]):
                action.v123 = temp
            else:
                v123 = temp 

            v120 = (v122 , v123); v120 = tuple(v120) if isinstance(v120, np.ndarray) else v120

            if model is not None:
                v124 = Line()
                model.add_object(v124) # add object to model
            else:
                v124 = Line(root = root)
            v124.origin = v120

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v126".split('.')[0]):
                action.v126 = temp
            else:
                v126 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v127".split('.')[0]):
                action.v127 = temp
            else:
                v127 = temp 

            v125 = (v126 , v127); v125 = tuple(v125) if isinstance(v125, np.ndarray) else v125

            temp = get_nested_attribute(action, 'v125')
            if temp is None:
                temp = v125
            if action is not None and hasattr(action, "v128".split('.')[0]):
                action.v128 = temp
            else:
                v128 = temp 


            temp = get_nested_attribute(action, 'v128')
            if temp is None:
                temp = v128
            if action is not None and hasattr(action, "v129".split('.')[0]):
                action.v129 = temp
            else:
                v129 = temp 


            temp = get_nested_attribute(action, '"red"')
            if temp is None:
                temp = "red"
            if action is not None and hasattr(action, "v130".split('.')[0]):
                action.v130 = temp
            else:
                v130 = temp 


            temp = get_nested_attribute(action, 'v130')
            if temp is None:
                temp = v130
            if action is not None and hasattr(action, "v131".split('.')[0]):
                action.v131 = temp
            else:
                v131 = temp 


            temp = get_nested_attribute(action, 'v131')
            if temp is None:
                temp = v131
            if action is not None and hasattr(action, "v132".split('.')[0]):
                action.v132 = temp
            else:
                v132 = temp 


            if action is not None:
                action.v124.length = v129
                action.v124.fill = v132
            else:
                v124.length = v129
                v124.fill = v132

            temp = get_nested_attribute(action, 'v124')
            if temp is None:
                temp = v124
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
            if action is not None and hasattr(action, "v134".split('.')[0]):
                action.v134 = temp
            else:
                v134 = temp 


            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v135".split('.')[0]):
                action.v135 = temp
            else:
                v135 = temp 

            v133 = (v134 , v135); v133 = tuple(v133) if isinstance(v133, np.ndarray) else v133

            if model is not None:
                v136 = Rectangle()
                model.add_object(v136) # add object to model
            else:
                v136 = Rectangle(root = root)
            v136.origin = v133

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v138".split('.')[0]):
                action.v138 = temp
            else:
                v138 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v139".split('.')[0]):
                action.v139 = temp
            else:
                v139 = temp 

            v137 = (v138 , v139); v137 = tuple(v137) if isinstance(v137, np.ndarray) else v137

            temp = get_nested_attribute(action, 'v137')
            if temp is None:
                temp = v137
            if action is not None and hasattr(action, "v140".split('.')[0]):
                action.v140 = temp
            else:
                v140 = temp 


            temp = get_nested_attribute(action, 'v140')
            if temp is None:
                temp = v140
            if action is not None and hasattr(action, "v141".split('.')[0]):
                action.v141 = temp
            else:
                v141 = temp 


            temp = get_nested_attribute(action, '"orange"')
            if temp is None:
                temp = "orange"
            if action is not None and hasattr(action, "v142".split('.')[0]):
                action.v142 = temp
            else:
                v142 = temp 


            temp = get_nested_attribute(action, 'v142')
            if temp is None:
                temp = v142
            if action is not None and hasattr(action, "v143".split('.')[0]):
                action.v143 = temp
            else:
                v143 = temp 


            temp = get_nested_attribute(action, 'v143')
            if temp is None:
                temp = v143
            if action is not None and hasattr(action, "v144".split('.')[0]):
                action.v144 = temp
            else:
                v144 = temp 


            if action is not None:
                action.v136.length = v141
                action.v136.fill = v144
            else:
                v136.length = v141
                v136.fill = v144

            temp = get_nested_attribute(action, 'v136')
            if temp is None:
                temp = v136
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
            if action is not None and hasattr(action, "v146".split('.')[0]):
                action.v146 = temp
            else:
                v146 = temp 


            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v147".split('.')[0]):
                action.v147 = temp
            else:
                v147 = temp 

            v145 = (v146 , v147); v145 = tuple(v145) if isinstance(v145, np.ndarray) else v145

            if model is not None:
                v148 = Ellipse()
                model.add_object(v148) # add object to model
            else:
                v148 = Ellipse(root = root)
            v148.origin = v145

            temp = get_nested_attribute(action, '60')
            if temp is None:
                temp = 60
            if action is not None and hasattr(action, "v150".split('.')[0]):
                action.v150 = temp
            else:
                v150 = temp 


            temp = get_nested_attribute(action, '40')
            if temp is None:
                temp = 40
            if action is not None and hasattr(action, "v151".split('.')[0]):
                action.v151 = temp
            else:
                v151 = temp 

            v149 = (v150 , v151); v149 = tuple(v149) if isinstance(v149, np.ndarray) else v149

            temp = get_nested_attribute(action, 'v149')
            if temp is None:
                temp = v149
            if action is not None and hasattr(action, "v152".split('.')[0]):
                action.v152 = temp
            else:
                v152 = temp 


            temp = get_nested_attribute(action, 'v152')
            if temp is None:
                temp = v152
            if action is not None and hasattr(action, "v153".split('.')[0]):
                action.v153 = temp
            else:
                v153 = temp 


            temp = get_nested_attribute(action, '"blue"')
            if temp is None:
                temp = "blue"
            if action is not None and hasattr(action, "v154".split('.')[0]):
                action.v154 = temp
            else:
                v154 = temp 


            temp = get_nested_attribute(action, 'v154')
            if temp is None:
                temp = v154
            if action is not None and hasattr(action, "v155".split('.')[0]):
                action.v155 = temp
            else:
                v155 = temp 


            temp = get_nested_attribute(action, 'v155')
            if temp is None:
                temp = v155
            if action is not None and hasattr(action, "v156".split('.')[0]):
                action.v156 = temp
            else:
                v156 = temp 


            if action is not None:
                action.v148.length = v153
                action.v148.fill = v156
            else:
                v148.length = v153
                v148.fill = v156

            temp = get_nested_attribute(action, 'v148')
            if temp is None:
                temp = v148
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
            if action is not None and hasattr(action, "v158".split('.')[0]):
                action.v158 = temp
            else:
                v158 = temp 


            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v159".split('.')[0]):
                action.v159 = temp
            else:
                v159 = temp 

            v160 = - np.array(v159)
            v157 = (v158 , v160); v157 = tuple(v157) if isinstance(v157, np.ndarray) else v157

            if model is not None:
                v161 = Text()
                model.add_object(v161) # add object to model
            else:
                v161 = Text(root = root)
            v161.origin = v157

            temp = get_nested_attribute(action, '"Bla bla ..."')
            if temp is None:
                temp = "Bla bla ..."
            if action is not None and hasattr(action, "v162".split('.')[0]):
                action.v162 = temp
            else:
                v162 = temp 


            temp = get_nested_attribute(action, 'v162')
            if temp is None:
                temp = v162
            if action is not None and hasattr(action, "v163".split('.')[0]):
                action.v163 = temp
            else:
                v163 = temp 


            temp = get_nested_attribute(action, 'v163')
            if temp is None:
                temp = v163
            if action is not None and hasattr(action, "v164".split('.')[0]):
                action.v164 = temp
            else:
                v164 = temp 


            temp = get_nested_attribute(action, '"purple"')
            if temp is None:
                temp = "purple"
            if action is not None and hasattr(action, "v165".split('.')[0]):
                action.v165 = temp
            else:
                v165 = temp 


            temp = get_nested_attribute(action, 'v165')
            if temp is None:
                temp = v165
            if action is not None and hasattr(action, "v166".split('.')[0]):
                action.v166 = temp
            else:
                v166 = temp 


            temp = get_nested_attribute(action, 'v166')
            if temp is None:
                temp = v166
            if action is not None and hasattr(action, "v167".split('.')[0]):
                action.v167 = temp
            else:
                v167 = temp 


            if action is not None:
                action.v161.text = v164
                action.v161.fill = v167
            else:
                v161.text = v164
                v161.fill = v167

            temp = get_nested_attribute(action, 'v161')
            if temp is None:
                temp = v161
            if action is not None and hasattr(action, "text".split('.')[0]):
                action.text = temp
            else:
                text = temp 
            if model is not None: 
                model.text = text
                model.last_text = copy.deepcopy(text)

            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v169".split('.')[0]):
                action.v169 = temp
            else:
                v169 = temp 

            v170 = - np.array(v169)

            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v171".split('.')[0]):
                action.v171 = temp
            else:
                v171 = temp 

            v168 = (v170 , v171); v168 = tuple(v168) if isinstance(v168, np.ndarray) else v168

            if model is not None:
                v172 = Arc()
                model.add_object(v172) # add object to model
            else:
                v172 = Arc(root = root)
            v172.origin = v168

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v174".split('.')[0]):
                action.v174 = temp
            else:
                v174 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v175".split('.')[0]):
                action.v175 = temp
            else:
                v175 = temp 

            v173 = (v174 , v175); v173 = tuple(v173) if isinstance(v173, np.ndarray) else v173

            temp = get_nested_attribute(action, 'v173')
            if temp is None:
                temp = v173
            if action is not None and hasattr(action, "v176".split('.')[0]):
                action.v176 = temp
            else:
                v176 = temp 


            temp = get_nested_attribute(action, 'v176')
            if temp is None:
                temp = v176
            if action is not None and hasattr(action, "v177".split('.')[0]):
                action.v177 = temp
            else:
                v177 = temp 


            temp = get_nested_attribute(action, '30')
            if temp is None:
                temp = 30
            if action is not None and hasattr(action, "v178".split('.')[0]):
                action.v178 = temp
            else:
                v178 = temp 


            temp = get_nested_attribute(action, 'v178')
            if temp is None:
                temp = v178
            if action is not None and hasattr(action, "v179".split('.')[0]):
                action.v179 = temp
            else:
                v179 = temp 


            temp = get_nested_attribute(action, 'v179')
            if temp is None:
                temp = v179
            if action is not None and hasattr(action, "v180".split('.')[0]):
                action.v180 = temp
            else:
                v180 = temp 


            temp = get_nested_attribute(action, '100')
            if temp is None:
                temp = 100
            if action is not None and hasattr(action, "v181".split('.')[0]):
                action.v181 = temp
            else:
                v181 = temp 


            temp = get_nested_attribute(action, 'v181')
            if temp is None:
                temp = v181
            if action is not None and hasattr(action, "v182".split('.')[0]):
                action.v182 = temp
            else:
                v182 = temp 


            temp = get_nested_attribute(action, 'v182')
            if temp is None:
                temp = v182
            if action is not None and hasattr(action, "v183".split('.')[0]):
                action.v183 = temp
            else:
                v183 = temp 


            temp = get_nested_attribute(action, '"tomato"')
            if temp is None:
                temp = "tomato"
            if action is not None and hasattr(action, "v184".split('.')[0]):
                action.v184 = temp
            else:
                v184 = temp 


            temp = get_nested_attribute(action, 'v184')
            if temp is None:
                temp = v184
            if action is not None and hasattr(action, "v185".split('.')[0]):
                action.v185 = temp
            else:
                v185 = temp 


            temp = get_nested_attribute(action, 'v185')
            if temp is None:
                temp = v185
            if action is not None and hasattr(action, "v186".split('.')[0]):
                action.v186 = temp
            else:
                v186 = temp 


            if action is not None:
                action.v172.length = v177
                action.v172.start = v180
                action.v172.extent = v183
                action.v172.outline = v186
            else:
                v172.length = v177
                v172.start = v180
                v172.extent = v183
                v172.outline = v186

            temp = get_nested_attribute(action, 'v172')
            if temp is None:
                temp = v172
            if action is not None and hasattr(action, "arc".split('.')[0]):
                action.arc = temp
            else:
                arc = temp 
            if model is not None: 
                model.arc = arc
                model.last_arc = copy.deepcopy(arc)

            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v188".split('.')[0]):
                action.v188 = temp
            else:
                v188 = temp 


            temp = get_nested_attribute(action, '0')
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v189".split('.')[0]):
                action.v189 = temp
            else:
                v189 = temp 

            v187 = (v188 , v189); v187 = tuple(v187) if isinstance(v187, np.ndarray) else v187

            if model is not None:
                v190 = ArcChord()
                model.add_object(v190) # add object to model
            else:
                v190 = ArcChord(root = root)
            v190.origin = v187

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v192".split('.')[0]):
                action.v192 = temp
            else:
                v192 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v193".split('.')[0]):
                action.v193 = temp
            else:
                v193 = temp 

            v191 = (v192 , v193); v191 = tuple(v191) if isinstance(v191, np.ndarray) else v191

            temp = get_nested_attribute(action, 'v191')
            if temp is None:
                temp = v191
            if action is not None and hasattr(action, "v194".split('.')[0]):
                action.v194 = temp
            else:
                v194 = temp 


            temp = get_nested_attribute(action, 'v194')
            if temp is None:
                temp = v194
            if action is not None and hasattr(action, "v195".split('.')[0]):
                action.v195 = temp
            else:
                v195 = temp 


            temp = get_nested_attribute(action, '30')
            if temp is None:
                temp = 30
            if action is not None and hasattr(action, "v196".split('.')[0]):
                action.v196 = temp
            else:
                v196 = temp 


            temp = get_nested_attribute(action, 'v196')
            if temp is None:
                temp = v196
            if action is not None and hasattr(action, "v197".split('.')[0]):
                action.v197 = temp
            else:
                v197 = temp 


            temp = get_nested_attribute(action, 'v197')
            if temp is None:
                temp = v197
            if action is not None and hasattr(action, "v198".split('.')[0]):
                action.v198 = temp
            else:
                v198 = temp 


            temp = get_nested_attribute(action, '150')
            if temp is None:
                temp = 150
            if action is not None and hasattr(action, "v199".split('.')[0]):
                action.v199 = temp
            else:
                v199 = temp 


            temp = get_nested_attribute(action, 'v199')
            if temp is None:
                temp = v199
            if action is not None and hasattr(action, "v200".split('.')[0]):
                action.v200 = temp
            else:
                v200 = temp 


            temp = get_nested_attribute(action, 'v200')
            if temp is None:
                temp = v200
            if action is not None and hasattr(action, "v201".split('.')[0]):
                action.v201 = temp
            else:
                v201 = temp 


            temp = get_nested_attribute(action, '"cyan"')
            if temp is None:
                temp = "cyan"
            if action is not None and hasattr(action, "v202".split('.')[0]):
                action.v202 = temp
            else:
                v202 = temp 


            temp = get_nested_attribute(action, 'v202')
            if temp is None:
                temp = v202
            if action is not None and hasattr(action, "v203".split('.')[0]):
                action.v203 = temp
            else:
                v203 = temp 


            temp = get_nested_attribute(action, 'v203')
            if temp is None:
                temp = v203
            if action is not None and hasattr(action, "v204".split('.')[0]):
                action.v204 = temp
            else:
                v204 = temp 


            if action is not None:
                action.v190.length = v195
                action.v190.start = v198
                action.v190.extent = v201
                action.v190.fill = v204
            else:
                v190.length = v195
                v190.start = v198
                v190.extent = v201
                v190.fill = v204

            temp = get_nested_attribute(action, 'v190')
            if temp is None:
                temp = v190
            if action is not None and hasattr(action, "arcC".split('.')[0]):
                action.arcC = temp
            else:
                arcC = temp 
            if model is not None: 
                model.arcC = arcC
                model.last_arcC = copy.deepcopy(arcC)

            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v206".split('.')[0]):
                action.v206 = temp
            else:
                v206 = temp 

            v207 = - np.array(v206)

            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v208".split('.')[0]):
                action.v208 = temp
            else:
                v208 = temp 

            v209 = - np.array(v208)
            v205 = (v207 , v209); v205 = tuple(v205) if isinstance(v205, np.ndarray) else v205

            if model is not None:
                v210 = PieSlice()
                model.add_object(v210) # add object to model
            else:
                v210 = PieSlice(root = root)
            v210.origin = v205

            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v212".split('.')[0]):
                action.v212 = temp
            else:
                v212 = temp 


            temp = get_nested_attribute(action, '50')
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v213".split('.')[0]):
                action.v213 = temp
            else:
                v213 = temp 

            v211 = (v212 , v213); v211 = tuple(v211) if isinstance(v211, np.ndarray) else v211

            temp = get_nested_attribute(action, 'v211')
            if temp is None:
                temp = v211
            if action is not None and hasattr(action, "v214".split('.')[0]):
                action.v214 = temp
            else:
                v214 = temp 


            temp = get_nested_attribute(action, 'v214')
            if temp is None:
                temp = v214
            if action is not None and hasattr(action, "v215".split('.')[0]):
                action.v215 = temp
            else:
                v215 = temp 


            temp = get_nested_attribute(action, '30')
            if temp is None:
                temp = 30
            if action is not None and hasattr(action, "v216".split('.')[0]):
                action.v216 = temp
            else:
                v216 = temp 


            temp = get_nested_attribute(action, 'v216')
            if temp is None:
                temp = v216
            if action is not None and hasattr(action, "v217".split('.')[0]):
                action.v217 = temp
            else:
                v217 = temp 


            temp = get_nested_attribute(action, 'v217')
            if temp is None:
                temp = v217
            if action is not None and hasattr(action, "v218".split('.')[0]):
                action.v218 = temp
            else:
                v218 = temp 


            temp = get_nested_attribute(action, '300')
            if temp is None:
                temp = 300
            if action is not None and hasattr(action, "v219".split('.')[0]):
                action.v219 = temp
            else:
                v219 = temp 


            temp = get_nested_attribute(action, 'v219')
            if temp is None:
                temp = v219
            if action is not None and hasattr(action, "v220".split('.')[0]):
                action.v220 = temp
            else:
                v220 = temp 


            temp = get_nested_attribute(action, 'v220')
            if temp is None:
                temp = v220
            if action is not None and hasattr(action, "v221".split('.')[0]):
                action.v221 = temp
            else:
                v221 = temp 


            temp = get_nested_attribute(action, '"blue"')
            if temp is None:
                temp = "blue"
            if action is not None and hasattr(action, "v222".split('.')[0]):
                action.v222 = temp
            else:
                v222 = temp 


            temp = get_nested_attribute(action, 'v222')
            if temp is None:
                temp = v222
            if action is not None and hasattr(action, "v223".split('.')[0]):
                action.v223 = temp
            else:
                v223 = temp 


            temp = get_nested_attribute(action, 'v223')
            if temp is None:
                temp = v223
            if action is not None and hasattr(action, "v224".split('.')[0]):
                action.v224 = temp
            else:
                v224 = temp 


            if action is not None:
                action.v210.length = v215
                action.v210.start = v218
                action.v210.extent = v221
                action.v210.fill = v224
            else:
                v210.length = v215
                v210.start = v218
                v210.extent = v221
                v210.fill = v224

            temp = get_nested_attribute(action, 'v210')
            if temp is None:
                temp = v210
            if action is not None and hasattr(action, "pieS".split('.')[0]):
                action.pieS = temp
            else:
                pieS = temp 
            if model is not None: 
                model.pieS = pieS
                model.last_pieS = copy.deepcopy(pieS)

            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v226".split('.')[0]):
                action.v226 = temp
            else:
                v226 = temp 


            temp = get_nested_attribute(action, 'cellSize')
            if temp is None:
                temp = cellSize
            if action is not None and hasattr(action, "v227".split('.')[0]):
                action.v227 = temp
            else:
                v227 = temp 

            v228 = - np.array(v227)
            v225 = (v226 , v228); v225 = tuple(v225) if isinstance(v225, np.ndarray) else v225

            if model is not None:
                v229 = Dot()
                model.add_object(v229) # add object to model
            else:
                v229 = Dot(root = root)
            v229.origin = v225

            temp = get_nested_attribute(action, '"black"')
            if temp is None:
                temp = "black"
            if action is not None and hasattr(action, "v230".split('.')[0]):
                action.v230 = temp
            else:
                v230 = temp 


            temp = get_nested_attribute(action, 'v230')
            if temp is None:
                temp = v230
            if action is not None and hasattr(action, "v231".split('.')[0]):
                action.v231 = temp
            else:
                v231 = temp 


            temp = get_nested_attribute(action, 'v231')
            if temp is None:
                temp = v231
            if action is not None and hasattr(action, "v232".split('.')[0]):
                action.v232 = temp
            else:
                v232 = temp 


            if action is not None:
                action.v229.fill = v232
            else:
                v229.fill = v232

            temp = get_nested_attribute(action, 'v229')
            if temp is None:
                temp = v229
            if action is not None and hasattr(action, "dot".split('.')[0]):
                action.dot = temp
            else:
                dot = temp 
            if model is not None: 
                model.dot = dot
                model.last_dot = copy.deepcopy(dot)

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
        v233 = Ex1() # this makes model = None in the end!
        model = model_backup
        model.add_object(v233) # add object to model
    else:
        v233 = Ex1(root = root, view = last_view)
      

    temp = get_nested_attribute(action, 'v233')
    if temp is None:
        temp = v233
    if action is not None and hasattr(action, "v234".split('.')[0]):
        action.v234 = temp
    else:
        v234 = temp 


    temp = get_nested_attribute(action, 'v234')
    if temp is None:
        temp = v234
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
    if action is not None and hasattr(action, "v235".split('.')[0]):
        action.v235 = temp
    else:
        v235 = temp 

     
    while (time.time() - last_refresh <= v235):
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

    last_refresh = time.time()
    view6.update()

    last_refresh = time.time()
    view7.update()

    last_refresh = time.time()
    view8.update()

    last_refresh = time.time()
    view9.update()


    temp = get_nested_attribute(action, '1')
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v236".split('.')[0]):
        action.v236 = temp
    else:
        v236 = temp 


    temp = get_nested_attribute(action, '1000')
    if temp is None:
        temp = 1000
    if action is not None and hasattr(action, "v237".split('.')[0]):
        action.v237 = temp
    else:
        v237 = temp 

    for i in range(v236, v237, 1):

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v238".split('.')[0]):
            action.v238 = temp
        else:
            v238 = temp 

        if action is not None:
            action.ex1.rotate(v238)
        else:
            ex1.rotate(v238)

        temp = get_nested_attribute(action, 'ex1.line.origin')
        if temp is None:
            temp = ex1.line.origin
        if action is not None and hasattr(action, "v239".split('.')[0]):
            action.v239 = temp
        else:
            v239 = temp 

        if action is not None:
            action.view2.move_absolute(v239)
        else:
            view2.move_absolute(v239)

        temp = get_nested_attribute(action, 'ex1.rec.origin')
        if temp is None:
            temp = ex1.rec.origin
        if action is not None and hasattr(action, "v240".split('.')[0]):
            action.v240 = temp
        else:
            v240 = temp 

        if action is not None:
            action.view3.move_absolute(v240)
        else:
            view3.move_absolute(v240)

        temp = get_nested_attribute(action, 'ex1.ell.origin')
        if temp is None:
            temp = ex1.ell.origin
        if action is not None and hasattr(action, "v241".split('.')[0]):
            action.v241 = temp
        else:
            v241 = temp 

        if action is not None:
            action.view4.move_absolute(v241)
        else:
            view4.move_absolute(v241)

        temp = get_nested_attribute(action, 'ex1.text.origin')
        if temp is None:
            temp = ex1.text.origin
        if action is not None and hasattr(action, "v242".split('.')[0]):
            action.v242 = temp
        else:
            v242 = temp 

        if action is not None:
            action.view5.move_absolute(v242)
        else:
            view5.move_absolute(v242)

        temp = get_nested_attribute(action, 'ex1.arc.origin')
        if temp is None:
            temp = ex1.arc.origin
        if action is not None and hasattr(action, "v243".split('.')[0]):
            action.v243 = temp
        else:
            v243 = temp 

        if action is not None:
            action.view6.move_absolute(v243)
        else:
            view6.move_absolute(v243)

        temp = get_nested_attribute(action, 'ex1.arcC.origin')
        if temp is None:
            temp = ex1.arcC.origin
        if action is not None and hasattr(action, "v244".split('.')[0]):
            action.v244 = temp
        else:
            v244 = temp 

        if action is not None:
            action.view7.move_absolute(v244)
        else:
            view7.move_absolute(v244)

        temp = get_nested_attribute(action, 'ex1.pieS.origin')
        if temp is None:
            temp = ex1.pieS.origin
        if action is not None and hasattr(action, "v245".split('.')[0]):
            action.v245 = temp
        else:
            v245 = temp 

        if action is not None:
            action.view8.move_absolute(v245)
        else:
            view8.move_absolute(v245)

        temp = get_nested_attribute(action, 'ex1.dot.origin')
        if temp is None:
            temp = ex1.dot.origin
        if action is not None and hasattr(action, "v246".split('.')[0]):
            action.v246 = temp
        else:
            v246 = temp 

        if action is not None:
            action.view9.move_absolute(v246)
        else:
            view9.move_absolute(v246)

        temp = get_nested_attribute(action, '10')
        if temp is None:
            temp = 10
        if action is not None and hasattr(action, "v247".split('.')[0]):
            action.v247 = temp
        else:
            v247 = temp 

         
        while (time.time() - last_refresh <= v247/1000):
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

        last_refresh = time.time()
        view6.update()

        last_refresh = time.time()
        view7.update()

        last_refresh = time.time()
        view8.update()

        last_refresh = time.time()
        view9.update()


    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v248".split('.')[0]):
        action.v248 = temp
    else:
        v248 = temp 

    print(v248)
    if action is not None:
        v249 = action.view.waitClick()
    else:
        v249 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v249')
    if temp is None:
        temp = v249
    if action is not None and hasattr(action, "v250".split('.')[0]):
        action.v250 = temp
    else:
        v250 = temp 


    temp = get_nested_attribute(action, 'v250')
    if temp is None:
        temp = v250
    if action is not None and hasattr(action, "v251".split('.')[0]):
        action.v251 = temp
    else:
        v251 = temp 


    temp = get_nested_attribute(action, 'v251')
    if temp is None:
        temp = v251
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
    if action is not None and hasattr(action, "v252".split('.')[0]):
        action.v252 = temp
    else:
        v252 = temp 

    print(v252)
    view.close(); views.remove(view) if last_view != view else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == view else last_view
