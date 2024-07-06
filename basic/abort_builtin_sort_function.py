"""

In Python, when you sort a list of lists (or any other iterable of iterables), the default behavior is to use 
the first element of each inner list (or iterable) as the primary key for comparison. This is because Python's 
sort() method and sorted() function use lexicographical ordering by default, which is similar to dictionary or 
phone book ordering.

Lexicographical ordering means that the elements are compared in a manner similar to the alphabetical order in 
dictionaries. For lists, tuples, and other sequences, this ordering is determined by comparing the first elements, 
and if they are equal, then by the second elements, and so on.


"""
import heapq


arr = [[1, 'a'], [-1, 'b'], [-3, 'a'], [-3, 'cc'], [-3, 'c']]
print(arr) # [[-3, 'a'], [-3, 'c'], [-3, 'cc'], [-1, 'b'], [1, 'a']]          'a' -> 'c' -> 'cc'



arr = [[1, 'a'], [-1, 'b'], [-3, 'a'], [-3, 'cc'], [-3, 'c']]
arr.sort(reverse=True)  # large -> small
print(arr)  # [[1, 'a'], [-1, 'b'], [-3, 'cc'], [-3, 'c'], [-3, 'a']]


# custom comparator
def comparator(arr):
    return arr[1]
arr = [[1, 'a'], [-1, 'b'], [-3, 'a'], [-3, 'cc'], [-3, 'c']]   # [[1, 'a'], [-3, 'a'], [-1, 'b'], [-3, 'c'], [-3, 'cc']]
arr.sort(key=comparator)
print(arr)


##############################################
"""
similar in heap

"""
minheap = [[1, 100], [-1, 10], [-5, 1], [10, 0]]
heapq.heapify(minheap)

while minheap:
  print(heapq.heappop(minheap))

