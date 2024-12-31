# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:20:52 2024

@author: PC
"""

from tri import *
import random
import timeit
from strgen import StringGenerator

def main(liste, *, number=1_000):
    print(f'mesure avec un tableau liste={liste},'f'calcul fait {number} fois:')
    
    import sys
    sys.setrecursionlimit(25_000)
    variantes=(tri_selection,tri_bulle,tri_insertion,quicksort)
    
    for tri in variantes:
        duree=timeit.timeit('tri.' + tri.__name__+f'({liste} )',setup='import tri',number=number)
        print(f'*{duree:8.5f}; {tri.__name__}')
        
if __name__=='__main__':
    liste=StringGenerator("[\1\l]{10}").render_list(1000,unique=True)
    main(liste)
    