import time as Timer
import math

# classe definita ad hoc per gestire l'array nell'heapsort.
class arrayHeap:
    list = []
    heap_size = 0

    def __init__(self):
        self.heap_size = 0
        self.list = None

    def __init__(self, lista):
        self.list = lista
        self.heap_size = 0

# funzioni ausiliare per il funzionamento.


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def parent(i): return math.trunc(i/2)
def left(i):
    if i==0:
        return 1
    return 2*i
def right(i):
    if i==0:
        return 2
    return (2*i)+1

# dato A, i figli dell'elemento A[i], ovvero A[2i] e A[2i+1] sono max_heap MA A[i] non è max_heap. Questa funzione
# confronta padre e figli per stabilire chi sia il max_heap tra loro
def max_heapify(A, i):
    l = left(i)
    r = right(i)
    if l >= len(A.list) : max_heapify(A, i-1)
    maxn = i
    if l <= A.heap_size and A.list[l] > A.list[i]:
        maxn = l
    else:
        maxn = i
    if r < len(A.list):
        if r <= A.heap_size and A.list[r] > A.list[maxn]:
            maxn = r
    if maxn != i:
        swap(A.list, i, maxn)
        max_heapify(A, maxn)

# costruisce l'albero di maxheap all'inizio, partendo con i confronti di maxheap dalla penultima riga e risalendo
# da dx a sx
def build_maxheap(A):
    A.heap_size = len(A.list)
    i = math.trunc((len(A.list)-1)/2)-1
    while i >= 0:
        max_heapify(A, i)
        i -= 1


def heap_sort(A):
    build_maxheap(A)
    for i in range(1, len(A.list)):
        swap(A.list, 0, i)
        A.heap_size -= 1
        max_heapify(A, 0)


def main():
    print("Algoritmo di ordinamento: HEAP SORT\n")
    print("Scrivi gli elementi dell'array da ordinare: (digita un carattere diverso da un numero per terminare)\n")
    A = []
    numx = input()
    while numx != "xd":
        A.append(int(numx))
        print("Inserito: ", (A[len(A)-1]), "in posizione: ", len(A)-1)
        numx = input()
    hA = arrayHeap(A)
    start = Timer.clock()
    heap_sort(hA)
    end = Timer.clock()

    for i in hA.list:
        print(i)
    print("------------------")
    print("L'ordinamento è stato eseguito in ", (end-start)*pow(10, 9), "microsecondi.")


main()
