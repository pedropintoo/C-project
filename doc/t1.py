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
    root = Tk()
    root.withdraw()

    top = Toplevel(root)

    v0 = 401
    v1 = v0
    v2 = v1
    v3 = 401
    v4 = v3
    v5 = v4
    v6 = "Illustrating the rectangle shape"
    v7 = v6
    v8 = v7
    v9 = "wheat"
    v10 = v9
    v11 = v10

    v12 = View(
        top=top,
        width = v2,
        height = v5,
        title = v8,
        background = v11
        )
    last_view = v12
    view = v12
    v14 = 10
    v15 = 0
    v13 = (v14 , v15)
    v17 = 200
    v18 = 60
    v16 = (v17 , v18)
    v19 = v16
    v20 = v19
    v21 = "blue"
    v22 = v21
    v23 = v22

    v24 = Rectangle(
        view=last_view,
        origin=v13,
        length = v20,
        fill = v23
        )
    last_view.add_object(v24)    
    v26 = 0
    v27 = 0
    v25 = (v26 , v27)
    v29 = 50
    v30 = 50
    v28 = (v29 , v30)
    v31 = v28
    v32 = v31
    v33 = "pink"
    v34 = v33
    v35 = v34
    v36 = 30
    v37 = v36
    v38 = v37
    v39 = 300
    v40 = v39
    v41 = v40

    v42 = PieSlice(
        view=last_view,
        origin=v25,
        length = v32,
        fill = v35,
        start = v38,
        extent = v41
        )
    last_view.add_object(v42) 
    pacman = v42
    v44 = 100
    v45 = 0
    v43 = (v44 , v45)
    v47 = 20
    v48 = 20
    v46 = (v47 , v48)
    v49 = v46
    v50 = v49
    v51 = "red"
    v52 = v51
    v53 = v52
    v54 = 89
    v55 = v54
    v56 = v55
    v57 = 359
    v58 = v57
    v59 = v58

    v60 = PieSlice(
        view=last_view,
        origin=v43,
        length = v50,
        fill = v53,
        start = v56,
        extent = v59
        )
    last_view.add_object(v60) 
    food1 = v60
    v61 = 401
    v62 = v61
    v63 = v62
    v64 = 401
    v65 = v64
    v66 = v65
    v67 = "Illustrating the rectangle shape"
    v68 = v67
    v69 = v68
    v70 = "wheat"
    v71 = v70
    v72 = v71

    v73 = View(
        top=top,
        width = v63,
        height = v66,
        title = v69,
        background = v72
        )
    last_view = v73
    view2 = v73
    v75 = 10
    v76 = - v75
    v77 = 0
    v74 = (v76 , v77)
    v79 = 200
    v80 = 60
    v78 = (v79 , v80)
    v81 = v78
    v82 = v81
    v83 = "blue"
    v84 = v83
    v85 = v84

    v86 = Rectangle(
        view=last_view,
        origin=v74,
        length = v82,
        fill = v85
        )
    last_view.add_object(v86)    
    v88 = 0
    v89 = 0
    v87 = (v88 , v89)
    v91 = 50
    v92 = 50
    v90 = (v91 , v92)
    v93 = v90
    v94 = v93
    v95 = "pink"
    v96 = v95
    v97 = v96
    v98 = 210
    v99 = v98
    v100 = v99
    v101 = 300
    v102 = v101
    v103 = v102

    v104 = PieSlice(
        view=last_view,
        origin=v87,
        length = v94,
        fill = v97,
        start = v100,
        extent = v103
        )
    last_view.add_object(v104) 
    pacman2 = v104
    v106 = 100
    v107 = - v106
    v108 = 0
    v105 = (v107 , v108)
    v110 = 20
    v111 = 20
    v109 = (v110 , v111)
    v112 = v109
    v113 = v112
    v114 = "red"
    v115 = v114
    v116 = v115
    v117 = 89
    v118 = v117
    v119 = v118
    v120 = 359
    v121 = v120
    v122 = v121

    v123 = PieSlice(
        view=last_view,
        origin=v105,
        length = v113,
        fill = v116,
        start = v119,
        extent = v122
        )
    last_view.add_object(v123) 
    food2 = v123
    last_refresh = time.time()
    view.update()
    last_refresh = time.time()
    view2.update()
    v124 = 1
    v125 = 10
    for i in range(v124, v125, 1):
        v126 = 1
        v127 = v126
        v128 = v127
        v129 = 359
        v130 = v129
        v131 = v130
        pacman.change(start = v128,
        extent = v131)
        v132 = 179
        v133 = v132
        v134 = v133
        v135 = 359
        v136 = v135
        v137 = v136
        pacman2.change(start = v134,
        extent = v137)
        v138 = "hidden"
        v139 = v138
        food1.change(state = v139)
        v141 = 0
        v142 = 10
        v143 = - v142
        v140 = (v141 , v143)
        food2.move(v140)
         
        v144 = 20
        while (time.time() - last_refresh <= v144/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
         
        v145 = 20
        while (time.time() - last_refresh <= v145/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view2.update()
        v146 = 30
        v147 = v146
        v148 = v147
        v149 = 300
        v150 = v149
        v151 = v150
        pacman.change(start = v148,
        extent = v151)
        v152 = 210
        v153 = v152
        v154 = v153
        v155 = 300
        v156 = v155
        v157 = v156
        pacman2.change(start = v154,
        extent = v157)
         
        v158 = 25
        while (time.time() - last_refresh <= v158/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        view.update()
        v160 = 10
        v161 = 0
        v159 = (v160 , v161)
        pacman.move(v159)
        v162 = "normal"
        v163 = v162
        food1.change(state = v163)
        v165 = 10
        v166 = 0
        v164 = (v165 , v166)
        view.move(v164)
        v168 = 10
        v169 = - v168
        v170 = 0
        v167 = (v169 , v170)
        pacman2.move(v167)
        v172 = 10
        v173 = - v172
        v174 = 0
        v171 = (v173 , v174)
        view2.move(v171)
        v176 = 0
        v177 = 10
        v175 = (v176 , v177)
        food2.move(v175)
        last_refresh = time.time()
        view.update()
        last_refresh = time.time()
        view2.update()
    v178 = "hidden"
    v179 = v178
    food1.change(state = v179)
    v180 = "hidden"
    v181 = v180
    food2.change(state = v181)
    last_refresh = time.time()
    view.update()
    last_refresh = time.time()
    view2.update()
    v182 = "Press any mouse button to quit"
    print(v182)
    v183 = last_view.waitClick()
    v184 = v183
    v185 = v184
    pos = v185
