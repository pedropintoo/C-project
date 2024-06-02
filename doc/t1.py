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


    temp = get_nested_attribute(action, '750')
    if temp is None:
        temp = 750
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

    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v6".split('.')[0]):
        action.v6 = temp
    else:
        v6 = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
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

    temp = get_nested_attribute(action, '550')
    if temp is None:
        temp = 550
    if action is not None and hasattr(action, "v14".split('.')[0]):
        action.v14 = temp
    else:
        v14 = temp 

    v15 = - np.array(v14)

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v16".split('.')[0]):
        action.v16 = temp
    else:
        v16 = temp 

    v13 = (v15 , v16); v13 = tuple(v13) if isinstance(v13, np.ndarray) else v13

    if model is not None:
        v17 = Arc()
        model.add_object(v17) # add object to model
    else:
        v17 = Arc(root = root)
    v17.origin = v13

    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v19".split('.')[0]):
        action.v19 = temp
    else:
        v19 = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v20".split('.')[0]):
        action.v20 = temp
    else:
        v20 = temp 

    v18 = (v19 , v20); v18 = tuple(v18) if isinstance(v18, np.ndarray) else v18

    temp = get_nested_attribute(action, 'v18')
    if temp is None:
        temp = v18
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


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
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


    temp = get_nested_attribute(action, '180')
    if temp is None:
        temp = 180
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


    temp = get_nested_attribute(action, '"blue"')
    if temp is None:
        temp = "blue"
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


    if action is not None:
        action.v17.length = v22
        action.v17.start = v25
        action.v17.extent = v28
        action.v17.outline = v31
    else:
        v17.length = v22
        v17.start = v25
        v17.extent = v28
        v17.outline = v31

    temp = get_nested_attribute(action, 'v17')
    if temp is None:
        temp = v17
    if action is not None and hasattr(action, "arc".split('.')[0]):
        action.arc = temp
    else:
        arc = temp 
    if model is not None: 
        model.arc = arc
        model.last_arc = copy.deepcopy(arc)

    temp = get_nested_attribute(action, '350')
    if temp is None:
        temp = 350
    if action is not None and hasattr(action, "v33".split('.')[0]):
        action.v33 = temp
    else:
        v33 = temp 

    v34 = - np.array(v33)

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v35".split('.')[0]):
        action.v35 = temp
    else:
        v35 = temp 

    v32 = (v34 , v35); v32 = tuple(v32) if isinstance(v32, np.ndarray) else v32

    if model is not None:
        v36 = ArcChord()
        model.add_object(v36) # add object to model
    else:
        v36 = ArcChord(root = root)
    v36.origin = v32

    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v38".split('.')[0]):
        action.v38 = temp
    else:
        v38 = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v39".split('.')[0]):
        action.v39 = temp
    else:
        v39 = temp 

    v37 = (v38 , v39); v37 = tuple(v37) if isinstance(v37, np.ndarray) else v37

    temp = get_nested_attribute(action, 'v37')
    if temp is None:
        temp = v37
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


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
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


    temp = get_nested_attribute(action, 'v43')
    if temp is None:
        temp = v43
    if action is not None and hasattr(action, "v44".split('.')[0]):
        action.v44 = temp
    else:
        v44 = temp 


    temp = get_nested_attribute(action, '180')
    if temp is None:
        temp = 180
    if action is not None and hasattr(action, "v45".split('.')[0]):
        action.v45 = temp
    else:
        v45 = temp 


    temp = get_nested_attribute(action, 'v45')
    if temp is None:
        temp = v45
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


    temp = get_nested_attribute(action, '"red"')
    if temp is None:
        temp = "red"
    if action is not None and hasattr(action, "v48".split('.')[0]):
        action.v48 = temp
    else:
        v48 = temp 


    temp = get_nested_attribute(action, 'v48')
    if temp is None:
        temp = v48
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


    if action is not None:
        action.v36.length = v41
        action.v36.start = v44
        action.v36.extent = v47
        action.v36.fill = v50
    else:
        v36.length = v41
        v36.start = v44
        v36.extent = v47
        v36.fill = v50

    temp = get_nested_attribute(action, 'v36')
    if temp is None:
        temp = v36
    if action is not None and hasattr(action, "arcchord".split('.')[0]):
        action.arcchord = temp
    else:
        arcchord = temp 
    if model is not None: 
        model.arcchord = arcchord
        model.last_arcchord = copy.deepcopy(arcchord)

    temp = get_nested_attribute(action, '150')
    if temp is None:
        temp = 150
    if action is not None and hasattr(action, "v52".split('.')[0]):
        action.v52 = temp
    else:
        v52 = temp 

    v53 = - np.array(v52)

    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v54".split('.')[0]):
        action.v54 = temp
    else:
        v54 = temp 

    v51 = (v53 , v54); v51 = tuple(v51) if isinstance(v51, np.ndarray) else v51

    if model is not None:
        v55 = PieSlice()
        model.add_object(v55) # add object to model
    else:
        v55 = PieSlice(root = root)
    v55.origin = v51

    temp = get_nested_attribute(action, '100')
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v57".split('.')[0]):
        action.v57 = temp
    else:
        v57 = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v58".split('.')[0]):
        action.v58 = temp
    else:
        v58 = temp 

    v56 = (v57 , v58); v56 = tuple(v56) if isinstance(v56, np.ndarray) else v56

    temp = get_nested_attribute(action, 'v56')
    if temp is None:
        temp = v56
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


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v61".split('.')[0]):
        action.v61 = temp
    else:
        v61 = temp 


    temp = get_nested_attribute(action, 'v61')
    if temp is None:
        temp = v61
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


    temp = get_nested_attribute(action, '180')
    if temp is None:
        temp = 180
    if action is not None and hasattr(action, "v64".split('.')[0]):
        action.v64 = temp
    else:
        v64 = temp 


    temp = get_nested_attribute(action, 'v64')
    if temp is None:
        temp = v64
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


    temp = get_nested_attribute(action, '"green"')
    if temp is None:
        temp = "green"
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


    temp = get_nested_attribute(action, 'v68')
    if temp is None:
        temp = v68
    if action is not None and hasattr(action, "v69".split('.')[0]):
        action.v69 = temp
    else:
        v69 = temp 


    if action is not None:
        action.v55.length = v60
        action.v55.start = v63
        action.v55.extent = v66
        action.v55.fill = v69
    else:
        v55.length = v60
        v55.start = v63
        v55.extent = v66
        v55.fill = v69

    temp = get_nested_attribute(action, 'v55')
    if temp is None:
        temp = v55
    if action is not None and hasattr(action, "pieslice".split('.')[0]):
        action.pieslice = temp
    else:
        pieslice = temp 
    if model is not None: 
        model.pieslice = pieslice
        model.last_pieslice = copy.deepcopy(pieslice)

    if model is not None:
        v70 = View()
        model.add_object(v70) # add object to model
    else:
        v70 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v70

    temp = get_nested_attribute(action, '30')
    if temp is None:
        temp = 30
    if action is not None and hasattr(action, "v71".split('.')[0]):
        action.v71 = temp
    else:
        v71 = temp 


    temp = get_nested_attribute(action, 'v71')
    if temp is None:
        temp = v71
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


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v74".split('.')[0]):
        action.v74 = temp
    else:
        v74 = temp 


    temp = get_nested_attribute(action, 'v74')
    if temp is None:
        temp = v74
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


    temp = get_nested_attribute(action, '1800')
    if temp is None:
        temp = 1800
    if action is not None and hasattr(action, "v77".split('.')[0]):
        action.v77 = temp
    else:
        v77 = temp 


    temp = get_nested_attribute(action, 'v77')
    if temp is None:
        temp = v77
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


    temp = get_nested_attribute(action, '401')
    if temp is None:
        temp = 401
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


    temp = get_nested_attribute(action, 'v81')
    if temp is None:
        temp = v81
    if action is not None and hasattr(action, "v82".split('.')[0]):
        action.v82 = temp
    else:
        v82 = temp 


    temp = get_nested_attribute(action, '"1"')
    if temp is None:
        temp = "1"
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


    temp = get_nested_attribute(action, 'v84')
    if temp is None:
        temp = v84
    if action is not None and hasattr(action, "v85".split('.')[0]):
        action.v85 = temp
    else:
        v85 = temp 


    temp = get_nested_attribute(action, '"alice blue"')
    if temp is None:
        temp = "alice blue"
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


    temp = get_nested_attribute(action, 'v87')
    if temp is None:
        temp = v87
    if action is not None and hasattr(action, "v88".split('.')[0]):
        action.v88 = temp
    else:
        v88 = temp 


    if action is not None:
        action.v70.Ox = v73
        action.v70.Oy = v76
        action.v70.width = v79
        action.v70.height = v82
        action.v70.title = v85
        action.v70.background = v88
    else:
        v70.Ox = v73
        v70.Oy = v76
        v70.width = v79
        v70.height = v82
        v70.title = v85
        v70.background = v88

    temp = get_nested_attribute(action, 'v70')
    if temp is None:
        temp = v70
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
    if action is not None and hasattr(action, "v89".split('.')[0]):
        action.v89 = temp
    else:
        v89 = temp 


    temp = get_nested_attribute(action, '5')
    if temp is None:
        temp = 5
    if action is not None and hasattr(action, "v90".split('.')[0]):
        action.v90 = temp
    else:
        v90 = temp 

    for i in range(v89, v90, 1):

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v91".split('.')[0]):
            action.v91 = temp
        else:
            v91 = temp 

        if action is not None:
            action.elipse.rotate(v91)
        else:
            elipse.rotate(v91)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v92".split('.')[0]):
            action.v92 = temp
        else:
            v92 = temp 

        if action is not None:
            action.arc.rotate(v92)
        else:
            arc.rotate(v92)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v93".split('.')[0]):
            action.v93 = temp
        else:
            v93 = temp 

        if action is not None:
            action.arcchord.rotate(v93)
        else:
            arcchord.rotate(v93)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v94".split('.')[0]):
            action.v94 = temp
        else:
            v94 = temp 

        if action is not None:
            action.pieslice.rotate(v94)
        else:
            pieslice.rotate(v94)

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v95".split('.')[0]):
            action.v95 = temp
        else:
            v95 = temp 

         
        while (time.time() - last_refresh <= v95):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v96".split('.')[0]):
        action.v96 = temp
    else:
        v96 = temp 

    v97 = - np.array(v96)

    temp = get_nested_attribute(action, 'v97')
    if temp is None:
        temp = v97
    if action is not None and hasattr(action, "v98".split('.')[0]):
        action.v98 = temp
    else:
        v98 = temp 


    temp = get_nested_attribute(action, 'v98')
    if temp is None:
        temp = v98
    if action is not None and hasattr(action, "arc.start".split('.')[0]):
        action.arc.start = temp
    else:
        arc.start = temp 


    temp = get_nested_attribute(action, '70')
    if temp is None:
        temp = 70
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


    temp = get_nested_attribute(action, 'v100')
    if temp is None:
        temp = v100
    if action is not None and hasattr(action, "arc.extent".split('.')[0]):
        action.arc.extent = temp
    else:
        arc.extent = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v101".split('.')[0]):
        action.v101 = temp
    else:
        v101 = temp 

    v102 = - np.array(v101)

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
    if action is not None and hasattr(action, "arcchord.start".split('.')[0]):
        action.arcchord.start = temp
    else:
        arcchord.start = temp 


    temp = get_nested_attribute(action, '70')
    if temp is None:
        temp = 70
    if action is not None and hasattr(action, "v104".split('.')[0]):
        action.v104 = temp
    else:
        v104 = temp 


    temp = get_nested_attribute(action, 'v104')
    if temp is None:
        temp = v104
    if action is not None and hasattr(action, "v105".split('.')[0]):
        action.v105 = temp
    else:
        v105 = temp 


    temp = get_nested_attribute(action, 'v105')
    if temp is None:
        temp = v105
    if action is not None and hasattr(action, "arcchord.extent".split('.')[0]):
        action.arcchord.extent = temp
    else:
        arcchord.extent = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v106".split('.')[0]):
        action.v106 = temp
    else:
        v106 = temp 

    v107 = - np.array(v106)

    temp = get_nested_attribute(action, 'v107')
    if temp is None:
        temp = v107
    if action is not None and hasattr(action, "v108".split('.')[0]):
        action.v108 = temp
    else:
        v108 = temp 


    temp = get_nested_attribute(action, 'v108')
    if temp is None:
        temp = v108
    if action is not None and hasattr(action, "pieslice.start".split('.')[0]):
        action.pieslice.start = temp
    else:
        pieslice.start = temp 


    temp = get_nested_attribute(action, '70')
    if temp is None:
        temp = 70
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


    temp = get_nested_attribute(action, 'v110')
    if temp is None:
        temp = v110
    if action is not None and hasattr(action, "pieslice.extent".split('.')[0]):
        action.pieslice.extent = temp
    else:
        pieslice.extent = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v111".split('.')[0]):
        action.v111 = temp
    else:
        v111 = temp 


    temp = get_nested_attribute(action, '5')
    if temp is None:
        temp = 5
    if action is not None and hasattr(action, "v112".split('.')[0]):
        action.v112 = temp
    else:
        v112 = temp 

    for i in range(v111, v112, 1):

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v113".split('.')[0]):
            action.v113 = temp
        else:
            v113 = temp 

        if action is not None:
            action.elipse.rotate(v113)
        else:
            elipse.rotate(v113)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v114".split('.')[0]):
            action.v114 = temp
        else:
            v114 = temp 

        if action is not None:
            action.arc.rotate(v114)
        else:
            arc.rotate(v114)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v115".split('.')[0]):
            action.v115 = temp
        else:
            v115 = temp 

        if action is not None:
            action.arcchord.rotate(v115)
        else:
            arcchord.rotate(v115)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v116".split('.')[0]):
            action.v116 = temp
        else:
            v116 = temp 

        if action is not None:
            action.pieslice.rotate(v116)
        else:
            pieslice.rotate(v116)

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v117".split('.')[0]):
            action.v117 = temp
        else:
            v117 = temp 

         
        while (time.time() - last_refresh <= v117):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


    temp = get_nested_attribute(action, '45')
    if temp is None:
        temp = 45
    if action is not None and hasattr(action, "v119".split('.')[0]):
        action.v119 = temp
    else:
        v119 = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v120".split('.')[0]):
        action.v120 = temp
    else:
        v120 = temp 

    v118 = (v119 , v120); v118 = tuple(v118) if isinstance(v118, np.ndarray) else v118

    temp = get_nested_attribute(action, 'v118')
    if temp is None:
        temp = v118
    if action is not None and hasattr(action, "v121".split('.')[0]):
        action.v121 = temp
    else:
        v121 = temp 


    temp = get_nested_attribute(action, 'v121')
    if temp is None:
        temp = v121
    if action is not None and hasattr(action, "elipse.length".split('.')[0]):
        action.elipse.length = temp
    else:
        elipse.length = temp 


    temp = get_nested_attribute(action, '45')
    if temp is None:
        temp = 45
    if action is not None and hasattr(action, "v123".split('.')[0]):
        action.v123 = temp
    else:
        v123 = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v124".split('.')[0]):
        action.v124 = temp
    else:
        v124 = temp 

    v122 = (v123 , v124); v122 = tuple(v122) if isinstance(v122, np.ndarray) else v122

    temp = get_nested_attribute(action, 'v122')
    if temp is None:
        temp = v122
    if action is not None and hasattr(action, "v125".split('.')[0]):
        action.v125 = temp
    else:
        v125 = temp 


    temp = get_nested_attribute(action, 'v125')
    if temp is None:
        temp = v125
    if action is not None and hasattr(action, "arc.length".split('.')[0]):
        action.arc.length = temp
    else:
        arc.length = temp 


    temp = get_nested_attribute(action, '45')
    if temp is None:
        temp = 45
    if action is not None and hasattr(action, "v127".split('.')[0]):
        action.v127 = temp
    else:
        v127 = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v128".split('.')[0]):
        action.v128 = temp
    else:
        v128 = temp 

    v126 = (v127 , v128); v126 = tuple(v126) if isinstance(v126, np.ndarray) else v126

    temp = get_nested_attribute(action, 'v126')
    if temp is None:
        temp = v126
    if action is not None and hasattr(action, "v129".split('.')[0]):
        action.v129 = temp
    else:
        v129 = temp 


    temp = get_nested_attribute(action, 'v129')
    if temp is None:
        temp = v129
    if action is not None and hasattr(action, "arcchord.length".split('.')[0]):
        action.arcchord.length = temp
    else:
        arcchord.length = temp 


    temp = get_nested_attribute(action, '45')
    if temp is None:
        temp = 45
    if action is not None and hasattr(action, "v131".split('.')[0]):
        action.v131 = temp
    else:
        v131 = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v132".split('.')[0]):
        action.v132 = temp
    else:
        v132 = temp 

    v130 = (v131 , v132); v130 = tuple(v130) if isinstance(v130, np.ndarray) else v130

    temp = get_nested_attribute(action, 'v130')
    if temp is None:
        temp = v130
    if action is not None and hasattr(action, "v133".split('.')[0]):
        action.v133 = temp
    else:
        v133 = temp 


    temp = get_nested_attribute(action, 'v133')
    if temp is None:
        temp = v133
    if action is not None and hasattr(action, "pieslice.length".split('.')[0]):
        action.pieslice.length = temp
    else:
        pieslice.length = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v134".split('.')[0]):
        action.v134 = temp
    else:
        v134 = temp 


    temp = get_nested_attribute(action, 'v134')
    if temp is None:
        temp = v134
    if action is not None and hasattr(action, "v135".split('.')[0]):
        action.v135 = temp
    else:
        v135 = temp 


    temp = get_nested_attribute(action, 'v135')
    if temp is None:
        temp = v135
    if action is not None and hasattr(action, "arc.start".split('.')[0]):
        action.arc.start = temp
    else:
        arc.start = temp 


    temp = get_nested_attribute(action, '180')
    if temp is None:
        temp = 180
    if action is not None and hasattr(action, "v136".split('.')[0]):
        action.v136 = temp
    else:
        v136 = temp 


    temp = get_nested_attribute(action, 'v136')
    if temp is None:
        temp = v136
    if action is not None and hasattr(action, "v137".split('.')[0]):
        action.v137 = temp
    else:
        v137 = temp 


    temp = get_nested_attribute(action, 'v137')
    if temp is None:
        temp = v137
    if action is not None and hasattr(action, "arc.extent".split('.')[0]):
        action.arc.extent = temp
    else:
        arc.extent = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v138".split('.')[0]):
        action.v138 = temp
    else:
        v138 = temp 


    temp = get_nested_attribute(action, 'v138')
    if temp is None:
        temp = v138
    if action is not None and hasattr(action, "v139".split('.')[0]):
        action.v139 = temp
    else:
        v139 = temp 


    temp = get_nested_attribute(action, 'v139')
    if temp is None:
        temp = v139
    if action is not None and hasattr(action, "arcchord.start".split('.')[0]):
        action.arcchord.start = temp
    else:
        arcchord.start = temp 


    temp = get_nested_attribute(action, '180')
    if temp is None:
        temp = 180
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


    temp = get_nested_attribute(action, 'v141')
    if temp is None:
        temp = v141
    if action is not None and hasattr(action, "arcchord.extent".split('.')[0]):
        action.arcchord.extent = temp
    else:
        arcchord.extent = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
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
    if action is not None and hasattr(action, "pieslice.start".split('.')[0]):
        action.pieslice.start = temp
    else:
        pieslice.start = temp 


    temp = get_nested_attribute(action, '180')
    if temp is None:
        temp = 180
    if action is not None and hasattr(action, "v144".split('.')[0]):
        action.v144 = temp
    else:
        v144 = temp 


    temp = get_nested_attribute(action, 'v144')
    if temp is None:
        temp = v144
    if action is not None and hasattr(action, "v145".split('.')[0]):
        action.v145 = temp
    else:
        v145 = temp 


    temp = get_nested_attribute(action, 'v145')
    if temp is None:
        temp = v145
    if action is not None and hasattr(action, "pieslice.extent".split('.')[0]):
        action.pieslice.extent = temp
    else:
        pieslice.extent = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v146".split('.')[0]):
        action.v146 = temp
    else:
        v146 = temp 


    temp = get_nested_attribute(action, '5')
    if temp is None:
        temp = 5
    if action is not None and hasattr(action, "v147".split('.')[0]):
        action.v147 = temp
    else:
        v147 = temp 

    for i in range(v146, v147, 1):

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v148".split('.')[0]):
            action.v148 = temp
        else:
            v148 = temp 

        if action is not None:
            action.elipse.rotate(v148)
        else:
            elipse.rotate(v148)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v149".split('.')[0]):
            action.v149 = temp
        else:
            v149 = temp 

        if action is not None:
            action.arc.rotate(v149)
        else:
            arc.rotate(v149)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v150".split('.')[0]):
            action.v150 = temp
        else:
            v150 = temp 

        if action is not None:
            action.arcchord.rotate(v150)
        else:
            arcchord.rotate(v150)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v151".split('.')[0]):
            action.v151 = temp
        else:
            v151 = temp 

        if action is not None:
            action.pieslice.rotate(v151)
        else:
            pieslice.rotate(v151)

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v152".split('.')[0]):
            action.v152 = temp
        else:
            v152 = temp 

         
        while (time.time() - last_refresh <= v152):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v153".split('.')[0]):
        action.v153 = temp
    else:
        v153 = temp 

    v154 = - np.array(v153)

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
    if action is not None and hasattr(action, "arc.start".split('.')[0]):
        action.arc.start = temp
    else:
        arc.start = temp 


    temp = get_nested_attribute(action, '70')
    if temp is None:
        temp = 70
    if action is not None and hasattr(action, "v156".split('.')[0]):
        action.v156 = temp
    else:
        v156 = temp 


    temp = get_nested_attribute(action, 'v156')
    if temp is None:
        temp = v156
    if action is not None and hasattr(action, "v157".split('.')[0]):
        action.v157 = temp
    else:
        v157 = temp 


    temp = get_nested_attribute(action, 'v157')
    if temp is None:
        temp = v157
    if action is not None and hasattr(action, "arc.extent".split('.')[0]):
        action.arc.extent = temp
    else:
        arc.extent = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v158".split('.')[0]):
        action.v158 = temp
    else:
        v158 = temp 

    v159 = - np.array(v158)

    temp = get_nested_attribute(action, 'v159')
    if temp is None:
        temp = v159
    if action is not None and hasattr(action, "v160".split('.')[0]):
        action.v160 = temp
    else:
        v160 = temp 


    temp = get_nested_attribute(action, 'v160')
    if temp is None:
        temp = v160
    if action is not None and hasattr(action, "arcchord.start".split('.')[0]):
        action.arcchord.start = temp
    else:
        arcchord.start = temp 


    temp = get_nested_attribute(action, '70')
    if temp is None:
        temp = 70
    if action is not None and hasattr(action, "v161".split('.')[0]):
        action.v161 = temp
    else:
        v161 = temp 


    temp = get_nested_attribute(action, 'v161')
    if temp is None:
        temp = v161
    if action is not None and hasattr(action, "v162".split('.')[0]):
        action.v162 = temp
    else:
        v162 = temp 


    temp = get_nested_attribute(action, 'v162')
    if temp is None:
        temp = v162
    if action is not None and hasattr(action, "arcchord.extent".split('.')[0]):
        action.arcchord.extent = temp
    else:
        arcchord.extent = temp 


    temp = get_nested_attribute(action, '35')
    if temp is None:
        temp = 35
    if action is not None and hasattr(action, "v163".split('.')[0]):
        action.v163 = temp
    else:
        v163 = temp 

    v164 = - np.array(v163)

    temp = get_nested_attribute(action, 'v164')
    if temp is None:
        temp = v164
    if action is not None and hasattr(action, "v165".split('.')[0]):
        action.v165 = temp
    else:
        v165 = temp 


    temp = get_nested_attribute(action, 'v165')
    if temp is None:
        temp = v165
    if action is not None and hasattr(action, "pieslice.start".split('.')[0]):
        action.pieslice.start = temp
    else:
        pieslice.start = temp 


    temp = get_nested_attribute(action, '70')
    if temp is None:
        temp = 70
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


    temp = get_nested_attribute(action, 'v167')
    if temp is None:
        temp = v167
    if action is not None and hasattr(action, "pieslice.extent".split('.')[0]):
        action.pieslice.extent = temp
    else:
        pieslice.extent = temp 


    temp = get_nested_attribute(action, '0')
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v168".split('.')[0]):
        action.v168 = temp
    else:
        v168 = temp 


    temp = get_nested_attribute(action, '5')
    if temp is None:
        temp = 5
    if action is not None and hasattr(action, "v169".split('.')[0]):
        action.v169 = temp
    else:
        v169 = temp 

    for i in range(v168, v169, 1):

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v170".split('.')[0]):
            action.v170 = temp
        else:
            v170 = temp 

        if action is not None:
            action.elipse.rotate(v170)
        else:
            elipse.rotate(v170)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v171".split('.')[0]):
            action.v171 = temp
        else:
            v171 = temp 

        if action is not None:
            action.arc.rotate(v171)
        else:
            arc.rotate(v171)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v172".split('.')[0]):
            action.v172 = temp
        else:
            v172 = temp 

        if action is not None:
            action.arcchord.rotate(v172)
        else:
            arcchord.rotate(v172)

        temp = get_nested_attribute(action, '35')
        if temp is None:
            temp = 35
        if action is not None and hasattr(action, "v173".split('.')[0]):
            action.v173 = temp
        else:
            v173 = temp 

        if action is not None:
            action.pieslice.rotate(v173)
        else:
            pieslice.rotate(v173)

        temp = get_nested_attribute(action, '1')
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v174".split('.')[0]):
            action.v174 = temp
        else:
            v174 = temp 

         
        while (time.time() - last_refresh <= v174):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()


    temp = get_nested_attribute(action, '"Press any mouse button to quit"')
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v175".split('.')[0]):
        action.v175 = temp
    else:
        v175 = temp 

    print(v175)
    if action is not None:
        v176 = action.view.waitClick()
    else:
        v176 = last_view.waitClick()

    temp = get_nested_attribute(action, 'v176')
    if temp is None:
        temp = v176
    if action is not None and hasattr(action, "v177".split('.')[0]):
        action.v177 = temp
    else:
        v177 = temp 


    temp = get_nested_attribute(action, 'v177')
    if temp is None:
        temp = v177
    if action is not None and hasattr(action, "v178".split('.')[0]):
        action.v178 = temp
    else:
        v178 = temp 


    temp = get_nested_attribute(action, 'v178')
    if temp is None:
        temp = v178
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
    if action is not None and hasattr(action, "v179".split('.')[0]):
        action.v179 = temp
    else:
        v179 = temp 

    print(v179)
    view.close(); views.remove(view) if last_view != view else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == view else last_view
