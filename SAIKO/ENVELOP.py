# -*- coding: utf-8 -*-

import math

ENVELOP = {
    'none' : (lambda x : 1),
    'test1' : (lambda x : 1 - x),
    'test2' : (lambda x : 16**(-x)),
    'test3' : (lambda x : 2**(-x)),
    'test4' : (lambda x : 1 / ( (3*x-0.5)**2 + 1 ))
}