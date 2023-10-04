#!/usr/bin/env python
import time

#-------------------------------------- RECURSIVE QUICK SORT -------------------------
# TODO: add the quick_sort.txt code snippet here
#----------------------------------------------------------------------------------

def partition(inList, start_index, end_index):   #  Lomuto partition scheme
    pivot = inList[end_index]  
    i = start_index - 1  
    for j in range(start_index, end_index):
        if inList[j] <= pivot:
            i = i + 1
            temp = inList[i]
            inList[i] = inList[j]
            inList[j] = temp
    inList[i+1], inList[end_index] = inList[end_index], inList[i+1]
    return i+1

def qsort(inList, start_index, end_index):
    if start_index < end_index:
        pivot_index = partition(inList, start_index, end_index)
        qsort(inList, start_index, pivot_index-1)
        qsort(inList, pivot_index+1, end_index)

def quick_sort(inList):
    qsort(inList, 0, len(inList)-1)

#------------------------------------- RECURSIVE HEAP SORT ------------------------
# TODO: add the heap_sort.txt code snippet here
#----------------------------------------------------------------------------------

def hsort(inList, heap_size, root_index):
    largest = root_index
    left_index = (2 * root_index) + 1
    right_index = (2 * root_index) + 2
    if left_index < heap_size and inList[left_index] > inList[largest]:
        largest = left_index
    if right_index < heap_size and inList[right_index] > inList[largest]:
        largest = right_index
    if largest != root_index:
        inList[root_index], inList[largest] = inList[largest], inList[root_index]
        hsort(inList, heap_size, largest)

def heap_sort(inList):
    n = len(inList)
    for i in range(n, -1, -1):
        hsort(inList, n, i)
    for i in range(n - 1, 0, -1):
        inList[i], inList[0] = inList[0], inList[i]
        hsort(inList, i, 0)

#------------------------------------------- Experiment Starts Here
def run_experiment(outfile):
    exp_start = time.perf_counter()
    file = open(outfile, "w")
    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
    file.write('<Plot title="Python quicksort() and heapsort()">\n')
    
    # USE THESE CONSTANTS TO CONTROL THE EXPERIMENT AND THE GRAPH OUTPUT 
    Nmin = 0         #     nominal= 0       N minimum, start value for number of items to sort 
    Nmax =900       #     nominal= 400       N maximum, end value for number of items to sort
    Ninc = 20        #    nominal= 2        X axis N value increment
    Ymin = 0         #     nominal= 0         min on Y axis in microseconds
    Ymax = 6000      #   nominal= 6000          max on Y axis in microseconds
    
    # ... (the rest of the code remains unchanged)
    # ... (you can keep the rest of the code as it is)

# ... (rest of the code remains unchanged)
# ... (you can keep the rest of the code as it is)
