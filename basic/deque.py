import collections
 
# initializing deque
queue = collections.deque([1,2,3])
 
# using append() to insert element at right end
# inserts 4 at the end of deque
queue.append(4)
 
# printing modified deque
print ("The deque after appending at right is : ")
print (queue)
 
# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
queue.appendleft(6)
 
# printing modified deque
print ("The deque after appending at left is : ")
print (queue)
 
# using pop() to delete element from right end
# deletes 4 from the right end of deque
queue.pop()
 
# printing modified deque
print ("The deque after deleting from right is : ")
print (queue)
 
# using popleft() to delete element from left end
# deletes 6 from the left end of deque
queue.popleft()
 
# printing modified deque
print ("The deque after deleting from left is : ")
print (queue)