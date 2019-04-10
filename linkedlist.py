class createlinkedlist:
    def __init__(self, node, next):
        self.node=node
        self.next=next

nodeobj=createlinkedlist(1, None)
head=nodeobj
for i in range(2,6):
    newnodeobj=createlinkedlist(i, None)
    nodeobj.next=newnodeobj
    nodeobj=newnodeobj

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

cur=future
cur.next=previous

while cur.next!=None:
    print(cur.node)
    cur=cur.next

print(cur.node)
