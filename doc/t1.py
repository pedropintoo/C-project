from tkinter import *
import time, os, sys

#################################################################
## Auxiliar
#################################################################
REFRESH_RATE = 0.1
last_refresh = time.time()
canvas_global = None
mouseX = None
mouseY = None
#################################################################
def coord(point):
    x = point[0]
    y = point[1]
    return (width/2-Ox+x, height/2+Oy-y)

def length(origin, point):
    return (origin[0]+point[0], origin[1]-point[1])

def rectangle(origin, length):
    p0 = (origin[0]-length[0]/2,origin[1]-length[1]/2)
    p1 = (origin[0]+length[0]/2,origin[1]-length[1]/2)
    p2 = (origin[0]+length[0]/2,origin[1]+length[1]/2)
    p3 = (origin[0]-length[0]/2,origin[1]+length[1]/2)
    return p0,p1,p2,p3,p0

def ellipse(origin, length):
    return (origin[0]-length[0]/2,origin[1]-length[1]/2),(origin[0]+length[0]/2,origin[1]+length[1]/2)

def onClick(event):
    global mouseX, mouseY
    mouseX, mouseY = event.x, event.y

def getMouse():
    global mouseX, mouseY
    top.update()
    mouseX = None; mouseY = None
    while mouseX == None:
        time.sleep(.1)
        top.update()

def waitClick():
    top.bind("<Button-1>", onClick)
    getMouse()
    return mouseX-width/2+Ox, height/2+Oy-mouseY
#################################################################


if __name__ == "__main__":
    root = Tk()
    root.withdraw()

    # default View values
    top = Toplevel(root)
    Ox = 0
    Oy = 0
    width = 201
    height = 201
    top.title("No title") 
    background = "black"

    v0 = 601
    v1 = v0
    v2 = v1
    v3 = 601
    v4 = v3
    v5 = v4
    v6 = "Illustrating the minimum level graphical models"
    v7 = v6
    v8 = v7
    v9 = "alice blue"
    v10 = v9
    v11 = v10

    height=v5
    width=v2
    top.title(v8)
    background=v11

    v12 = Canvas(top, height=height, width=width, background=background)
    v12.pack()
    canvas_global = v12
    view = v12
    v13 = 200
    v14 = v13
    v15 = v14
    cellSize = v15
    v17 = cellSize
    v18 = - v17
    v19 = cellSize
    v16 = (v18 , v19)
    v21 = 50
    v22 = 50
    v20 = (v21 , v22)
    v23 = v20
    v24 = v23
    v25 = "red"
    v26 = v25
    v27 = v26

    origin = coord(v16)
    line_length = length(origin, v24)
    canvas_global.create_line(origin, line_length, fill=v27)
    # TODO: assign to a var
     
    v29 = 0.5
    while (time.time() - last_refresh <= v29):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    top.update() # TODO: Update only the view!
    v31 = 0
    v32 = cellSize
    v30 = (v31 , v32)
    v34 = 50
    v35 = 50
    v33 = (v34 , v35)
    v36 = v33
    v37 = v36
    v38 = "orange"
    v39 = v38
    v40 = v39

    origin = coord(v30)
    canvas_global.create_line(rectangle(origin, v37), fill=v40)
    # TODO: assign to a var
     
    v42 = 0.5
    while (time.time() - last_refresh <= v42):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    top.update() # TODO: Update only the view!
    v44 = cellSize
    v45 = cellSize
    v43 = (v44 , v45)
    v47 = 60
    v48 = 40
    v46 = (v47 , v48)
    v49 = v46
    v50 = v49
    v51 = "blue"
    v52 = v51
    v53 = v52

    origin = coord(v43)
    canvas_global.create_oval(ellipse(origin, v50), fill=v53)
    # TODO: assign to a var
     
    v55 = 0.5
    while (time.time() - last_refresh <= v55):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    top.update() # TODO: Update only the view!
    v57 = cellSize
    v58 = - v57
    v59 = 0
    v56 = (v58 , v59)
    v61 = 50
    v62 = 50
    v60 = (v61 , v62)
    v63 = v60
    v64 = v63
    v65 = 30
    v66 = v65
    v67 = v66
    v68 = 100
    v69 = v68
    v70 = v69
    v71 = "tomato"
    v72 = v71
    v73 = v72

    origin = coord(v56)
    canvas_global.create_arc(ellipse(origin,v64),style=ARC,start=v67,extent=v70,outline=v73)
    # TODO: assign to a var
     
    v75 = 0.5
    while (time.time() - last_refresh <= v75):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    top.update() # TODO: Update only the view!
    v77 = cellSize
    v78 = 0
    v76 = (v77 , v78)
    v80 = 50
    v81 = 50
    v79 = (v80 , v81)
    v82 = v79
    v83 = v82
    v84 = 30
    v85 = v84
    v86 = v85
    v87 = 150
    v88 = v87
    v89 = v88
    v90 = "cyan"
    v91 = v90
    v92 = v91

    origin = coord(v76)
    canvas_global.create_arc(ellipse(origin,v83),style=CHORD,start=v86,extent=v89,fill=v92)
    # TODO: assign to a var
     
    v94 = 0.5
    while (time.time() - last_refresh <= v94):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    top.update() # TODO: Update only the view!
    v96 = cellSize
    v97 = - v96
    v98 = cellSize
    v99 = - v98
    v95 = (v97 , v99)
    v101 = 50
    v102 = 50
    v100 = (v101 , v102)
    v103 = v100
    v104 = v103
    v105 = 30
    v106 = v105
    v107 = v106
    v108 = 300
    v109 = v108
    v110 = v109
    v111 = "blue"
    v112 = v111
    v113 = v112

    origin = coord(v95)
    canvas_global.create_arc(ellipse(origin,v104),style=PIESLICE,start=v107,extent=v110,fill=v113)
    # TODO: assign to a var
     
    v115 = 0.5
    while (time.time() - last_refresh <= v115):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    top.update() # TODO: Update only the view!
    v117 = 0
    v118 = cellSize
    v119 = - v118
    v116 = (v117 , v119)
    v120 = "Bla bla ..."
    v121 = v120
    v122 = v121
    v123 = "purple"
    v124 = v123
    v125 = v124

    origin = coord(v116)
    canvas_global.create_text(origin,text=v122, fill=v125)
    # TODO: assign to a var
     
    v127 = 0.5
    while (time.time() - last_refresh <= v127):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    top.update() # TODO: Update only the view!
    v129 = cellSize
    v130 = cellSize
    v131 = - v130
    v128 = (v129 , v131)
    v132 = "black"
    v133 = v132
    v134 = v133

    origin = coord(v128)
    canvas_global.create_rectangle(origin, origin, fill=v134)
    # TODO: assign to a var
     
    v136 = 0.5
    while (time.time() - last_refresh <= v136):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    top.update() # TODO: Update only the view!
    v137 = 401
    v138 = v137
    v139 = v138
    v140 = 401
    v141 = v140
    v142 = v141
    v143 = "Illustrating the rectangle shape"
    v144 = v143
    v145 = v144
    v146 = "wheat"
    v147 = v146
    v148 = v147

    height=v142
    width=v139
    top.title(v145)
    background=v148

    v149 = Canvas(top, height=height, width=width, background=background)
    v149.pack()
    canvas_global = v149
    view = v149
     
    v150 = 0.5
    while (time.time() - last_refresh <= v150):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    top.update() # TODO: Update only the view!
    v152 = 10
    v153 = 0
    v151 = (v152 , v153)
    v155 = 200
    v156 = 60
    v154 = (v155 , v156)
    v157 = v154
    v158 = v157
    v159 = "blue"
    v160 = v159
    v161 = v160

    origin = coord(v151)
    canvas_global.create_line(rectangle(origin, v158), fill=v161)
    # TODO: assign to a var
     
    v163 = 0.5
    while (time.time() - last_refresh <= v163):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    top.update() # TODO: Update only the view!
    v165 = 0
    v166 = 0
    v164 = (v165 , v166)
    v168 = 50
    v169 = 50
    v167 = (v168 , v169)
    v170 = v167
    v171 = v170
    v172 = "pink"
    v173 = v172
    v174 = v173
    v175 = 30
    v176 = v175
    v177 = v176
    v178 = 300
    v179 = v178
    v180 = v179

    origin = coord(v164)
    canvas_global.create_arc(ellipse(origin,v171),style=PIESLICE,start=v177,extent=v180,fill=v174)
    # TODO: assign to a var
     
    v182 = 0.5
    while (time.time() - last_refresh <= v182):
        time.sleep(REFRESH_RATE)   

    last_refresh = time.time()
    top.update() # TODO: Update only the view!
    v183 = 1
    v184 = 10
    for i in range(v183, v184, 1):
        v185 = "pedro "
        print(v185)
        v186 = i
        print(v186)
    v187 = waitClick()
    v188 = v187
    v189 = v188
    p = v189
    v190 = p
    print(v190)
