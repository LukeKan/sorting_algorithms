import time as Timer
from merge import merge_sort
from quick import quick_sort
from insertion import insertion
import random


def main():
    print("Benchmark per alcuni algoritmi di ordinamento: \n")
    print("Scegli quale tipo di inserimento vuoi effettuare:\n1) Manuale\n2)[13,12,7,2,1]")
    print("3)[55,2,11,3,62,1,-5,9]\n4)[0,2,5,6,7,8,1,9]\n5)Array enorme")
    check = True
    while check:
        try:
            choice = int(input())
            check = False
        except:
            pass
    A = []
    if choice == 2:
        A = [13, 12, 7, 2, 1]
    elif choice == 3:
        A = [55, 2, 11, 3, 62, 1, -5, 9]
    elif choice == 4:
        A = [0, 2, 5, 6, 7, 8, 1, 9]
    elif choice == 5:
        for i in range(0, 120000):
            A.append(random.randint(-3000, 3000))
    else:
        print("Scrivi gli elementi dell'array da ordinare: (digita un carattere diverso da un numero per terminare)\n")
        numx = input()
        while numx != "xd":
            A.append(int(numx))
            print("Inserito: ", (A[len(A) - 1]), "in posizione: ", len(A) - 1)
            numx = input()
    time_dict = dict()
    # -----quicksort--------
    to_ord = A
    start = Timer.clock()
    quick_sort(to_ord, 0, len(to_ord) - 1)
    end = Timer.clock()
    time_dict["quick"] = end - start
    # ---------------------

    # -----heapsort--------
    # to_ord = A
    # hA = arrayHeap(to_ord)
    # start = Timer.clock()
    # heap_sort(hA)
    # end = Timer.clock()
    # time_dict["heap"] = end - start
    # ---------------------

    # -----mergesort--------
    to_ord = A
    start = Timer.clock()
    merge_sort(to_ord, 0, len(to_ord) - 1)
    end = Timer.clock()
    time_dict["merge"] = end - start
    # ---------------------

    # -----insertionsort--------
    to_ord = A
    start = Timer.clock()
    insertion(to_ord)
    end = Timer.clock()
    time_dict["insertion"] = end - start
    # ---------------------

    print('-' * 80)
    print("L'Insertion-sort è stato eseguito in ", time_dict["insertion"] * pow(10, 3), "millisecondi.")
    print('-' * 80)
    print("Il Merge-sort è stato eseguito in ", time_dict["merge"] * pow(10, 3), "millisecondi.")
    print('-' * 80)
    print("Il Quick-sort è stato eseguito in ", time_dict["quick"] * pow(10, 3), "millisecondi.")
