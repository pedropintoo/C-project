from tkinter import *
from AGLClasses import *
import math
import time, os, sys

#################################################################
## Auxiliar
#################################################################
REFRESH_RATE = 0.1
last_refresh = time.time()
last_view = None
mouseX = None
mouseY = None
model = None
#################################################################

if __name__ == "__main__":
    root = Root()

    v0 = 2
    v1 = v0
    v2 = v1
    a = v2
    v3 = "teste"
    v4 = v3
    v5 = v4
    type_ = v5
    v6 = "jorguinho"
    v7 = v6
    v8 = v7
    name = v8
    v11 = a
    v12 = 3
    v10 = v11 >= v12
    v15 = type_
    v16 = "teste"
    v14 = v15 == v16
    v18 = name
    v19 = "jorguinho"
    v17 = v18 == v19
    v13 = v14 and v17
    v9 = v10 or v13
    if v9:
        v20 = 1
        v21 = 10
        for j in range(v20, v21, 1):
            v22 = "pedro é lindo"
            print(v22)
    else:
        v23 = "nao é"
        print(v23)
