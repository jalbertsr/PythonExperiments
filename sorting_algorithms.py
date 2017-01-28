# -*- coding: utf-8 -*-
"""
@author: jalbert
Implementation of three sorting algorithms with complexity 0(n^2) and the comparasion of time execution between them. 
"""

import random
from time import time

lst = [random.randint(0, 200) for x in range(50)]


def bubble_sort(array):
    
    for i in range(len(array)):
        for j in range(len(array)-1-i):
             if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
   
def insertion_sort(array):
    
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array

def selection_sort(array):
    
    for slot in range(len(array)-1,0,-1):
        maxpos = 0
        for index in range(slot+1):
           if array[index] > array[maxpos]:
               maxpos = index
        temp = array[slot]
        array[slot] = array[maxpos]
        array[maxpos] = temp
    return array
        

t0 = time()
bubble_sort(lst)
ft0 = time()
elapsed0 = ft0 - t0

print "Bubble sort algorithm"
print "Execution time: %.10f sec" % (elapsed0)
print "==================================="

t1 = time()
insertion_sort(lst)
ft1 = time()
elapsed1 = ft1 - t1

print "Insertion sort algorithm"
print "Execution time: %.10f sec" % (elapsed1)
print "==================================="

t2 = time()
selection_sort(lst)
ft2 = time()
elapsed2 = ft2 - t2

print "Selection sort algorithm"
print "Execution time: %.10f sec" % (elapsed2)
print "===================================\n"

algorithms = {'Bubble': elapsed0, 'Insertion': elapsed1, 'Selection': elapsed2} 

print "From best algorithm to worst:\n"
for key, value in sorted(algorithms.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)







