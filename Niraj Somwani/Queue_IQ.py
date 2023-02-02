#Interview Question in Queue
#Question1:Implementation of queue using list

class Queue:
  def __init__(self, size):
    self.queue = [None] * size
    self.capacity = size
    self.front = 0
    self.last = -1
    self.count = 0

#Removing the item from Queue
  def pop(self):
    if self.isEmpty():
      print("Queue is Empty")
      exit(1)  
    print("Removing the element:", self.queue[self.front])  
    self.front = (self.front + 1) % self.capacity
    self.count = self.count -1

#Adding item items in Queue
  def append(self, value):
    if self.isFull():
      print("Queue is Full")  
      exit(1)
    print("Adding the element:", value)
    self.last = (self.last + 1) % self.capacity
    self.queue[self.last] = value
    self.count = self.count + 1


  def peek(self):
    if self.isEmpty():
      print("Queue is Empty")
      exit(1)
    return self.queue[self.front]  

  def size(self):
    return self.count    

  def isEmpty (self):
    return self.size() == 0       

  def isFull (self):
    return self.size() == self.capacity   


if __name__ == "__main__":
   cust_queue = Queue(10)
   print("Size of the Queue is", cust_queue.size())
   cust_queue.append(20)
   cust_queue.append(40)
   cust_queue.append(60)
   cust_queue.append(80)
   cust_queue.append(100)
   cust_queue.append(120)
   cust_queue.append(140)
   print("Size of the Queue is", cust_queue.size())
   cust_queue.pop()
   if cust_queue.isEmpty():
     print("Empty Queue")
   else:
     print("Queue is not Empty")  
