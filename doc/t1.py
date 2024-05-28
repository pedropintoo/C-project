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

    v1 = 401
    v2 = v1
    v3 = v2
    v4 = 401
    v5 = v4
    v6 = v5
<<<<<<< HEAD
    v7 = "Illustrating the rectangle shape"
    v8 = v7
    v9 = v8
    v10 = "black"
=======
    v7 = "1 Illustrating the rectangle shape"
    v8 = v7
    v9 = v8
    v10 = "wheat"
>>>>>>> c18894c (initial boolean and if expressions)
    v11 = v10
    v12 = v11

    v0 = View(root = root)
    last_view = v0
    v0.width = v3
    v0.height = v6
    v0.title = v9
    v0.background = v12
    view = v0
    v14 = 10
    v15 = 0
    v13 = (v14 , v15)
<<<<<<< HEAD
    v16 = v13
    v17 = v16
    p = v17
    v18 = p
    v21 = 100
    v22 = 100
    v20 = (v21 , v22)
    v23 = v20
    v24 = v23
    v25 = "pink"
    v26 = v25
    v27 = v26

    v19 = Rectangle(root = root)
    v19.origin = v18
    v19.length = v24
    v19.fill = v27
    v28 = p
    v31 = 50
    v32 = 50
    v30 = (v31 , v32)
    v33 = v30
    v34 = v33
    v35 = "wheat"
    v36 = v35
    v37 = v36

    v29 = Rectangle(root = root)
    v29.origin = v28
    v29.length = v34
    v29.fill = v37
    r = v29
    last_refresh = time.time()
    last_view = view
    view.update()
    v38 = 1
    v39 = 10
    for i in range(v38, v39, 1):
        v40 = "hidden"
        v41 = v40
        r.state = v41
         
        v42 = 100
        while (time.time() - last_refresh <= v42/1000):
=======
    v18 = 200
    v19 = 60
    v17 = (v18 , v19)
    v20 = v17
    v21 = v20
    v22 = "blue"
    v23 = v22
    v24 = v23

    v16 = Rectangle(root = root)
    v16.origin = v13
    v16.length = v21
    v16.fill = v24
    v26 = 0
    v27 = 0
    v25 = (v26 , v27)
    v30 = 50
    v31 = 50
    v29 = (v30 , v31)
    v32 = v29
    v33 = v32
    v34 = "pink"
    v35 = v34
    v36 = v35
    v37 = 30
    v38 = v37
    v39 = v38
    v40 = 300
    v41 = v40
    v42 = v41

    v28 = PieSlice(root = root)
    v28.origin = v25
    v28.length = v33
    v28.fill = v36
    v28.start = v39
    v28.extent = v42
    pacman = v28
    v44 = 100
    v45 = 0
    v43 = (v44 , v45)
    v48 = 20
    v49 = 20
    v47 = (v48 , v49)
    v50 = v47
    v51 = v50
    v52 = "red"
    v53 = v52
    v54 = v53
    v55 = 89
    v56 = v55
    v57 = v56
    v58 = 359
    v59 = v58
    v60 = v59

    v46 = PieSlice(root = root)
    v46.origin = v43
    v46.length = v51
    v46.fill = v54
    v46.start = v57
    v46.extent = v60
    food1 = v46
    v62 = 401
    v63 = v62
    v64 = v63
    v65 = 401
    v66 = v65
    v67 = v66
    v68 = "2 Illustrating the rectangle shape"
    v69 = v68
    v70 = v69
    v71 = "wheat"
    v72 = v71
    v73 = v72

    v61 = View(root = root)
    last_view = v61
    v61.width = v64
    v61.height = v67
    v61.title = v70
    v61.background = v73
    view2 = v61
    last_refresh = time.time()
    last_view = view
    view.update()
    last_refresh = time.time()
    last_view = view2
    view2.update()
    v74 = 1
    v75 = 10
    for i in range(v74, v75, 1):
        v76 = 1
        v77 = v76
        v78 = v77
        v79 = 359
        v80 = v79
        v81 = v80

        pacman.start = v78
        pacman.extent = v81
        v82 = "hidden"
        v83 = v82
        food1.state = v83
         
        v84 = 20
        while (time.time() - last_refresh <= v84/1000):
>>>>>>> c18894c (initial boolean and if expressions)
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        last_view = view
        view.update()
<<<<<<< HEAD
        v43 = "normal"
        v44 = v43
        r.state = v44
         
        v45 = 100
        while (time.time() - last_refresh <= v45/1000):
=======
         
        v85 = 20
        while (time.time() - last_refresh <= v85/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        last_view = view2
        view2.update()
        v86 = 30
        v87 = v86
        v88 = v87
        v89 = 300
        v90 = v89
        v91 = v90

        pacman.start = v88
        pacman.extent = v91
         
        v92 = 25
        while (time.time() - last_refresh <= v92/1000):
>>>>>>> c18894c (initial boolean and if expressions)
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        last_view = view
        view.update()
<<<<<<< HEAD
    v46 = "Press any mouse button to quit"
    print(v46)
    v47 = last_view.waitClick()
    v48 = v47
    p = v48
=======
        v94 = 10
        v95 = 0
        v93 = (v94 , v95)
        pacman.move_relative(v93)
        v96 = "normal"
        v97 = v96
        food1.state = v97
        v99 = 10
        v100 = 0
        v98 = (v99 , v100)
        view.move_relative(v98)
        last_refresh = time.time()
        last_view = view
        view.update()
        last_refresh = time.time()
        last_view = view2
        view2.update()
    v101 = "hidden"
    v102 = v101
    food1.state = v102
    last_refresh = time.time()
    last_view = view
    view.update()
    last_refresh = time.time()
    last_view = view2
    view2.update()
    v103 = "Press any mouse button to quit"
    print(v103)
    v104 = last_view.waitClick()
    v105 = v104
    v106 = v105
    pos = v106
>>>>>>> c18894c (initial boolean and if expressions)
