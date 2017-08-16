# -*- coding: utf-8 -*-
def debug_countingSort(A,B,C,k,n):
    for i in range(k):
        c[i] =0
    print c
    for j in range(n):
        print j
        c[A[j]-1] = c[A[j]-1] + 1   #c[i] = |{key = i}|
        print c
    for i in range(1,k):
        c[i] = c[i] + c[i-1]    #C[i] = |{key ≤i}|
        print 'cc',c
    for j in range(n-1,-1,-1):
        print 'j',j
        print 'A[j]',A[j]
        print 'c[A[j]-1]-1',c[A[j]-1]-1
        print
        B[c[A[j]-1]-1] = A[j]
        print B
        c[A[j]-1] = c[A[j]-1]-1
    return B

def countingSort(A,B,C,k,n):
    for i in range(k):
        c[i] =0
    for j in range(n):
        c[A[j]-1] = c[A[j]-1] + 1   #c[i] = |{key = i}|
    for i in range(1,k):
        c[i] = c[i] + c[i-1]    #C[i] = |{key ≤i}|
    for j in range(n-1,-1,-1):
        B[c[A[j]-1]-1] = A[j]
        c[A[j]-1] = c[A[j]-1]-1
    return B


if __name__ == '__main__':
    A = [4,1,3,4,3] #k = 1...4
    k = 4
    n = len(A)
    B = [None for i in range(n)]
    c = [0 for i in range(k)]
    print A
    print debug_countingSort(A,B,c,k,n)
    print
    print countingSort(A,B,c,k,n)
