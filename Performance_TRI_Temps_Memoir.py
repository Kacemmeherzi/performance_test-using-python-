from tri import *
import timeit
import random
import tracemalloc

def main(liste, *, number=1_000):
    print(f'Mesure avec un tableau={liste} \n,'
          f'Tri fait pour le même tableau {number} fois :')

    # Limite de récursion pour quicksort
    import sys
    sys.setrecursionlimit(25_000)

    variantes = {tri_selection, tri_bulle, tri_insertion, quicksort}
    for tri in variantes:
        # Mesurer le temps
        durée = timeit.timeit('tri.' + tri.__name__ + f'({liste})', setup='import tri', number=number)

        # Mesurer la mémoire
        tracemalloc.start()
        tri(liste.copy())  # Appliquer le tri
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Affichage des résultats
        print(f'* {durée:8.5f} sec : {tri.__name__}')
        print(f'  Consommation de mémoire : {current / 1024:0.2f} KB (courant), {peak / 1024:0.2f} KB (pic)')

if __name__ == '__main__':
    liste = random.sample(range(-1000000, 1000000), 500)
    main(liste)