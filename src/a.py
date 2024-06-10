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


    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v1".split('[')[0].split('.')[0]):
        action.v1 = temp
    else:
        v1 = temp 


    temp = get_nested_attribute(action, '2', locals())
    if temp is None:
        temp = 2
    if action is not None and hasattr(action, "v2".split('[')[0].split('.')[0]):
        action.v2 = temp
    else:
        v2 = temp 


    temp = get_nested_attribute(action, '3', locals())
    if temp is None:
        temp = 3
    if action is not None and hasattr(action, "v3".split('[')[0].split('.')[0]):
        action.v3 = temp
    else:
        v3 = temp 


    temp = get_nested_attribute(action, '4', locals())
    if temp is None:
        temp = 4
    if action is not None and hasattr(action, "v4".split('[')[0].split('.')[0]):
        action.v4 = temp
    else:
        v4 = temp 


    temp = get_nested_attribute(action, '5', locals())
    if temp is None:
        temp = 5
    if action is not None and hasattr(action, "v5".split('[')[0].split('.')[0]):
        action.v5 = temp
    else:
        v5 = temp 

    v0 = [v1,v2,v3,v4,v5]

    temp = get_nested_attribute(action, 'v0', locals())
    if temp is None:
        temp = v0
    if action is not None and hasattr(action, "v6".split('[')[0].split('.')[0]):
        action.v6 = temp
    else:
        v6 = temp 


    temp = get_nested_attribute(action, 'v6', locals())
    if temp is None:
        temp = v6
    if action is not None and hasattr(action, "v7".split('[')[0].split('.')[0]):
        action.v7 = temp
    else:
        v7 = temp 


    temp = get_nested_attribute(action, 'v7', locals())
    if temp is None:
        temp = v7
    if action is not None and hasattr(action, "var__agl__a".split('[')[0].split('.')[0]):
        action.var__agl__a = temp
    else:
        var__agl__a = temp 
    if model is not None: 
        model.var__agl__a = var__agl__a
        model.last_var__agl__a = copy.deepcopy(var__agl__a)

    temp = get_nested_attribute(action, '"a"', locals())
    if temp is None:
        temp = "a"
    if action is not None and hasattr(action, "v9".split('[')[0].split('.')[0]):
        action.v9 = temp
    else:
        v9 = temp 


    temp = get_nested_attribute(action, '"b"', locals())
    if temp is None:
        temp = "b"
    if action is not None and hasattr(action, "v10".split('[')[0].split('.')[0]):
        action.v10 = temp
    else:
        v10 = temp 


    temp = get_nested_attribute(action, '"c"', locals())
    if temp is None:
        temp = "c"
    if action is not None and hasattr(action, "v11".split('[')[0].split('.')[0]):
        action.v11 = temp
    else:
        v11 = temp 


    temp = get_nested_attribute(action, '"d"', locals())
    if temp is None:
        temp = "d"
    if action is not None and hasattr(action, "v12".split('[')[0].split('.')[0]):
        action.v12 = temp
    else:
        v12 = temp 


    temp = get_nested_attribute(action, '"e"', locals())
    if temp is None:
        temp = "e"
    if action is not None and hasattr(action, "v13".split('[')[0].split('.')[0]):
        action.v13 = temp
    else:
        v13 = temp 

    v8 = [v9,v10,v11,v12,v13]

    temp = get_nested_attribute(action, 'v8', locals())
    if temp is None:
        temp = v8
    if action is not None and hasattr(action, "v14".split('[')[0].split('.')[0]):
        action.v14 = temp
    else:
        v14 = temp 


    temp = get_nested_attribute(action, 'v14', locals())
    if temp is None:
        temp = v14
    if action is not None and hasattr(action, "v15".split('[')[0].split('.')[0]):
        action.v15 = temp
    else:
        v15 = temp 


    temp = get_nested_attribute(action, 'v15', locals())
    if temp is None:
        temp = v15
    if action is not None and hasattr(action, "var__agl__b".split('[')[0].split('.')[0]):
        action.var__agl__b = temp
    else:
        var__agl__b = temp 
    if model is not None: 
        model.var__agl__b = var__agl__b
        model.last_var__agl__b = copy.deepcopy(var__agl__b)

    temp = get_nested_attribute(action, '1', locals())
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v19".split('[')[0].split('.')[0]):
        action.v19 = temp
    else:
        v19 = temp 


    temp = get_nested_attribute(action, '2', locals())
    if temp is None:
        temp = 2
    if action is not None and hasattr(action, "v20".split('[')[0].split('.')[0]):
        action.v20 = temp
    else:
        v20 = temp 

    v18 = (v19 , v20); v18 = tuple(v18) if isinstance(v18, np.ndarray) else v18

    temp = get_nested_attribute(action, '3', locals())
    if temp is None:
        temp = 3
    if action is not None and hasattr(action, "v22".split('[')[0].split('.')[0]):
        action.v22 = temp
    else:
        v22 = temp 


    temp = get_nested_attribute(action, '4', locals())
    if temp is None:
        temp = 4
    if action is not None and hasattr(action, "v23".split('[')[0].split('.')[0]):
        action.v23 = temp
    else:
        v23 = temp 

    v21 = (v22 , v23); v21 = tuple(v21) if isinstance(v21, np.ndarray) else v21
    v17 = [v18,v21]

    temp = get_nested_attribute(action, '1', locals())
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v26".split('[')[0].split('.')[0]):
        action.v26 = temp
    else:
        v26 = temp 


    temp = get_nested_attribute(action, '2', locals())
    if temp is None:
        temp = 2
    if action is not None and hasattr(action, "v27".split('[')[0].split('.')[0]):
        action.v27 = temp
    else:
        v27 = temp 

    v25 = (v26 , v27); v25 = tuple(v25) if isinstance(v25, np.ndarray) else v25

    temp = get_nested_attribute(action, '3', locals())
    if temp is None:
        temp = 3
    if action is not None and hasattr(action, "v29".split('[')[0].split('.')[0]):
        action.v29 = temp
    else:
        v29 = temp 


    temp = get_nested_attribute(action, '4', locals())
    if temp is None:
        temp = 4
    if action is not None and hasattr(action, "v30".split('[')[0].split('.')[0]):
        action.v30 = temp
    else:
        v30 = temp 

    v28 = (v29 , v30); v28 = tuple(v28) if isinstance(v28, np.ndarray) else v28
    v24 = [v25,v28]
    v16 = [v17,v24]

    temp = get_nested_attribute(action, 'v16', locals())
    if temp is None:
        temp = v16
    if action is not None and hasattr(action, "v31".split('[')[0].split('.')[0]):
        action.v31 = temp
    else:
        v31 = temp 


    temp = get_nested_attribute(action, 'v31', locals())
    if temp is None:
        temp = v31
    if action is not None and hasattr(action, "v32".split('[')[0].split('.')[0]):
        action.v32 = temp
    else:
        v32 = temp 


    temp = get_nested_attribute(action, 'v32', locals())
    if temp is None:
        temp = v32
    if action is not None and hasattr(action, "var__agl__c".split('[')[0].split('.')[0]):
        action.var__agl__c = temp
    else:
        var__agl__c = temp 
    if model is not None: 
        model.var__agl__c = var__agl__c
        model.last_var__agl__c = copy.deepcopy(var__agl__c)

    temp = get_nested_attribute(action, '1', locals())
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v36".split('[')[0].split('.')[0]):
        action.v36 = temp
    else:
        v36 = temp 


    temp = get_nested_attribute(action, '2', locals())
    if temp is None:
        temp = 2
    if action is not None and hasattr(action, "v37".split('[')[0].split('.')[0]):
        action.v37 = temp
    else:
        v37 = temp 

    v35 = (v36 , v37); v35 = tuple(v35) if isinstance(v35, np.ndarray) else v35

    temp = get_nested_attribute(action, '3', locals())
    if temp is None:
        temp = 3
    if action is not None and hasattr(action, "v39".split('[')[0].split('.')[0]):
        action.v39 = temp
    else:
        v39 = temp 


    temp = get_nested_attribute(action, '4', locals())
    if temp is None:
        temp = 4
    if action is not None and hasattr(action, "v40".split('[')[0].split('.')[0]):
        action.v40 = temp
    else:
        v40 = temp 

    v38 = (v39 , v40); v38 = tuple(v38) if isinstance(v38, np.ndarray) else v38

    temp = get_nested_attribute(action, '5', locals())
    if temp is None:
        temp = 5
    if action is not None and hasattr(action, "v42".split('[')[0].split('.')[0]):
        action.v42 = temp
    else:
        v42 = temp 


    temp = get_nested_attribute(action, '6', locals())
    if temp is None:
        temp = 6
    if action is not None and hasattr(action, "v43".split('[')[0].split('.')[0]):
        action.v43 = temp
    else:
        v43 = temp 

    v41 = (v42 , v43); v41 = tuple(v41) if isinstance(v41, np.ndarray) else v41

    temp = get_nested_attribute(action, '7', locals())
    if temp is None:
        temp = 7
    if action is not None and hasattr(action, "v45".split('[')[0].split('.')[0]):
        action.v45 = temp
    else:
        v45 = temp 


    temp = get_nested_attribute(action, '8', locals())
    if temp is None:
        temp = 8
    if action is not None and hasattr(action, "v46".split('[')[0].split('.')[0]):
        action.v46 = temp
    else:
        v46 = temp 

    v44 = (v45 , v46); v44 = tuple(v44) if isinstance(v44, np.ndarray) else v44

    temp = get_nested_attribute(action, '9', locals())
    if temp is None:
        temp = 9
    if action is not None and hasattr(action, "v48".split('[')[0].split('.')[0]):
        action.v48 = temp
    else:
        v48 = temp 


    temp = get_nested_attribute(action, '10', locals())
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v49".split('[')[0].split('.')[0]):
        action.v49 = temp
    else:
        v49 = temp 

    v47 = (v48 , v49); v47 = tuple(v47) if isinstance(v47, np.ndarray) else v47
    v34 = [v35,v38,v41,v44,v47]

    temp = get_nested_attribute(action, '1', locals())
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v52".split('[')[0].split('.')[0]):
        action.v52 = temp
    else:
        v52 = temp 


    temp = get_nested_attribute(action, '2', locals())
    if temp is None:
        temp = 2
    if action is not None and hasattr(action, "v53".split('[')[0].split('.')[0]):
        action.v53 = temp
    else:
        v53 = temp 

    v51 = (v52 , v53); v51 = tuple(v51) if isinstance(v51, np.ndarray) else v51

    temp = get_nested_attribute(action, '3', locals())
    if temp is None:
        temp = 3
    if action is not None and hasattr(action, "v55".split('[')[0].split('.')[0]):
        action.v55 = temp
    else:
        v55 = temp 


    temp = get_nested_attribute(action, '4', locals())
    if temp is None:
        temp = 4
    if action is not None and hasattr(action, "v56".split('[')[0].split('.')[0]):
        action.v56 = temp
    else:
        v56 = temp 

    v54 = (v55 , v56); v54 = tuple(v54) if isinstance(v54, np.ndarray) else v54

    temp = get_nested_attribute(action, '5', locals())
    if temp is None:
        temp = 5
    if action is not None and hasattr(action, "v58".split('[')[0].split('.')[0]):
        action.v58 = temp
    else:
        v58 = temp 


    temp = get_nested_attribute(action, '6', locals())
    if temp is None:
        temp = 6
    if action is not None and hasattr(action, "v59".split('[')[0].split('.')[0]):
        action.v59 = temp
    else:
        v59 = temp 

    v57 = (v58 , v59); v57 = tuple(v57) if isinstance(v57, np.ndarray) else v57

    temp = get_nested_attribute(action, '7', locals())
    if temp is None:
        temp = 7
    if action is not None and hasattr(action, "v61".split('[')[0].split('.')[0]):
        action.v61 = temp
    else:
        v61 = temp 


    temp = get_nested_attribute(action, '8', locals())
    if temp is None:
        temp = 8
    if action is not None and hasattr(action, "v62".split('[')[0].split('.')[0]):
        action.v62 = temp
    else:
        v62 = temp 

    v60 = (v61 , v62); v60 = tuple(v60) if isinstance(v60, np.ndarray) else v60

    temp = get_nested_attribute(action, '9', locals())
    if temp is None:
        temp = 9
    if action is not None and hasattr(action, "v64".split('[')[0].split('.')[0]):
        action.v64 = temp
    else:
        v64 = temp 


    temp = get_nested_attribute(action, '10', locals())
    if temp is None:
        temp = 10
    if action is not None and hasattr(action, "v65".split('[')[0].split('.')[0]):
        action.v65 = temp
    else:
        v65 = temp 

    v63 = (v64 , v65); v63 = tuple(v63) if isinstance(v63, np.ndarray) else v63
    v50 = [v51,v54,v57,v60,v63]
    v33 = [v34,v50]

    temp = get_nested_attribute(action, 'v33', locals())
    if temp is None:
        temp = v33
    if action is not None and hasattr(action, "v66".split('[')[0].split('.')[0]):
        action.v66 = temp
    else:
        v66 = temp 


    temp = get_nested_attribute(action, 'v66', locals())
    if temp is None:
        temp = v66
    if action is not None and hasattr(action, "var__agl__c".split('[')[0].split('.')[0]):
        action.var__agl__c = temp
    else:
        var__agl__c = temp 


    temp = get_nested_attribute(action, 'var__agl__c', locals())
    if temp is None:
        temp = var__agl__c
    if action is not None and hasattr(action, "v68".split('[')[0].split('.')[0]):
        action.v68 = temp
    else:
        v68 = temp 


    temp = get_nested_attribute(action, 'var__agl__c', locals())
    if temp is None:
        temp = var__agl__c
    if action is not None and hasattr(action, "v69".split('[')[0].split('.')[0]):
        action.v69 = temp
    else:
        v69 = temp 


    temp = get_nested_attribute(action, 'var__agl__c', locals())
    if temp is None:
        temp = var__agl__c
    if action is not None and hasattr(action, "v70".split('[')[0].split('.')[0]):
        action.v70 = temp
    else:
        v70 = temp 


    temp = get_nested_attribute(action, 'var__agl__c', locals())
    if temp is None:
        temp = var__agl__c
    if action is not None and hasattr(action, "v71".split('[')[0].split('.')[0]):
        action.v71 = temp
    else:
        v71 = temp 

    v67 = [v68,v69,v70,v71]

    temp = get_nested_attribute(action, 'v67', locals())
    if temp is None:
        temp = v67
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


    temp = get_nested_attribute(action, 'v73', locals())
    if temp is None:
        temp = v73
    if action is not None and hasattr(action, "var__agl__e".split('[')[0].split('.')[0]):
        action.var__agl__e = temp
    else:
        var__agl__e = temp 
    if model is not None: 
        model.var__agl__e = var__agl__e
        model.last_var__agl__e = copy.deepcopy(var__agl__e)

    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v76".split('[')[0].split('.')[0]):
        action.v76 = temp
    else:
        v76 = temp 


    temp = get_nested_attribute(action, 'var__agl__c[v76]', locals())
    if temp is None:
        temp = var__agl__c[v76]
    if action is not None and hasattr(action, "v75".split('[')[0].split('.')[0]):
        action.v75 = temp
    else:
        v75 = temp 


    temp = get_nested_attribute(action, '1', locals())
    if temp is None:
        temp = 1
    if action is not None and hasattr(action, "v78".split('[')[0].split('.')[0]):
        action.v78 = temp
    else:
        v78 = temp 


    temp = get_nested_attribute(action, 'var__agl__c[v78]', locals())
    if temp is None:
        temp = var__agl__c[v78]
    if action is not None and hasattr(action, "v77".split('[')[0].split('.')[0]):
        action.v77 = temp
    else:
        v77 = temp 

    v74 = [v75,v77]

    temp = get_nested_attribute(action, 'v74', locals())
    if temp is None:
        temp = v74
    if action is not None and hasattr(action, "v79".split('[')[0].split('.')[0]):
        action.v79 = temp
    else:
        v79 = temp 


    temp = get_nested_attribute(action, 'v79', locals())
    if temp is None:
        temp = v79
    if action is not None and hasattr(action, "v80".split('[')[0].split('.')[0]):
        action.v80 = temp
    else:
        v80 = temp 


    temp = get_nested_attribute(action, 'v80', locals())
    if temp is None:
        temp = v80
    if action is not None and hasattr(action, "var__agl__i".split('[')[0].split('.')[0]):
        action.var__agl__i = temp
    else:
        var__agl__i = temp 
    if model is not None: 
        model.var__agl__i = var__agl__i
        model.last_var__agl__i = copy.deepcopy(var__agl__i)

    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v82".split('[')[0].split('.')[0]):
        action.v82 = temp
    else:
        v82 = temp 


    temp = get_nested_attribute(action, '0', locals())
    if temp is None:
        temp = 0
    if action is not None and hasattr(action, "v83".split('[')[0].split('.')[0]):
        action.v83 = temp
    else:
        v83 = temp 


    temp = get_nested_attribute(action, 'var__agl__c[v82][v83]', locals())
    if temp is None:
        temp = var__agl__c[v82][v83]
    if action is not None and hasattr(action, "v81".split('[')[0].split('.')[0]):
        action.v81 = temp
    else:
        v81 = temp 


    temp = get_nested_attribute(action, 'v81', locals())
    if temp is None:
        temp = v81
    if action is not None and hasattr(action, "v84".split('[')[0].split('.')[0]):
        action.v84 = temp
    else:
        v84 = temp 


    temp = get_nested_attribute(action, 'v84', locals())
    if temp is None:
        temp = v84
    if action is not None and hasattr(action, "v85".split('[')[0].split('.')[0]):
        action.v85 = temp
    else:
        v85 = temp 


    temp = get_nested_attribute(action, 'v85', locals())
    if temp is None:
        temp = v85
    if action is not None and hasattr(action, "var__agl__h".split('[')[0].split('.')[0]):
        action.var__agl__h = temp
    else:
        var__agl__h = temp 
    if model is not None: 
        model.var__agl__h = var__agl__h
        model.last_var__agl__h = copy.deepcopy(var__agl__h)

    temp = get_nested_attribute(action, 'var__agl__h', locals())
    if temp is None:
        temp = var__agl__h
    if action is not None and hasattr(action, "v86".split('[')[0].split('.')[0]):
        action.v86 = temp
    else:
        v86 = temp 

    print(v86)
