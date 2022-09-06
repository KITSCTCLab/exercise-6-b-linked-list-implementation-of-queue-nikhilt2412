class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    nn = Node(data)
    if(self.last != None):
      self.last.next = nn
      self.last = nn
    
    else:
      self.head = nn
      self.last = nn

  def dequeue(self) -> None:
    if(self.head != None):
      temp = self.head
      self.head = temp.next

  def status(self) -> None:
    if(self.head  != None):
      temp = self.head
      while temp.next!= None:
        print(temp.data, end = "")
        print("=>", end = "")
        temp = temp.next
      print(temp.data, end = "=>")
      
    print("None")
    
# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
