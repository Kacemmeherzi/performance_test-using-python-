# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:44:22 2024

@author: PC
"""

from tri import *
import random
import timeit


def main(liste, *, number=100):
    print(f'mesure avec un tableau liste={liste},'f'calcul fait {number} fois:')
    
    import sys
    sys.setrecursionlimit(5_000)
    variantes=(tri_selection,tri_bulle, tri_insertion, quicksort)
    
    for tri in variantes:
        duree=timeit.timeit('tri.' + tri.__name__+f'({liste} )',setup='import tri',number=number)
        print(f'*{duree:8.5f}; {tri.__name__}')
        
if __name__=='__main__':
    liste=random.sample(range(-10000000,10000000),500)
    main(liste)
    