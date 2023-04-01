#Linear Search in Python
'''
def linearSearch(array,n,x):
    #Going through array sequentially
    for i in range(0,n): #0 to 4
        if (array[i] == x):
            return i
    return -1
array = [2,4,0,1,9]
x= 1#key
n=len(array)
result = linearSearch(array,n,x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index:",result)
'''
#Binary search in python
'''   
def binarySearch(array,x,low,high):
    while low <= high:
        mid=low+(high-low)//2
        if array[mid] == x:
            return mid
        elif array[mid]<x:
            low =mid +1
        else:
            high=mid-1
    return -1
array=[3,4,5,6,7,8,9]
x=5
result=binarySearch(array,x,0,len(array)-1)
if result != -1:
    print("Element is present at index" +str(result))
else:
    print("not found")
'''

'''
class Node:
    def __init__(self,item):
        self.left = None
        self.right = None
        self.val = item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->",end='')
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+"->", end=' ')

    
def preorder(root):
    if root:
        print(str(root.val)+"->", end=' ')
        preorder(root.left)
        preorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Inorder traversal")
inorder(root)
print("\n Preorder traversal")
preorder(root)
print("\n Postorder traversal")
postorder(root)
'''

#Binary search tree operations in python

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key)+ "->", end=' ')
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minValueNode(node):
    current=node
    while(current.left is not None):
        current = current.left
    return current
def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left=deleteNode(root.left,key)
    elif(key >root.key):
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root = None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValueNode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root
    
root=None
root=insert(root, 8)
root=insert(root, 3)
root=insert(root, 1)
root=insert(root, 6)
root=insert(root, 7)
root=insert(root, 10)
root=insert(root, 14)
root=insert(root, 4)
print("inorder traversal: ",end=' ')
inorder(root)
print("\ndelete 10")
root=deleteNode(root,6)
print("inorder traversal: ",end=' ')
inorder(root)



#qts-->11
'''
A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating 
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:
count_compartments()- returns the total number of compartments
 in the train
check_vacancy()-returns the count of the compartments in which
 more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where 
data in each node refers to a compartment.
A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating 
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:

count_compartments()- returns the total number of compartments in the train
check_vacancy()-returns the count of the compartments in which more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where data in each node refers to a compartment.


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        temp=self.headval
        while temp is not None:
            print(temp.data.comp_name,temp.data.t_seat,temp.data.n_pass)
            print()
            temp=temp.next

    def athead(self,data):
        newnode=node(data)
        if(self.headval==None):
            self.headval=newnode
        else:
            newnode.next=self.headval
            self.headval=newnode
    def atend(self,data):
        newnode=node(data)
        if(self.headval==None):
            self.headval=newnode
        else:
            temp=self.headval
            while(temp.next != None):
                temp=temp.next
            temp.next=newnode

    def len(self):
        cnt=0
        temp=self.headval
        while temp is not None:
            cnt+=1
            temp=temp.next
        print(cnt)
   

class train:
    def __init__(self,tname,c_list):
        self.tname=tname
        self.c_list=c_list

    def get_train_name(self):
        return self.tname
    
    def get_compartment(self):
        self.c_list.listprint()

    def count_compartment(self):
        self.c_list.len()
    
    def check_vacancy(self):
        temp=self.c_list.headval
        cnt=0
        while temp is not None:
            if(temp.data.t_seat-temp.data.n_pass >= temp.data.t_seat//2):
                cnt+=1
            temp=temp.next
        print(cnt)



class Compartment:
    def __init__(self,comp_name,n_pass,t_seat):
        self.comp_name=comp_name
        self.t_seat=t_seat
        self.n_pass=n_pass
    
list=linkedlist()
c1=Compartment("SL",250,400)
c2=Compartment("2AC",125,280)
c3=Compartment("3AC",120,300)
c4=Compartment("FC",160,300)
c5=Compartment("1AC",100,210)
list.atend(c1)
list.atend(c2)
list.atend(c3)
list.atend(c4)
list.atend(c5)

t1=train("Rajadhani",list)
t1.count_compartment()
t1.check_vacancy()
t1.get_compartment()
print(t1.get_train_name())

'''


















