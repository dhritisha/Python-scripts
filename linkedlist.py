class createLinkedList:
    def __init__(self, node, next):
        self.node=node
        self.next=next

nodeObj=createLinkedList(1, None)
head=nodeObj
for i in range(2,6):
    newNodeObj=createLinkedList(i, None)
    nodeObj.next=newNodeObj
    nodeObj=newNodeObj

prev=head
while prev.next != None:
    print(prev.node)
    prev=prev.next

print(prev.node)



#Reverse a linked list

previous=None
cur=head

while cur.next!=None:
    future=cur.next
    cur.next=previous
    previous=cur
    cur=future

cur.next=previous

while cur.next!=None:
    print(cur.node)
    cur=cur.next

print(cur.node)
