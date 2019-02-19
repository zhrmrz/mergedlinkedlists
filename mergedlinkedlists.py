from practice import Node,LinkedList
def mergeLists(flist,slist,mergedList):
    currentF=flist.head
    currentS=slist.head
    while True:
        if currentF is None:
            mergedList.insert(currentS)
            break
        if currentF.data<currentS.data:
            currentFN=currentF.next
            currentF.next=None
            mergedList.insert(currentF)
            currentF=currentFN
        else:
            currentSN=currentS.next
            currentS.next=None
            mergedList.insert(currentS)
            currentS=currentSN
node1=Node(1)
node2=Node(3)
node3=Node(4)
flist=LinkedList()
flist.insert(node1)
flist.insert(node2)
flist.insert(node3)
node4=Node(2)
node5=Node(7)
node6=Node(9)
slist=LinkedList()
slist.insert(node4)
slist.insert(node5)
slist.insert(node6)
print("Printing flist:")
flist.printList()
print("printing slist:")
slist.printList()
print("printing mergedlist:")
mergedList=LinkedList()
mergeLists(flist,slist,mergedList)
del flist
del slist
mergedList.printList()
