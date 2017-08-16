def merge(unalista, mitadIzquierda, mitadDerecha):
    i = j = k = 0
    while i<len(mitadIzquierda) and j<len(mitadDerecha):
        if mitadIzquierda[i]<mitadDerecha[j]:
            unalista[k] = mitadIzquierda[i]
            i = i + 1
        else:
            unalista[k] = mitadDerecha[j]
            j = j + 1
        k = k + 1
    while i < len(mitadIzquierda):
        unalista[k] = mitadIzquierda[i]
        i = i + 1
        k = k + 1
    while j < len(mitadDerecha):
        unalista[k] = mitadDerecha[j]
        j = j + 1
        k = k + 1


def mergeSort(unalista):
    if len(unalista)>1:
        mitad = len(unalista)/2
        mitadIzquierda = unalista[:mitad]
        mitadDerecha   = unalista[mitad:]
        mergeSort(mitadIzquierda)
        mergeSort(mitadDerecha)
        merge(unalista,mitadIzquierda,mitadDerecha)


if __name__ == '__main__':
    lista = [54,26,93,17,77,31,44,55,20]
    print lista
    mergeSort(lista)
    print lista
    l = [1,2,3,7,11]
    r = [8,9,10,12]
    lr = [None for x in range(len(l)+len(r))]
    merge(lr,l,r)
    print lr

