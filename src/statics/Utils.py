'''
Created on Jan 30, 2015

@author: AlirezaF
'''

from hashlib import md5


def get_md5(*args):
    m = md5()
    for arg in args:
        # bytes takes iterable objects
        if (type(arg) == str):
        # m.update(bytes(list(arg)))
            m.update(arg.encode())
        else:
            m.update(arg)    
    return md5().hexdigest()
