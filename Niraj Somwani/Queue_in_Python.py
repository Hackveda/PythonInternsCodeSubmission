from collections import deque


#Checking the type to queue
queue = deque(["Niraj", "Vivek", "Parth"])
type(queue)


#Operation perform in Queue
#Adding queue
queue.append("Sumit") 
queue


#popleft queue
queue.popleft()   #remove from left side item of queue
queue


#adding item at the top of queue
queue.appendleft("Dhaval")
queue


#Copying queue
queue1 = queue.copy()
queue1


#Clear the queue
queue.clear()
queue


#Count the queue
queue1.count("Vivek")


#Extend queue
additional_queue = ["Raj","Mehul","Sandip"]
queue1.extend(additional_queue)
queue1


#Arrange the extended queue on left side
queue1.extendleft(additional_queue)
queue1


#find index of item in queue
queue1.index("Parth")


#insert a new item in queue at random index
queue1.insert(5,"Niraj")
queue1


#pop item in queue
queue1.pop()
queue1


#pop item from the left of the queue
queue1.popleft()
queue1


#Remove item
queue1.remove("Mehul")
queue1


#Reverse the queue
queue1.reverse()
queue1


#Rotate the queue
queue1.rotate(4)
queue1
