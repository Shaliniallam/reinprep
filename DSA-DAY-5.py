#qts-->1
'''WAP function which accepts two linked lists containing interger data and an
integer , n and merges the two linked lists, such that list2 is merged with
list1 after n number of nodes.
Note :- Assume the value of n1 will always be less than or equal to the no.of
nodes in list1.

Sample Input
list1 = 1->2->4->3->5
list2 = 9->8->11

Experted Output
n = 2 
1->2->9->8->11->4->3->5

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def lists(list1: ListNode, list2: ListNode, n: int) -> ListNode:
   
    prev = None
    curr = list1
    i = 1
    while curr and i <= n:
        prev = curr
        curr = curr.next
        i += 1

    prev.next = list2
    while list2.next:
        list2 = list2.next
    list2.next = curr

    return list1
list1 = ListNode(1, ListNode(2, ListNode(4, ListNode(3, ListNode(5)))))
list2 = ListNode(9, ListNode(8, ListNode(11)))
n = 2
result = lists(list1, list2, n)
while result:
    print(result.val, end="->")
    result = result.next
    
'''

#qts-->2
class Queue:
    def __init__(self,max_size):
        self.__rear=-1
        self.__front=0
        self.__max_size=max_size
        self.__element=[None]*self.__max_size
       
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
            print("Queue is full")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            data=self._element[self._rear]
            self.__front+=1
        return data
    def display(self):
        for index in range(self._front,self._rear+1):
              print(self.__element[index])
    def get_max_marks(self):
        return self.__max_size
    def gender(self):
        count=0
        count1=0
        if(self.is_empty()):
            print("Queue is empty")
        for index in range(self.__front,self.__rear+1):
            if self.__element[index]=="Male":
                count+=1
            elif self.__element[index]=="Female": 
                count1+=1
        return count,count1
                
queue1=Queue(5)
queue1.enqueue("Male")
queue1.enqueue("Female")
queue1.enqueue("Female")
queue1.enqueue("Female")
queue1.enqueue("Male")
print(queue1.gender())




