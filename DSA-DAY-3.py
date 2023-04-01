#LINKEDLIST
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head=prev
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
llist=LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print("given linked list")
llist.printList()
llist.reverse()
print("\nReversed linked list")
llist.printList()'''


#DOUBLE LINKEDLIST

'''class Node:
    def __init__(self,value):
        self.previous = None
        self.data = value
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def length(self):
        temp = self.head
        count=0
        while temp is not None:
            temp = temp.next
            count+=1
        return count
    
    def insertAtBeginning(self,value): #15
        new_node = Node(value) #2000
        if self.isEmpty():
            self.head = new_node #800.head=1000
        else:
            new_node.next = self.head #200.next=1000
            self.head.previous = new_node #2000
            self.head = new_node

    def insertAtEnd(self,value): #15
        new_node = Node(value) #2000
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp = self.head #1000
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.previous = temp

    def insertAtPosition(self,value,position):
        temp = self.head
        count = 0
        while temp is not None:
            if count==position-1:
                break
            count += 1
            temp=temp.next
        if position == 1:
            self.insertAtBegining(value)
        elif temp is None:
            print("There are less then ()-1 elements in the linked list.cannot insert at() position".formate(position,position))
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node = Node(value)
            new_node.next=temp.next
            new_node.previous=temp
            temp.next.previous=new_node
            temp.next=new_node

    def deleteFromBegining(self):
        if self.isEmpty():
            print("linked list is empty.cannot delete elements.")
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.previous=None
      
            

    def deleteFromLast(self):
        if self.isEmpty():
            print("list is empty.cannot delete elements.")
        elif self.head.next is None:
            self.head = None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.previous.next=None
            temp.previous=None

    def deleteFromPosition(self,position):
        if self.isEmpty():
            print("linked list is empty.cannot delete elements.")
        elif position == 1:
            self.insertAtBegining()
        else:
            temp=self.head
            count=1
            while temp is not None:
                if count == position:
                    break
                temp=temp.next
                count=+1
            if temp is None:
                print("There are less than {} elements in linked list")
            elif temp.next is None:
                self.deletefromLast()
                return
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
            temp.next = None
            temp.previous = None


            
            
            


    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp = temp.next 
                
                
    

x = DoublyLinkedList() #800
print(x.isEmpty())
x.insertAtBeginning(5)
x.printLinkedList()
x.insertAtBeginning(15)
x.insertAtBeginning(25)
x.insertAtBeginning(35)
x.printLinkedList()
print("No. of Nodes",x.length())

print(x.isEmpty())
x.insertAtEnd(5)
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("No. of Nodes",x.length())
print("insert at position 2 number 8")
x.insertAtPosition(8,2)
x.printLinkedList()
print("delete from the begining")
x.deleteFromBegining()
x.printLinkedList()
print("delete at the last")
x.deleteFromBegining()
'''
#POSTFIX EVALUTION
class Evaluate:
    def __init__(self,capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
    def isEmpty(self):
        return True if self.top == -1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    def push(self,op):
        self.top += 1
        self.array.append(op)

    def evaluatePostfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2+i+val1)))
        return int(self.pop())
if __name__ == '__main__':
    exp = "231*+9-"
    obj = Evaluate(len(exp))
    print("Postfix Evaluation : %d" %(obj.evaluatePostfix(exp)))


    























        
