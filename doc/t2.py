def get_nested_attribute(obj, attr_path, local_dict=None):
    if obj is None:
        return None
    if local_dict is not None:
        return aaa(obj, attr_path, local_dict)

    attributes = attr_path.split('.')
    current_object = obj
    for attr in attributes:
        if hasattr(current_object, attr):
            current_object = getattr(current_object, attr)
        else:
            return None
    return current_object

def aaa(obj, attr_path, local_dict):
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
        return aaa(obj, attr_path, local_dict) 
    else:
        return obj

class Test2:
    def __init__(self):
        self.a = 1
        self.b = [2,3]
        self.c = 3

class Test:
    def __init__(self):
        e = Test2()
        self.a = [[1],e]
        self.b = 1
        self.c = 3
        self.d = None
        

test = Test()
# print(get_nested_attribute(test, 'a')[test.b]) # 1

b = 1

string = 'a[b].b[1]'
# this should be converted in:
print(aaa(test, string, locals()))

