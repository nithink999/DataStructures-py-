class Node:
  def __init__(self, data=None, next = None):
    self.data = data
    self.next = next
class LinkedList:
  def __init__(self):
    self.head=None
  def insert_at_beginning(self, data):
    node= Node(data, self.head)
    self.head = node
  def insert_at_theend(self,data):
    if self.head is None:
      self.head = Node(data, None)
      return
    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next= Node(data,None)
  def print(self):
    if self.head is None:
      print("Empty Linked List")
      return
    itr= self.head
    llstr=''
    while itr:
      llstr += str(itr.data) + '-->'
      itr= itr.next
    print(llstr)
  def insert_values(self, data_list):
    self.head= None
    for data in data_list:
      self.insert_at_theend(data)
  def count(self):
    itr=self.head
    count=0
    while itr:
      count+=1
      itr= itr.next
    return count
  def remove_at(self, index):
    if index<0 or index>self.count():
      raise Exception("Invalid Index")
    if index==0:
      self.head = self.head.next
      return self.print()
    count=0
    itr= self.head
    while itr:
      count+=1
      if(count==index):
        break
      itr= itr.next
    itr.next= itr.next.next
    self.print()
  def insert_at(self,index,data):
    if index<0 or index>self.count():
      raise Exception("Invalid Index")
    if index == 0:
      self.insert_at_beginning(data)
      return self.print()
    # if index == self.count():
    #    self.insert_at_theend(data)
    #    return self.print()
    count=0
    itr= self.head
    while itr:
      count+=1
      if(count==index):
        break
      itr= itr.next
    node = Node(data,itr.next)
    itr.next=node
    return self.print()
    
      
    
    
    
      
      
      
if __name__=='__main__':
  ll= LinkedList()
  # ll.insert_at_beginning(5)
  # ll.insert_at_beginning(8)
  # ll.insert_at_beginning(67)
  # ll.insert_at_theend(99)
  ll.insert_values(["good","boii","nithin","damn","letsgooo"])
  ll.print()
  print("Length:", ll.count())
  # ll.remove_at(-2)
  ll.insert_at(5,"raj")

  
      
    
    
    
    
    
    