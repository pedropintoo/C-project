from tkinter import *
from AGLClasses import *
import time, os, sys

#################################################################
## Auxiliar
#################################################################
REFRESH_RATE = 0.1
last_refresh = time.time()
last_view = None
mouseX = None
mouseY = None
#################################################################

if __name__ == "__main__":
    root = Root()

    v1 = 601
    v2 = v1
    v3 = v2
    v4 = 601
    v5 = v4
    v6 = v5
    v7 = "Illustrating the minimum level graphical models"
    v8 = v7
    v9 = v8
    v10 = "alice blue"
    v11 = v10
    v12 = v11

    v0 = View(root = root)
    last_view = v0
    v0.width = v3
    v0.height = v6
    v0.title = v9
    v0.background = v12
    view = v0
    v14 = 0
    v15 = 0
    v13 = (v14 , v15)
    v19 = 1
    v20 = 80
    v18 = (v19 , v20)
    v22 = 30
    v23 = 50
    v21 = (v22 , v23)
    v25 = 100
    v26 = 100
    v24 = (v25 , v26)
    v17 = [v18,v21,v24]
    v27 = v17
    v28 = v27
    v29 = "red"
    v30 = v29
    v31 = v30

    v16 = PolyLine(root = root)
    v16.origin = v13
    v16.points = v28
    v16.fill = v31
    p = v16
    v33 = 100
    v34 = 100
    v32 = (v33 , v34)
    v38 = 80
    v39 = 1
    v37 = (v38 , v39)
    v41 = 50
    v42 = 30
    v40 = (v41 , v42)
    v44 = 100
    v45 = - v44
    v46 = 100
    v43 = (v45 , v46)
    v36 = [v37,v40,v43]
    v47 = v36
    v48 = v47
    v49 = "blue"
    v50 = v49
    v51 = v50

    v35 = Spline(root = root)
    v35.origin = v32
    v35.points = v48
    v35.fill = v51
    spline = v35
    v53 = 100
    v54 = - v53
    v55 = 100
    v52 = (v54 , v55)
    v59 = 100
    v60 = - v59
    v61 = 100
    v58 = (v60 , v61)
    v63 = 10
    v64 = 100
    v62 = (v63 , v64)
    v66 = 100
    v67 = 10
    v65 = (v66 , v67)
    v69 = 3
    v70 = 75
    v68 = (v69 , v70)
    v57 = [v58,v62,v65,v68]
    v71 = v57
    v72 = v71
    v73 = "blue"
    v74 = v73
    v75 = v74
    v76 = "black"
    v77 = v76
    v78 = v77

    v56 = Polygon(root = root)
    v56.origin = v52
    v56.points = v72
    v56.fill = v75
    v56.outline = v78
    poligono = v56
    v80 = 100
    v81 = 100
    v79 = (v80 , v81)
    v85 = 90
    v86 = - v85
    v87 = 30
    v84 = (v86 , v87)
    v89 = 62
    v90 = 39
    v88 = (v89 , v90)
    v92 = 50
    v93 = 100
    v91 = (v92 , v93)
    v95 = 31
    v96 = 45
    v94 = (v95 , v96)
    v83 = [v84,v88,v91,v94]
    v97 = v83
    v98 = v97
    v99 = "yellow"
    v100 = v99
    v101 = v100
    v102 = "blue"
    v103 = v102
    v104 = v103

    v82 = Blob(root = root)
    v82.origin = v79
    v82.points = v98
    v82.fill = v101
    v82.outline = v104
    blob = v82
    last_refresh = time.time()
    last_view = view
    view.update()
    v105 = last_view.waitClick()
    v106 = v105
    v107 = v106
    pos = v107
