import time as Timer
import math

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, p, r):
    x = A[r]
    i = p-1
    j = p
    while j <= r-1:
        if A[j] <= x:
            i += 1
            swap(A, i, j)
        j += 1
    swap(A, i+1, r)
    return i+1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


# def main():
#     print("Algoritmo di ordinamento: QUICK SORT\n")
#     print("Scrivi gli elementi dell'array da ordinare: (digita un carattere diverso da un numero per terminare)\n")
#     A = []
#     numx = input()
#     while numx != "xd":
#         A.append(int(numx))
#         print("Inserito: ", (A[len(A)-1]), "in posizione: ", len(A)-1)
#         numx = input()
#     start = Timer.clock()
#     quick_sort(A, 0, len(A)-1)
#     end = Timer.clock()
#
#     for i in A:
#         print(i)
#     print("------------------")
#     print("L'ordinamento è stato eseguito in ", (end-start)*pow(10, 9), "microsecondi.")
#
#
# main()
