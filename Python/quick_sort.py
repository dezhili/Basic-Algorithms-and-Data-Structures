# last element pivot

import random
import time

#end is included index
def quick_sort(array, start, end):
    if end > start:
        wall = partition(array, start, end)
        quick_sort(array, start, wall-1)
        quick_sort(array, wall+1, end)

# pivot is the end
def partition(array, start, end):
    wall = start
    pivot = array[end]
    for cur in range(start, end):
        if array[cur] < pivot:
            array[wall], array[cur] = array[cur], array[wall]
            wall += 1
    array[wall], array[end] = array[end], array[wall]
    return wall

a = [random.randint(0, 500000) for i in range(0,500000)]
# a = [3, 2, 1, 4, 5]
start_time = time.time()
quick_sort(a, 0, len(a)-1)
# print(a)
print("--- %s seconds ---" % (time.time() - start_time))
