# -*- coding: utf-8 -*-
# 以utf-8的编码读取
'a test module'
__author__ = 'chenbin'

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('Dict object has no attribute %s' % key)

    def __setattr__(self, key, value):
        self[key] = value

def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)

print(create_args_string(3))
