import time as Timer
import math


def merge(A_merge, p, q, r):
    # prima metà di A
    n = q-p
    # seconda metà di A
    m = r-q
    R = []
    L = []
    # copio la prima metà degli elementi dell'array A in L
    i = 0
    while i <= n:
        L.append(A_merge[p+i])
        i += 1
    # copio la seconda metà degli elementi dell'array A in L
    i = 1
    while i <= m:
        R.append(A_merge[q+i])
        i += 1
    # inserisco degli infiniti in fondo per i confronti
    L.append(math.inf)
    R.append(math.inf)
    # ---DEBUG---- print("Lunghezza di L: ", len(L), "\nLunghezza di R: ", len(R), "\nLunghezza di A: ", len(A_merge))
    i = 0
    j = 0
    k = p
    # faccio il MERGE dei due sottoarray L e R in A confrontando i singoli elementi, partendo da 0 in entrambi gli array
    while k <= r:
        if L[i] <= R[j]:
            A_merge[k] = L[i]
            i += 1
        else:
            A_merge[k] = R[j]
            j += 1
        k += 1


def merge_sort(A, p, r):
    if p < r:
        q = math.trunc((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


# def main():
#     print("Algoritmo di ordinamento: MERGE SORT\n")
#     print("Scrivi gli elementi dell'array da ordinare: (digita un carattere diverso da un numero per terminare)\n")
#     A = []
#     numx = input()
#     while numx != "xd":
#         A.append(int(numx))
#         print("Inserito: ", (A[len(A)-1]), "in posizione: ", len(A)-1)
#         numx = input()
#     start = Timer.clock()
#     merge_sort(A, 0, len(A)-1)
#     end = Timer.clock()
#
#     for i in A:
#         print(i)
#     print("------------------")
#     print("L'ordinamento è stato eseguito in ", (end-start)*pow(10, 9), "microsecondi.")
#
#
# main()
