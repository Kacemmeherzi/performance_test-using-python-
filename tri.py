# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 18:32:27 2021

@author: start-up
"""
from random import*
def tri_selection(liste):
   
    for etape in range(len(liste) - 1):
        # Placer dans liste[etape] le plus petit élément de liste[etape:]
        #    Trouver l'indice imin du plus petit élément de liste[etape:]
        imin, mini = etape, liste[etape]
        for i in range(etape+1, len(liste)):
            if liste[i] < mini:
                imin, mini = i, liste[i]
        #    Permuter les éléments aux indices etape et imin
        liste[etape], liste[imin] = mini, liste[etape]
        
    return liste 
def tri_bulle(liste):
     n=len(liste)
     for i in range(n):
         for j in range(0,n-i-1):
             if liste[j]>liste[j+1]:
                 liste[j],liste[j+1]=liste[j+1],liste[j]
     return liste 

def tri_insertion(tab): 
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k
    return tab

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    return arr