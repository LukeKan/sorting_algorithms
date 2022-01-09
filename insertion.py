import time as Timer

def insertion(A):
    j = 1
    while j < len(A):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
        j += 1
# insertion è sequenziale:
# IDEA: partendo da lunghezza due a partire da sx ordino il sottoarray. Ad ogni ciclo aumento la dimensione del sottoarray
# che sto ordinando finchè non arrivo ad avere il sottoarray==array. L'ordinamento consiste nel shiftare a dx del
# sottoarray gli elementi più grandi e di "creare dei buchi" lasciando dei duplicati che verranno rimpiazzati (INSERT)
# nella posizione del doppione più a dx.
# dato un array in input -> se l'array è lungo 1 è ordinato, altrimenti procede:
# a)prende l'elemento in seconda posizione; fa partire un ciclo a partire dall'elemento in prima posizione: se
# l'elemento è più grande del secondo lo copio letteralmente. alla fine del ciclo, ricopio nella posizione
# immediatamente successiva il secondo elemento.
# b) procedo con il terzo elemento(J=2); ripeto il confronto con il secondo elemento, sapendo che i primi due elementi
# sono ordinati dal punto a). Se il secondo è più grande del terzo, lo copio al posto del terzo e faccio il confronto anche
# con il primo ed eventualmente copio il primo nella seconda posizione. alla fine copio l'elemento di partenza nel posto
# successivo all'ultimo attuale.
# c) ripeto quest'operazione finchè non ho ordinato tutto.

# def main():
#     print("Algoritmo di ordinamento: INSERTION SORT\n")
#     print("Scrivi gli elementi dell'array da ordinare: (digita un carattere diverso da un numero per terminare)\n")
#     A = []
#     numx = input()
#     while numx != "xd":
#         A.append(int(numx))
#         print("Inserito: ", (A[len(A)-1]), "in posizione: ", len(A)-1)
#         numx = input()
#     start = Timer.clock()
#     insertion(A)
#     end = Timer.clock()
#
#     for i in A:
#         print(i)
#     print("------------------")
#     print("L'ordinamento è stato eseguito in ", (end-start)*pow(10, 9), "microsecondi.")
#
#
# main()
