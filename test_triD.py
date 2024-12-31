"""
Created on Thu Oct  3 10:16:11 2024

@author: PC
"""

from tri import *

tabnum=[6,-6,0,-1000,1000,-8]
tabchaine=['adem','ali','zied','ines','marwa']
tabtri=[0,10,100,1000,10000]
tabvide=[]
tabfin=[0,10,100,1000,10000,-1]
tabinver=[50,18,0,-1,-100]
tabdoubles= [8, 2, 9, 2, 1, 8, 7]

def test_tri_selection():
    assert tri_selection(tabnum)==[-1000,-8,-6,0,6,1000]
    assert tri_selection(tabchaine)==['adem','ali','ines','marwa','zied']
    assert tri_selection(tabtri)==[0,10,100,1000,10000]
    assert tri_selection(tabvide)==[]
    assert tri_selection(tabfin)==[-1,0,10,100,1000,10000]
    assert tri_selection(tabinver)==[-100,-1,0,18,50]
    assert tri_selection(tabdoubles)==[1, 2, 2, 7, 8, 8,9]

def test_tri_bulle():
    assert tri_bulle(tabnum)==[-1000,-8,-6,0,6,1000]
    assert tri_bulle(tabchaine)==['adem','ali','ines','marwa','zied']
    assert tri_bulle(tabtri)==[0,10,100,1000,10000]
    assert tri_bulle(tabvide)==[]
    assert tri_bulle(tabfin)==[-1,0,10,100,1000,10000]
    assert tri_bulle(tabinver)==[-100,-1,0,18,50]
    assert tri_bulle(tabdoubles)==[1, 2, 2, 7, 8, 8,9]
def test_tri_insertion():
    assert tri_insertion(tabnum)==[-1000,-8,-6,0,6,1000]
    assert tri_insertion(tabchaine)==['adem','ali','ines','marwa','zied']
    assert tri_insertion(tabtri)==[0,10,100,1000,10000]
    assert tri_insertion(tabvide)==[]
    assert tri_insertion(tabfin)==[-1,0,10,100,1000,10000]
    assert tri_insertion(tabinver)==[-100,-1,0,18,50]
    assert tri_insertion(tabdoubles)==[1, 2, 2, 7, 8, 8,9]

def test_tri_rapide():
    assert quicksort(tabnum)==[-1000,-8,-6,0,6,1000]
    assert quicksort(tabchaine)==['adem','ali','ines','marwa','zied']
    assert quicksort(tabtri)==[0,10,100,1000,10000]
    assert quicksort(tabvide)==[]
    assert quicksort(tabfin)==[-1,0,10,100,1000,10000]
    assert quicksort(tabinver)==[-100,-1,0,18,50]
    assert quicksort(tabdoubles)==[1, 2, 2, 7, 8, 8,9]