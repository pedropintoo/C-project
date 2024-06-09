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
def get_nested_attribute(obj, attr_path, local_dict):
    if obj is None:
        return None
    if attr_path == '':
        return obj    

    # recursive approach
    attr = attr_path.split('.')[0]
    if '[' in attr:
        attr, index = attr.split('[')
        varIndex = index[:-1]
        # consider []...[]
        idx = None
        if varIndex in local_dict:
            idx = local_dict[varIndex]
        else:
            idx = int(varIndex)

        if hasattr(obj, attr):
            obj = getattr(obj, attr)
            obj = obj[idx]
        else:
            return None
    else:
        if hasattr(obj, attr):
            obj = getattr(obj, attr)
        else:
            return None

    if '.' in attr_path:
        attr_path = '.'.join(attr_path.split('.')[1:])
        return get_nested_attribute(obj, attr_path, local_dict) 
    else:
        return obj
#################################################################

if __name__ == "__main__":
    root = Root(views, last_view)

    #################################################################
    ## Model
    #################################################################
    class Fire(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self

            temp = get_nested_attribute(action, '75', locals())
            if temp is None:
                temp = 75
            if action is not None and hasattr(action, "v1".split('[')[0].split('.')[0]):
                action.v1 = temp
            else:
                v1 = temp 


            temp = get_nested_attribute(action, '0', locals())
            if temp is None:
                temp = 0
            if action is not None and hasattr(action, "v2".split('[')[0].split('.')[0]):
                action.v2 = temp
            else:
                v2 = temp 

            v0 = (v1 , v2); v0 = tuple(v0) if isinstance(v0, np.ndarray) else v0

            if model is not None:
                v3 = Rectangle()
                model.add_object(v3) # add object to model
            else:
                v3 = Rectangle(root = root)
            v3.origin = v0

            temp = get_nested_attribute(action, '15', locals())
            if temp is None:
                temp = 15
            if action is not None and hasattr(action, "v5".split('[')[0].split('.')[0]):
                action.v5 = temp
            else:
                v5 = temp 


            temp = get_nested_attribute(action, '2', locals())
            if temp is None:
                temp = 2
            if action is not None and hasattr(action, "v6".split('[')[0].split('.')[0]):
                action.v6 = temp
            else:
                v6 = temp 

            v4 = (v5 , v6); v4 = tuple(v4) if isinstance(v4, np.ndarray) else v4

            temp = get_nested_attribute(action, 'v4', locals())
            if temp is None:
                temp = v4
            if action is not None and hasattr(action, "v7".split('[')[0].split('.')[0]):
                action.v7 = temp
            else:
                v7 = temp 


            temp = get_nested_attribute(action, 'v7', locals())
            if temp is None:
                temp = v7
            if action is not None and hasattr(action, "v8".split('[')[0].split('.')[0]):
                action.v8 = temp
            else:
                v8 = temp 


            temp = get_nested_attribute(action, '"red"', locals())
            if temp is None:
                temp = "red"
            if action is not None and hasattr(action, "v9".split('[')[0].split('.')[0]):
                action.v9 = temp
            else:
                v9 = temp 


            temp = get_nested_attribute(action, 'v9', locals())
            if temp is None:
                temp = v9
            if action is not None and hasattr(action, "v10".split('[')[0].split('.')[0]):
                action.v10 = temp
            else:
                v10 = temp 


            temp = get_nested_attribute(action, 'v10', locals())
            if temp is None:
                temp = v10
            if action is not None and hasattr(action, "v11".split('[')[0].split('.')[0]):
                action.v11 = temp
            else:
                v11 = temp 


            temp = get_nested_attribute(action, '"hidden"', locals())
            if temp is None:
                temp = "hidden"
            if action is not None and hasattr(action, "v12".split('[')[0].split('.')[0]):
                action.v12 = temp
            else:
                v12 = temp 


            temp = get_nested_attribute(action, 'v12', locals())
            if temp is None:
                temp = v12
            if action is not None and hasattr(action, "v13".split('[')[0].split('.')[0]):
                action.v13 = temp
            else:
                v13 = temp 


            temp = get_nested_attribute(action, 'v13', locals())
            if temp is None:
                temp = v13
            if action is not None and hasattr(action, "v14".split('[')[0].split('.')[0]):
                action.v14 = temp
            else:
                v14 = temp 


            if action is not None:
                action.v3.length = v8
                action.v3.fill = v11
                action.v3.state = v14
            else:
                v3.length = v8
                v3.fill = v11
                v3.state = v14

            temp = get_nested_attribute(action, 'v3', locals())
            if temp is None:
                temp = v3
            if action is not None and hasattr(action, "var__agl__flame".split('[')[0].split('.')[0]):
                action.var__agl__flame = temp
            else:
                var__agl__flame = temp 
            if model is not None: 
                model.var__agl__flame = var__agl__flame
                model.last_var__agl__flame = copy.deepcopy(var__agl__flame)
            class v15(Enum):
                var__agl__red = auto()
                var__agl__blue = auto() 
            global var__agl__red; var__agl__red = v15.var__agl__red
            global var__agl__blue; var__agl__blue = v15.var__agl__blue   
            v16 = v15(1) # first is default

            temp = get_nested_attribute(action, 'v16', locals())
            if temp is None:
                temp = v16
            if action is not None and hasattr(action, "v17".split('[')[0].split('.')[0]):
                action.v17 = temp
            else:
                v17 = temp 


            temp = get_nested_attribute(action, 'v17', locals())
            if temp is None:
                temp = v17
            if action is not None and hasattr(action, "var__agl__color".split('[')[0].split('.')[0]):
                action.var__agl__color = temp
            else:
                var__agl__color = temp 
            if model is not None: 
                model.var__agl__color = var__agl__color
                model.last_var__agl__color = copy.deepcopy(var__agl__color)

            self.fixCoords()

        def create_object(self, view):
            action = self

            if self.var__agl__flame.state != self.last_var__agl__flame.state:

                temp = get_nested_attribute(action, '"The flame is "', locals())
                if temp is None:
                    temp = "The flame is "
                if action is not None and hasattr(action, "v18".split('[')[0].split('.')[0]):
                    action.v18 = temp
                else:
                    v18 = temp 

                print(v18)

                temp = get_nested_attribute(action, 'var__agl__flame.state', locals())
                if temp is None:
                    temp = var__agl__flame.state
                if action is not None and hasattr(action, "v19".split('[')[0].split('.')[0]):
                    action.v19 = temp
                else:
                    v19 = temp 

                print(v19)

                temp = get_nested_attribute(action, 'var__agl__flame.state', locals())
                if temp is None:
                    temp = var__agl__flame.state
                if action is not None and hasattr(action, "v21".split('[')[0].split('.')[0]):
                    action.v21 = temp
                else:
                    v21 = temp 


                temp = get_nested_attribute(action, '"normal"', locals())
                if temp is None:
                    temp = "normal"
                if action is not None and hasattr(action, "v22".split('[')[0].split('.')[0]):
                    action.v22 = temp
                else:
                    v22 = temp 

                v20 = np.array(v21) == np.array(v22); v20 = tuple(v20) if isinstance(v20, np.ndarray) else v20
                if v20:

                    temp = get_nested_attribute(action, 'var__agl__color', locals())
                    if temp is None:
                        temp = var__agl__color
                    if action is not None and hasattr(action, "v24".split('[')[0].split('.')[0]):
                        action.v24 = temp
                    else:
                        v24 = temp 


                    temp = get_nested_attribute(action, 'var__agl__blue', locals())
                    if temp is None:
                        temp = var__agl__blue
                    if action is not None and hasattr(action, "v25".split('[')[0].split('.')[0]):
                        action.v25 = temp
                    else:
                        v25 = temp 

                    v23 = np.array(v24) == np.array(v25); v23 = tuple(v23) if isinstance(v23, np.ndarray) else v23
                    if v23:

                        temp = get_nested_attribute(action, '"red"', locals())
                        if temp is None:
                            temp = "red"
                        if action is not None and hasattr(action, "v26".split('[')[0].split('.')[0]):
                            action.v26 = temp
                        else:
                            v26 = temp 


                        temp = get_nested_attribute(action, 'v26', locals())
                        if temp is None:
                            temp = v26
                        if action is not None and hasattr(action, "v27".split('[')[0].split('.')[0]):
                            action.v27 = temp
                        else:
                            v27 = temp 


                        temp = get_nested_attribute(action, 'v27', locals())
                        if temp is None:
                            temp = v27
                        if action is not None and hasattr(action, "var__agl__flame.fill".split('[')[0].split('.')[0]):
                            action.var__agl__flame.fill = temp
                        else:
                            var__agl__flame.fill = temp 


                        temp = get_nested_attribute(action, 'var__agl__red', locals())
                        if temp is None:
                            temp = var__agl__red
                        if action is not None and hasattr(action, "v28".split('[')[0].split('.')[0]):
                            action.v28 = temp
                        else:
                            v28 = temp 


                        temp = get_nested_attribute(action, 'v28', locals())
                        if temp is None:
                            temp = v28
                        if action is not None and hasattr(action, "v29".split('[')[0].split('.')[0]):
                            action.v29 = temp
                        else:
                            v29 = temp 


                        temp = get_nested_attribute(action, 'v29', locals())
                        if temp is None:
                            temp = v29
                        if action is not None and hasattr(action, "var__agl__color".split('[')[0].split('.')[0]):
                            action.var__agl__color = temp
                        else:
                            var__agl__color = temp 
                        
                    else:

                        temp = get_nested_attribute(action, '"blue"', locals())
                        if temp is None:
                            temp = "blue"
                        if action is not None and hasattr(action, "v30".split('[')[0].split('.')[0]):
                            action.v30 = temp
                        else:
                            v30 = temp 


                        temp = get_nested_attribute(action, 'v30', locals())
                        if temp is None:
                            temp = v30
                        if action is not None and hasattr(action, "v31".split('[')[0].split('.')[0]):
                            action.v31 = temp
                        else:
                            v31 = temp 


                        temp = get_nested_attribute(action, 'v31', locals())
                        if temp is None:
                            temp = v31
                        if action is not None and hasattr(action, "var__agl__flame.fill".split('[')[0].split('.')[0]):
                            action.var__agl__flame.fill = temp
                        else:
                            var__agl__flame.fill = temp 


                        temp = get_nested_attribute(action, 'var__agl__blue', locals())
                        if temp is None:
                            temp = var__agl__blue
                        if action is not None and hasattr(action, "v32".split('[')[0].split('.')[0]):
                            action.v32 = temp
                        else:
                            v32 = temp 


                        temp = get_nested_attribute(action, 'v32', locals())
                        if temp is None:
                            temp = v32
                        if action is not None and hasattr(action, "v33".split('[')[0].split('.')[0]):
                            action.v33 = temp
                        else:
                            v33 = temp 


                        temp = get_nested_attribute(action, 'v33', locals())
                        if temp is None:
                            temp = v33
                        if action is not None and hasattr(action, "var__agl__color".split('[')[0].split('.')[0]):
                            action.var__agl__color = temp
                        else:
                            var__agl__color = temp 

                            
                self.last_var__agl__flame.state = copy.deepcopy(self.var__agl__flame.state)
        
            action = None
            super().create_object(view)
            model = None

        def __deepcopy__(self, memo=None):
            """Create a deep copy of the model."""
            if memo is None:
                memo = {} # this is required by the deepcopy protocol
            new_model = Fire()

            self.copyAttributesTo(new_model)
            return new_model       

    #################################################################
    #################################################################
    ## Model
    #################################################################
    class Pacman(Model):
        def __init__(self, root: Root = None, view: View = None, origin=(0,0)):
            super().__init__(root=root, view=view, origin=origin)
            model = self

            if model is not None:
                v34 = PieSlice()
                model.add_object(v34) # add object to model
            else:
                v34 = PieSlice(root = root)

            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v36".split('[')[0].split('.')[0]):
                action.v36 = temp
            else:
                v36 = temp 


            temp = get_nested_attribute(action, '50', locals())
            if temp is None:
                temp = 50
            if action is not None and hasattr(action, "v37".split('[')[0].split('.')[0]):
                action.v37 = temp
            else:
                v37 = temp 

            v35 = (v36 , v37); v35 = tuple(v35) if isinstance(v35, np.ndarray) else v35

            temp = get_nested_attribute(action, 'v35', locals())
            if temp is None:
                temp = v35
            if action is not None and hasattr(action, "v38".split('[')[0].split('.')[0]):
                action.v38 = temp
            else:
                v38 = temp 


            temp = get_nested_attribute(action, 'v38', locals())
            if temp is None:
                temp = v38
            if action is not None and hasattr(action, "v39".split('[')[0].split('.')[0]):
                action.v39 = temp
            else:
                v39 = temp 


            temp = get_nested_attribute(action, '"pink"', locals())
            if temp is None:
                temp = "pink"
            if action is not None and hasattr(action, "v40".split('[')[0].split('.')[0]):
                action.v40 = temp
            else:
                v40 = temp 


            temp = get_nested_attribute(action, 'v40', locals())
            if temp is None:
                temp = v40
            if action is not None and hasattr(action, "v41".split('[')[0].split('.')[0]):
                action.v41 = temp
            else:
                v41 = temp 


            temp = get_nested_attribute(action, 'v41', locals())
            if temp is None:
                temp = v41
            if action is not None and hasattr(action, "v42".split('[')[0].split('.')[0]):
                action.v42 = temp
            else:
                v42 = temp 


            temp = get_nested_attribute(action, '30', locals())
            if temp is None:
                temp = 30
            if action is not None and hasattr(action, "v43".split('[')[0].split('.')[0]):
                action.v43 = temp
            else:
                v43 = temp 


            temp = get_nested_attribute(action, 'v43', locals())
            if temp is None:
                temp = v43
            if action is not None and hasattr(action, "v44".split('[')[0].split('.')[0]):
                action.v44 = temp
            else:
                v44 = temp 


            temp = get_nested_attribute(action, 'v44', locals())
            if temp is None:
                temp = v44
            if action is not None and hasattr(action, "v45".split('[')[0].split('.')[0]):
                action.v45 = temp
            else:
                v45 = temp 


            temp = get_nested_attribute(action, '300', locals())
            if temp is None:
                temp = 300
            if action is not None and hasattr(action, "v46".split('[')[0].split('.')[0]):
                action.v46 = temp
            else:
                v46 = temp 


            temp = get_nested_attribute(action, 'v46', locals())
            if temp is None:
                temp = v46
            if action is not None and hasattr(action, "v47".split('[')[0].split('.')[0]):
                action.v47 = temp
            else:
                v47 = temp 


            temp = get_nested_attribute(action, 'v47', locals())
            if temp is None:
                temp = v47
            if action is not None and hasattr(action, "v48".split('[')[0].split('.')[0]):
                action.v48 = temp
            else:
                v48 = temp 


            if action is not None:
                action.v34.length = v39
                action.v34.fill = v42
                action.v34.start = v45
                action.v34.extent = v48
            else:
                v34.length = v39
                v34.fill = v42
                v34.start = v45
                v34.extent = v48

            temp = get_nested_attribute(action, 'v34', locals())
            if temp is None:
                temp = v34
            if action is not None and hasattr(action, "var__agl__face".split('[')[0].split('.')[0]):
                action.var__agl__face = temp
            else:
                var__agl__face = temp 
            if model is not None: 
                model.var__agl__face = var__agl__face
                model.last_var__agl__face = copy.deepcopy(var__agl__face)

            temp = get_nested_attribute(action, '20', locals())
            if temp is None:
                temp = 20
            if action is not None and hasattr(action, "v50".split('[')[0].split('.')[0]):
                action.v50 = temp
            else:
                v50 = temp 


            temp = get_nested_attribute(action, '35', locals())
            if temp is None:
                temp = 35
            if action is not None and hasattr(action, "v51".split('[')[0].split('.')[0]):
                action.v51 = temp
            else:
                v51 = temp 

            v49 = (v50 , v51); v49 = tuple(v49) if isinstance(v49, np.ndarray) else v49

            if model is not None:
                v52 = Ellipse()
                model.add_object(v52) # add object to model
            else:
                v52 = Ellipse(root = root)
            v52.origin = v49

            temp = get_nested_attribute(action, '"black"', locals())
            if temp is None:
                temp = "black"
            if action is not None and hasattr(action, "v53".split('[')[0].split('.')[0]):
                action.v53 = temp
            else:
                v53 = temp 


            temp = get_nested_attribute(action, 'v53', locals())
            if temp is None:
                temp = v53
            if action is not None and hasattr(action, "v54".split('[')[0].split('.')[0]):
                action.v54 = temp
            else:
                v54 = temp 


            temp = get_nested_attribute(action, 'v54', locals())
            if temp is None:
                temp = v54
            if action is not None and hasattr(action, "v55".split('[')[0].split('.')[0]):
                action.v55 = temp
            else:
                v55 = temp 


            temp = get_nested_attribute(action, '5', locals())
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v57".split('[')[0].split('.')[0]):
                action.v57 = temp
            else:
                v57 = temp 


            temp = get_nested_attribute(action, '5', locals())
            if temp is None:
                temp = 5
            if action is not None and hasattr(action, "v58".split('[')[0].split('.')[0]):
                action.v58 = temp
            else:
                v58 = temp 

            v56 = (v57 , v58); v56 = tuple(v56) if isinstance(v56, np.ndarray) else v56

            temp = get_nested_attribute(action, 'v56', locals())
            if temp is None:
                temp = v56
            if action is not None and hasattr(action, "v59".split('[')[0].split('.')[0]):
                action.v59 = temp
            else:
                v59 = temp 


            temp = get_nested_attribute(action, 'v59', locals())
            if temp is None:
                temp = v59
            if action is not None and hasattr(action, "v60".split('[')[0].split('.')[0]):
                action.v60 = temp
            else:
                v60 = temp 


            if action is not None:
                action.v52.fill = v55
                action.v52.length = v60
            else:
                v52.fill = v55
                v52.length = v60

            temp = get_nested_attribute(action, 'v52', locals())
            if temp is None:
                temp = v52
            if action is not None and hasattr(action, "var__agl__eye".split('[')[0].split('.')[0]):
                action.var__agl__eye = temp
            else:
                var__agl__eye = temp 
            if model is not None: 
                model.var__agl__eye = var__agl__eye
                model.last_var__agl__eye = copy.deepcopy(var__agl__eye)

            if model is not None:
                model_backup = model
                v61 = Fire() # this makes model = None in the end!
                model = model_backup
                model.add_object(v61) # add object to model
            else:
                v61 = Fire(root = root, view = last_view)
              

            temp = get_nested_attribute(action, 'v61', locals())
            if temp is None:
                temp = v61
            if action is not None and hasattr(action, "v62".split('[')[0].split('.')[0]):
                action.v62 = temp
            else:
                v62 = temp 


            temp = get_nested_attribute(action, 'v62', locals())
            if temp is None:
                temp = v62
            if action is not None and hasattr(action, "var__agl__fire".split('[')[0].split('.')[0]):
                action.var__agl__fire = temp
            else:
                var__agl__fire = temp 
            if model is not None: 
                model.var__agl__fire = var__agl__fire
                model.last_var__agl__fire = copy.deepcopy(var__agl__fire)
            class v82(Enum):
                var__agl__Open = auto()
                var__agl__Close = auto() 
            global var__agl__Open; var__agl__Open = v82.var__agl__Open
            global var__agl__Close; var__agl__Close = v82.var__agl__Close   
            v83 = v82(1) # first is default

            temp = get_nested_attribute(action, 'v83', locals())
            if temp is None:
                temp = v83
            if action is not None and hasattr(action, "v84".split('[')[0].split('.')[0]):
                action.v84 = temp
            else:
                v84 = temp 


            temp = get_nested_attribute(action, 'v84', locals())
            if temp is None:
                temp = v84
            if action is not None and hasattr(action, "var__agl__mouth".split('[')[0].split('.')[0]):
                action.var__agl__mouth = temp
            else:
                var__agl__mouth = temp 
            if model is not None: 
                model.var__agl__mouth = var__agl__mouth
                model.last_var__agl__mouth = copy.deepcopy(var__agl__mouth)

            self.fixCoords()

        def create_object(self, view):
            action = self

            if self.var__agl__fire.var__agl__flame.state != self.last_var__agl__fire.var__agl__flame.state:

                temp = get_nested_attribute(action, 'var__agl__fire.var__agl__flame.state', locals())
                if temp is None:
                    temp = var__agl__fire.var__agl__flame.state
                if action is not None and hasattr(action, "v64".split('[')[0].split('.')[0]):
                    action.v64 = temp
                else:
                    v64 = temp 


                temp = get_nested_attribute(action, '"normal"', locals())
                if temp is None:
                    temp = "normal"
                if action is not None and hasattr(action, "v65".split('[')[0].split('.')[0]):
                    action.v65 = temp
                else:
                    v65 = temp 

                v63 = np.array(v64) == np.array(v65); v63 = tuple(v63) if isinstance(v63, np.ndarray) else v63
                if v63:

                    temp = get_nested_attribute(action, '"red"', locals())
                    if temp is None:
                        temp = "red"
                    if action is not None and hasattr(action, "v66".split('[')[0].split('.')[0]):
                        action.v66 = temp
                    else:
                        v66 = temp 


                    temp = get_nested_attribute(action, 'v66', locals())
                    if temp is None:
                        temp = v66
                    if action is not None and hasattr(action, "v67".split('[')[0].split('.')[0]):
                        action.v67 = temp
                    else:
                        v67 = temp 


                    temp = get_nested_attribute(action, 'v67', locals())
                    if temp is None:
                        temp = v67
                    if action is not None and hasattr(action, "v68".split('[')[0].split('.')[0]):
                        action.v68 = temp
                    else:
                        v68 = temp 


                    temp = get_nested_attribute(action, '10', locals())
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v70".split('[')[0].split('.')[0]):
                        action.v70 = temp
                    else:
                        v70 = temp 


                    temp = get_nested_attribute(action, '10', locals())
                    if temp is None:
                        temp = 10
                    if action is not None and hasattr(action, "v71".split('[')[0].split('.')[0]):
                        action.v71 = temp
                    else:
                        v71 = temp 

                    v69 = (v70 , v71); v69 = tuple(v69) if isinstance(v69, np.ndarray) else v69

                    temp = get_nested_attribute(action, 'v69', locals())
                    if temp is None:
                        temp = v69
                    if action is not None and hasattr(action, "v72".split('[')[0].split('.')[0]):
                        action.v72 = temp
                    else:
                        v72 = temp 


                    temp = get_nested_attribute(action, 'v72', locals())
                    if temp is None:
                        temp = v72
                    if action is not None and hasattr(action, "v73".split('[')[0].split('.')[0]):
                        action.v73 = temp
                    else:
                        v73 = temp 


                    if action is not None:
                        action.var__agl__eye.fill = v68
                        action.var__agl__eye.length = v73
                    else:
                        var__agl__eye.fill = v68
                        var__agl__eye.length = v73    
                else:

                    temp = get_nested_attribute(action, 'var__agl__face.fill', locals())
                    if temp is None:
                        temp = var__agl__face.fill
                    if action is not None and hasattr(action, "v74".split('[')[0].split('.')[0]):
                        action.v74 = temp
                    else:
                        v74 = temp 


                    temp = get_nested_attribute(action, 'v74', locals())
                    if temp is None:
                        temp = v74
                    if action is not None and hasattr(action, "v75".split('[')[0].split('.')[0]):
                        action.v75 = temp
                    else:
                        v75 = temp 


                    temp = get_nested_attribute(action, 'v75', locals())
                    if temp is None:
                        temp = v75
                    if action is not None and hasattr(action, "v76".split('[')[0].split('.')[0]):
                        action.v76 = temp
                    else:
                        v76 = temp 


                    temp = get_nested_attribute(action, '5', locals())
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v78".split('[')[0].split('.')[0]):
                        action.v78 = temp
                    else:
                        v78 = temp 


                    temp = get_nested_attribute(action, '5', locals())
                    if temp is None:
                        temp = 5
                    if action is not None and hasattr(action, "v79".split('[')[0].split('.')[0]):
                        action.v79 = temp
                    else:
                        v79 = temp 

                    v77 = (v78 , v79); v77 = tuple(v77) if isinstance(v77, np.ndarray) else v77

                    temp = get_nested_attribute(action, 'v77', locals())
                    if temp is None:
                        temp = v77
                    if action is not None and hasattr(action, "v80".split('[')[0].split('.')[0]):
                        action.v80 = temp
                    else:
                        v80 = temp 


                    temp = get_nested_attribute(action, 'v80', locals())
                    if temp is None:
                        temp = v80
                    if action is not None and hasattr(action, "v81".split('[')[0].split('.')[0]):
                        action.v81 = temp
                    else:
                        v81 = temp 


                    if action is not None:
                        action.var__agl__eye.fill = v76
                        action.var__agl__eye.length = v81
                    else:
                        var__agl__eye.fill = v76
                        var__agl__eye.length = v81
                    
                self.last_var__agl__fire.var__agl__flame.state = copy.deepcopy(self.var__agl__fire.var__agl__flame.state)


            if self.var__agl__mouth != self.last_var__agl__mouth:

                temp = get_nested_attribute(action, 'var__agl__mouth', locals())
                if temp is None:
                    temp = var__agl__mouth
                if action is not None and hasattr(action, "v86".split('[')[0].split('.')[0]):
                    action.v86 = temp
                else:
                    v86 = temp 


                temp = get_nested_attribute(action, 'var__agl__Open', locals())
                if temp is None:
                    temp = var__agl__Open
                if action is not None and hasattr(action, "v87".split('[')[0].split('.')[0]):
                    action.v87 = temp
                else:
                    v87 = temp 

                v85 = np.array(v86) == np.array(v87); v85 = tuple(v85) if isinstance(v85, np.ndarray) else v85
                if v85:

                    temp = get_nested_attribute(action, '30', locals())
                    if temp is None:
                        temp = 30
                    if action is not None and hasattr(action, "v88".split('[')[0].split('.')[0]):
                        action.v88 = temp
                    else:
                        v88 = temp 


                    temp = get_nested_attribute(action, 'v88', locals())
                    if temp is None:
                        temp = v88
                    if action is not None and hasattr(action, "v89".split('[')[0].split('.')[0]):
                        action.v89 = temp
                    else:
                        v89 = temp 


                    temp = get_nested_attribute(action, 'v89', locals())
                    if temp is None:
                        temp = v89
                    if action is not None and hasattr(action, "v90".split('[')[0].split('.')[0]):
                        action.v90 = temp
                    else:
                        v90 = temp 


                    temp = get_nested_attribute(action, '300', locals())
                    if temp is None:
                        temp = 300
                    if action is not None and hasattr(action, "v91".split('[')[0].split('.')[0]):
                        action.v91 = temp
                    else:
                        v91 = temp 


                    temp = get_nested_attribute(action, 'v91', locals())
                    if temp is None:
                        temp = v91
                    if action is not None and hasattr(action, "v92".split('[')[0].split('.')[0]):
                        action.v92 = temp
                    else:
                        v92 = temp 


                    temp = get_nested_attribute(action, 'v92', locals())
                    if temp is None:
                        temp = v92
                    if action is not None and hasattr(action, "v93".split('[')[0].split('.')[0]):
                        action.v93 = temp
                    else:
                        v93 = temp 


                    if action is not None:
                        action.var__agl__face.start = v90
                        action.var__agl__face.extent = v93
                    else:
                        var__agl__face.start = v90
                        var__agl__face.extent = v93

                    temp = get_nested_attribute(action, '"normal"', locals())
                    if temp is None:
                        temp = "normal"
                    if action is not None and hasattr(action, "v94".split('[')[0].split('.')[0]):
                        action.v94 = temp
                    else:
                        v94 = temp 


                    temp = get_nested_attribute(action, 'v94', locals())
                    if temp is None:
                        temp = v94
                    if action is not None and hasattr(action, "v95".split('[')[0].split('.')[0]):
                        action.v95 = temp
                    else:
                        v95 = temp 


                    temp = get_nested_attribute(action, 'v95', locals())
                    if temp is None:
                        temp = v95
                    if action is not None and hasattr(action, "var__agl__fire.var__agl__flame.state".split('[')[0].split('.')[0]):
                        action.var__agl__fire.var__agl__flame.state = temp
                    else:
                        var__agl__fire.var__agl__flame.state = temp 
                    
                else:

                    temp = get_nested_attribute(action, '1', locals())
                    if temp is None:
                        temp = 1
                    if action is not None and hasattr(action, "v96".split('[')[0].split('.')[0]):
                        action.v96 = temp
                    else:
                        v96 = temp 


                    temp = get_nested_attribute(action, 'v96', locals())
                    if temp is None:
                        temp = v96
                    if action is not None and hasattr(action, "v97".split('[')[0].split('.')[0]):
                        action.v97 = temp
                    else:
                        v97 = temp 


                    temp = get_nested_attribute(action, 'v97', locals())
                    if temp is None:
                        temp = v97
                    if action is not None and hasattr(action, "v98".split('[')[0].split('.')[0]):
                        action.v98 = temp
                    else:
                        v98 = temp 


                    temp = get_nested_attribute(action, '359', locals())
                    if temp is None:
                        temp = 359
                    if action is not None and hasattr(action, "v99".split('[')[0].split('.')[0]):
                        action.v99 = temp
                    else:
                        v99 = temp 


                    temp = get_nested_attribute(action, 'v99', locals())
                    if temp is None:
                        temp = v99
                    if action is not None and hasattr(action, "v100".split('[')[0].split('.')[0]):
                        action.v100 = temp
                    else:
                        v100 = temp 


                    temp = get_nested_attribute(action, 'v100', locals())
                    if temp is None:
                        temp = v100
                    if action is not None and hasattr(action, "v101".split('[')[0].split('.')[0]):
                        action.v101 = temp
                    else:
                        v101 = temp 


                    if action is not None:
                        action.var__agl__face.start = v98
                        action.var__agl__face.extent = v101
                    else:
                        var__agl__face.start = v98
                        var__agl__face.extent = v101

                    temp = get_nested_attribute(action, '"hidden"', locals())
                    if temp is None:
                        temp = "hidden"
                    if action is not None and hasattr(action, "v102".split('[')[0].split('.')[0]):
                        action.v102 = temp
                    else:
                        v102 = temp 


                    temp = get_nested_attribute(action, 'v102', locals())
                    if temp is None:
                        temp = v102
                    if action is not None and hasattr(action, "v103".split('[')[0].split('.')[0]):
                        action.v103 = temp
                    else:
                        v103 = temp 


                    temp = get_nested_attribute(action, 'v103', locals())
                    if temp is None:
                        temp = v103
                    if action is not None and hasattr(action, "var__agl__fire.var__agl__flame.state".split('[')[0].split('.')[0]):
                        action.var__agl__fire.var__agl__flame.state = temp
                    else:
                        var__agl__fire.var__agl__flame.state = temp 

                    
                self.last_var__agl__mouth = copy.deepcopy(self.var__agl__mouth)
        
            action = None
            super().create_object(view)
            model = None

        def __deepcopy__(self, memo=None):
            """Create a deep copy of the model."""
            if memo is None:
                memo = {} # this is required by the deepcopy protocol
            new_model = Pacman()

            self.copyAttributesTo(new_model)
            return new_model       

    #################################################################


    if model is not None:
        v104 = Rectangle()
        model.add_object(v104) # add object to model
    else:
        v104 = Rectangle(root = root)

    temp = get_nested_attribute(action, '650', locals())
    if temp is None:
        temp = 650
    if action is not None and hasattr(action, "v106".split('[')[0].split('.')[0]):
        action.v106 = temp
    else:
        v106 = temp 


    temp = get_nested_attribute(action, '70', locals())
    if temp is None:
        temp = 70
    if action is not None and hasattr(action, "v107".split('[')[0].split('.')[0]):
        action.v107 = temp
    else:
        v107 = temp 

    v105 = (v106 , v107); v105 = tuple(v105) if isinstance(v105, np.ndarray) else v105

    temp = get_nested_attribute(action, 'v105', locals())
    if temp is None:
        temp = v105
    if action is not None and hasattr(action, "v108".split('[')[0].split('.')[0]):
        action.v108 = temp
    else:
        v108 = temp 


    temp = get_nested_attribute(action, 'v108', locals())
    if temp is None:
        temp = v108
    if action is not None and hasattr(action, "v109".split('[')[0].split('.')[0]):
        action.v109 = temp
    else:
        v109 = temp 


    temp = get_nested_attribute(action, '"blue"', locals())
    if temp is None:
        temp = "blue"
    if action is not None and hasattr(action, "v110".split('[')[0].split('.')[0]):
        action.v110 = temp
    else:
        v110 = temp 


    temp = get_nested_attribute(action, 'v110', locals())
    if temp is None:
        temp = v110
    if action is not None and hasattr(action, "v111".split('[')[0].split('.')[0]):
        action.v111 = temp
    else:
        v111 = temp 


    temp = get_nested_attribute(action, 'v111', locals())
    if temp is None:
        temp = v111
    if action is not None and hasattr(action, "v112".split('[')[0].split('.')[0]):
        action.v112 = temp
    else:
        v112 = temp 


    if action is not None:
        action.v104.length = v109
        action.v104.fill = v112
    else:
        v104.length = v109
        v104.fill = v112

    if model is not None:
        v113 = View()
        model.add_object(v113) # add object to model
    else:
        v113 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v113
    root.last_view = last_view

    temp = get_nested_attribute(action, '30', locals())
    if temp is None:
        temp = 30
    if action is not None and hasattr(action, "v114".split('[')[0].split('.')[0]):
        action.v114 = temp
    else:
        v114 = temp 


    temp = get_nested_attribute(action, 'v114', locals())
    if temp is None:
        temp = v114
    if action is not None and hasattr(action, "v115".split('[')[0].split('.')[0]):
        action.v115 = temp
    else:
        v115 = temp 


    temp = get_nested_attribute(action, 'v115', locals())
    if temp is None:
        temp = v115
    if action is not None and hasattr(action, "v116".split('[')[0].split('.')[0]):
        action.v116 = temp
    else:
        v116 = temp 


    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v117".split('[')[0].split('.')[0]):
        action.v117 = temp
    else:
        v117 = temp 


    temp = get_nested_attribute(action, 'v117', locals())
    if temp is None:
        temp = v117
    if action is not None and hasattr(action, "v118".split('[')[0].split('.')[0]):
        action.v118 = temp
    else:
        v118 = temp 


    temp = get_nested_attribute(action, 'v118', locals())
    if temp is None:
        temp = v118
    if action is not None and hasattr(action, "v119".split('[')[0].split('.')[0]):
        action.v119 = temp
    else:
        v119 = temp 


    temp = get_nested_attribute(action, '1800', locals())
    if temp is None:
        temp = 1800
    if action is not None and hasattr(action, "v120".split('[')[0].split('.')[0]):
        action.v120 = temp
    else:
        v120 = temp 


    temp = get_nested_attribute(action, 'v120', locals())
    if temp is None:
        temp = v120
    if action is not None and hasattr(action, "v121".split('[')[0].split('.')[0]):
        action.v121 = temp
    else:
        v121 = temp 


    temp = get_nested_attribute(action, 'v121', locals())
    if temp is None:
        temp = v121
    if action is not None and hasattr(action, "v122".split('[')[0].split('.')[0]):
        action.v122 = temp
    else:
        v122 = temp 


    temp = get_nested_attribute(action, '401', locals())
    if temp is None:
        temp = 401
    if action is not None and hasattr(action, "v123".split('[')[0].split('.')[0]):
        action.v123 = temp
    else:
        v123 = temp 


    temp = get_nested_attribute(action, 'v123', locals())
    if temp is None:
        temp = v123
    if action is not None and hasattr(action, "v124".split('[')[0].split('.')[0]):
        action.v124 = temp
    else:
        v124 = temp 


    temp = get_nested_attribute(action, 'v124', locals())
    if temp is None:
        temp = v124
    if action is not None and hasattr(action, "v125".split('[')[0].split('.')[0]):
        action.v125 = temp
    else:
        v125 = temp 


    temp = get_nested_attribute(action, '"1"', locals())
    if temp is None:
        temp = "1"
    if action is not None and hasattr(action, "v126".split('[')[0].split('.')[0]):
        action.v126 = temp
    else:
        v126 = temp 


    temp = get_nested_attribute(action, 'v126', locals())
    if temp is None:
        temp = v126
    if action is not None and hasattr(action, "v127".split('[')[0].split('.')[0]):
        action.v127 = temp
    else:
        v127 = temp 


    temp = get_nested_attribute(action, 'v127', locals())
    if temp is None:
        temp = v127
    if action is not None and hasattr(action, "v128".split('[')[0].split('.')[0]):
        action.v128 = temp
    else:
        v128 = temp 


    temp = get_nested_attribute(action, '"alice blue"', locals())
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v129".split('[')[0].split('.')[0]):
        action.v129 = temp
    else:
        v129 = temp 


    temp = get_nested_attribute(action, 'v129', locals())
    if temp is None:
        temp = v129
    if action is not None and hasattr(action, "v130".split('[')[0].split('.')[0]):
        action.v130 = temp
    else:
        v130 = temp 


    temp = get_nested_attribute(action, 'v130', locals())
    if temp is None:
        temp = v130
    if action is not None and hasattr(action, "v131".split('[')[0].split('.')[0]):
        action.v131 = temp
    else:
        v131 = temp 


    if action is not None:
        action.v113.Ox = v116
        action.v113.Oy = v119
        action.v113.width = v122
        action.v113.height = v125
        action.v113.title = v128
        action.v113.background = v131
    else:
        v113.Ox = v116
        v113.Oy = v119
        v113.width = v122
        v113.height = v125
        v113.title = v128
        v113.background = v131

    temp = get_nested_attribute(action, 'v113', locals())
    if temp is None:
        temp = v113
    if action is not None and hasattr(action, "var__agl__view".split('[')[0].split('.')[0]):
        action.var__agl__view = temp
    else:
        var__agl__view = temp 
    if model is not None: 
        model.var__agl__view = var__agl__view
        model.last_var__agl__view = copy.deepcopy(var__agl__view)

    temp = get_nested_attribute(action, '650', locals())
    if temp is None:
        temp = 650
    if action is not None and hasattr(action, "v134".split('[')[0].split('.')[0]):
        action.v134 = temp
    else:
        v134 = temp 

    v135 = - np.array(v134)

    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v136".split('[')[0].split('.')[0]):
        action.v136 = temp
    else:
        v136 = temp 

    v133 = (v135 , v136); v133 = tuple(v133) if isinstance(v133, np.ndarray) else v133

    if model is not None:
        model_backup = model
        v132 = Pacman() # this makes model = None in the end!
        model = model_backup
        model.add_object(v132) # add object to model
    else:
        v132 = Pacman(root = root, view = last_view)
    v132.move_absolute(v133)  

    temp = get_nested_attribute(action, 'v132', locals())
    if temp is None:
        temp = v132
    if action is not None and hasattr(action, "v137".split('[')[0].split('.')[0]):
        action.v137 = temp
    else:
        v137 = temp 


    temp = get_nested_attribute(action, 'v137', locals())
    if temp is None:
        temp = v137
    if action is not None and hasattr(action, "var__agl__pacman".split('[')[0].split('.')[0]):
        action.var__agl__pacman = temp
    else:
        var__agl__pacman = temp 
    if model is not None: 
        model.var__agl__pacman = var__agl__pacman
        model.last_var__agl__pacman = copy.deepcopy(var__agl__pacman)

    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v139".split('[')[0].split('.')[0]):
        action.v139 = temp
    else:
        v139 = temp 


    temp = get_nested_attribute(action, '100', locals())
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v140".split('[')[0].split('.')[0]):
        action.v140 = temp
    else:
        v140 = temp 

    v138 = (v139 , v140); v138 = tuple(v138) if isinstance(v138, np.ndarray) else v138
    if action is not None:
        action.var__agl__pacman.move_relative(v138)
    else:
        var__agl__pacman.move_relative(v138)

    if model is not None:
        v141 = View()
        model.add_object(v141) # add object to model
    else:
        v141 = View(root = root)
    if last_view is not None:
        views.append(last_view)    
    last_view = v141
    root.last_view = last_view

    temp = get_nested_attribute(action, '450', locals())
    if temp is None:
        temp = 450
    if action is not None and hasattr(action, "v142".split('[')[0].split('.')[0]):
        action.v142 = temp
    else:
        v142 = temp 

    v143 = - np.array(v142)

    temp = get_nested_attribute(action, 'v143', locals())
    if temp is None:
        temp = v143
    if action is not None and hasattr(action, "v144".split('[')[0].split('.')[0]):
        action.v144 = temp
    else:
        v144 = temp 


    temp = get_nested_attribute(action, 'v144', locals())
    if temp is None:
        temp = v144
    if action is not None and hasattr(action, "v145".split('[')[0].split('.')[0]):
        action.v145 = temp
    else:
        v145 = temp 


    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v146".split('[')[0].split('.')[0]):
        action.v146 = temp
    else:
        v146 = temp 


    temp = get_nested_attribute(action, 'v146', locals())
    if temp is None:
        temp = v146
    if action is not None and hasattr(action, "v147".split('[')[0].split('.')[0]):
        action.v147 = temp
    else:
        v147 = temp 


    temp = get_nested_attribute(action, 'v147', locals())
    if temp is None:
        temp = v147
    if action is not None and hasattr(action, "v148".split('[')[0].split('.')[0]):
        action.v148 = temp
    else:
        v148 = temp 


    temp = get_nested_attribute(action, '200', locals())
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v149".split('[')[0].split('.')[0]):
        action.v149 = temp
    else:
        v149 = temp 


    temp = get_nested_attribute(action, 'v149', locals())
    if temp is None:
        temp = v149
    if action is not None and hasattr(action, "v150".split('[')[0].split('.')[0]):
        action.v150 = temp
    else:
        v150 = temp 


    temp = get_nested_attribute(action, 'v150', locals())
    if temp is None:
        temp = v150
    if action is not None and hasattr(action, "v151".split('[')[0].split('.')[0]):
        action.v151 = temp
    else:
        v151 = temp 


    temp = get_nested_attribute(action, '200', locals())
    if temp is None:
        temp = 200
    if action is not None and hasattr(action, "v152".split('[')[0].split('.')[0]):
        action.v152 = temp
    else:
        v152 = temp 


    temp = get_nested_attribute(action, 'v152', locals())
    if temp is None:
        temp = v152
    if action is not None and hasattr(action, "v153".split('[')[0].split('.')[0]):
        action.v153 = temp
    else:
        v153 = temp 


    temp = get_nested_attribute(action, 'v153', locals())
    if temp is None:
        temp = v153
    if action is not None and hasattr(action, "v154".split('[')[0].split('.')[0]):
        action.v154 = temp
    else:
        v154 = temp 


    temp = get_nested_attribute(action, '"2"', locals())
    if temp is None:
        temp = "2"
    if action is not None and hasattr(action, "v155".split('[')[0].split('.')[0]):
        action.v155 = temp
    else:
        v155 = temp 


    temp = get_nested_attribute(action, 'v155', locals())
    if temp is None:
        temp = v155
    if action is not None and hasattr(action, "v156".split('[')[0].split('.')[0]):
        action.v156 = temp
    else:
        v156 = temp 


    temp = get_nested_attribute(action, 'v156', locals())
    if temp is None:
        temp = v156
    if action is not None and hasattr(action, "v157".split('[')[0].split('.')[0]):
        action.v157 = temp
    else:
        v157 = temp 


    temp = get_nested_attribute(action, '"alice blue"', locals())
    if temp is None:
        temp = "alice blue"
    if action is not None and hasattr(action, "v158".split('[')[0].split('.')[0]):
        action.v158 = temp
    else:
        v158 = temp 


    temp = get_nested_attribute(action, 'v158', locals())
    if temp is None:
        temp = v158
    if action is not None and hasattr(action, "v159".split('[')[0].split('.')[0]):
        action.v159 = temp
    else:
        v159 = temp 


    temp = get_nested_attribute(action, 'v159', locals())
    if temp is None:
        temp = v159
    if action is not None and hasattr(action, "v160".split('[')[0].split('.')[0]):
        action.v160 = temp
    else:
        v160 = temp 


    if action is not None:
        action.v141.Ox = v145
        action.v141.Oy = v148
        action.v141.width = v151
        action.v141.height = v154
        action.v141.title = v157
        action.v141.background = v160
    else:
        v141.Ox = v145
        v141.Oy = v148
        v141.width = v151
        v141.height = v154
        v141.title = v157
        v141.background = v160

    temp = get_nested_attribute(action, 'v141', locals())
    if temp is None:
        temp = v141
    if action is not None and hasattr(action, "var__agl__view2".split('[')[0].split('.')[0]):
        action.var__agl__view2 = temp
    else:
        var__agl__view2 = temp 
    if model is not None: 
        model.var__agl__view2 = var__agl__view2
        model.last_var__agl__view2 = copy.deepcopy(var__agl__view2)

    temp = get_nested_attribute(action, 'var__agl__pacman.origin', locals())
    if temp is None:
        temp = var__agl__pacman.origin
    if action is not None and hasattr(action, "v161".split('[')[0].split('.')[0]):
        action.v161 = temp
    else:
        v161 = temp 

    if action is not None:
        action.var__agl__view2.move_absolute(v161)
    else:
        var__agl__view2.move_absolute(v161)

    temp = get_nested_attribute(action, '650', locals())
    if temp is None:
        temp = 650
    if action is not None and hasattr(action, "v163".split('[')[0].split('.')[0]):
        action.v163 = temp
    else:
        v163 = temp 

    v164 = - np.array(v163)

    temp = get_nested_attribute(action, '100', locals())
    if temp is None:
        temp = 100
    if action is not None and hasattr(action, "v165".split('[')[0].split('.')[0]):
        action.v165 = temp
    else:
        v165 = temp 

    v166 = - np.array(v165)
    v162 = (v164 , v166); v162 = tuple(v162) if isinstance(v162, np.ndarray) else v162


    v167 = copy.deepcopy(var__agl__pacman)
    v167.move_absolute(v162)  
    root.add_object(v167) 


    temp = get_nested_attribute(action, 'v167', locals())
    if temp is None:
        temp = v167
    if action is not None and hasattr(action, "v168".split('[')[0].split('.')[0]):
        action.v168 = temp
    else:
        v168 = temp 


    temp = get_nested_attribute(action, 'v168', locals())
    if temp is None:
        temp = v168
    if action is not None and hasattr(action, "v169".split('[')[0].split('.')[0]):
        action.v169 = temp
    else:
        v169 = temp 


    temp = get_nested_attribute(action, 'v169', locals())
    if temp is None:
        temp = v169
    if action is not None and hasattr(action, "var__agl__pacman2".split('[')[0].split('.')[0]):
        action.var__agl__pacman2 = temp
    else:
        var__agl__pacman2 = temp 
    if model is not None: 
        model.var__agl__pacman2 = var__agl__pacman2
        model.last_var__agl__pacman2 = copy.deepcopy(var__agl__pacman2)

    temp = get_nested_attribute(action, '"wheat"', locals())
    if temp is None:
        temp = "wheat"
    if action is not None and hasattr(action, "v170".split('[')[0].split('.')[0]):
        action.v170 = temp
    else:
        v170 = temp 


    temp = get_nested_attribute(action, 'v170', locals())
    if temp is None:
        temp = v170
    if action is not None and hasattr(action, "v171".split('[')[0].split('.')[0]):
        action.v171 = temp
    else:
        v171 = temp 


    temp = get_nested_attribute(action, 'v171', locals())
    if temp is None:
        temp = v171
    if action is not None and hasattr(action, "var__agl__pacman2.var__agl__face.fill".split('[')[0].split('.')[0]):
        action.var__agl__pacman2.var__agl__face.fill = temp
    else:
        var__agl__pacman2.var__agl__face.fill = temp 

    last_refresh = time.time()
    var__agl__view.update()

    last_refresh = time.time()
    var__agl__view2.update()


    temp = get_nested_attribute(action, '"Press any mouse button to start the first animation"', locals())
    if temp is None:
        temp = "Press any mouse button to start the first animation"
    if action is not None and hasattr(action, "v172".split('[')[0].split('.')[0]):
        action.v172 = temp
    else:
        v172 = temp 

    print(v172)
    v173 = root.waitClick()

    temp = get_nested_attribute(action, 'v173', locals())
    if temp is None:
        temp = v173
    if action is not None and hasattr(action, "v174".split('[')[0].split('.')[0]):
        action.v174 = temp
    else:
        v174 = temp 


    temp = get_nested_attribute(action, 'v174', locals())
    if temp is None:
        temp = v174
    if action is not None and hasattr(action, "v175".split('[')[0].split('.')[0]):
        action.v175 = temp
    else:
        v175 = temp 


    temp = get_nested_attribute(action, 'v175', locals())
    if temp is None:
        temp = v175
    if action is not None and hasattr(action, "var__agl__pos".split('[')[0].split('.')[0]):
        action.var__agl__pos = temp
    else:
        var__agl__pos = temp 
    if model is not None: 
        model.var__agl__pos = var__agl__pos
        model.last_var__agl__pos = copy.deepcopy(var__agl__pos)

    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v176".split('[')[0].split('.')[0]):
        action.v176 = temp
    else:
        v176 = temp 


    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v177".split('[')[0].split('.')[0]):
        action.v177 = temp
    else:
        v177 = temp 


    temp = get_nested_attribute(action, '13', locals())
    if temp is None:
        temp = 13
    if action is not None and hasattr(action, "v178".split('[')[0].split('.')[0]):
        action.v178 = temp
    else:
        v178 = temp 


    temp = get_nested_attribute(action, '13', locals())
    if temp is None:
        temp = 13
    if action is not None and hasattr(action, "v179".split('[')[0].split('.')[0]):
        action.v179 = temp
    else:
        v179 = temp 

    v180 = (v179*math.cos(math.radians(v177)) , v179*math.sin(math.radians(v177))); v180 = tuple(v180) if isinstance(v180, np.ndarray) else v180

    temp = get_nested_attribute(action, 'v180', locals())
    if temp is None:
        temp = v180
    if action is not None and hasattr(action, "v181".split('[')[0].split('.')[0]):
        action.v181 = temp
    else:
        v181 = temp 


    temp = get_nested_attribute(action, 'v181', locals())
    if temp is None:
        temp = v181
    if action is not None and hasattr(action, "v182".split('[')[0].split('.')[0]):
        action.v182 = temp
    else:
        v182 = temp 


    temp = get_nested_attribute(action, 'v182', locals())
    if temp is None:
        temp = v182
    if action is not None and hasattr(action, "var__agl__walk_vector".split('[')[0].split('.')[0]):
        action.var__agl__walk_vector = temp
    else:
        var__agl__walk_vector = temp 
    if model is not None: 
        model.var__agl__walk_vector = var__agl__walk_vector
        model.last_var__agl__walk_vector = copy.deepcopy(var__agl__walk_vector)

    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v185".split('[')[0].split('.')[0]):
        action.v185 = temp
    else:
        v185 = temp 


    temp = get_nested_attribute(action, 'var__agl__pacman.origin[v185]', locals())
    if temp is None:
        temp = var__agl__pacman.origin[v185]
    if action is not None and hasattr(action, "v184".split('[')[0].split('.')[0]):
        action.v184 = temp
    else:
        v184 = temp 


    temp = get_nested_attribute(action, '650', locals())
    if temp is None:
        temp = 650
    if action is not None and hasattr(action, "v186".split('[')[0].split('.')[0]):
        action.v186 = temp
    else:
        v186 = temp 

    v183 = np.array(v184) >= np.array(v186); v183 = tuple(v183) if isinstance(v183, np.ndarray) else v183
    while True:

        temp = get_nested_attribute(action, 'var__agl__Close', locals())
        if temp is None:
            temp = var__agl__Close
        if action is not None and hasattr(action, "v187".split('[')[0].split('.')[0]):
            action.v187 = temp
        else:
            v187 = temp 


        temp = get_nested_attribute(action, 'v187', locals())
        if temp is None:
            temp = v187
        if action is not None and hasattr(action, "v188".split('[')[0].split('.')[0]):
            action.v188 = temp
        else:
            v188 = temp 


        temp = get_nested_attribute(action, 'v188', locals())
        if temp is None:
            temp = v188
        if action is not None and hasattr(action, "var__agl__pacman.var__agl__mouth".split('[')[0].split('.')[0]):
            action.var__agl__pacman.var__agl__mouth = temp
        else:
            var__agl__pacman.var__agl__mouth = temp 


        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v189".split('[')[0].split('.')[0]):
            action.v189 = temp
        else:
            v189 = temp 

         
        while (time.time() - last_refresh <= v189/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        var__agl__view.update()

        last_refresh = time.time()
        var__agl__view2.update()


        temp = get_nested_attribute(action, 'var__agl__Open', locals())
        if temp is None:
            temp = var__agl__Open
        if action is not None and hasattr(action, "v190".split('[')[0].split('.')[0]):
            action.v190 = temp
        else:
            v190 = temp 


        temp = get_nested_attribute(action, 'v190', locals())
        if temp is None:
            temp = v190
        if action is not None and hasattr(action, "v191".split('[')[0].split('.')[0]):
            action.v191 = temp
        else:
            v191 = temp 


        temp = get_nested_attribute(action, 'v191', locals())
        if temp is None:
            temp = v191
        if action is not None and hasattr(action, "var__agl__pacman.var__agl__mouth".split('[')[0].split('.')[0]):
            action.var__agl__pacman.var__agl__mouth = temp
        else:
            var__agl__pacman.var__agl__mouth = temp 


        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v192".split('[')[0].split('.')[0]):
            action.v192 = temp
        else:
            v192 = temp 

         
        while (time.time() - last_refresh <= v192/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        var__agl__view.update()

        last_refresh = time.time()
        var__agl__view2.update()


        temp = get_nested_attribute(action, 'var__agl__walk_vector', locals())
        if temp is None:
            temp = var__agl__walk_vector
        if action is not None and hasattr(action, "v193".split('[')[0].split('.')[0]):
            action.v193 = temp
        else:
            v193 = temp 

        if action is not None:
            action.var__agl__pacman.move_relative(v193)
        else:
            var__agl__pacman.move_relative(v193)

        temp = get_nested_attribute(action, 'var__agl__walk_vector', locals())
        if temp is None:
            temp = var__agl__walk_vector
        if action is not None and hasattr(action, "v194".split('[')[0].split('.')[0]):
            action.v194 = temp
        else:
            v194 = temp 

        if action is not None:
            action.var__agl__view2.move_relative(v194)
        else:
            var__agl__view2.move_relative(v194)

        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v195".split('[')[0].split('.')[0]):
            action.v195 = temp
        else:
            v195 = temp 

         
        while (time.time() - last_refresh <= v195/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        var__agl__view.update()

        last_refresh = time.time()
        var__agl__view2.update()


        temp = get_nested_attribute(action, 'var__agl__pacman.origin', locals())
        if temp is None:
            temp = var__agl__pacman.origin
        if action is not None and hasattr(action, "v196".split('[')[0].split('.')[0]):
            action.v196 = temp
        else:
            v196 = temp 

        print(v196)
        # refresh the condition

        temp = get_nested_attribute(action, '0', locals())
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v185".split('[')[0].split('.')[0]):
            action.v185 = temp
        else:
            v185 = temp 


        temp = get_nested_attribute(action, 'var__agl__pacman.origin[v185]', locals())
        if temp is None:
            temp = var__agl__pacman.origin[v185]
        if action is not None and hasattr(action, "v184".split('[')[0].split('.')[0]):
            action.v184 = temp
        else:
            v184 = temp 


        temp = get_nested_attribute(action, '650', locals())
        if temp is None:
            temp = 650
        if action is not None and hasattr(action, "v186".split('[')[0].split('.')[0]):
            action.v186 = temp
        else:
            v186 = temp 

        v183 = np.array(v184) >= np.array(v186); v183 = tuple(v183) if isinstance(v183, np.ndarray) else v183
        ##
        if v183:
            break   # Repeat until condition is false

    temp = get_nested_attribute(action, '"Press any mouse button to start the second animation"', locals())
    if temp is None:
        temp = "Press any mouse button to start the second animation"
    if action is not None and hasattr(action, "v197".split('[')[0].split('.')[0]):
        action.v197 = temp
    else:
        v197 = temp 

    print(v197)
    v198 = root.waitClick()

    temp = get_nested_attribute(action, 'v198', locals())
    if temp is None:
        temp = v198
    if action is not None and hasattr(action, "v199".split('[')[0].split('.')[0]):
        action.v199 = temp
    else:
        v199 = temp 


    temp = get_nested_attribute(action, 'v199', locals())
    if temp is None:
        temp = v199
    if action is not None and hasattr(action, "v200".split('[')[0].split('.')[0]):
        action.v200 = temp
    else:
        v200 = temp 


    temp = get_nested_attribute(action, 'v200', locals())
    if temp is None:
        temp = v200
    if action is not None and hasattr(action, "var__agl__pos".split('[')[0].split('.')[0]):
        action.var__agl__pos = temp
    else:
        var__agl__pos = temp 
    if model is not None: 
        model.var__agl__pos = var__agl__pos
        model.last_var__agl__pos = copy.deepcopy(var__agl__pos)

    temp = get_nested_attribute(action, 'var__agl__pacman2.origin', locals())
    if temp is None:
        temp = var__agl__pacman2.origin
    if action is not None and hasattr(action, "v201".split('[')[0].split('.')[0]):
        action.v201 = temp
    else:
        v201 = temp 

    if action is not None:
        action.var__agl__view2.move_absolute(v201)
    else:
        var__agl__view2.move_absolute(v201)
    last_refresh = time.time()
    var__agl__view.update()

    last_refresh = time.time()
    var__agl__view2.update()


    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v204".split('[')[0].split('.')[0]):
        action.v204 = temp
    else:
        v204 = temp 


    temp = get_nested_attribute(action, 'var__agl__pacman2.origin[v204]', locals())
    if temp is None:
        temp = var__agl__pacman2.origin[v204]
    if action is not None and hasattr(action, "v203".split('[')[0].split('.')[0]):
        action.v203 = temp
    else:
        v203 = temp 


    temp = get_nested_attribute(action, '650', locals())
    if temp is None:
        temp = 650
    if action is not None and hasattr(action, "v205".split('[')[0].split('.')[0]):
        action.v205 = temp
    else:
        v205 = temp 

    v202 = np.array(v203) >= np.array(v205); v202 = tuple(v202) if isinstance(v202, np.ndarray) else v202
    while True:

        temp = get_nested_attribute(action, 'var__agl__Close', locals())
        if temp is None:
            temp = var__agl__Close
        if action is not None and hasattr(action, "v206".split('[')[0].split('.')[0]):
            action.v206 = temp
        else:
            v206 = temp 


        temp = get_nested_attribute(action, 'v206', locals())
        if temp is None:
            temp = v206
        if action is not None and hasattr(action, "v207".split('[')[0].split('.')[0]):
            action.v207 = temp
        else:
            v207 = temp 


        temp = get_nested_attribute(action, 'v207', locals())
        if temp is None:
            temp = v207
        if action is not None and hasattr(action, "var__agl__pacman2.var__agl__mouth".split('[')[0].split('.')[0]):
            action.var__agl__pacman2.var__agl__mouth = temp
        else:
            var__agl__pacman2.var__agl__mouth = temp 


        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v208".split('[')[0].split('.')[0]):
            action.v208 = temp
        else:
            v208 = temp 

         
        while (time.time() - last_refresh <= v208/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        var__agl__view.update()

        last_refresh = time.time()
        var__agl__view2.update()


        temp = get_nested_attribute(action, 'var__agl__Open', locals())
        if temp is None:
            temp = var__agl__Open
        if action is not None and hasattr(action, "v209".split('[')[0].split('.')[0]):
            action.v209 = temp
        else:
            v209 = temp 


        temp = get_nested_attribute(action, 'v209', locals())
        if temp is None:
            temp = v209
        if action is not None and hasattr(action, "v210".split('[')[0].split('.')[0]):
            action.v210 = temp
        else:
            v210 = temp 


        temp = get_nested_attribute(action, 'v210', locals())
        if temp is None:
            temp = v210
        if action is not None and hasattr(action, "var__agl__pacman2.var__agl__mouth".split('[')[0].split('.')[0]):
            action.var__agl__pacman2.var__agl__mouth = temp
        else:
            var__agl__pacman2.var__agl__mouth = temp 


        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v211".split('[')[0].split('.')[0]):
            action.v211 = temp
        else:
            v211 = temp 

         
        while (time.time() - last_refresh <= v211/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        var__agl__view.update()

        last_refresh = time.time()
        var__agl__view2.update()


        temp = get_nested_attribute(action, 'var__agl__walk_vector', locals())
        if temp is None:
            temp = var__agl__walk_vector
        if action is not None and hasattr(action, "v212".split('[')[0].split('.')[0]):
            action.v212 = temp
        else:
            v212 = temp 

        if action is not None:
            action.var__agl__pacman2.move_relative(v212)
        else:
            var__agl__pacman2.move_relative(v212)

        temp = get_nested_attribute(action, 'var__agl__walk_vector', locals())
        if temp is None:
            temp = var__agl__walk_vector
        if action is not None and hasattr(action, "v213".split('[')[0].split('.')[0]):
            action.v213 = temp
        else:
            v213 = temp 

        if action is not None:
            action.var__agl__view2.move_relative(v213)
        else:
            var__agl__view2.move_relative(v213)

        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v214".split('[')[0].split('.')[0]):
            action.v214 = temp
        else:
            v214 = temp 

         
        while (time.time() - last_refresh <= v214/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        var__agl__view.update()

        last_refresh = time.time()
        var__agl__view2.update()

        # refresh the condition

        temp = get_nested_attribute(action, '0', locals())
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v204".split('[')[0].split('.')[0]):
            action.v204 = temp
        else:
            v204 = temp 


        temp = get_nested_attribute(action, 'var__agl__pacman2.origin[v204]', locals())
        if temp is None:
            temp = var__agl__pacman2.origin[v204]
        if action is not None and hasattr(action, "v203".split('[')[0].split('.')[0]):
            action.v203 = temp
        else:
            v203 = temp 


        temp = get_nested_attribute(action, '650', locals())
        if temp is None:
            temp = 650
        if action is not None and hasattr(action, "v205".split('[')[0].split('.')[0]):
            action.v205 = temp
        else:
            v205 = temp 

        v202 = np.array(v203) >= np.array(v205); v202 = tuple(v202) if isinstance(v202, np.ndarray) else v202
        ##
        if v202:
            break   # Repeat until condition is false

    temp = get_nested_attribute(action, '"Press any mouse button to rotate the pacmans"', locals())
    if temp is None:
        temp = "Press any mouse button to rotate the pacmans"
    if action is not None and hasattr(action, "v215".split('[')[0].split('.')[0]):
        action.v215 = temp
    else:
        v215 = temp 

    print(v215)
    v216 = root.waitClick()

    temp = get_nested_attribute(action, 'v216', locals())
    if temp is None:
        temp = v216
    if action is not None and hasattr(action, "v217".split('[')[0].split('.')[0]):
        action.v217 = temp
    else:
        v217 = temp 


    temp = get_nested_attribute(action, 'v217', locals())
    if temp is None:
        temp = v217
    if action is not None and hasattr(action, "v218".split('[')[0].split('.')[0]):
        action.v218 = temp
    else:
        v218 = temp 


    temp = get_nested_attribute(action, 'v218', locals())
    if temp is None:
        temp = v218
    if action is not None and hasattr(action, "var__agl__pos".split('[')[0].split('.')[0]):
        action.var__agl__pos = temp
    else:
        var__agl__pos = temp 
    if model is not None: 
        model.var__agl__pos = var__agl__pos
        model.last_var__agl__pos = copy.deepcopy(var__agl__pos)

    temp = get_nested_attribute(action, '180', locals())
    if temp is None:
        temp = 180
    if action is not None and hasattr(action, "v219".split('[')[0].split('.')[0]):
        action.v219 = temp
    else:
        v219 = temp 

    if action is not None:
        action.var__agl__pacman.rotate(v219)
    else:
        var__agl__pacman.rotate(v219)

    temp = get_nested_attribute(action, '180', locals())
    if temp is None:
        temp = 180
    if action is not None and hasattr(action, "v220".split('[')[0].split('.')[0]):
        action.v220 = temp
    else:
        v220 = temp 

    if action is not None:
        action.var__agl__pacman2.rotate(v220)
    else:
        var__agl__pacman2.rotate(v220)

    temp = get_nested_attribute(action, 'var__agl__walk_vector', locals())
    if temp is None:
        temp = var__agl__walk_vector
    if action is not None and hasattr(action, "v221".split('[')[0].split('.')[0]):
        action.v221 = temp
    else:
        v221 = temp 

    v222 = - np.array(v221)

    temp = get_nested_attribute(action, 'v222', locals())
    if temp is None:
        temp = v222
    if action is not None and hasattr(action, "v223".split('[')[0].split('.')[0]):
        action.v223 = temp
    else:
        v223 = temp 


    temp = get_nested_attribute(action, 'v223', locals())
    if temp is None:
        temp = v223
    if action is not None and hasattr(action, "var__agl__walk_vector".split('[')[0].split('.')[0]):
        action.var__agl__walk_vector = temp
    else:
        var__agl__walk_vector = temp 

    last_refresh = time.time()
    var__agl__view.update()

    last_refresh = time.time()
    var__agl__view2.update()


    temp = get_nested_attribute(action, '"Press any mouse button to start the third animation"', locals())
    if temp is None:
        temp = "Press any mouse button to start the third animation"
    if action is not None and hasattr(action, "v224".split('[')[0].split('.')[0]):
        action.v224 = temp
    else:
        v224 = temp 

    print(v224)
    v225 = root.waitClick()

    temp = get_nested_attribute(action, 'v225', locals())
    if temp is None:
        temp = v225
    if action is not None and hasattr(action, "v226".split('[')[0].split('.')[0]):
        action.v226 = temp
    else:
        v226 = temp 


    temp = get_nested_attribute(action, 'v226', locals())
    if temp is None:
        temp = v226
    if action is not None and hasattr(action, "v227".split('[')[0].split('.')[0]):
        action.v227 = temp
    else:
        v227 = temp 


    temp = get_nested_attribute(action, 'v227', locals())
    if temp is None:
        temp = v227
    if action is not None and hasattr(action, "var__agl__pos".split('[')[0].split('.')[0]):
        action.var__agl__pos = temp
    else:
        var__agl__pos = temp 
    if model is not None: 
        model.var__agl__pos = var__agl__pos
        model.last_var__agl__pos = copy.deepcopy(var__agl__pos)

    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v230".split('[')[0].split('.')[0]):
        action.v230 = temp
    else:
        v230 = temp 


    temp = get_nested_attribute(action, 'var__agl__pacman2.origin[v230]', locals())
    if temp is None:
        temp = var__agl__pacman2.origin[v230]
    if action is not None and hasattr(action, "v229".split('[')[0].split('.')[0]):
        action.v229 = temp
    else:
        v229 = temp 


    temp = get_nested_attribute(action, '650', locals())
    if temp is None:
        temp = 650
    if action is not None and hasattr(action, "v231".split('[')[0].split('.')[0]):
        action.v231 = temp
    else:
        v231 = temp 

    v232 = - np.array(v231)
    v228 = np.array(v229) <= np.array(v232); v228 = tuple(v228) if isinstance(v228, np.ndarray) else v228
    while True:

        temp = get_nested_attribute(action, 'var__agl__Close', locals())
        if temp is None:
            temp = var__agl__Close
        if action is not None and hasattr(action, "v233".split('[')[0].split('.')[0]):
            action.v233 = temp
        else:
            v233 = temp 


        temp = get_nested_attribute(action, 'v233', locals())
        if temp is None:
            temp = v233
        if action is not None and hasattr(action, "v234".split('[')[0].split('.')[0]):
            action.v234 = temp
        else:
            v234 = temp 


        temp = get_nested_attribute(action, 'v234', locals())
        if temp is None:
            temp = v234
        if action is not None and hasattr(action, "var__agl__pacman2.var__agl__mouth".split('[')[0].split('.')[0]):
            action.var__agl__pacman2.var__agl__mouth = temp
        else:
            var__agl__pacman2.var__agl__mouth = temp 


        temp = get_nested_attribute(action, 'var__agl__Close', locals())
        if temp is None:
            temp = var__agl__Close
        if action is not None and hasattr(action, "v235".split('[')[0].split('.')[0]):
            action.v235 = temp
        else:
            v235 = temp 


        temp = get_nested_attribute(action, 'v235', locals())
        if temp is None:
            temp = v235
        if action is not None and hasattr(action, "v236".split('[')[0].split('.')[0]):
            action.v236 = temp
        else:
            v236 = temp 


        temp = get_nested_attribute(action, 'v236', locals())
        if temp is None:
            temp = v236
        if action is not None and hasattr(action, "var__agl__pacman.var__agl__mouth".split('[')[0].split('.')[0]):
            action.var__agl__pacman.var__agl__mouth = temp
        else:
            var__agl__pacman.var__agl__mouth = temp 


        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v237".split('[')[0].split('.')[0]):
            action.v237 = temp
        else:
            v237 = temp 

         
        while (time.time() - last_refresh <= v237/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        var__agl__view.update()

        last_refresh = time.time()
        var__agl__view2.update()


        temp = get_nested_attribute(action, 'var__agl__Open', locals())
        if temp is None:
            temp = var__agl__Open
        if action is not None and hasattr(action, "v238".split('[')[0].split('.')[0]):
            action.v238 = temp
        else:
            v238 = temp 


        temp = get_nested_attribute(action, 'v238', locals())
        if temp is None:
            temp = v238
        if action is not None and hasattr(action, "v239".split('[')[0].split('.')[0]):
            action.v239 = temp
        else:
            v239 = temp 


        temp = get_nested_attribute(action, 'v239', locals())
        if temp is None:
            temp = v239
        if action is not None and hasattr(action, "var__agl__pacman2.var__agl__mouth".split('[')[0].split('.')[0]):
            action.var__agl__pacman2.var__agl__mouth = temp
        else:
            var__agl__pacman2.var__agl__mouth = temp 


        temp = get_nested_attribute(action, 'var__agl__Open', locals())
        if temp is None:
            temp = var__agl__Open
        if action is not None and hasattr(action, "v240".split('[')[0].split('.')[0]):
            action.v240 = temp
        else:
            v240 = temp 


        temp = get_nested_attribute(action, 'v240', locals())
        if temp is None:
            temp = v240
        if action is not None and hasattr(action, "v241".split('[')[0].split('.')[0]):
            action.v241 = temp
        else:
            v241 = temp 


        temp = get_nested_attribute(action, 'v241', locals())
        if temp is None:
            temp = v241
        if action is not None and hasattr(action, "var__agl__pacman.var__agl__mouth".split('[')[0].split('.')[0]):
            action.var__agl__pacman.var__agl__mouth = temp
        else:
            var__agl__pacman.var__agl__mouth = temp 


        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v242".split('[')[0].split('.')[0]):
            action.v242 = temp
        else:
            v242 = temp 

         
        while (time.time() - last_refresh <= v242/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        var__agl__view.update()

        last_refresh = time.time()
        var__agl__view2.update()


        temp = get_nested_attribute(action, 'var__agl__walk_vector', locals())
        if temp is None:
            temp = var__agl__walk_vector
        if action is not None and hasattr(action, "v243".split('[')[0].split('.')[0]):
            action.v243 = temp
        else:
            v243 = temp 

        if action is not None:
            action.var__agl__pacman2.move_relative(v243)
        else:
            var__agl__pacman2.move_relative(v243)

        temp = get_nested_attribute(action, 'var__agl__walk_vector', locals())
        if temp is None:
            temp = var__agl__walk_vector
        if action is not None and hasattr(action, "v244".split('[')[0].split('.')[0]):
            action.v244 = temp
        else:
            v244 = temp 

        if action is not None:
            action.var__agl__pacman.move_relative(v244)
        else:
            var__agl__pacman.move_relative(v244)

        temp = get_nested_attribute(action, 'var__agl__walk_vector', locals())
        if temp is None:
            temp = var__agl__walk_vector
        if action is not None and hasattr(action, "v245".split('[')[0].split('.')[0]):
            action.v245 = temp
        else:
            v245 = temp 

        if action is not None:
            action.var__agl__view2.move_relative(v245)
        else:
            var__agl__view2.move_relative(v245)

        temp = get_nested_attribute(action, '1', locals())
        if temp is None:
            temp = 1
        if action is not None and hasattr(action, "v246".split('[')[0].split('.')[0]):
            action.v246 = temp
        else:
            v246 = temp 

         
        while (time.time() - last_refresh <= v246/1000):
            time.sleep(REFRESH_RATE)   

        last_refresh = time.time()
        var__agl__view.update()

        last_refresh = time.time()
        var__agl__view2.update()

        # refresh the condition

        temp = get_nested_attribute(action, '0', locals())
        if temp is None:
            temp = 0
        if action is not None and hasattr(action, "v230".split('[')[0].split('.')[0]):
            action.v230 = temp
        else:
            v230 = temp 


        temp = get_nested_attribute(action, 'var__agl__pacman2.origin[v230]', locals())
        if temp is None:
            temp = var__agl__pacman2.origin[v230]
        if action is not None and hasattr(action, "v229".split('[')[0].split('.')[0]):
            action.v229 = temp
        else:
            v229 = temp 


        temp = get_nested_attribute(action, '650', locals())
        if temp is None:
            temp = 650
        if action is not None and hasattr(action, "v231".split('[')[0].split('.')[0]):
            action.v231 = temp
        else:
            v231 = temp 

        v232 = - np.array(v231)
        v228 = np.array(v229) <= np.array(v232); v228 = tuple(v228) if isinstance(v228, np.ndarray) else v228
        ##
        if v228:
            break   # Repeat until condition is false

    temp = get_nested_attribute(action, '"Press any mouse button to quit"', locals())
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v247".split('[')[0].split('.')[0]):
        action.v247 = temp
    else:
        v247 = temp 

    print(v247)
    v248 = root.waitClick()

    temp = get_nested_attribute(action, 'v248', locals())
    if temp is None:
        temp = v248
    if action is not None and hasattr(action, "v249".split('[')[0].split('.')[0]):
        action.v249 = temp
    else:
        v249 = temp 


    temp = get_nested_attribute(action, 'v249', locals())
    if temp is None:
        temp = v249
    if action is not None and hasattr(action, "v250".split('[')[0].split('.')[0]):
        action.v250 = temp
    else:
        v250 = temp 


    temp = get_nested_attribute(action, 'v250', locals())
    if temp is None:
        temp = v250
    if action is not None and hasattr(action, "var__agl__pos".split('[')[0].split('.')[0]):
        action.var__agl__pos = temp
    else:
        var__agl__pos = temp 
    if model is not None: 
        model.var__agl__pos = var__agl__pos
        model.last_var__agl__pos = copy.deepcopy(var__agl__pos)

    var__agl__view2.close(); views.remove(var__agl__view2) if last_view != var__agl__view2 else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == var__agl__view2 else last_view
    root.last_view = last_view

    temp = get_nested_attribute(action, '"Press any mouse button to quit"', locals())
    if temp is None:
        temp = "Press any mouse button to quit"
    if action is not None and hasattr(action, "v251".split('[')[0].split('.')[0]):
        action.v251 = temp
    else:
        v251 = temp 

    print(v251)
    v252 = root.waitClick()

    temp = get_nested_attribute(action, 'v252', locals())
    if temp is None:
        temp = v252
    if action is not None and hasattr(action, "v253".split('[')[0].split('.')[0]):
        action.v253 = temp
    else:
        v253 = temp 


    temp = get_nested_attribute(action, 'v253', locals())
    if temp is None:
        temp = v253
    if action is not None and hasattr(action, "var__agl__pos".split('[')[0].split('.')[0]):
        action.var__agl__pos = temp
    else:
        var__agl__pos = temp 

    var__agl__view.close(); views.remove(var__agl__view) if last_view != var__agl__view else None
    last_view = (views.pop(-1) if len(views) > 0 else None) if last_view == var__agl__view else last_view
    root.last_view = last_view
