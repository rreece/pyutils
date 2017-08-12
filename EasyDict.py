"""
EasyDict.py
"""

class EasyDict(dict):
    def __init__(self, d=None, **kw):
        if d:
            super(EasyDict, self).__init__(d)
        else: 
            super(EasyDict, self).__init__()
        super(EasyDict, self).update(kw)
    def __getattr__(self, name):
        return self[name]
    def __setattr__(self, name, value):
        super(EasyDict, self).__setitem__(name,value)
    def __missing__(self, name):
        super(EasyDict, self).__setitem__(name, EasyDict())
        return super(EasyDict, self).__getitem__(name)


#-----------------------------------------------------------------------------

if __name__ == '__main__':
    
    ## intialize with an existing dictionary
    d = {'a':1, 'b':2}
    d1 = EasyDict(d)
    print d1

    ## intialize with keyword parameters
    d2 = EasyDict(c=3, x='hello')
    print d2

    ## manipulate directly through .
    d3 = EasyDict()
    d3.a = 1
    d3.b = 'two'
    d3.w.x = 100
    d3.w.y = 200
    print d3

