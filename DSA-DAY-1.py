

'''class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        #[None,None,None,None]
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    
    def push(self,data): #data=5
        if(self.is_full()):
            print("Stack is full!!")
        else:
            self.__top+=1 #self._top=3
            self.__elements[self.__top]=data #5
            #[5,6,7,8]

    def pop(self):
        if(self.is_empty()):
            print("Stack is empty!!")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("Stack is empty")
        else:
            index=self.__top #3
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

ball_stack=Stack(4)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(5)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("Size of the stack",ball_stack.get_max_size())
print("Element deleted",ball_stack.pop())
print("After deleting the element")
ball_stack.display()
print("Size of the stack",ball_stack.get_max_size())'''

#QTS--->2
#QUEUE
'''
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print(" queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
        
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size


queue1=Queue(10)
print("it is full",queue1.is_full())
print("it is empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
queue1.display()
print("elements deleted",queue1.dequeue())
queue1.display() '''
    
    
#QTS--->3

'''Given a queue of whole number.write a python function to return a a new queue which
contains the evenly divisible numbers.
sample input:
13983,10080,7113,2520,2500(front - rear)
output:
10080,2520(front-rear)


from queue import Queue

def get_evenly_divisible_numbers(queue):
    new_queue = Queue()
    while not queue.empty():
        num = queue.get()
        if num % 2 == 0:
            new_queue.put(num)
    return new_queue
original_queue = Queue()
original_queue.put(13983)
original_queue.put(10080)
original_queue.put(7113)
original_queue.put(2520)
original_queue.put(2500)

new_queue = get_evenly_divisible_numbers(original_queue)

while not new_queue.empty():
    
    print(new_queue.get())'''


#qts-->4

'''
Given two lists,both having string elements, write a python program using python
program using python lists to create a new string as per the rule given below:
the first element in list1 should be merged with last element in list2,second element
in list1 should be merged with second last element in list2 and so on.if an element
in list1/list2 in None ,then the corresponding element in the other list should be kept
as it is in the merged list.



list1=['A','app','a','d','ke','th','doc','awa']
list2=['y','tor','e','eps','ay',None,'le','n']
list2.reverse()
result = []
for i, j in zip(list1, list2):
  
    if i is None:
        result.append(j)
    elif j is None:
        result.append(i)
    else:
        result.append(i + j)

result = '   '.join(result)

print(result)
'''
#qts-->5
'''
Given two queues, one integer queue and another character queue,
Write a python program to merge then to form a sigle queue.
Follow the below rules for merging:
Merge elements at the same position starting with the integer queue.
If one of the queue has more elements than the other, add all the additional
elements at the end of the output queue.
Note: max_size of the merged queue should be the sum of the size of both the queues.

For example,
Input-- queue1:3,6,8 queue2:b,y,u,t,r,o
Output-- 3,b,6,y,8,u,t,r,o 


queue1 = [3, 6, 8]
queue2 = ['b', 'y', 'u', 't', 'r', 'o']

result = []

for i in range(min(len(queue1), len(queue2))):
    result.append(queue1[i])
    result.append(queue2[i])

if len(queue1) > len(queue2):
    result.extend(queue1[len(queue2):])
else:
    result.extend(queue2[len(queue1):])

print(result)
result=','.join([str(ele)for ele in result])
print(result) '''

#Traversing a Linked List

class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def AtBegining(self,newdata):#"sun"
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self,newdata):
         NewNode = Node(newdata)
         if self.headval is None:
             self.headval = NewNode
             return
         laste = self.headval
         while(laste.nextval):
             laste = laste.nextval 
         laste.nextval=NewNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode=Node(newdata)
        NewNode.nextval=middle_node.nextval
        middle_node.nextval = NewNode
        

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3
list.AtBegining("sun")
list.AtEnd("Thu")
list.Inbetween(list.headval.nextval.nextval.nextval.nextval.nextval,"Fri")
list.listprint()

    
        
